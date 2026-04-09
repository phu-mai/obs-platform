import grafanalib.core as g

TRACEQL = [
    g.Text(
        mode="markdown",
        gridPos=g.GridPos(h=30,w=24,x=0,y=1),
        content=r'''
### Introduction

This document is a cheatsheet for Grafana Tempo TraceQL frequently used queries to get insights from trace IDs.

### Common Queries

##### Find all traces has duration more than `30s`

```
{traceDuration> 30s}
```

##### Find all traces has duration more than `30s` and less than `60s`

```
{traceDuration>30s && traceDuration<60s}
```

##### Find all spans that are from `istio-proxy` to sidecar container service

```
{resource.service.name="authentication.lxp-core"}
```

##### Find all spans that are served by app service

```
{resource.service.name="authentication"}
```

##### Find all spans with protocol `grpc`

```
{resource.service.name="audit.lxp-core" && .grpc.path!="" }
```

##### Find all spans with protocol `http`

```
{resource.service.name="audit.lxp-core" && .http.url!="" }
```

##### Find all spans by span kind

- `SERVER` Indicates that the span covers server-side handling of a synchronous RPC or other remote request. This span is often the child of a remote `CLIENT` span that was expected to wait for a response.
- `CLIENT` Indicates that the span describes a request to some remote service. This span is usually the parent of a remote `SERVER` span and does not end until the response is received.
- `PRODUCER` Indicates that the span describes the initiators of an asynchronous request. This parent span will often end before the corresponding child `CONSUMER` span, possibly even before the child span starts. In messaging scenarios with batching, tracing individual messages requires a new PRODUCER span per message to be created.
- `CONSUMER` Indicates that the span describes a child of an asynchronous `PRODUCER` request.
- `INTERNAL` Default value. Indicates that the span represents an internal operation within an application, as opposed to an operations with remote parents or children.

```
{kind=producer}
```

To summarize the interpretation of these kinds:

| **SpanKind** | **Synchronous** | **Asynchronous** | **Remote Incoming** | **Remote Outgoing** |
|:------------:|:---------------:|:----------------:|:-------------------:|:-------------------:|
|    CLIENT    |       yes       |                  |                     |         yes         |
|    SERVER    |       yes       |                  |         yes         |                     |
|   PRODUCER   |                 |        yes       |                     |        maybe        |
|   CONSUMER   |                 |        yes       |        maybe        |                     |
|   INTERNAL   |                 |                  |                     |                     |

        ''',
    ),
]

dashboard = g.Dashboard(
    title="LXP / Cheatsheet / TraceQL",
    description="This dashboard provides common queries for TraceQL.",
    tags=["cheatsheet","leapxpert"],
    time=g.Time("now-5m", "now"),
    refresh="off",
    uid="lxp-cheatsheet-traceql",
    version=1,
    links=[
        g.DashboardLink(
            title="Observability Cheatsheets",
            type="dashboards",
            tags=["cheatsheet","leapxpert"],
            asDropdown=True,
            includeVars=True,
            keepTime=True,
            targetBlank=True
        )
    ],
    panels=TRACEQL,
).auto_panel_ids()

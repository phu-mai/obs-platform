import grafanalib.core as g

PROMQL = [
    g.Text(
        mode="markdown",
        gridPos=g.GridPos(h=45,w=24,x=0,y=1),
        content=r'''
### Introduction

This document is a cheatsheet for Prometheus Query Language (PromQL) frequently used to visualize and aggregate metrics.

### Common Queries

##### Get image list from containers excluding `istio-proxy`

```
sum by (pod, namespace, container, image) (
    kube_pod_container_info{container!="istio-proxy",container!=""}
)
```

##### Get OOMKilled pods

```
(kube_pod_container_status_restarts_total - kube_pod_container_status_restarts_total offset 5m >= 1)
    and ignoring (reason)
min_over_time(kube_pod_container_status_last_terminated_reason{reason="OOMKilled"}[5m]) == 1
```

##### Get CrashLoopBackoff pods

```
(kube_pod_container_status_restarts_total - kube_pod_container_status_restarts_total offset 5m >= 1)
    and ignoring (reason)
min_over_time(kube_pod_container_status_last_terminated_reason{reason="Error"}[5m]) == 1
```

##### Get pods not in `Running` or `Succeeded` phase

Pod Life Cycle can be found [here](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)

```
sum by (namespace, pod, phase) (min_over_time(kube_pod_status_phase{phase!~"Running|Succeeded",namespace=~"$fmop_namespace"}[10m])) > 0
```

##### Get request rate (rps) for `http` protocol from to particular app container

```
sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
  rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="http"}[5m])
)
```

##### Get request rate (rps) for `grpc` protocol from to particular app container

```
sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
  rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="grpc"}[5m])
)
```

##### Get error percentage for `http` protocol from to particular app container

```
(
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="http", response_code=~"[4-5][0-9][0-9]"}[5m])
    )
    or
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="http", response_code=~"[4-5][0-9][0-9]"}[5m]) * 0
    )
/
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="http"}[5m])
    )
)
```

##### Get error percentage for `grpc` protocol from to particular app container

```
(
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="grpc", response_code="0", response_flags="-"}[5m])
    )
    or
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="grpc", response_code="0", response_flags="-"}[5m]) * 0
    )
    /
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="grpc"}[5m])
    )
)
    OR
(
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="grpc", response_code="200", response_flags!="-" }[5m])
    )
    or
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="grpc", response_code="200", response_flags!="-"}[5m]) * 0
    )
    /
    sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
        rate(istio_requests_total{app=~"<app_name>", reporter="destination", request_protocol="grpc"}[5m])
    )
)
```

##### Get request duration for `http` protocol from to particular app container

```
sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
  rate(istio_request_duration_milliseconds_sum{app=~"<app_name>", reporter=~"destination", request_protocol="http"}[5m])
)
  /
sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
  rate(istio_request_duration_milliseconds_count{app=~"<app_name>", reporter=~"destination", request_protocol="http"}[5m])
)
```

##### Get request duration for `grpc` protocol from to particular app container

```
sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
  rate(istio_request_duration_milliseconds_sum{app=~"<app_name>", reporter=~"destination", request_protocol="grpc"}[5m])
)
  /
sum by (source_workload, destination_workload, request_protocol, response_flags, response_code) (
  rate(istio_request_duration_milliseconds_count{app=~"<app_name>", reporter=~"destination", request_protocol="grpc"}[5m])
)
```
        ''',
    ),
]

dashboard = g.Dashboard(
    title="LXP / Cheatsheet / PromQL",
    description="This dashboard provides common queries for PromQL.",
    tags=["cheatsheet","leapxpert"],
    time=g.Time("now-5m", "now"),
    refresh="off",
    uid="lxp-cheatsheet-promql",
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
    panels=PROMQL,
).auto_panel_ids()

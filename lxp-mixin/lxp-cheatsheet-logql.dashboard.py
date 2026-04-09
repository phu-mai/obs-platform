import grafanalib.core as g

LOGQL = [
    g.Text(
        mode="markdown",
        gridPos=g.GridPos(h=45,w=24,x=0,y=1),
        content=r'''
### Introduction

This document is a cheatsheet for Grafana Loki LogQL frequently used queries to extract fields from log messages.

### Common Queries

##### Extract email address

```
{container="usermanagement"} | regexp "(?P<email_address>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})"
```

##### Extract phone number

```
{container="usermanagement"} |= "persona" | regexp "mobilePhoneNumber=(?P<mobilePhoneNunber>\\d{7,})"
```

##### Extract phone number

```
sum by (ip) (count_over_time({container="konnectivity-agent"} |= `error dialing backend` | regexp `(?P<ip>((?:[0-9]{1,3}\.){3}[0-9]{1,3}))`[5m]))
```

##### Extract `roomId` and `userId` failed to be registered

```
sum by (roomId, userId) (
    {container="matrix"} |= "SynapseError: 403 - Application service has not registered this user" | regexp "(?P<room>!\\w+:\\w+).*(?P<user>\\(\\@\\w+:\\w+\\))”[2m]
)
```

##### Check register user by agent

```
sum by (gateway_agent,email_address,domain) (
    count_over_time(
        {domain=~"mac2[2-3]-igateway.mc.leapxloud.com"} |= "Registered agent macAccount"
        | json
        | line_format "{{.msg}}"
        | regexp "Registered agent macAccount:\"(?P<gateway_agent>\\w+-\\w+-\\d{1,3})\"\\s\\w+:\"(?P<email_address>\\w+@email.example)\""[5m]
    )
)
```

##### Extract API path from `istio-proxy` container

```
sum by (app,path) (
    count_over_time(
        {container="istio-proxy",app=~"api-server|keymanagement"}
        |= "/v1"
        != "/v1/matrix/"
        != "/v1/message-statuses"
        != "/v1/thumbnail/leapxpert"
        != "/v1/profiles?userId"
        != "/v1/client-profiles/"
        != "/v1/delegations?delegatee"
        != "/v1/delegations?delegator"
        != "/v1/workflows"
        != "/v1/users/"
        | regexp "(?P<path>\\/v1(?:\\/[^\\/\\s]*){1,2})"[5m]) #{1,2} handle how many slashes
)
```

##### Extract more labels from `istio-proxy` logs

```
sum by (path,status_code,forward_for,duration) (
    count_over_time({app="wechat-miniapp-integration",container="istio-proxy"} | pattern `<_> "<method> <path> <protocol>" <status_code> <response_flags> <response_code_details> <connection_termination_details> "<failure_reason>" <bytes_received> <bytes_sent> <duration> <upstream_time> "<forward_for>" "<agent>" "<req_id>" "<authority>" "<upstream_host>" <upstream_cluster> <upstream_local_address> <downstream_local_address> <downstream_remote_address> <requested_server_name> <route_name>` != "/opentelemetry.proto.collector.trace.v1.TraceService/Export" != "Blackbox Exporter/0.23.0" != "macquarie-prod-saas-docdb.cluster-cmtpccfzscjl.ap-southeast-2.docdb.amazonaws.com" [5m])
)
```

### How to use LogQL regex efficiently

LogQL regex provides a way to leverage regexp query function to extract fields in log messages and make it as label for aggregation.

Here are the recommended steps to extract roomId (e.g `!NWKEhLdmAEDDuSFZTb:leapxpert`) and api (e.g joined_member, state) path in below log messages

```
"GET /_matrix/client/r0/rooms/!NWKEhLdmAEDDuSFZTb:leapxpert/joined_members?access_token=redacted HTTP/1.1" 403 - via_upstream - "-" 0 58 3 3 "-" "akka-http/10.2.10" "89a1c506-a6ea-96db-b88a-2cd22db93dc4" "synapse.lxp-core:8008" "10.0.1.199:8008" inbound|8008|| 127.0.0.6:45307 10.0.1.199:8008 10.0.0.86:54978 - default traceID=7654f5f829bed4690de1f31281c4854b traceSampled=1
"GET /_matrix/client/r0/rooms/!NWKEhLdmAEDDuSFZTb:leapxpert/state?access_token=redacted&user_id=%40commander%3Aleapxpert HTTP/1.1" 403 - via_upstream - "-" 0 135 8 8 "-" "akka-http/10.2.10" "186851fe-c171-46d2-a080-95c348944b26" "synapse.lxp-core:8008" "10.0.1.199:8008" inbound|8008|| 127.0.0.6:45307 10.0.1.199:8008 10.0.0.86:54978 - default traceID=7654f5f829bed4690de1f31281c4854b traceSampled=1
"GET /_matrix/client/r0/rooms/!NWKEhLdmAEDDuSFZTb:leapxpert/joined_members?access_token=redacted HTTP/1.1" 403 - via_upstream - "-" 0 58 7 6 "-" "akka-http/10.2.10" "bda22976-5c0d-489a-958b-b0ad9fc309da" "synapse.lxp-core:8008" "10.0.1.199:8008" inbound|8008|| 127.0.0.6:45307 10.0.1.199:8008 10.0.0.86:54978 - default traceID=7654f5f829bed4690de1f31281c4854b traceSampled=1
"GET /_matrix/client/r0/rooms/!NWKEhLdmAEDDuSFZTb:leapxpert/state/m.room.name?access_token=redacted&user_id=%40commander%3Aleapxpert HTTP/1.1" 403 - via_upstream - "-" 0 135 10 10 "-" "akka-http/10.2.10" "1716372b-9b91-4b0e-a287-4b13d7065c82" "synapse.lxp-core:8008" "10.0.1.199:8008" inbound|8008|| 127.0.0.6:45307 10.0.1.199:8008 10.0.0.86:54978 - default traceID=7654f5f829bed4690de1f31281c4854b traceSampled=1
"GET /_matrix/client/r0/rooms/!NWKEhLdmAEDDuSFZTb:leapxpert/state?access_token=redacted&user_id=%40656f42497d7fd37b1d02ead9%3Aleapxpert HTTP/1.1" 403 - via_upstream - "-" 0 150 18 18 "-" "akka-http/10.2.10" "29f09e75-4ecf-410e-a09a-cc9f92ebabc5" "synapse.lxp-core:8008" "10.0.1.199:8008" inbound|8008|| 127.0.0.6:34403 10.0.1.199:8008 10.0.0.86:46572 - default traceID=362fbea5a405a0fd362fbea5a405a0fd traceSampled=1
```

- Write a regex query in [regex101](https://regex101.com/): build, test, and debug regex with regex group. You can read about regex group here [regex](https://grafana.com/docs/loki/latest/send-data/promtail/stages/regex/#regex)
    ```
    \"GET \/_matrix\/client\/r0\/rooms\/(?P<room>.*:leapxpert)\/(?P<api>.+)\?.+
    ```
- Escape regex expression with this [site](https://onlinestringtools.com/escape-string)
    ```
    \\\"GET \\/_matrix\\/client\\/r0\\/rooms\\/(?P<room>.*:leapxpert)\\/(?P<api>.+)\\?.+
    ```
- Put all together in LogQL query. In below query, we want to extract from container `istio-proxy` of `matrix` log messages that contain `GET` and `403 - via_upstream`.
    ```
    sum by (room,api) (count_over_time({container="istio-proxy",app="matrix"} |= "GET" |= "403 - via_upstream" | regexp "\\\"GET \\/_matrix\\/client\\/r0\\/rooms\\/(?P<room>.*:leapxpert)\\/(?P<api>.+)\\?.+"[5m]))
    ```
        ''',
    ),
]

dashboard = g.Dashboard(
    title="LXP / Cheatsheet / LogQL",
    description="This dashboard provides common queries for LogQL.",
    tags=["cheatsheet","leapxpert"],
    time=g.Time("now-5m", "now"),
    refresh="off",
    uid="lxp-cheatsheet-logql",
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
    panels=LOGQL,
).auto_panel_ids()

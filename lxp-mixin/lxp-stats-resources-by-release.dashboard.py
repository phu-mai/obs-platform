import grafanalib.core as g

FMOP_STATEFUL_SERVICES=[
    g.TimeSeries(
        title="Memory Usage",
        dataSource="${datasource}",
        targets=[
            g.Target(
                expr="sum by (container, namespace, pod) (container_memory_working_set_bytes{container=~\"$fmop_stateful_container\"})",
                legendFormat="Namespace {{namespace}} | Container {{container}} | Usage {{pod}}",
                format="timeseries",
                instant=False
            ),
            g.Target(
                expr="max by (namespace, container) (kube_pod_container_resource_requests{container=~\"$fmop_stateful_container\",resource=\"memory\"})",
                legendFormat="Namespace {{namespace}} | Container {{container}} | Request",
                format="timeseries",
                instant=False
            ),
            g.Target(
                expr="max by (namespace, container) (kube_pod_container_resource_limits{container=~\"$fmop_stateful_container\",resource=\"memory\"})",
                legendFormat="Namespace {{namespace}} | Container {{container}} | Limit",
                format="timeseries",
                instant=False
            )
        ],
        unit="bytes",
        legendPlacement="bottom",
        legendCalcs=["min","max","last"],
        legendDisplayMode="table",
        tooltipMode="multi",
        gridPos=g.GridPos(h=11, w=12, y=16, x=0),
    ),
    g.TimeSeries(
        title="CPU Usage",
        dataSource="${datasource}",
        targets=[
            g.Target(
                expr="sum by (container, namespace, pod) (rate(container_cpu_usage_seconds_total{container=~\"$fmop_stateful_container\"}[$__rate_interval]))",
                legendFormat="Namespace {{namespace}} | Container {{container}} | Usage {{pod}}",
                format="timeseries",
                instant=False
            ),
            g.Target(
                expr="max by (namespace, container) (kube_pod_container_resource_requests{container=~\"$fmop_stateful_container\",resource=\"cpu\"})",
                legendFormat="Namespace {{namespace}} | Container {{container}} | Request",
                format="timeseries",
                instant=False
            ),
            g.Target(
                expr="max by (namespace, container) (kube_pod_container_resource_limits{container=~\"$fmop_stateful_container\",resource=\"cpu\"})",
                legendFormat="Namespace {{namespace}} | Container {{container}} | Limit",
                format="timeseries",
                instant=False
            )
        ],
        unit="none",
        legendPlacement="bottom",
        legendCalcs=["min","max","last"],
        legendDisplayMode="table",
        tooltipMode="multi",
        gridPos=g.GridPos(h=11, w=12, y=16, x=13),
    ),
    g.Table(
        title="Volume Capacity",
        unit="none",
        align="center",
        showHeader=True,
        filterable=True,
        dataSource="${datasource}",
        sortBy=[
            g.TableSortByField(displayName="Volume Usage (%)", desc=True),
        ],
        gridPos=g.GridPos(w=24, h=10, y=28, x=0),
        targets=[
            g.Target(
                expr=r'''
sum by (persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"})
                ''',
                format="table",
                instant=True,
            ),
            g.Target(
                expr=r'''
sum by (persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"})
-
sum by (persistentvolumeclaim) (kubelet_volume_stats_available_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"})
                ''',
                format="table",
                instant=True,
            ),
            g.Target(
                expr=r'''
(sum by (persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"})
-
sum by (persistentvolumeclaim) (kubelet_volume_stats_available_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"}))
/
sum by (persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"}) * 100
                ''',
                format="table",
                instant=True,
            ),
        ],
        transformations=[
            {
                "id": "merge",
                "options": {}
            },
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True
                    },
                    "includeByName": {},
                    "indexByName": {},
                    "renameByName": {
                        "Value #A": "Volume Capacity (GB)",
                        "Value #B": "Volume Usage (GB)",
                        "Value #C": "Volume Usage (%)",
                        "persistentvolumeclaim": "Persistent Volume Claim"
                    }
                }
            }
        ],
        overrides=[
            {
                "matcher": {
                    "id": "byName",
                    "options": "Volume Usage (%)"
                },
                "properties": [
                    {
                        "id": "unit",
                        "value": "percent"
                    },
                    {
                        "id": "thresholds",
                        "value": {
                            "mode": "absolute",
                            "steps": [
                                {
                                    "color": "green",
                                    "value": "null"
                                },
                                {
                                    "color": "#EAB839",
                                    "value": 80
                                },
                                {
                                    "color": "red",
                                    "value": 90
                                }
                            ]
                        }
                    },
                    {
                        "id": "custom.cellOptions",
                        "value": {
                            "type": "color-background"
                        }
                    }
                ]
            }
        ]
    ),
    g.TimeSeries(
        title="Volume Usage",
        dataSource="${datasource}",
        targets=[
            g.Target(
                expr=r'''
(sum by (persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"})
-
sum by (persistentvolumeclaim) (kubelet_volume_stats_available_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"}))
/
sum by (persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{job="kubelet", metrics_path="/metrics", namespace=~".*", persistentvolumeclaim=~"$persistentvolumeclaim"}) * 100
                ''',
                legendFormat="{{persistentvolumeclaim}}",
                format="timeseries",
                instant=False
            )
        ],
        unit="bytes",
        legendPlacement="bottom",
        legendCalcs=["min","max","last"],
        legendDisplayMode="table",
        tooltipMode="multi",
        gridPos=g.GridPos(h=11, w=24, y=53, x=0),
    )
]
dashboard = g.Dashboard(
    title="LXP / Stats / Resources by Release",
    description="This dashboard provides stats for resources by release.",
    tags=["stats","leapxpert"],
    time=g.Time("now-1h", "now"),
    refresh="",
    uid="lxp-stats-resources-by-release",
    timezone="browser",
    links=[
        g.DashboardLink(
            title="Observability Stats",
            type="dashboards",
            tags=["stats","leapxpert"],
            asDropdown=True,
            includeVars=True,
            keepTime=True,
            targetBlank=True
        )
    ],
    templating=g.Templating(
        list=[
            g.Template(
                name="datasource",
                label="Datasource",
                type="datasource",
                dataSource="Prometheus",
                query="prometheus",
            ),
            g.Template(
                name="fmop_namespace",
                label="FMOP Namespace",
                dataSource="${datasource}",
                query="label_values(grpc_server_handled_total{instance=~\".*:15020\"},namespace)",
                refresh=2,
                includeAll=True,
                multi=True,
            ),
            g.Template(
                name="fmop_app_container",
                label="FMOP App Container",
                dataSource="${datasource}",
                query="label_values(container_memory_working_set_bytes{namespace=~\"$fmop_namespace\", container!~\"matrix|vault.*|keycloak|minio.*\"},container)",
                refresh=2,
                includeAll=True,
                multi=True,
                default="api-server",
            ),
            g.Template(
                name="fmop_release_version",
                label="FMOP Release Version",
                dataSource="${datasource}",
                query="label_values(istio_agent_go_info,lxp_version)",
                refresh=2,
                includeAll=True,
                multi=True,
            ),
            g.Template(
                name="fmop_stateful_container",
                label="FMOP Stateful Container",
                dataSource="${datasource}",
                query="label_values(container_memory_working_set_bytes{container=~\"matrix|keycloak|vault|kafka|zookeeper|minio|elasticsearch|postgres|mongodb-primary|mongodb-secondary|mongodb-arbiter\"},container)",
                refresh=2,
                includeAll=True,
                multi=True,
                default="keycloak",
            ),
            g.Template(
                name="persistentvolumeclaim",
                label="FMOP Stateful Persistent Volume",
                dataSource="${datasource}",
                query="label_values(kubelet_volume_stats_capacity_bytes,persistentvolumeclaim)",
                refresh=2,
                includeAll=True,
                multi=True,
            ),
            g.Template(
                name="min_interval",
                label="Min Interval",
                type="custom",
                query="7d,15d,30d",
                options=[
                    {
                        "selected": False,
                        "text": "7d",
                        "value": "7d"
                    },
                    {
                        "selected": True,
                        "text": "15d",
                        "value": "15d"
                    },
                    {
                        "selected": False,
                        "text": "30d",
                        "value": "30d"
                    }
                ],
            ),
        ]
    ),
    panels=[
        g.Text(
            mode="markdown",
            gridPos=g.GridPos(h=11,w=24,x=0,y=0),
            content=r'''
### Dashboard Naming
LeapXpert dashboards will be created with prefix `lxp-`.

`lxp-resource-by-release` contains resource usage of FMOP app, stateful services & volume usage.

### How To

`FMOP Applications`
  * `FMOP Namespace` droplist is only used `FMOP App Container`
  * `FMOP App Container` droplist is used to filter specific application. `api-server` is set by default
  * `FMOP Release Version` droplist is used to filter specific image release versions.

`FMOP Stateful Services`
  * `FMOP Stateful Container` droplist is used to filter specific stateful services.
  * `Persistent Volumer` droplist is used to filter specific stateful services.

`Min Interval` is a time span that is used when aggregating or grouping data points by time. This is only used for table graphs.
        ''',
        ),
        g.RowPanel(title="FMOP Applications", gridPos=g.GridPos(w=24, h=1, x=0, y=12)),
        g.TimeSeries(
            title="Memory Usage",
            dataSource="${datasource}",
            targets=[
                g.Target(
                    expr=r'''
sum by (container, namespace, lxp_version) (
    container_memory_working_set_bytes{container=~"$fmop_app_container",namespace=~"$fmop_namespace"}
    * on(container, namespace, pod)
        group_left (lxp_version)
    istio_agent_go_info{container=~"$fmop_app_container",namespace=~"$fmop_namespace",lxp_version=~"$fmop_release_version"}
)
                    ''',
                    legendFormat="Namespace {{namespace}} | Container {{container}} | Usage {{lxp_version}}",
                    format="timeseries",
                    instant=False
                ),
                g.Target(
                    expr=r'''
max by (container, namespace, lxp_version) (
    max by (namespace, container, pod) (
        kube_pod_container_resource_requests{namespace=~"$fmop_namespace",container=~"$fmop_app_container",resource="memory"}
    )
    * on(container, namespace, pod)
    group_left (lxp_version) istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container",lxp_version=~"$fmop_release_version"}
)
                    ''',
                    legendFormat="Namespace {{namespace}} | Container {{container}} | Request {{lxp_version}}",
                    format="timeseries",
                    instant=False
                ),
                g.Target(
                    expr=r'''
max by (container, namespace, lxp_version) (
    max by (namespace, container, pod) (
        kube_pod_container_resource_limits{namespace=~"$fmop_namespace",resource="memory",container=~"$fmop_app_container"}
    )
    * on(container, namespace, pod)
    group_left (lxp_version) istio_agent_go_info{container=~"$fmop_app_container",namespace=~"$fmop_namespace",lxp_version=~"$fmop_release_version"}
)
                    ''',
                    legendFormat="Namespace {{namespace}} | Container {{container}} | Limit {{lxp_version}}",
                    format="timeseries",
                    instant=False
                )
            ],
            unit="bytes",
            legendPlacement="bottom",
            legendCalcs=["min","max","last"],
            legendDisplayMode="table",
            tooltipMode="multi",
            gridPos=g.GridPos(h=11, w=12, y=13, x=0),
        ),
        g.TimeSeries(
            title="CPU Usage",
            dataSource="${datasource}",
            targets=[
                g.Target(
                    expr=r'''
sum by (container, namespace, lxp_version) (
    rate(container_cpu_usage_seconds_total{namespace=~"$fmop_namespace",container=~"$fmop_app_container"}[$__rate_interval])
        * on(container, namespace, pod)
        group_left (lxp_version)
    istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container",lxp_version=~"$fmop_release_version"}
)
                    ''',
                    legendFormat="Namespace {{namespace}} | Container {{container}} | Usage {{lxp_version}}",
                    format="timeseries",
                    instant=False
                ),
                g.Target(
                    expr=r'''
max by (container, namespace, lxp_version) (
    max by (namespace, container, pod) (
        kube_pod_container_resource_requests{namespace=~"$fmop_namespace",container=~"$fmop_app_container",resource="cpu"}
    )
    * on(container, namespace, pod)
    group_left (lxp_version) istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container",lxp_version=~"$fmop_release_version"}
)
                    ''',
                    legendFormat="Namespace {{namespace}} | Container {{container}} | Request {{lxp_version}}",
                    format="timeseries",
                    instant=False
                ),
                g.Target(
                    expr=r'''
max by (container, namespace, lxp_version) (
    max by (namespace, container, pod) (
        kube_pod_container_resource_limits{namespace=~"$fmop_namespace",container=~"$fmop_app_container",resource="cpu"}
    )
    * on(container, namespace, pod)
    group_left (lxp_version) istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container",lxp_version=~"$fmop_release_version"}
)
                    ''',
                    legendFormat="Namespace {{namespace}} | Container {{container}} | Limit {{lxp_version}}",
                    format="timeseries",
                    instant=False
                )
            ],
            unit="number",
            legendPlacement="bottom",
            legendCalcs=["min","max","last"],
            legendDisplayMode="table",
            tooltipMode="multi",
            gridPos=g.GridPos(h=11, w=12, y=13, x=13),
        ),
        g.Table(
            title="Resource Requests & Limits by release version",
            unit="none",
            align="center",
            showHeader=True,
            filterable=True,
            dataSource="${datasource}",
            sortBy=[
                g.TableSortByField(displayName="Container", desc=False),
            ],
            gridPos=g.GridPos(w=24, h=10, y=14, x=0),
            targets=[
                g.Target(
                    expr=r'''
(max by (namespace, container,pod) (
    kube_pod_container_resource_requests{namespace=~"$fmop_namespace",container=~"$fmop_app_container",resource="cpu"}
)
* on(container, namespace, pod)
  group_left (lxp_version) istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container"}) * 1000
                    ''',
                    format="table",
                    instant=False,
                    interval="$min_interval"
                ),
                g.Target(
                    expr=r'''
(max by (namespace, container,pod) (
    kube_pod_container_resource_limits{namespace=~"$fmop_namespace",container=~"$fmop_app_container",resource="cpu"}
)
* on(container, namespace, pod)
  group_left (lxp_version) istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container"}) * 1000
                    ''',
                    format="table",
                    instant=False,
                    interval="$min_interval"
                ),
                g.Target(
                    expr=r'''
max by (namespace, container, pod) (
    kube_pod_container_resource_requests{namespace=~"$fmop_namespace",container=~"$fmop_app_container",resource="memory"}
)
* on(container, namespace, pod)
    group_left (lxp_version) istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container"}
                    ''',
                    format="table",
                    instant=False,
                    interval="$min_interval"
                ),
                g.Target(
                    expr=r'''
max by (namespace, container, pod) (
    kube_pod_container_resource_limits{namespace=~"$fmop_namespace",container=~"$fmop_app_container",resource="memory"}
)
* on(container, namespace, pod)
    group_left (lxp_version) istio_agent_go_info{namespace=~"$fmop_namespace",container=~"$fmop_app_container"}
                    ''',
                    format="table",
                    instant=False,
                    interval="$min_interval"
                ),
            ],
            transformations=[
                {
                    "id": "merge",
                    "options": {}
                },
                {
                    "id": "organize",
                    "options": {
                        "excludeByName": {
                            "Time": True,
                            "pod": True
                        },
                        "indexByName": {},
                        "renameByName": {
                            "Value #A": "CPU Requests (m)",
                            "Value #B": "CPU Limits (m)",
                            "Value #C": "Memory Requests",
                            "Value #D": "Memory Limits",
                            "Value #E": "Memory Limit",
                            "container": "Container",
                            "lxp_version": "Release Version",
                            "namespace": "Namespace"
                        }
                    }
                }
            ],
            overrides=[
                {
                    "matcher": {
                        "id": "byName",
                        "options": "CPU Requests (m)"
                    },
                    "properties": [
                        {
                            "id": "unit",
                            "value": "short"
                        }
                    ]
                },
                {
                    "matcher": {
                        "id": "byName",
                        "options": "CPU Limits (m)"
                    },
                    "properties": [
                        {
                            "id": "unit",
                            "value": "short"
                        }
                    ]
                },
                {
                    "matcher": {
                        "id": "byName",
                        "options": "Memory Requests"
                    },
                    "properties": [
                        {
                            "id": "unit",
                            "value": "bytes"
                        }
                    ]
                },
                {
                    "matcher": {
                        "id": "byName",
                        "options": "Memory Limits"
                    },
                    "properties": [
                        {
                            "id": "unit",
                            "value": "bytes"
                        }
                    ]
                }
            ]
        ),
        g.RowPanel(
            title="FMOP Stateful Services",
            gridPos=g.GridPos(w=24, h=1, x=0, y=15),
            collapsed=True,
            panels=FMOP_STATEFUL_SERVICES
        ),
    ],
    version=1
)

import grafanalib.core as g

dashboard = g.Dashboard(
    title="LXP / Stats / MongoDB Collections",
    description="This dashboard provides stats for MongoDB collections.",
    tags=["stats","leapxpert"],
    time=g.Time("now-1h", "now"),
    refresh="1m",
    uid="lxp-stats-mongodb-collections",
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
                name="collection",
                label="Collection",
                dataSource="${datasource}",
                query="label_values(mongodb_collection_size,collection)",
                refresh=2,
                includeAll=True,
                multi=True,
            ),
            g.Template(
                name="index",
                label="Index",
                dataSource="${datasource}",
                query="label_values(mongodb_collection_index_size{collection=~\"$collection\"},index)",
                refresh=2,
                includeAll=True,
                multi=True,
            ),
        ]
    ),
    panels=[
        g.RowPanel(title="Overview", gridPos=g.GridPos(w=24, h=1, x=0, y=0)),
        g.Table(
            title="Collection Stats",
            description="`Total Index Size` is only available for `Containerized MongoDB` and `AWS DocumentDB`",
            unit="short",
            align="center",
            showHeader=True,
            filterable=True,
            dataSource="${datasource}",
            sortBy=[
                g.TableSortByField(displayName="Collection", desc=False),
            ],
            gridPos=g.GridPos(w=24, h=12, y=1, x=0),
            targets=[
                g.Target(
                    expr="sum by (collection) (mongodb_collection_count{collection=~\"$collection\"})",
                    format="table",
                    instant=True,
                    refId="CollectionDocuments"
                ),
                g.Target(
                    expr="sum by (collection) (mongodb_collection_size{collection=~\"$collection\"})",
                    format="table",
                    instant=True,
                    refId="CollectionSize"
                ),
                g.Target(
                    expr="sum by (collection) (mongodb_collection_index_count{collection=~\"$collection\"})",
                    format="table",
                    instant=True,
                    refId="NumberOfIndexes"
                ),
                g.Target(
                    expr="sum by (collection) (mongodb_collection_total_index_size{collection=~\"$collection\"})",
                    format="table",
                    instant=True,
                    refId="TotalIndexSize"
                ),
                g.Target(
                    expr="sum by (collection) (mongodb_collection_avg_obj_size{collection=~\"$collection\"})",
                    format="table",
                    instant=True,
                    refId="AverageDocumentSize"
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
                        "renameByName": {
                            "Value": "Average Document Size",
                            "Value #CollectionDocuments": "Collection Documents",
                            "Value #CollectionSize": "Collection Size",
                            "Value #NumberOfIndexes": "Number of Indexes",
                            "Value #TotalIndexSize": "Total Index Size",
                            "Value #AverageDocumentSize": "Average Document Size",
                            "collection": "Collection"
                        }
                    }
                }
            ],
            overrides=[
                {
                    "matcher": {
                        "id": "byName",
                        "options": "Collection Documents"
                    },
                    "properties": [
                        {
                            "id": "unit",
                            "value": "none"
                        }
                    ]
                },
                {
                    "matcher": {
                        "id": "byName",
                        "options": "Collection Size"
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
                        "options": "Number of Indexes"
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
                        "options": "Total Index Size"
                    },
                    "properties": [
                        {
                            "id": "unit",
                            "value": "bytes"
                        },
                        {
                            "id": "mappings",
                            "value": [
                                {
                                    "options": {
                                        "0": {
                                            "index": 0,
                                            "text": "N/A"
                                        }
                                    },
                                    "type": "value"
                                },
                                {
                                    "options": {
                                    "match": "null",
                                    "result": {
                                        "index": 1,
                                        "text": "N/A"
                                    }
                                    },
                                    "type": "special"
                                }
                            ]
                        }
                    ]
                },
                {
                    "matcher": {
                        "id": "byName",
                        "options": "Average Document Size"
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
        g.Table(
            title="Index Stats",
            description="This graphs only covers `Containerized Mongodb` and `AWS DocumentDB` backends",
            unit="bytes",
            align="center",
            dataSource="${datasource}",
            showHeader=True,
            filterable=True,
            sortBy=[
                g.TableSortByField(displayName="Collection", desc=False),
            ],
            gridPos=g.GridPos(w=24, h=12, y=13, x=0),
            targets=[
                g.Target(
                    expr="sum by (collection,index) (mongodb_collection_index_size{collection=~\"$collection\",index=~\"$index\"})",
                    format="table",
                    instant=True,
                ),
            ],
            transformations=[
                {
                    "id": "organize",
                    "options": {
                        "excludeByName": {
                            "Time": True
                        },
                        "includeByName": {},
                        "renameByName": {
                            "Value": "Size",
                            "collection": "Collection",
                            "index": "Index",
                        }
                    }
                }
            ],
        ),
        g.RowPanel(title="Collections & Index Stats", gridPos=g.GridPos(w=24, h=1, y=14, x=0)),
        g.TimeSeries(
            title="Document & Index Count",
            dataSource="${datasource}",
            targets=[
                g.Target(
                    expr='sum by (collection) (mongodb_collection_count{collection=~\"$collection\"})',
                    legendFormat="{{collection}} | Document Count",
                    format="timeseries",
                    instant=False
                ),
                g.Target(
                    expr='sum by (collection) (mongodb_collection_index_count{collection=~\"$collection\"})',
                    legendFormat="{{collection}} | Index Count",
                    format="timeseries",
                    instant=False
                )
            ],
            unit="none",
            legendPlacement="bottom",
            legendCalcs=["min","max","last"],
            legendDisplayMode="table",
            tooltipMode="multi",
            gridPos=g.GridPos(h=10, w=12, y=15, x=0),
        ),
        g.TimeSeries(
            title="Collection & Index Size",
            dataSource="${datasource}",
            targets=[
                g.Target(
                    expr='sum by (collection) (mongodb_collection_size{collection=~\"$collection\"})',
                    legendFormat="{{collection}} | Collection Size",
                    format="timeseries",
                    instant=False
                ),
                g.Target(
                    expr='sum by (collection) (mongodb_collection_total_index_size{collection=~\"$collection\"})',
                    legendFormat="{{collection}} | Total Index Size",
                    format="timeseries",
                    instant=False
                )
            ],
            unit="bytes",
            legendPlacement="bottom",
            legendCalcs=["min","max","last"],
            legendDisplayMode="table",
            tooltipMode="multi",
            gridPos=g.GridPos(h=10, w=12, y=15, x=13),
        ),
        g.TimeSeries(
            title="Object Size by Collection",
            dataSource="${datasource}",
            targets=[
                g.Target(
                    expr='sum by (collection) (mongodb_collection_avg_obj_size{collection=~\"$collection\"})',
                    format="timeseries",
                    instant=False
                )
            ],
            unit="bytes",
            legendPlacement="bottom",
            legendCalcs=["min","max","last"],
            legendDisplayMode="table",
            tooltipMode="multi",
            gridPos=g.GridPos(h=10, w=12, y=26, x=0),
        ),
        g.TimeSeries(
            title="Object Size by Collection",
            dataSource="${datasource}",
            targets=[
                g.Target(
                    expr='sum by (collection,index) (mongodb_collection_index_size{collection=~\"$collection\",index=~\"$index\"})',
                    format="timeseries",
                    legendFormat="Collection {{collection}} | Index {{index}}",
                    instant=False
                )
            ],
            unit="bytes",
            legendPlacement="bottom",
            legendCalcs=["min","max","last"],
            legendDisplayMode="table",
            tooltipMode="multi",
            gridPos=g.GridPos(h=10, w=12, y=26, x=13),
        ),
    ],
    version=1
)

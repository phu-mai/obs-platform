{{/*
Azure Metrics Cosmo MongoDB
*/}}
{{- define "azure-metrics-exporter.azureMetricsCosmoMongodb" -}}
{{- if .Values.podMonitor.podMetricsEndpoints.services.azureMetricsCosmoMongodb.enabled }}
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-total-requests"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - MongoRequests
      - MongoRequestCharge
    interval: ["PT5M"]
    timespan: ["PT5M"]
    aggregation:
      - count
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-total-failed-requests"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - MongoRequests
      - MongoRequestCharge
    interval: ["PT5M"]
    timespan: ["PT5M"]
    metricFilter: ["Status eq 'Fail'"]
    aggregation:
      - count
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-mongodb-request-count-by-command"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - MongoRequests
      - MongoRequestCharge
    interval: ["PT5M"]
    timespan: ["PT5M"]
    metricFilter: ["CommandName eq '*' and CollectionName eq '*'"]
    metricTop: ["50"]
    aggregation:
      - count
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-mongodb-failed-request"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - MongoRequests
      - MongoRequestCharge
    metricFilter: ["Status eq 'Fail' and CollectionName eq '*' and CommandName eq '*' and ErrorCode eq '*'"]
    metricTop: ["50"]
    aggregation:
      - count
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
  metricRelabelings:
    {{- range $key, $value := $.Values.podMonitor.podMetricsEndpoints.services.azureMetricsCosmoMongodb.errorCodes }}
    - sourceLabels: [result]
      regex: "{{ $key }}"
      replacement: {{ $value }}
      targetLabel: error_name
      action: replace
    {{- end }}
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-mongodb-average"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - ServiceAvailability
    interval: ["PT1H"]
    timespan: ["PT1H"]
    aggregation:
      - average
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-mongodb-average-server-side-latency"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - ServerSideLatency
    metricFilter: ["CollectionName eq '*' and OperationType eq '*'"]
    metricTop: ["50"]
    interval: ["PT5M"]
    timespan: ["PT5M"]
    aggregation:
      - average
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-mongodb-max-ru"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - NormalizedRUConsumption
    metricFilter: ["CollectionName eq '*'"]
    metricTop: ["50"]
    interval: ["PT5M"]
    timespan: ["PT5M"]
    aggregation:
      - maximum
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-physical-partition-size-info"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - PhysicalPartitionSizeInfo
    interval: ["PT5M"]
    timespan: ["PT5M"]
    aggregation:
      - maximum
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-physical-partition-size-info-by-collection"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - PhysicalPartitionSizeInfo
    metricFilter: ["CollectionName eq '*'"]
    metricTop: ["50"]
    interval: ["PT5M"]
    timespan: ["PT5M"]
    aggregation:
      - maximum
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-physical-partition-size-info-by-physicalpartitionid"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - PhysicalPartitionSizeInfo
    metricFilter: ["PhysicalPartitionId eq '*'"]
    metricTop: ["50"]
    interval: ["PT5M"]
    timespan: ["PT5M"]
    aggregation:
      - maximum
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cosmo-physical-partition-throughput-info-by-collection"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DocumentDB/databaseAccounts"]
    metric:
      - PhysicalPartitionThroughputInfo
    metricFilter: ["CollectionName eq '*'"]
    metricTop: ["50"]
    interval: ["PT1M"]
    timespan: ["PT1M"]
    aggregation:
      - maximum
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
{{- end }}
{{- end }}

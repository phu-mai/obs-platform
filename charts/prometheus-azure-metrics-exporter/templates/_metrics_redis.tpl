{{/*
Azure Metrics Redis
*/}}
{{- define "azure-metrics-exporter.azureMetricsCacheRedis" -}}
{{- if .Values.podMonitor.podMetricsEndpoints.services.azureMetricsCacheRedis.enabled }}
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-cache-redis-total"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.Cache/redis"]
    metric:
      - cachehits
      - cachemisses
      - cachemissrate
      - evictedkeys
      - expiredkeys
      - getcommands
      - setcommands
      - totalcommandsprocessed
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["ShardId eq '*'"]
    metricTop: ["10"]
    aggregation:
      - total
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
    name: ["azure-metrics-cache-redis-maximum"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.Cache/redis"]
    metric:
      - cacheRead
      - cacheWrite
      - connectedclients
      - errors
      - operationsPerSecond
      - percentProcessorTime
      - serverLoad
      - totalkeys
      - usedmemory
      - usedmemorypercentage
      - usedmemoryRss
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["ShardId eq '*'"]
    metricTop: ["10"]
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
    name: ["azure-metrics-cache-redis-average"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.Cache/redis"]
    metric:
      - cacheLatency
    interval: ["PT5M"]
    timespan: ["PT5M"]
    metricFilter: ["ShardId eq '*'"]
    metricTop: ["10"]
    aggregation:
      - average
  relabelings:
    - sourceLabels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: replace
      replacement: $1
      regex: (.*)
      targetLabel: app
{{- end }}
{{- end }}

{{/*
Azure Metrics EventHub
*/}}
{{- define "azure-metrics-exporter.azureMetricsEventHub" -}}
{{- if .Values.podMonitor.podMetricsEndpoints.services.azureMetricsEventHub.enabled }}
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-eventhub-maximum"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.EventHub/namespaces"]
    metric:
      - ActiveConnections
      - ConnectionsClosed
      - ConnectionsOpened
      - NamespaceCpuUsage
      - NamespaceMemoryUsage
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
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-eventhub-total"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.EventHub/namespaces"]
    metric:
      - IncomingBytes
      - IncomingMessages
      - IncomingRequests
      - OutgoingBytes
      - OutgoingMessages
      - ServerErrors
      - SuccessfulRequests
      - ThrottledRequests
      - UserErrors
      - QuotaExceededErrors
    interval: ["PT1M"]
    timespan: ["PT1M"]
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
    name: ["azure-metrics-eventhub-total-by-entityname"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.EventHub/namespaces"]
    metric:
      - IncomingBytes
      - IncomingMessages
      - IncomingRequests
      - OutgoingBytes
      - OutgoingMessages
      - ServerErrors
      - SuccessfulRequests
      - ThrottledRequests
      - UserErrors
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["EntityName eq '*'"]
    metricTop: ["50"]
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
    name: ["azure-metrics-eventhub-average"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.EventHub/namespaces"]
    metric:
      - Size
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["EntityName eq '*'"]
    metricTop: ["50"]
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

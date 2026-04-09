{{/*
Azure Frontdoor Metrics
*/}}
{{- define "azure-metrics-exporter.azureFrontdoor" -}}
{{- if .Values.podMonitor.podMetricsEndpoints.services.azureFrontdoor.enabled }}
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-fd-backend-request-latency"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.Network/frontdoors"]
    metric:
      - BackendRequestLatency
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["Backend eq '*'"]
    metricTop: ["50"]
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
    name: ["azure-metrics-fd-total-latency"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.Network/frontdoors"]
    metric:
      - TotalLatency
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["ClientCountry eq '*' and HttpStatus eq '*'"]
    metricTop: ["50"]
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
    name: ["azure-metrics-fd-request-count"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.Network/frontdoors"]
    metric:
      - RequestCount
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["ClientCountry eq '*' and HttpStatus eq '*'"]
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
    name: ["azure-metrics-fd-backend-request-count"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.Network/frontdoors"]
    metric:
      - BackendRequestCount
    interval: ["PT1M"]
    timespan: ["PT1M"]
    metricFilter: ["Backend eq '*' and HttpStatus eq '*'"]
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

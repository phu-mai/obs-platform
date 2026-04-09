
{{/*
Azure Metrics Postgres Flexible Server
*/}}
{{- define "azure-metrics-exporter.azureMetricsPostgresFlexible" -}}
{{- if .Values.podMonitor.podMetricsEndpoints.services.azureMetricsPostgresFlexible.enabled }}
- interval: {{ $.Values.podMonitor.podMetricsEndpoints.interval }}
  scrapeTimeout: {{ $.Values.podMonitor.podMetricsEndpoints.scrapeTimeout }}
  port: http
  path: /probe/metrics/list
  params:
    name: ["azure-metrics-database-postgresql-flexible-average"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DBforPostgreSQL/flexibleServers"]
    metric:
      - active_connections
      - backup_storage_used
      - cpu_percent
      - disk_queue_depth
      - iops
      - maximum_used_transactionIDs
      - memory_percent
      - read_iops
      - read_throughput
      - storage_percent
      - storage_used
      - write_iops
      - write_throughput
    interval: ["PT15M"]
    timespan: ["PT15M"]
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
    name: ["azure-metrics-database-postgresql-flexible-total"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DBforPostgreSQL/flexibleServers"]
    metric:
      - connections_failed
      - connections_succeeded
      - temp_bytes
      - temp_files
    interval: ["PT15M"]
    timespan: ["PT15M"]
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
    name: ["azure-metrics-database-postgresql-flexible-total-db"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DBforPostgreSQL/flexibleServers"]
    metric:
      - deadlocks
    interval: ["PT15M"]
    timespan: ["PT15M"]
    metricFilter: ["DatabaseName eq '*'"]
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
    name: ["azure-metrics-database-postgresql-flexible-maximum"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DBforPostgreSQL/flexibleServers"]
    metric:
      - longest_query_time_sec
      - longest_transaction_time_sec
      - max_connections
      - is_db_alive
    interval: ["PT30M"]
    timespan: ["PT30M"]
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
    name: ["azure-metrics-database-postgresql-flexible-maximum-state"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DBforPostgreSQL/flexibleServers"]
    metric:
      - sessions_by_state
    interval: ["PT15M"]
    timespan: ["PT15M"]
    metricFilter: ["State eq '*'"]
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
    name: ["azure-metrics-database-postgresql-flexible-maximum-event"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DBforPostgreSQL/flexibleServers"]
    metric:
      - sessions_by_wait_event_type
    interval: ["PT15M"]
    timespan: ["PT15M"]
    metricFilter: ["WaitEventType eq '*'"]
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
    name: ["azure-metrics-database-postgresql-flexible-maximum-db"]
    subscription:
    {{ include "azure-metrics-exporter.subscription" . | indent 6 }}
    template: ["{name}_{metric}_{unit}"]
    resourceType: ["Microsoft.DBforPostgreSQL/flexibleServers"]
    metric:
      - numbackends
      - client_connections_active
      - client_connections_waiting
      - server_connections_active
      - server_connections_idle
      - total_pooled_connections
      - num_pools
    interval: ["PT15M"]
    timespan: ["PT15M"]
    metricFilter: ["DatabaseName eq '*'"]
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

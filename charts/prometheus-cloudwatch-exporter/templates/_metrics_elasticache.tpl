{{/*
AWS Metrics Elasticache
*/}}
{{- define "prometheus-cloudwatch-exporter.elasticache" -}}
{{- range .Values.services.elasticache.metricNames }}
- aws_dimensions:
    - CacheClusterId
  aws_metric_name: {{ . }}
  aws_namespace: AWS/ElastiCache
  delay_seconds: {{ $.Values.services.elasticache.delaySeconds | default "300" | int }}
  use_get_metric_data: {{ $.Values.useGetMetricData }}
{{- end }}
{{- end }}

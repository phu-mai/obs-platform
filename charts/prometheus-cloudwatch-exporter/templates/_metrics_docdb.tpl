{{/*
AWS Metrics DocumentDB
*/}}
{{- define "prometheus-cloudwatch-exporter.docdb" -}}
{{- range .Values.services.docdb.metricNames }}
- aws_dimensions:
    - DBClusterIdentifier
    - Role
  aws_metric_name: {{ . }}
  aws_namespace: AWS/DocDB
  delay_seconds: {{ $.Values.services.docdb.delaySeconds | default "300" | int }}
  use_get_metric_data: {{ $.Values.useGetMetricData }}
{{- end }}
{{- end }}

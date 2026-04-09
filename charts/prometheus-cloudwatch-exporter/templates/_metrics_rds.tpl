{{/*
AWS Metrics RDS
*/}}
{{- define "prometheus-cloudwatch-exporter.rds" -}}
{{- range .Values.services.rds.metricNames }}
- aws_dimensions:
    - DBInstanceIdentifier
  aws_metric_name: {{ . }}
  aws_namespace: AWS/RDS
  delay_seconds: {{ $.Values.services.rds.delaySeconds | default "300" | int }}
  use_get_metric_data: {{ $.Values.useGetMetricData }}
{{- end }}
{{- end }}

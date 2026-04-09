{{/*
AWS Metrics MSK
*/}}
{{- define "prometheus-cloudwatch-exporter.msk" -}}
{{- range .Values.services.msk.clusterName }}
- aws_dimensions:
    - Cluster Name
  aws_namespace: AWS/Kafka
  aws_metric_name: {{ . }}
  delay_seconds: {{ $.Values.services.msk.delaySeconds | default "300" | int }}
  use_get_metric_data: {{ $.Values.useGetMetricData }}
{{- end }}
{{- range .Values.services.msk.clusterNameBrokerID }}
- aws_dimensions:
    - Cluster Name
    - Broker ID
  aws_namespace: AWS/Kafka
  aws_metric_name: {{ . }}
  delay_seconds: {{ $.Values.services.msk.delaySeconds | default "300" | int }}
  use_get_metric_data: {{ $.Values.useGetMetricData }}
{{- end }}
{{- range .Values.services.msk.clusterNameConsumerGroupTopic }}
- aws_dimensions:
    - Cluster Name
    - Consumer Group
    - Topic
  aws_namespace: AWS/Kafka
  aws_metric_name: {{ . }}
  delay_seconds: {{ $.Values.services.msk.delaySeconds | default "300" | int }}
  use_get_metric_data: {{ $.Values.useGetMetricData }}
{{- end }}
{{- end }}

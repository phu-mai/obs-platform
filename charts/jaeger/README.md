# Jaeger Standalone

Helm chart for Jaeger Standalone deployment with badger storage backend.

Ref. <https://www.jaegertracing.io/docs/1.18/deployment/#badger---local-storage/>

This helm chart is made particularly for HSBC where Grafana Tempo isn't allowed to be deployed due to AGPL license. Ref. <https://grafana.com/blog/2021/04/20/grafana-loki-tempo-relicensing-to-agplv3/>

## How to install

Install jaeger in specific namespace

```bash
helm upgrade --install jaeger <path_to_chart> -n <namespace> --create-namespace
```

Update helm values to match your needs.

```yaml
containerPorts:
  - name: zinkin
    port: 9411
    protocol: TCP
  - name: otel-grpc
    port: 4317
    protocol: TCP
  - name: jaeger-thrift
    port: 14268
    protocol: TCP
  - name: admin-ui
    port: 16686
    protocol: TCP

resources:
  requests:
    cpu: 100m
    memory: 1Gi
  limits:
    cpu: 1000m
    memory: 2.5Gi

persistence:
  storageClassName: <storage_class_name>
  size: 30Gi
```

Note: List of supported ports <https://www.jaegertracing.io/docs/1.47/getting-started/#all-in-one/>

## How to validate setup

Deploy client tracing to reproduce trace

```bash
kubectl apply -f client-tracing.yaml -n <namespace>
```

Access client tracing UI http://localhost:8080 and produce trace by clicking on blue buttons. Trace ID then can be found in log of client-tracing pod

```bash
kubectl port-forward pod/client-tracing-675589487c-tpd2f 8080:8080 -n <namespace>
```

Access Jaeger UI

```bash
kubectl port-forward svc/jaeger 16686:16686 -n <namespace>
```

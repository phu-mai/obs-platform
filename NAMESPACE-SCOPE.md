# How to deploy kube-prometheus-stack with namespace scope

Sample value for namespace scope deployment can be found here [here](./ci/namespace-scope/values.yaml)

## Understand kube-prometheus-stack

`kube-prometheus-stack` is a bundle helm charts of the following dependencies and each dependency will have their own RBAC setup.

- grafana
- kube-state-metrics
- prometheus-node-exporter
- prometheus-operator

Refer below guideline to disable/enable specific components

### Disable PSP(Pod Security Policy)

According to Kubernetes Announcement, PSP will be deprecated starting from `1.21`. So avoid spending more efforts to handle namespace scope for PSP, then it will be disabled in all namespace deployment
Ref: <https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/>

### Disable Cluster APIs monitoring

Since monitoring scope is limited to resources in provided namespaces so we don't need to monitor below components

```yaml
coreDns:
  enabled: false
kubeApiServer:
  enabled: false
kubeControllerManager:
  enabled: false
kubeEtcd:
  enabled: false
kubeDns:
  enabled: false
kubeScheduler:
  enabled: false
kubeProxy:
  enabled: false
kubelet:
  enabled: false
nodeExporter:
  enabled: false
```

### Enable namespace scope for grafana

Deploy grafana in namespace scope is builtin supported.

Set `namespaced` as below to enable namespace scope deployment

```
grafana:
  enabled: true
  rbac:
    namespaced: true
    pspEnabled: false
```

### Enable namespace scope for kube-state-metrics

Deploy kube-state-metrics in namespace scope is builtin supported.

Set `namespaces` and set `useClusterRole` as below to enable namespace scope deployment

```yaml
kube-state-metrics:
  rbac:
    useClusterRole: false
  podSecurityPolicy:
    enabled: false
  namespaces: monitoring,lxp-data,lxp-core,lxp-frontend,lxp-integration
```

### Enable namespace scope for prometheus operator

Set `customRbac.create` to `true` and define `customRbac.namespaces` that needs to be monitored

```yaml
global:
  customRbac:
    create: true
    namespaces:
      - monitoring
      - lxp-data
      - lxp-core
  rbac:
    pspEnabled: false
```

Set prometheus-operator to be watch CRD only in specific namespaces

```yaml
prometheusOperator:
  kubeletService:
    enabled: false
  namespaces:
    additional:
      - monitoring
      - lxp-data
      - lxp-core
```

### Create servicemonitor/podmonitor

Create `PodMonitor` or `ServiceMonitor` in same namespace with prometheus and you should see target scraped by prometheus

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  annotations:
    meta.helm.sh/release-name: redis
    meta.helm.sh/release-namespace: monitoring
  labels:
    app.kubernetes.io/instance: redis
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: redis
    helm.sh/chart: redis-15.6.1
    observability: prometheus-operator
  name: redis
  namespace: monitoring
spec:
  endpoints:
    - interval: 30s
      port: http-metrics
  namespaceSelector:
    matchNames:
      - lxp-data
  selector:
    matchLabels:
      app.kubernetes.io/component: metrics
      app.kubernetes.io/instance: redis
      app.kubernetes.io/name: redis
```

## Config promtail to keep logs of specific namespaces

```yaml
promtail:
  enabled: true
  namespaceOverride: logging
  resources:
    limits:
      cpu: 200m
      memory: 128Mi
    requests:
      cpu: 100m
      memory: 128Mi
  rbac:
    pspEnabled: false
  config:
    snippets:
      pipelineStages:
      - cri: {}
      - match:
          selector: '{namespace!~"monitoring|logging|lxp-core|lxp-data|lxp-integration|lxp-frontend|istio-system"}'
          action: drop
      - match:
          selector: '{fmop="true"}'
          stages:
          - json:
              expressions:
                log: log
          - json:
              expressions:
                level: level
              source: log
          - labels:
              level:
      extraRelabelConfigs:
        - action: labelmap
          regex: __meta_kubernetes_pod_label_leap_expert_(.+)
    clients:
      - url: http://observability-loki:3100/loki/api/v1/push
        tenant_id: tenant-id
        external_labels:
          cluster: cluster-name
        basic_auth:
          username: foo
          password: bar
```

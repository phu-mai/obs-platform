# Deployment Notes

## Azure Active Directory App Registration

Steps to register an app and assign role to app on subscription

* An application must be registered by follow these step
  * On Azure Portal search Azure Active Directory
  * Click on App registrations
  * Add New application registration

* Configure registered application must have reading permission to Azure Monitor
  * On Azure Portal choose Subscriptions
  * Select your subcriiption
  * Click on Access control (IAM)
  * Click on Role assignments then click on Add and select Add role assignment from drop list
  * Assign Role "Monitoring Reader" and select your_app_created_in_above_step

## Define helm values

Reference helm values is below

```yaml
fullnameOverride: azure-metrics-exporter

service:
  type: ClusterIP
  port: 8080

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi

env:
  - name: DEBUG
    value: "true"
  - name: VERBOSE
    value: "true"
  - name: DEVELOPMENT_WEBUI
    value: "true"
  - name: AZURE_SERVICEDISCOVERY_CACHE
    value: "5m"
  - name: AZURE_CLIENT_ID
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  - name: AZURE_TENANT_ID
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  - name: AZURE_CLIENT_SECRET
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  - name: AZURE_SUBSCRIPTION_ID
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

podMonitor:
  additionalLabels:
    observability: prometheus-operator
  podMetricsEndpoints:
    params:
      name: ["azure-metric-eventhub"]
      subscription:
        - xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
      template: ["{name}_{metric}_{unit}"]
      filter: ["resourceType eq 'Microsoft.EventHub/namespaces'"]
      metric:
        - ActiveConnections
        - ConnectionsClosed
        - ConnectionsOpened
        - IncomingMessages
        - IncomingRequests
        - OutgoingBytes
        - OutgoingMessages
        - QuotaExceededErrors
        - ServerErrors
        - Size
        - SuccessfulRequests
        - ThrottledRequests
        - UserErrors
      interval: ["PT15M"]
      timespan: ["PT15M"]
      aggregation:
        - average
        - total
```

## What need to be updated

### Input Azure AD register app credential

* AZURE_CLIENT_ID
* AZURE_TENANT_ID
* AZURE_CLIENT_SECRET
* AZURE_SUBSCRIPTION_ID

```yaml
env:
  - name: DEBUG
    value: "true"
  - name: VERBOSE
    value: "true"
  - name: DEVELOPMENT_WEBUI
    value: "true"
  - name: AZURE_SERVICEDISCOVERY_CACHE
    value: "5m"
  - name: AZURE_CLIENT_ID
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  - name: AZURE_TENANT_ID
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  - name: AZURE_CLIENT_SECRET
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  - name: AZURE_SUBSCRIPTION_ID
    value: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

### Update list Azure metrics and resources

The following information can be collected here <https://docs.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-supported>

* Resource Type
* Metrics
* Aggregation Type

```yaml
podMonitor:
  additionalLabels:
    observability: prometheus-operator
  podMetricsEndpoints:
    params:
      name: ["azure-metric-eventhub"]
      subscription:
        - xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
      template: ["{name}_{metric}_{unit}"]
      filter: ["resourceType eq 'Microsoft.EventHub/namespaces'"]
      metric:
        - ActiveConnections
        - ConnectionsClosed
        - ConnectionsOpened
        - IncomingMessages
        - IncomingRequests
        - OutgoingBytes
        - OutgoingMessages
        - QuotaExceededErrors
        - ServerErrors
        - Size
        - SuccessfulRequests
        - ThrottledRequests
        - UserErrors
      interval: ["PT15M"]
      timespan: ["PT15M"]
      aggregation:
        - average
        - total
```

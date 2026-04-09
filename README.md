# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Chart operations](#chart-operations)
    - [Add new sub-chart](#add-new-sub-chart)
    - [Upgrade sub-chart version](#upgrade-sub-chart-version)
  - [Generate helm chart template](#generate-helm-chart-template)
    - [Package and release observability chart](#package-and-release-observability-chart)
  - [CI Notes](#ci-notes)
    - [Update supports Kubernetes list](#update-supports-kubernetes-list)
  - [Cloud Monitoring](#cloud-monitoring)
    - [AWS Cloudwatch exporter access request](#aws-cloudwatch-exporter-access-request)
    - [AWS EC2 service discovery config access request](#aws-ec2-service-discovery-config-access-request)
    - [Azure metrics exporter access request](#azure-metrics-exporter-access-request)
  - [How to fix CVE for kube-webhook-certgen](#how-to-fix-cve-for-kube-webhook-certgen)
  - [How to get started with grafanalib](#how-to-get-started-with-grafanalib)
  - [Configure prometheus-kafka-exporter for Azure Eventbus and AWS MSK](#configure-prometheus-kafka-exporter-for-azure-eventbus-and-aws-msk)
    - [Azure Eventbus](#azure-eventbus)
    - [AWS MSK](#aws-msk)

## Introduction
The Observability charts for Kubernetes. Easy install of a full observability stack into a k8s cluster with a CLI tool or Helm charts

## Chart operations

### Add new sub-chart

Pull helm chart

```bash
# Add new helm repository
helm repo add grafana https://grafana.github.io/helm-charts

# Update helm repo to get latest chart version
helm repo update

# Pull latest helm chart
cd charts
helm pull grafana/tempo

# Pull specific helm chart version
cd charts
helm pull grafana/tempo --version 0.9.0

# Uncompress helm chart tgz
tar xvf tempo-0.9.0.tgz
rm tempo-0.9.0.tgz
```

Update `Chart.yaml` to add new dependency charts

```yaml
dependencies:
  - name: tempo
    version: "4.0.*"
    repository: "file://../charts/tempo" # This is to load local charts
    condition: tempo.enabled
```

Update default values for new chart in `values.yaml`

```yaml
---
tempo:
  enabled: false
```

### Upgrade sub-chart version

Follow steps in [How to add new helm chart](#How-to-add-new-helm-chart)

## Generate helm chart template

Update helm values under directory `values/`

```bash

# Install needed tools for CI
brew install yq
brew install prometheus

# Generate release file for envs that are not managed by ArgoCD
make release env=<environment name>

# Verify template generation for namespace-scope and cluster-scope
make release env=<environment name>

# Create chart release based on chart version
make chart

# Clean up the test
make clean
```

### Package and release observability chart

Make sure chart version has been updated correctly in `Chart.yaml`.
First we create a tag to release:

```bash
git tag 1.22.4
```

Then push the new tag:

```bash
git push --tags
```

This will push the new tag to the repo. Then we will need to create a release for this tag manually from Github release page.

After that, we need to package the chart and push to the helm repository:

```bash
make chart
```

## CI Notes

### Update supports Kubernetes list

Login to CircleCI console > Select project `observability-chart` > Select `Project Setting` > Select `Environment Variables`

To add environment variables > Select `Add Environment Variables` > Input below `Name` and `Value`

```text
Name: KUBERNETES_VERSIONS
Value: v1.23.0,v1.24.0,v1.25.0
```

## Cloud Monitoring

### AWS Cloudwatch exporter access request

Create IAM Policy with actions to list and get metrics from AWS CloudWatch. The permission `tag:GetResources` is needed when you need to monitor resources by tag.

Attach policy to an IAM User and provide IAM User programmatic credentials.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "tag:GetResources",
                "cloudwatch:GetMetricData",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```

### AWS EC2 service discovery config access request

Create IAM Policy with actions to describe EC2 instances.

Attach policy to an IAM User and provide IAM User programmatic credentials.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeTags",
                "ec2:DescribeSnapshots"
            ],
            "Resource": "*"
        }
    ]
}
```

### Azure metrics exporter access request

Step to register an app and assign role to app on specific subscription:

- Register an application: `Azure Active Directory` > `App registrations` > `New application registration` > Input `< app_name >`
- Permission associate to Azure Monitor App: `Subscriptions` > `Select Subscription` > `Access control (IAM)` > `Role assignments` > `Add` > `Add role assignment` > Role : `"Monitoring Reader"` > Select `< app_name >`.

## How to fix CVE for kube-webhook-certgen

Clone code repository from kube-webhook-certgen

```bash
$ git clone https://github.com/kubernetes/ingress-nginx.git
$ cd ingress-nginx
$ ll images/
-rw-r--r--  1 user  user   2.3K May 29 14:47 Makefile
-rw-r--r--  1 user  user   934B May 29 14:42 README.md
drwxr-xr-x  5 user  user   160B May 29 14:42 cfssl
drwxr-xr-x  6 user  user   192B May 29 14:42 custom-error-pages
drwxr-xr-x  5 user  user   160B May 29 14:42 e2e-test-echo
drwxr-xr-x  5 user  user   160B May 29 14:42 ext-auth-example-authsvc
drwxr-xr-x  5 user  user   160B May 29 14:42 fastcgi-helloserver
drwxr-xr-x  5 user  user   160B May 29 14:42 go-grpc-greeter-server
drwxr-xr-x  5 user  user   160B May 29 14:42 httpbun
drwxr-xr-x  8 user  user   256B May 29 14:42 kube-webhook-certgen
drwxr-xr-x  8 user  user   256B May 29 14:42 nginx
drwxr-xr-x  7 user  user   224B May 29 14:42 nginx-1.25
drwxr-xr-x  7 user  user   224B May 29 14:42 opentelemetry
drwxr-xr-x  6 user  user   192B May 29 14:42 test-runner
```

Update TAG in `images/kube-webhook-certgen/TAG` to specific tag (e.g `1.9.1`)

Update platform for image build `images/Makefile` to `PLATFORMS?=linux/amd64` and build image for kube-webhook-certgen

```bash
$ make NAME=kube-webhook-certgen push
done
cat: kube-webhook-certgen/EXTRAARGS: No such file or directory
docker buildx build \
                --label=org.opencontainers.image.source=https://github.com/kubernetes/ingress-nginx \
                --label=org.opencontainers.image.licenses=Apache-2.0 \
                --label=org.opencontainers.image.description="Ingress NGINX kube-webhook-certgen image" \
                --build-arg BASE_IMAGE=registry.k8s.io/ingress-nginx/nginx-1.25:v0.0.6@sha256:b3e027ab191eb9461a9bcf25092eabb1d547cba164992dbd722c1aa2b4a936ee \
                --build-arg GOLANG_VERSION=1.22.2 \
                --platform=linux/amd64 --push \
                --progress=plain \
                --pull  \
                -t local/kube-webhook-certgen:v1.9.2 kube-webhook-certgen/rootfs
#0 building with "desktop-linux" instance using docker driver

#14 ERROR: denied: requested access to the resource is denied
------
 > pushing local/kube-webhook-certgen:v1.9.2 with docker:
```

Docker tag image `local/kube-webhook-certgen:v1.9.2` to expected registry

```bash
docker tag local/kube-webhook-certgen:v1.9.2 <image_registry>/kube-webhook-certgen:v1.9.2
```

## How to get started with grafanalib

`grafanalib` is just a Python package. So you can init virtual environment for python as below command

```bash
python -m venv .venv
```

Activate python virtualenv

```bash
source .venv/bin/activate
```

Generate dashboard to json

```bash
generate-dashboard -o lxp-mixin/lxp-cheatsheet-promql.json lxp-mixin/lxp-cheatsheet-promql.dashboard.py
```

## Configure prometheus-kafka-exporter for Azure Eventbus and AWS MSK

### Azure Eventbus

Define helm values as below

```yaml
prometheus-kafka-exporter:
  verbosity: 1
  extraArgs:
    - --log.level=debug
  kafkaServer:
    - example-namespace.servicebus.windows.net:9093
  kafkaBrokerVersion: "1.0.0"
  tls:
    enabled: true
    insecureSkipVerify: true
  sasl:
    enabled: true
    handshake: false
    scram:
      enabled: true
      mechanism: plain
      username: example_user
      password: example_password
```

The output of generated command in deployment manifest should be as below:

```bash
./kafka_exporter \
  --kafka.server='example-namespace.servicebus.windows.net:9093' \
  --sasl.enabled \
  --sasl.mechanism='plain' \
  --sasl.username='$ConnectionString' \
  --sasl.password='Endpoint=sb://example-namespace.servicebus.windows.net/;SharedAccessKeyName=<redacted>;SharedAccessKey=<redacted>' \
  --tls.enabled \
  --tls.insecure-skip-tls-verify \
  --log.level=debug \
  --verbosity=1 \
  --kafka.version=1.0.0
```

### AWS MSK

Define helm values as below

```yaml
prometheus-kafka-exporter:
  verbosity: 1
  extraArgs:
    - --log.level=debug
  kafkaServer:
    - kafka-headless.lxp-data.svc.cluster.local:9092
```

The output of generated command in deployment manifest should be as below:

```bash
./kafka_exporter --kafka.server=kafka-headless.lxp-data.svc.cluster.local:9092 \
  --log.level=debug \
  --verbosity=1
```
# obs-obs-platform
# obs-obs-platform

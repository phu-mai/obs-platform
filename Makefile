export CHART_VERSION := $$(cat Chart.yaml| grep '^version' | awk '{print $$2}')

clean:
	@-rm -rf test/*
	@-rm -rf *.tgz
	@-rm -rf lxp-mixin/*.json

generate:
	@-echo "------------------Verify template generation for cluster-scope------------------"
	@-helm template observability . -f ci/cluster-scope/values.yaml \
			--namespace monitoring \
			--output-dir test/ci/cluster-scope \
			--api-versions monitoring.coreos.com/v1 \
			--api-versions monitoring.coreos.com/v1/ServiceMonitor \
			--api-versions cert-manager.io/v1 \
			--api-versions networking.istio.io/v1beta1 \
			--api-versions telemetry.istio.io/v1alpha1 \
			--set prometheusAzureMetricsExporter.enabled=true \
			--set prometheusKafkaExporter.enabled=true ;
	@-echo "------------------Verify template generation for namespace-scope------------------"
	@-helm template observability . -f ci/namespace-scope/values.yaml \
			--namespace monitoring \
			--output-dir test/ci/namespace-scope \
			--api-versions monitoring.coreos.com/v1 \
			--api-versions monitoring.coreos.com/v1/ServiceMonitor \
			--api-versions cert-manager.io/v1 \
			--api-versions networking.istio.io/v1beta1 \
			--api-versions telemetry.istio.io/v1alpha1;

	@-echo "------------------Reformat alert rules for promtool check for cluster-scope------------------"
	@-mkdir test/ci/cluster-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules-eval
	@-for i in $$(ls test/ci/cluster-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules/); \
			do yq eval '.spec' test/ci/cluster-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules/$$i \
			> test/ci/cluster-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules-eval/$$i; done
	@-echo "------------------Reformat alert rules for promtool check for namespace-scope------------------"
	@-mkdir test/ci/namespace-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules-eval
	@-for i in $$(ls test/ci/namespace-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules/); \
			do yq eval '.spec' test/ci/namespace-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules/$$i \
			> test/ci/namespace-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules-eval/$$i; done

	@-echo "------------------Validate alerting rules for cluster-scope------------------"
	@-promtool check rules test/ci/cluster-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules-eval/*.yaml
	@-echo "------------------Validate alerting rules for namespace-scope------------------"
	@-promtool check rules test/ci/namespace-scope/observability/charts/kube-prometheus-stack-add-ons/templates/rules-eval/*.yaml

	@-echo "------------------List of charts------------------"
	@-ls test/*/*/*/* | awk '{print $0}'
	@-echo ""

chart:
	@-mkdir -p test/observability-${CHART_VERSION}
	@-helm package .
	@-tar xvf observability-${CHART_VERSION}.tgz -C test/observability-${CHART_VERSION}
	@-echo "------------------List of files/folders in release------------------"
	@-ls test/observability-${CHART_VERSION}/observability/charts | awk '{print $0}'

dashboard:
	@-echo "------------------Generate lxp-mixin dashboards------------------"
	@-python -m venv .venv && \
		source .venv/bin/activate && \
		pip install -r requirements.txt &&\
		for i in $$(ls lxp-mixin | grep "py$$" | cut -d '.' -f1); \
			do echo "Generating $$i.json" && \
				generate-dashboard -o lxp-mixin/$$i.json lxp-mixin/$$i.dashboard.py; done

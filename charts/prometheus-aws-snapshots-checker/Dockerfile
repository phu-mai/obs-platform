FROM amazon/aws-cli:2.11.17
RUN yum update -y && \
    yum upgrade -y && \
    yum install -y jq && \
    yum clean all && \
    rm -rf /var/cache/yum
ENTRYPOINT ["/bin/bash"]

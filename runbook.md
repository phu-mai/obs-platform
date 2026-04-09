# Table of Contents

- [Table of Contents](#table-of-contents)
- [Core Services](#core-services)
  - [Vault](#vault)
    - [Alert Name: "VaultPodIsSealed"](#alert-name-vaultpodissealed)
    - [Alert Name: "VaultHasNoActiveNode"](#alert-name-vaulthasnoactivenode)
  - [Messaging](#messaging)
  - [Minio](#minio)
    - [Alert Name: "MinioOfflineDisks"](#alert-name-minioofflinedisks)
- [Middleware Services](#middleware-services)
  - [Elasticsearch](#elasticsearch)
    - [Alert Name: "ElasticsearchClusterRed"](#alert-name-elasticsearchclusterred)
    - [Alert Name: "ElasticsearchClusterYellow"](#alert-name-elasticsearchclusteryellow)
    - [Alert Name: "ElasticsearchHeapUsageTooHigh"](#alert-name-elasticsearchheapusagetoohigh)
    - [Alert Name: "ElasticsearchHeapUsageWarning"](#alert-name-elasticsearchheapusagewarning)
    - [Alert Name: "ElasticsearchUnhealthyNodes"](#alert-name-elasticsearchunhealthynodes)
    - [Alert Name: "ElasticsearchUnassignedShards"](#alert-name-elasticsearchunassignedshards)
  - [Kafka](#kafka)
    - [Alert Name: "KafkaDown"](#alert-name-kafkadown)
    - [Alert Name: "KafkaUnhealthyBroker"](#alert-name-kafkaunhealthybroker)
    - [Alert Name: "KafkaMemoryLow"](#alert-name-kafkamemorylow)
    - [Alert Name: "KafkaOfflinePartitionCount"](#alert-name-kafkaofflinepartitioncount)
    - [Alert Name: "KafkaHasNoActiveController"](#alert-name-kafkahasnoactivecontroller)
    - [Alert Name: "KafkaUnderReplicatedPartition"](#alert-name-kafkaunderreplicatedpartition)
    - [Alert Name: "KafkaConsumerGroupLag"](#alert-name-kafkaconsumergrouplag)
    - [Alert Name: "StrimziFoundNoKafkaResources"](#alert-name-strimzifoundnokafkaresources)
    - [Alert Name: "StrimziKafkaResourceNotReady"](#alert-name-strimzikafkaresourcenotready)
  - [MongoDB](#mongodb)
    - [Alert Name: "MongodbDown"](#alert-name-mongodbdown)
    - [Alert Name: "MongoStatefulsetUnscheduable"](#alert-name-mongostatefulsetunscheduable)
    - [Alert Name: "MongoReplicationLag"](#alert-name-mongoreplicationlag)
    - [Alert Name: "MongoReplsetMermberUnhealthy"](#alert-name-mongoreplsetmermberunhealthy)
    - [Alert Name: "MongoReplsetMemberInRecoveringState"](#alert-name-mongoreplsetmemberinrecoveringstate)
    - [Alert Name: "MongoReplsetMemberUnknown"](#alert-name-mongoreplsetmemberunknown)
    - [Alert Name: "MongoReplsetMemberUnreachable"](#alert-name-mongoreplsetmemberunreachable)
    - [Alert Name: "MongoReplsetMemberRollback"](#alert-name-mongoreplsetmemberrollback)
    - [Alert Name: "MongoReplsetMemberRemoved"](#alert-name-mongoreplsetmemberremoved)
    - [Alert Name: "MongoHighConnections"](#alert-name-mongohighconnections)
    - [Alert Name: "MongodbCursorsOpenTooMany"](#alert-name-mongodbcursorsopentoomany)
    - [Alert Name: "MongodbCursorsTimeouts"](#alert-name-mongodbcursorstimeouts)
  - [Redis](#redis)
    - [Alert Name: "RedisDown"](#alert-name-redisdown)
    - [Alert Name: "RedisOutOfConfiguredMaxmemory"](#alert-name-redisoutofconfiguredmaxmemory)
    - [Alert Name: "RedisTooManyConnections"](#alert-name-redistoomanyconnections)
    - [Alert Name: "RedisRejectedConnections"](#alert-name-redisrejectedconnections)
    - [Alert Name: "RedisStatefulsetUnscheduable"](#alert-name-redisstatefulsetunscheduable)
  - [Postgres](#postgres)
    - [Alert Name: "PostgresDown"](#alert-name-postgresdown)
    - [Alert Name: "PostgresExporterDown"](#alert-name-postgresexporterdown)
    - [Alert Name: "PostgresReplicationLag"](#alert-name-postgresreplicationlag)
    - [Alert Name: "PostgresDelayedReplicaLagAboveThreshold"](#alert-name-postgresdelayedreplicalagabovethreshold)
    - [Alert Name: "PostgresLongRunningQueriesCount"](#alert-name-postgreslongrunningqueriescount)
    - [Alert Name: "PostgresLongLivedTransaction"](#alert-name-postgreslonglivedtransaction)
    - [Alert Name: "PostgresXlogNoConsumption"](#alert-name-postgresxlognoconsumption)
    - [Alert Name: "PostgresConnectionsTooHigh"](#alert-name-postgresconnectionstoohigh)
    - [Alert Name: "PostgresVacuumAgeInSeconds"](#alert-name-postgresvacuumageinseconds)
    - [Alert Name: "PostgresVacuumAnalyzeAgeInSeconds"](#alert-name-postgresvacuumanalyzeageinseconds)
    - [Alert Name: "PostgresStatDatabaseTempBytes"](#alert-name-postgresstatdatabasetempbytes)
    - [Alert Name: "PostgresLocksCount"](#alert-name-postgreslockscount)
    - [Alert Name: "PostgresStatefulsetUnscheduable"](#alert-name-postgresstatefulsetunscheduable)
    - [Alert Name: "PostgresSuperuserCount"](#alert-name-postgressuperusercount)
  - [Zookeeper](#zookeeper)
    - [Alert Name: "ZookeeperDown"](#alert-name-zookeeperdown)
    - [Alert Name: "ZookeeperMissingLeader"](#alert-name-zookeepermissingleader)
    - [Alert Name: "ZookeeperQuorumSize"](#alert-name-zookeeperquorumsize)
    - [Alert Name: "ZooKeeperMemoryLow"](#alert-name-zookeepermemorylow)
    - [Alert Name: "ZooKeeperStatefulsetUnscheduable"](#alert-name-zookeeperstatefulsetunscheduable)
  - [Istio](#istio)
    - [Alert Name: "IstioDeploymentNotReady"](#alert-name-istiodeploymentnotready)
    - [Alert Name: "IstioHigh4xxErrorRateByDestinationPercentage"](#alert-name-istiohigh4xxerrorratebydestinationpercentage)
    - [Alert Name: "IstioHigh5xxErrorRateByDestinationPercentage"](#alert-name-istiohigh5xxerrorratebydestinationpercentage)
    - [Alert Name: "IstioGrpcDeadlineExceededErrors"](#alert-name-istiogrpcdeadlineexceedederrors)
    - [Alert Name: "IstioGrpcDeadlineExceededErrorsToIntegrations"](#alert-name-istiogrpcdeadlineexceedederrorstointegrations)
  - [Velero](#velero)
    - [Alert Name: "VeleroBackupPartialFailures"](#alert-name-velerobackuppartialfailures)
    - [Alert Name: "VeleroBackupFailed"](#alert-name-velerobackupfailed)
  - [Cert-manager](#cert-manager)
    - [Alert Name: "CertManagerAbsent"](#alert-name-certmanagerabsent)
    - [Alert Name: "CertManagerCertExpirySoon"](#alert-name-certmanagercertexpirysoon)
    - [Alert Name: "CertManagerCertNotReady"](#alert-name-certmanagercertnotready)
    - [Alert Name: "CertManagerHittingRateLimits"](#alert-name-certmanagerhittingratelimits)
  - [Prometheus](#prometheus)
    - [Alert Name: "PrometheusTenantDisappeared"](#alert-name-prometheustenantdisappeared)
- [App](#app)
  - [Common Application Alerts](#common-application-alerts)
    - [Alert Name: "AppExecutionSlow"](#alert-name-appexecutionslow)
    - [Alert Name: "KafkaClientHasLostConnections"](#alert-name-kafkaclienthaslostconnections)
    - [Alert Name: "KafkaClientProducerException"](#alert-name-kafkaclientproducerexception)
    - [Alert Name: "KafkaClientConsumerException"](#alert-name-kafkaclientconsumerexception)
    - [Alert Name: "RedisClientHasLostConnections"](#alert-name-redisclienthaslostconnections)
    - [Alert Name: "MongodbClientHasLostConnections"](#alert-name-mongodbclienthaslostconnections)
    - [Alert Name: "ServiceErrorLogs"](#alert-name-serviceerrorlogs)
  - [Application Alerts](#application-alerts)
    - [API-Server Service](#api-server-service)
      - [Alert Name: "SSOLoginFailed"](#alert-name-ssologinfailed)
    - [Audit Service](#audit-service)
      - [Alert Name: "AuditExportResultsFailed"](#alert-name-auditexportresultsfailed)
      - [Alert Name: "AuditRecoverMatrixRoomRequestFailed"](#alert-name-auditrecovermatrixroomrequestfailed)
    - [Data Retention](#data-retention)
      - [Alert Name: "AuditDataRetentionIsDelayed"](#alert-name-auditdataretentionisdelayed)
      - [Alert Name: "AuditPeriodicPollNotWorking"](#alert-name-auditperiodicpollnotworking)
      - [Alert Name: "AuditDataRetentionJobFailed"](#alert-name-auditdataretentionjobfailed)
      - [Alert Name: "AuditDataRetentionJobPartiallyFailed"](#alert-name-auditdataretentionjobpartiallyfailed)
      - [Alert Name: "AuditDataRetentionPendingJobs"](#alert-name-auditdataretentionpendingjobs)
      - [Alert Name: "AuditDataRetentionMediaFileFailed"](#alert-name-auditdataretentionmediafilefailed)
      - [Alert Name: "L2AuditContainerOOMKilled"](#alert-name-l2auditcontaineroomkilled)
      - [Alert Name: "SearchDataRetentionDocsDeletionFailed"](#alert-name-searchdataretentiondocsdeletionfailed)
      - [Alert Name: "ProxymessagingDataRetentionPurgeMartrixRoomFailed"](#alert-name-proxymessagingdataretentionpurgemartrixroomfailed)
      - [Alert Name: "AuditDataRetentionMatrixRoomPurgeFailed"](#alert-name-auditdataretentionmatrixroompurgefailed)
      - [Alert Name: "AuditDataRetentionDeleteEntityFailed"](#alert-name-auditdataretentiondeleteentityfailed)
      - [Alert Name: "ProxymessagingDataRetentionRedactEventFailed"](#alert-name-proxymessagingdataretentionredacteventfailed)
    - [Authentication Service](#authentication-service)
      - [Alert Name: "AuthenticationLoginFailed"](#alert-name-authenticationloginfailed)
      - [Alert Name: "AuthorizationRequestFailed"](#alert-name-authorizationrequestfailed)
      - [Alert Name: "AuthenticationVaultRequestFailed"](#alert-name-authenticationvaultrequestfailed)
      - [Alert Name: "AuthenticationKeycloakRequestFailed"](#alert-name-authenticationkeycloakrequestfailed)
    - [Whatsapp Archived Gateway Service](#whatsapp-archived-gateway-service)
      - [Alert Name: "WAGClientOutdated"](#alert-name-wagclientoutdated)
    - [Whatsapp Integration Archived Service](#whatsapp-integration-archived-service)
      - [Alert Name: "WAAEmailRegistrationInstructionFailed"](#alert-name-waaemailregistrationinstructionfailed)
      - [Alert Name: "WAAImportMessageMaxRetryExceeded"](#alert-name-waaimportmessagemaxretryexceeded)
    - [Whatsapp Native Integration Service](#whatsapp-native-integration-service)
      - [Alert Name: "WhatsappNativeSendMediaTemplateFailed"](#alert-name-whatsappnativesendmediatemplatefailed)
      - [Alert Name: "WhatsappNativeSendCloudMessageError"](#alert-name-whatsappnativesendcloudmessageerror)
      - [Alert Name: "WhatsappNativeSendCloudMessage2xxError"](#alert-name-whatsappnativesendcloudmessage2xxerror)
    - [Wechat Native Integration Service](#wechat-native-integration-service)
      - [Alert Name: "WechatNativeEnableIntegrationFailed"](#alert-name-wechatnativeenableintegrationfailed)
      - [Alert Name: "WechatNativeDisableIntegrationFailed"](#alert-name-wechatnativedisableintegrationfailed)
      - [Alert Name: "WechatNativeCompleteIntegrationFailed"](#alert-name-wechatnativecompleteintegrationfailed)
      - [Alert Name: "WechatNativeOnboardingTriggerOtpFailed"](#alert-name-wechatnativeonboardingtriggerotpfailed)
      - [Alert Name: "WechatNativeOnboardingVerifyOtpFailed"](#alert-name-wechatnativeonboardingverifyotpfailed)
      - [Alert Name: "WechatNativeWechatServerApiCallFailed"](#alert-name-wechatnativewechatserverapicallfailed)
    - [Wechat Miniap Integration Service](#wechat-miniap-integration-service)
      - [Alert Name: "WechatMiniappEnableIntegrationFailed"](#alert-name-wechatminiappenableintegrationfailed)
      - [Alert Name: "WechatMiniappDisableIntegrationFailed"](#alert-name-wechatminiappdisableintegrationfailed)
      - [Alert Name: "WechatMiniappClientAuthenticationFailed"](#alert-name-wechatminiappclientauthenticationfailed)
      - [Alert Name: "WechatMiniappTriggerOTPFailed"](#alert-name-wechatminiapptriggerotpfailed)
      - [Alert Name: "WechatMiniappVerifyOTPFailed"](#alert-name-wechatminiappverifyotpfailed)
      - [Alert Name: "WechatMiniappGetOAFailed"](#alert-name-wechatminiappgetoafailed)
      - [Alert Name: "WechatMiniappGetWechatMiniappAccountFailed"](#alert-name-wechatminiappgetwechatminiappaccountfailed)
      - [Alert Name: "WechatMiniappCallAPIServerFailed"](#alert-name-wechatminiappcallapiserverfailed)
    - [Wecom Integration Service](#wecom-integration-service)
      - [Alert Name: "WecomSsoLoginStartFailed"](#alert-name-wecomssologinstartfailed)
      - [Alert Name: "WecomSsoLoginCompleteFailed"](#alert-name-wecomssologincompletefailed)
      - [Alert Name: "WecomContactUserCreateFailed"](#alert-name-wecomcontactusercreatefailed)
      - [Alert Name: "WecomContactClientCreateFailed"](#alert-name-wecomcontactclientcreatefailed)
      - [Alert Name: "WecomClientVerificationStartFailed"](#alert-name-wecomclientverificationstartfailed)
      - [Alert Name: "WecomClientVerificationCompleteFailed"](#alert-name-wecomclientverificationcompletefailed)
      - [Alert Name: "WecomTencentPlatformApiCallFailed"](#alert-name-wecomtencentplatformapicallfailed)
      - [Alert Name: "WecomTencentLicenseExpired"](#alert-name-wecomtencentlicenseexpired)
      - [Alert Name: "WecomTencentWhitelistIPMismatched"](#alert-name-wecomtencentwhitelistipmismatched)
      - [Alert Name: "WecomTencentInvalidSecret"](#alert-name-wecomtencentinvalidsecret)
    - [Customer Model Sync Service](#customer-model-sync-service)
      - [Alert Name: "CustomerModelSyncGraphAPIFailed"](#alert-name-customermodelsyncgraphapifailed)
      - [Alert Name: "CustomerModelSyncAntiphonyFailed"](#alert-name-customermodelsyncantiphonyfailed)
      - [Alert Name: "CustomerModelSyncAADFailed"](#alert-name-customermodelsyncaadfailed)
      - [Alert Name: "CustomerModelSyncMosaicFailed"](#alert-name-customermodelsyncmosaicfailed)
      - [Alert Name: "CustomerModelSyncSalesforcePullChangesFailed"](#alert-name-customermodelsyncsalesforcepullchangesfailed)
      - [Alert Name: "CustomerModelSyncSalesforceOauthFailed"](#alert-name-customermodelsyncsalesforceoauthfailed)
      - [Alert Name: "CustomerModelSyncSalesforceQueryFailed"](#alert-name-customermodelsyncsalesforcequeryfailed)
    - [SMS Integration Service](#sms-integration-service)
      - [Alert Name: "SMSRegisterAccountFailed"](#alert-name-smsregisteraccountfailed)
      - [Alert Name: "SMSUnregisterAccountFailed"](#alert-name-smsunregisteraccountfailed)
      - [Alert Name: "SMSSendMessageFailed"](#alert-name-smssendmessagefailed)
      - [Alert Name: "SMSReceiveMessageFailed"](#alert-name-smsreceivemessagefailed)
      - [Alert Name: "SMSSendMessageLatency"](#alert-name-smssendmessagelatency)
    - [iMessage Archiving Integration](#imessage-archiving-integration)
      - [Alert Name: "ImessageNumberOfIncomingMessageFailedDaily"](#alert-name-imessagenumberofincomingmessagefaileddaily)
      - [Alert Name: "ImessageTranscodeImageFailed"](#alert-name-imessagetranscodeimagefailed)
      - [Alert Name: "ImessageTranscodeAudioFailed"](#alert-name-imessagetranscodeaudiofailed)
      - [Alert Name: "ImessageGenerateThumbnailFailed"](#alert-name-imessagegeneratethumbnailfailed)
      - [Alert Name: "ImessageIncomingMessagesFailed"](#alert-name-imessageincomingmessagesfailed)
      - [Alert Name: "ImessageDownstreamServiceFailed"](#alert-name-imessagedownstreamservicefailed)
    - [Teams2B Integration Service](#teams2b-integration-service)
      - [Alert Name: "Teams2bRefreshSubscriptionWebhookFailed"](#alert-name-teams2brefreshsubscriptionwebhookfailed)
      - [Alert Name: "Teams2bRefreshSubscriptionCronJobFailed"](#alert-name-teams2brefreshsubscriptioncronjobfailed)
      - [Alert Name: "Teams2bIncomingTrafficDroppedWorkingDays"](#alert-name-teams2bincomingtrafficdroppedworkingdays)
      - [Alert Name: "Teams2bNoIncommingTrafficWorkingDays"](#alert-name-teams2bnoincommingtrafficworkingdays)
      - [Alert Name: "Teams2bOutgoingTrafficDroppedWorkingDays"](#alert-name-teams2boutgoingtrafficdroppedworkingdays)
      - [Alert Name: "Teams2bNoOutgoingTrafficWorkingDays"](#alert-name-teams2bnooutgoingtrafficworkingdays)
  - [Others](#others)
    - [Alert Name: "KubeContainerOOMKilled"](#alert-name-kubecontaineroomkilled)
    - [Alert Name: "KubeInitContainerOOMKilled"](#alert-name-kubeinitcontaineroomkilled)
    - [Alert Name: "KubeContainerLivenessProbeFailed"](#alert-name-kubecontainerlivenessprobefailed)
    - [Alert Name: "KubeManyNodesNotReady"](#alert-name-kubemanynodesnotready)
    - [Alert Name: "KubePodMemUsageHigh"](#alert-name-kubepodmemusagehigh)
    - [Alert Name: "KubePodCpuUsageHigh](#alert-name-kubepodcpuusagehigh)
    - [Alert Name: "KubePodFailedToPullImage"](#alert-name-kubepodfailedtopullimage)
- [Grafana Agent](#grafana-agent)
  - [AgentTracingReceiverErrors](#agenttracingreceivererrors)
  - [AgentTracingExporterErrors](#agenttracingexportererrors)
- [Cloud Services Monitoring](#cloud-services-monitoring)
  - [AWS Cloudwatch](#aws-cloudwatch)
    - [DocumentDBCPUUtilization](#documentdbcpuutilization)
    - [DocumentDBLowMemNumOperationsThrottled](#documentdblowmemnumoperationsthrottled)
    - [DocumentDBLowMemThrottleQueueDepth](#documentdblowmemthrottlequeuedepth)
    - [DocumentDBLowMemThrottleMaxQueueDepth](#documentdblowmemthrottlemaxqueuedepth)
    - [DocumentDBDatabaseConnections](#documentdbdatabaseconnections)
    - [DocumentDBBufferCacheHitRatio](#documentdbbuffercachehitratio)
    - [DocumentDBIndexBufferCacheHitRatio](#documentdbindexbuffercachehitratio)
    - [DocumentDBDatabaseCursors](#documentdbdatabasecursors)
    - [DocumentDBDBClusterReplicaLagMaximum](#documentdbdbclusterreplicalagmaximum)
    - [ElasticacheEngineCPUUtilization](#elasticacheenginecpuutilization)
    - [ElasticacheCurrConnections](#elasticachecurrconnections)
    - [ElasticacheMemoryUsagePercentage](#elasticachememoryusagepercentage)
    - [ElasticacheAuthenticationFailures](#elasticacheauthenticationfailures)
    - [ElasticacheReplicationLag](#elasticachereplicationlag)
    - [OpenSearchClusterStatusRed](#opensearchclusterstatusred)
    - [OpenSearchClusterStatusYellow](#opensearchclusterstatusyellow)
    - [OpenSearchFreeStorageSpace](#opensearchfreestoragespace)
    - [OpenSearchClusterIndexWritesBlocked](#opensearchclusterindexwritesblocked)
    - [OpenSearchCPUUtilization](#opensearchcpuutilization)
    - [OpenSearchShardsActive](#opensearchshardsactive)
    - [OpenSearchMasterReachableFromNode](#opensearchmasterreachablefromnode)
    - [OpenSearchThreadpoolWriteQueue](#opensearchthreadpoolwritequeue)
    - [OpenSearchThreadpoolWriteRejected](#opensearchthreadpoolwriterejected)
    - [OpenSearchDiskQueueDepth](#opensearchdiskqueuedepth)
    - [RDSDatabaseConnections](#rdsdatabaseconnections)
    - [RDSFreeableMemory](#rdsfreeablememory)
    - [RDSFreeStorageSpace](#rdsfreestoragespace)
    - [RDSCPUUtilization](#rdscpuutilization)
    - [RDSDiskLatency](#rdsdisklatency)
    - [MSKHasNoActiveController](#mskhasnoactivecontroller)
    - [MSKOfflinePartitionCount](#mskofflinepartitioncount)
    - [MSKZooKeeperSessionState](#mskzookeepersessionstate)
    - [MSKCPUUtilization](#mskcpuutilization)
    - [MSKMemoryUtilization](#mskmemoryutilization)
    - [MSKUnderReplicatedPartition](#mskunderreplicatedpartition)
    - [MSKConsumerGroupLag](#mskconsumergrouplag)
  - [Azure Metrics](#azure-metrics)
    - [Alert Name: "AzureDatabasePostgresFlexibleStorageUsage"](#alert-name-azuredatabasepostgresflexiblestorageusage)
    - [Alert Name: "AzureDatabasePostgresFlexibleCpuUsage"](#alert-name-azuredatabasepostgresflexiblecpuusage)
    - [Alert Name: "AzureDatabasePostgresFlexibleMemoryUsage"](#alert-name-azuredatabasepostgresflexiblememoryusage)
    - [Alert Name: "AzureDatabasePostgresFlexibleMaxConnections"](#alert-name-azuredatabasepostgresflexiblemaxconnections)
    - [Alert Name: "AzureDatabasePostgresFlexibleNoConnections"](#alert-name-azuredatabasepostgresflexiblenoconnections)
    - [Alert Name: "AzureDatabasePostgresFlexibleDeadlocks"](#alert-name-azuredatabasepostgresflexibledeadlocks)
    - [Alert Name: "AzureDatabasePostgresFlexibleDbNotAlive"](#alert-name-azuredatabasepostgresflexibledbnotalive)
    - [Alert Name: "AzureDatabasePostgresFlexibleFailedConnections"](#alert-name-azuredatabasepostgresflexiblefailedconnections)
    - [Alert Name: "AzureEventhubNamespaceCpuUsage"](#alert-name-azureeventhubnamespacecpuusage)
    - [Alert Name: "AzureEventhubNamespaceMemoryUsage"](#alert-name-azureeventhubnamespacememoryusage)
    - [Alert Name: "AzureEventhubServerErrors"](#alert-name-azureeventhubservererrors)
    - [Alert Name: "AzureEventhubThrottledRequests"](#alert-name-azureeventhubthrottledrequests)
    - [Alert Name: "AzureEventhubQuotaExceededErrors"](#alert-name-azureeventhubquotaexceedederrors)
    - [Alert Name: "AzureCacheRedisCpuUsage"](#alert-name-azurecacherediscpuusage)
    - [Alert Name: "AzureCacheRedisMemoryUsage"](#alert-name-azurecacheredismemoryusage)
    - [Alert Name: "AzureCacheRedisServerLoadUsage"](#alert-name-azurecacheredisserverloadusage)
    - [Alert Name: "AzureCacheRedisErrorOperations"](#alert-name-azurecacherediserroroperations)
    - [Alert Name: "AzureCacheRedisHighConnectedClients"](#alert-name-azurecacheredishighconnectedclients)
    - [Alert Name: "AzureCosmoMongodbOperationLatency"](#alert-name-azurecosmomongodboperationlatency)
    - [Alert Name: "AzureCosmoMongodbPhysicalPartitionSize16GB"](#alert-name-azurecosmomongodbphysicalpartitionsize16gb)
    - [Alert Name: "AzureCosmoMongodbPhysicalPartitionSize18GB"](#alert-name-azurecosmomongodbphysicalpartitionsize18gb)
    - [Alert Name: "AzureCosmoMongodbPhysicalPartitionSize26GB"](#alert-name-azurecosmomongodbphysicalpartitionsize26gb)
    - [Alert Name: "AzureCosmoMongodbPhysicalPartitionSize28GB"](#alert-name-azurecosmomongodbphysicalpartitionsize28gb)
    - [Alert Name: "AzureCosmoMongodbCollectionUnhealthy"](#alert-name-azurecosmomongodbcollectionunhealthy)
    - [Alert Name: "AzureCosmoMongodbErrorRequests"](#alert-name-azurecosmomongodberrorrequests)
    - [Alert Name: "AzureCosmoMongodbServiceAvailability"](#alert-name-azurecosmomongodbserviceavailability)
  - [Event Hubs](#event-hubs)
    - [Alert Name: "EventHubsConsumerGroupLag"](#alert-name-eventhubsconsumergrouplag)
    - [Alert Name: "EventHubsNumberOfTopicsLimit"](#alert-name-eventhubsnumberoftopicslimit)
  - [Frontdoor](#frontdoor)
    - [Alert Name: "AzureFrontdoorBackendLatency"](#alert-name-azurefrontdoorbackendlatency)
    - [Alert Name: "AzureFrontdoorBackendRequestFailed"](#alert-name-azurefrontdoorbackendrequestfailed)
    - [Alert Name: "AzureFrontdoorClientRequestFailed"](#alert-name-azurefrontdoorclientrequestfailed)
- [Integration](#integration)
  - [MacOS Node Exporter](#macos-node-exporter)
    - [Alert Name: "MacInstanceDown1H"](#alert-name-macinstancedown1h)
    - [Alert Name: "MacInstanceDownTimes1D"](#alert-name-macinstancedowntimes1d)
    - [Alert Name: "MacInstanceCpuHigh"](#alert-name-macinstancecpuhigh)
    - [Alert Name: "MacInstanceMemoryHigh"](#alert-name-macinstancememoryhigh)
  - [iGateway](#igateway)
    - [Alert Name: "iMessageLargeFileAttachment"](#alert-name-imessagelargefileattachment)
    - [Alert Name: "iMessageRetryMessage"](#alert-name-imessageretrymessage)
    - [Alert Name: "iMessageRotationDisabled"](#alert-name-imessagerotationdisabled)
    - [Alert Name: "iMessageRotationStuck"](#alert-name-imessagerotationstuck)
    - [Alert Name: "iGatewayUnauthorizedAccess"](#alert-name-igatewayunauthorizedaccess)
    - [Alert Name: "igatewayAgentSqliteDbCorrupted"](#alert-name-igatewayagentsqlitedbcorrupted)
  - [WhatsApp](#whatsapp)
    - [Alert Name: "WhatsappApiError"](#alert-name-whatsappapierror)
    - [Alert Name: "WhatsappApiErrorTemplateGetBanned"](#alert-name-whatsappapierrortemplategetbanned)
    - [Alert Name: "WhatsappApiErrorParameterValueIsNotValid"](#alert-name-whatsappapierrorparametervalueisnotvalid)
    - [Alert Name: "WhatsappVersionExpired"](#alert-name-whatsappversionexpired)
    - [Alert Name: "WhatsappVersionExpiry15Days"](#alert-name-whatsappversionexpiry15days)
    - [Alert Name: "WhatsappVersionExpiry7Days"](#alert-name-whatsappversionexpiry7days)
    - [Alert Name: "WhatsappOutMessageError"](#alert-name-whatsappoutmessageerror)
- [Endpoints Monitor](#endpoints-monitor)
  - [Probe](#probe)
    - [Alert Name: "BlackboxExporterHTTPEndpointDown"](#alert-name-blackboxexporterhttpendpointdown)
    - [Alert Name: "BlackboxExporterFmopBeUrlEndpointDown"](#alert-name-blackboxexporterfmopbeurlendpointdown)
    - [Alert Name: "BlackboxExporteriMessageHTTPEndpointDown"](#alert-name-blackboxexporterimessagehttpendpointdown)
    - [Alert Name: "BlackboxExporterWhatsappEndpointDown"](#alert-name-blackboxexporterwhatsappendpointdown)
    - [Alert Name: "BlackboxExporterEndpointCertificateExpiry"](#alert-name-blackboxexporterendpointcertificateexpiry)

# Core Services

## Vault

### Alert Name: "VaultPodIsSealed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when vault pod has sealed status

- Actions:

      # Get status of vault pod
      kubectl get pod --namespace < namespace > | grep vault

      # Check vault status
      for i in {0..2}; do kubectl exec -it vault-$i --namespace < namespace > -- sh -c "vault status"; done

      # Check vault seal/unseal config and find keywork seal
      ## If you find awskms, azurekeyvault, gcpckms then vault is configured auto-unsealed
      ## If you don't find seal keyword then it's manual unsealed
      kubectl get cm vault-config --namespace < namespace > -o jsonpath='{.data.extraconfig\-from\-values\.hcl}'

      # For manual unsealed case, make sure you have unsealed key before delete the vault pod that's having the issue.

      # For auto-unsealed case, you can delete the vault pod that's having the issue

### Alert Name: "VaultHasNoActiveNode"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when vault cluster has not active node

- Actions:

      # Get status of vault pod
      kubectl get pod --namespace < namespace > | grep vault

      # Check vault status
      for i in {0..2}; do kubectl exec -it vault-$i --namespace < namespace > -- sh -c "vault status"; done

      # Check vault seal/unseal config and find keywork seal
      ## If you find awskms, azurekeyvault, gcpckms then vault is configured auto-unsealed
      ## If you don't find seal keyword then it's manual unsealed
      kubectl get cm vault-config --namespace < namespace > -o jsonpath='{.data.extraconfig\-from\-values\.hcl}'

      # For manual unsealed case, make sure you have unsealed key before you rolling restart the vault statefulset
      kubectl rollout restart sts/vault --namespace < namespace >

      # For auto-unsealed case, you can delete the vault pod that's having the issue
      kubectl rollout restart sts/vault --namespace < namespace >

## Messaging

## Minio

### Alert Name: "MinioOfflineDisks"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when minio pod has offline disks.

- Actions:

      # Get status of pod from deployment name
      kubectl get pod --namespace < namespace > | grep minio

      # Get logs of pod from above command output
      kubectl logs -f <pod_name> | grep -E "host is down|corrupted backend|cmd.StorageErr"

      # Restart deployment to fix the issue.

# Middleware Services

## Elasticsearch

### Alert Name: "ElasticsearchClusterRed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when elasticsearch cluster state is red and it indicates that the specific shard is not allocated in the cluster.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep elasticsearch

      # Get access to service to check
      kubectl port-forward pod/< elasticsearch_pod_name > 9200 --namespace < namespace >

      # Execute the commands
      ## To get more information about cluster state
      curl -X GET "localhost:9200/_cat/health?v"
      ## To check why shard is not allocated
      curl -X GET "localhost:9200/_cluster/allocation/explain?pretty"

### Alert Name: "ElasticsearchClusterYellow"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when elasticsearch cluster state is yellow and it means that the primary shard is allocated but replicas are not.

### Alert Name: "ElasticsearchHeapUsageTooHigh"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when heap memory usage get high above 90%.

- Actions:

      # Get access to service to check
      kubectl port-forward pod/< elasticsearch_pod_name > 9200 --namespace < namespace >

      # Execute the commands
      ## To get more information about cluster allocation state
      curl -X GET localhost:9200/_cat/allocation?v

- Note: high memory can be because of too many shards on one node, it wil take sometime for cluster rebalance automatically.

### Alert Name: "ElasticsearchHeapUsageWarning"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when heap memory usage get high above 80%.

- Actions:

      # Get access to service to check
      kubectl port-forward pod/< elasticsearch_pod_name > 9200 --namespace < namespace >

      # Execute the commands
      ## To get more information about cluster allocation state
      curl -X GET localhost:9200/_cat/allocation?v

- Note: high memory can be because of too many shards on one node, it wil take sometime for cluster re-balance automatically.

### Alert Name: "ElasticsearchUnhealthyNodes"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when total healthy nodes of Elasticsearch cluster less than 3.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep elasticsearch

      # Get access to service to check
      kubectl port-forward pod/< elasticsearch_pod_name > 9200 --namespace < namespace >

      # Execute the commands
      ## To get more information about cluster state
      curl -X GET "localhost:9200/_cat/health?v"
      ## To check why shard is not allocated
      curl -X GET "localhost:9200/_cluster/allocation/explain?pretty"

### Alert Name: "ElasticsearchUnassignedShards"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when there is unassigned shards found on Elasticsearch cluster.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep elasticsearch

      # Get access to service to check
      kubectl port-forward pod/< elasticsearch_pod_name > 9200 --namespace < namespace >

      # Execute the commands
      ## To get more information about cluster state
      curl -X GET "localhost:9200/_cat/health?v"
      ## To check why shard is not allocated
      curl -X GET "localhost:9200/_cluster/allocation/explain?pretty"

## Kafka

### Alert Name: "KafkaDown"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when kafka statefulset pod is down.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

### Alert Name: "KafkaUnhealthyBroker"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when a Kafka broker is not in running state.

- Actions:

      # Check logs of pod to see why broker is not in running state
      kubectl logs <pod> --namespace <namespace>

### Alert Name: "KafkaMemoryLow"

- Severity: Critical

- Duration: 10m

- Description: This alert will be triggered when memory heap usage is higher than 90% of memory limit.

### Alert Name: "KafkaOfflinePartitionCount"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when number of partitions that don’t have an active leader and are hence not writable or readable.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep kafka

      # Check which topic has offline partition
      kubectl exec -it kafka-cluster-kafka-0 --namespace < namespace > -- sh -c "/opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka-cluster-kafka-bootstrap:9092 --command-config /tmp/strimzi.properties kafka-cluster-zookeeper-client:2181 --describe | grep 'Leader: -1'"

      # Check if cluster has enough brokers
      kubectl exec -it kafka-cluster-kafka-0 --namespace < namespace > -- sh -c "/opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server kafka-cluster-kafka-bootstrap:9092 | awk '/id/{print $1}'"

      # If you find any brokers missing from about commands and pod is still running then you need to read logs for more information

### Alert Name: "KafkaHasNoActiveController"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when no broker in the cluster is reporting as the active controller.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep kafka

      # Check if cluster has enough brokers
      kubectl exec -it kafka-cluster-kafka-0 --namespace < namespace > -- sh -c "/opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server kafka-cluster-kafka-bootstrap:9092 | awk '/id/{print $1}'"

      # If you find any brokers missing from about commands and pod is still running then you need to read logs for more information

### Alert Name: "KafkaUnderReplicatedPartition"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when under replicated partitions found on one ore more broker.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep kafka

      # Check if cluster has enough brokers
      kubectl exec -it kafka-cluster-kafka-0 --namespace < namespace > -- sh -c "/opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server kafka-cluster-kafka-bootstrap:9092 --command-config /tmp/strimzi.properties kafka-cluster-zookeeper-client:2181 --describe --under-replicated-partitions"

      # When you identify the broker that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "KafkaConsumerGroupLag"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when a kafka consumergroup has many lag messages.

- Actions:

      # Based on consumergroup check log of relative service (e.g)
      kubectl logs -f <pod_name> -n <namespace>
      # Rollout restart application base on consumergroup name

### Alert Name: "StrimziFoundNoKafkaResources"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when strimzi cluster operator hasn't found any Kafka CRD resources in cluster for 5m.

- Actions:

      # Check if kafka resources is deployed
      kubectl get kakfa -A

      # Check log of strimzi cluster operator pod
      kubectl logs -f <pod_name> -n <namespace>

### Alert Name: "StrimziKafkaResourceNotReady"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when strimzi cluster operator shows kafka resource state not ready.

- Actions:

      # Check log of strimzi cluster operator pod
      kubectl logs -f <pod_name> -n <namespace>

      # Check if all kafka/zookeeper/export are fine
      kubectl get pod -n <namespace> | grep -E "kafka|zookeeper|kafka-exporter"

## MongoDB

### Alert Name: "MongodbDown"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when mongodb exporter cannot connect to mongodb instance

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongodb | grep -v Completed

      # If mongodb exporter fail to connect to mongodb or it gets pending for creation
      # Then this alert can lower priority because prometheus cannot scrape metrics from mongodb-exporter

      # If mongodb-exporter is normal then you need to check mongodb pod for more information
      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If deployment gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

### Alert Name: "MongoStatefulsetUnscheduable"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when statefulset of mongodb get failed to created

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

### Alert Name: "MongoReplicationLag"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when replication lag between mongodb primary and secondary is over 300s.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Connect to mongo pod and show queries that has been running more than 10 seconds
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -n < namespace > -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'db.currentOp({\"secs_running\": {\$gte: 10}})'"

      # Configure mongo to log slow queries that has running than 10 seconds
      # Ref. https://docs.mongodb.com/manual/tutorial/manage-the-database-profiler/#profiling-levels
      kubectl exec -it mongo-primary-0  mongo-secondary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'db.setProfilingLevel(1, 10000)'"

      # List top 10 slowest queries that has been running more than 10 seconds
      kubectl exec -it mongo-primary-0  mongo-secondary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'db.system.profile.find({millis:{\$gt:100}}).limit(10)'"

      # Rollback configure mongodb profiling to default
      kubectl exec -it mongo-primary-0  mongo-secondary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'db.setProfilingLevel(0, 100)'"

### Alert Name: "MongoReplsetMermberUnhealthy"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when one instance in mongodb replicaset has unhealthy.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Show replication status
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'rs.status()'"

      # When you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "MongoReplsetMemberInRecoveringState"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when mongo instance in replicaset has status which status code is 3.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Ref. https://docs.mongodb.com/manual/reference/replica-states/

      # Show replication status
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'rs.status()'"

      # When you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "MongoReplsetMemberUnknown"

- Severity: Critical

- Duration: 2m

- Description: - Description: This alert will be triggered when mongo instance in replicaset has status which status code is 6.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Ref. https://docs.mongodb.com/manual/reference/replica-states/

      # Show replication status
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'rs.status()'"

      # When you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "MongoReplsetMemberUnreachable"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when mongo instance in replicaset has status which status code is 8.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Ref. https://docs.mongodb.com/manual/reference/replica-states/

      # Show replication status
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'rs.status()'"

      # When you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "MongoReplsetMemberRollback"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when mongo instance in replicaset has status which status code is 9.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Ref. https://docs.mongodb.com/manual/reference/replica-states/

      # Show replication status
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'rs.status()'"

      # When you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "MongoReplsetMemberRemoved"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when mongo instance in replicaset has status which status code is 10.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Ref. https://docs.mongodb.com/manual/reference/replica-states/

      # Show replication status
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'rs.status()'"

      # When you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "MongoHighConnections"

- Severity: Warning/Critical

- Duration: 5m

- Description: This alert will be triggered when mongodb cluster has high connection percentage from 80% up to 90%.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep mongo | grep -v Completed

      # Show connections stats
      export MONGODB_CONNECTION_STRING=$( kubectl get secret prometheus-mongodb-exporter -o jsonpath="{.data.mongodb-uri}" | base64 -D)
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'db.serverStatus().connections'"

      # Sorting connections by IP
      kubectl exec -it mongo-primary-0 -- bash -c "mongo $MONGODB_CONNECTION_STRING --eval 'db.currentOp(true).inprog.reduce((accumulator, connection) => { ipaddress = connection.client ? connection.client.split(\":\")[0] : \"Internal\"; accumulator[ipaddress] = (accumulator[ipaddress] || 0) + 1; accumulator[\"TOTAL_CONNECTION_COUNT\"]++; return accumulator; }, { TOTAL_CONNECTION_COUNT: 0 })'"

### Alert Name: "MongodbCursorsOpenTooMany"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when there is high cursors open found on mongo replicaset cluster.

### Alert Name: "MongodbCursorsTimeouts"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when there is high cursors timeout found on mongo replicaset cluster.

## Redis

### Alert Name: "RedisDown"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when redis instance is down

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

      # When you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "RedisOutOfConfiguredMaxmemory"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when redis memory usage is above redis max memory config

- Actions:

      # Get redis maxmemory config
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli config get maxmemory*"

      # If maxmemory-policy config is noeviction, in this example maxmemory will be increase to 1GB
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli config set maxmemory 1gb"

### Alert Name: "RedisTooManyConnections"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when connections on redis is over 100 connections.

- Actions:

      # Get redis connected clients
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli info | grep connect"

      # Get details from client connections
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli client list"

      # Get redis maxclients config
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli config get maxclients*"

      # Increase maxclients if needed
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli config set maxclients 10000"

### Alert Name: "RedisRejectedConnections"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when there is rejected connections found on redis instance.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

      # If redis pod doesn't get failed to create
      # Get redis connected clients
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli info | grep connect"

      # Get redis maxclients config
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli config get maxclients*"

      # Increase maxclients if needed
      kubectl exec -it redis-master-0 -c redis -n < namespace > -- sh -c "redis-cli config set maxclients 10000"

### Alert Name: "RedisStatefulsetUnscheduable"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when there is high cursors timeout found on mongo replicaset cluster.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

## Postgres

### Alert Name: "PostgresDown"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when postgres container is down.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If deployment gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

      # If postgres pod doesn't get failed to create
      # And you identify the instance that has the issue, you need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "PostgresExporterDown"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when side car postgres container is down.

- Actions:

      # You need to get logs for more information.
      kubectl logs < pod_name > -n < namespace > -f --tail 30

### Alert Name: "PostgresReplicationLag"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when replication lag on postgres slave is higher than 10m for 5m.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it postgres-slave-0 -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show slow queries running more than 5m
      SELECT pid, user, pg_stat_activity.query_start, now() - pg_stat_activity.query_start AS query_time, query, state, wait_event_type, wait_event FROM pg_stat_activity WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';

      # Show queries that are blocking other queries
      SELECT activity.pid, activity.usename, activity.query, blocking.pid AS blocking_id, blocking.query AS blocking_query FROM pg_stat_activity AS activity JOIN pg_stat_activity AS blocking ON blocking.pid = ANY(pg_blocking_pids(activity.pid));

      # Select pid that runs more than 5m or blocks another session
      # pg_cancel_backend(pid) will attempt to gracefully kill a running query process.
      # pg_terminate_backend(pid) will immediately kill the running query process, but potentially have side affects across additional queries running on your database server. The full connection may be reset when running pg_terminate_backend, so other running queries can be affected. Use as a last resort.

### Alert Name: "PostgresDelayedReplicaLagAboveThreshold"

- Severity: Critical

- Duration: 10m

- Description: This alert will be triggered when replication lag on postgres slave is above 1h for 10m

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it postgres-slave-0 -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show slow queries running more than 5m
      SELECT pid, user, pg_stat_activity.query_start, now() - pg_stat_activity.query_start AS query_time, query, state, wait_event_type, wait_event FROM pg_stat_activity WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';

      # Select pid that runs more than 5m or blocks another session
      # pg_cancel_backend(pid) will attempt to gracefully kill a running query process.
      # pg_terminate_backend(pid) will immediately kill the running query process, but potentially have side affects across additional queries running on your database server. The full connection may be reset when running pg_terminate_backend, so other running queries can be affected. Use as a last resort.

### Alert Name: "PostgresLongRunningQueriesCount"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when there are 2 more long queries running found on postgres instances for 5m.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show slow queries running more than 5m
      SELECT pid, user, pg_stat_activity.query_start, now() - pg_stat_activity.query_start AS query_time, query, state, wait_event_type, wait_event FROM pg_stat_activity WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';

      # Select pid that runs more than 5m or blocks another session
      # pg_cancel_backend(pid) will attempt to gracefully kill a running query process.
      # pg_terminate_backend(pid) will immediately kill the running query process, but potentially have side affects across additional queries running on your database server. The full connection may be reset when running pg_terminate_backend, so other running queries can be affected. Use as a last resort.

### Alert Name: "PostgresLongLivedTransaction"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when long live transaction is over 600 seconds for 5m.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it postgres-slave-0 -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show log_min_duration_statement setting
      SELECT * FROM pg_settings WHERE name = 'log_min_duration_statement';

      # When you know postgres will log transactions that run longer than setting milliseconds
      kubectl logs < pod_name > -n < namespace> --follow --tail 10

### Alert Name: "PostgresXlogNoConsumption"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when there are no xlog consumed on slave.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Exec to pod and execute below queries
      kubectl exec -it postgres-master-0 -c postgres -- bash -c "pg_controldata | grep checkpoint"
      kubectl exec -it postgres-slave-0 -c postgres -- bash -c "pg_controldata | grep checkpoint"

      # Compare latest checkpoint info to get current xlog position on slave instance
      # All wal files can be found in $PGDATA/pg_wal directory

### Alert Name: "PostgresConnectionsTooHigh"

- Severity: Warning

- Duration: 10m

- Description: This alert will be triggered when mongodb exporter cannot connect to mongodb instance

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show details stats of connection on postgtes instance
      SELECT datname,usename,client_addr,backend_start,query_start,state FROM pg_stat_activity;show idle_in_transaction_session_timeout;

      # Find all idle connections on postgres instance
      SELECT datname,usename,client_addr,backend_start,query_start,state FROM pg_stat_activity WHERE state = 'idle';

      # Depend on state of connections to decide whether we should terminate idle process or not.

### Alert Name: "PostgresVacuumAgeInSeconds"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when vacuum is running more than 1h.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show stat of vacuum progress
      SELECT * FROM pg_stat_progress_vacuum;

      # Select pid that runs more than 5m or blocks another session
      # pg_cancel_backend(pid) will attempt to gracefully kill a running query process.
      # pg_terminate_backend(pid) will immediately kill the running query process, but potentially have side affects across additional queries running on your database server. The full connection may be reset when running pg_terminate_backend, so other running queries can be affected. Use as a last resort.

      # Consider to move to crontab vacuum to avoid vacuum in working hours

### Alert Name: "PostgresVacuumAnalyzeAgeInSeconds"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when vacuum analyze is running more than 1 hour.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show stat of vacuum progress
      SELECT * FROM pg_stat_progress_vacuum;

      # Select pid that runs more than 5m or blocks another session
      # pg_cancel_backend(pid) will attempt to gracefully kill a running query process.
      # pg_terminate_backend(pid) will immediately kill the running query process, but potentially have side affects across additional queries running on your database server. The full connection may be reset when running pg_terminate_backend, so other running queries can be affected. Use as a last resort.

      # Consider to move to crontab vacuum to avoid vacuum in working hours

### Alert Name: "PostgresStatDatabaseTempBytes"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when temp file size on postgres database is higher than 100MB.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Get details about temp file size on database
      SELECT datname,temp_files,temp_bytes FROM pg_stat_database;

      # Temp file size will be increased depending on long running queries or complex query
      # To get more information about which query causing the issue
      SELECT datname,usename,backend_start,query_start,state,query FROM pg_stat_activity;

### Alert Name: "PostgresLocksCount"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when database lock is higher than 100.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Exec to pod and execute below queries
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable"

      # Show details about blocking query
      SELECT activity.pid,
            activity.usename,
            activity.query,
            blocking.pid AS blocking_id,
            blocking.query AS blocking_query
      FROM pg_stat_activity AS activity
      JOIN pg_stat_activity AS blocking ON blocking.pid = ANY(pg_blocking_pids(activity.pid));

### Alert Name: "PostgresStatefulsetUnscheduable"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when postgres pod gets failed to be created.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

### Alert Name: "PostgresSuperuserCount"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when mongodb exporter cannot connect to mongodb instance

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep postgres

      # Export postgres password as env var
      export POSTGRES_PASSWORD=$(kubectl get secret postgres -n < namespace > -o json | jq -r '.data."postgresql-password"' | base64 -D)

      # Show owner of databases and permissions of database user.
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable -c '\du+'"
      kubectl exec -it < pod_name > -c postgres -- bash -c "psql postgresql://postgres:${POSTGRES_PASSWORD}@127.0.0.1:5432/postgres?sslmode=disable -c '\l"

## Zookeeper

### Alert Name: "ZookeeperDown"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when zookeeper statefulset pod is down.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

### Alert Name: "ZookeeperMissingLeader"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when zookeeper has no leaders.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # Check if server has not in error state
      for zk in $(kubectk get pod --namespace < namespace > | grep zookeeper | awk '{print $1}'); do echo --------$zk------- && kubectl exec -it $zk -- bash -c "echo ruok | nc localhost 12181"; done

      # Show details of zookeeper instance
      for zk in $(kubectk get pod --namespace < namespace > | grep zookeeper | awk '{print $1}'); do echo --------$zk------- && kubectl exec -it $zk -- bash -c "echo srvr | nc localhost 12181"; done

### Alert Name: "ZookeeperQuorumSize"

- Severity: Warning/Critical

- Duration: 2m

- Description: This alert will be triggered when zookeper quorum size is decreased from 3 to 0 depending on severity of the alert.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # Check if server has not in error state
      for zk in $(kubectk get pod --namespace < namespace > | grep zookeeper | awk '{print $1}'); do echo --------$zk------- && kubectl exec -it $zk -- bash -c "echo ruok | nc localhost 12181"; done

      # Show details of zookeeper instance
      for zk in $(kubectk get pod --namespace < namespace > | grep zookeeper | awk '{print $1}'); do echo --------$zk------- && kubectl exec -it $zk -- bash -c "echo srvr | nc localhost 12181"; done

### Alert Name: "ZooKeeperMemoryLow"

- Severity: Critical

- Duration: 10m

- Description: This alert will be triggered when memory heap usage is higher than 90% of memory limit.

### Alert Name: "ZooKeeperStatefulsetUnscheduable"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when zookeeper statefulset pod gets failed to scheduled.

- Actions:

      # Get status of pod from statefulset name
      kubectl get pod --namespace < namespace > | grep < statefulset_name >

      # If no pod found in above command
      kubectl describe sts < statefulset_name > --namespace < namespace >

      # If statefulset gets failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

## Istio

### Alert Name: "IstioDeploymentNotReady"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when istio components (istiod, ingressgateway, egressgateway and kiali) are not ready.

- Actions:

      # Get status of pod from deployment name
      kubectl get pod --namespace < namespace > | grep < deployment_name >

      # If no pod found in above command
      kubectl describe deployment < deployment_name > --namespace < namespace >

      # If istio deployments get failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

### Alert Name: "IstioHigh4xxErrorRateByDestinationPercentage"

- Severity: Warning/Critical

- Duration: 10-15m

- Description: This alert will be triggered when total incoming error rate with HTTP code 4xx on istio proxie of specific destination higher is higher than 5% for warning and 10% for critical.

- Actions:

      # Query prometheus to understand which source service having issue
      sum by (destination_workload,destination_workload_namespace,response_code,response_flags,source_canonical_service) (irate(istio_requests_total{reporter="destination",response_code=~"4[0-9][0-9]"}[5m]))

      # Check response flags for more information
      https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage

### Alert Name: "IstioHigh5xxErrorRateByDestinationPercentage"

- Severity: Warning/Critical

- Duration: 10-15m

- Description: This alert will be triggered when total incoming error rate with HTTP code 4xx on istio proxie of specific destination higher is higher than 5% for warning and 10% for critical.

- Actions:

      # Query prometheus to understand which source service having issue
      sum by (destination_workload,destination_workload_namespace,response_code,response_flags,source_canonical_service) (irate(istio_requests_total{reporter="destination",response_code=~"5[0-9][0-9]"}[5m]))

      # Check response flags for more information
      https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage

### Alert Name: "IstioGrpcDeadlineExceededErrors"

- Severity: Critical

- Duration: 15m

- Description: This alert will be triggered when there're many DEADLINE_EXCEEDED GRPC requests for 15 minutes.

- Actions:

      - Check service logs and traces for any errors:
        - TraceQL: `{status = error}`.
        - LogQL: `{app="<service>", container="istio-proxy"} |= "remote_reset"`
      - Restart service if needed. If still not work restart ingress gateway first, then restart service.

### Alert Name: "IstioGrpcDeadlineExceededErrorsToIntegrations"

- Severity: Critical

- Duration: 15m

- Description: This alert will be triggered when there're many DEADLINE_EXCEEDED GRPC requests for 15 minutes from integration services to proxymessaging.

- Actions:

      - Check service logs and traces for any errors:
        - TraceQL: `{status = error}`.
        - LogQL: `{app="<service>", container="istio-proxy"} |= "remote_reset"`
      - Restart service if needed. If still not work restart ingress gateway first, then restart service.
      - If source_workload is imessage-archiving-integration, we need to read DT team to check.

## Velero

### Alert Name: "VeleroBackupPartialFailures"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when partial backup is failed.

- Actions:

      # List state of all backups
      velero backup get

      # Describe why backup is failed
      velero backup describe < backup_name >

      # Get logs from backup_name
      velero backup logs < backup_name >

      # Get log from velero pod
      kubectl logs < pod_name > -n < namespace> --follow --tail 10

### Alert Name: "VeleroBackupFailed"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when backup is failed.

- Actions:

      # List state of all backups
      velero backup get

      # Describe why backup is failed
      velero backup describe < backup_name >

      # Get logs from backup_name
      velero backup logs < backup_name >

      # Get log from velero pod
      kubectl logs < pod_name > -n < namespace> --follow --tail 10

## Cert-manager

### Alert Name: "CertManagerAbsent"

- Severity: Critical

- Duration: 10m

- Description: This alert will be triggered when prometheus fails to scrape metrics from cert-manager.

- Actions:

      # Get status of pod from deployment name
      kubectl get pod --namespace < namespace > | grep < deployment_name >

      # If no pod found in above command
      kubectl describe deployment < deployment_name > --namespace < namespace >

      # If istio deployments get failed to create because of below reasons
      Node Selector: update deployment manifest yaml to include nodeSelector by labels getting from command 'kubectl get nodes --show-labels'
      Toleration: describe node to see if toleration has been set from command 'kubectl get nodes < node_name > | grep Taints'
      Worker nodes are not ready: drain pods from not ready nodes to reduce load on the node and check monitoring about memory/cpu usage by all pods on that node.

      # If cert-manager pod is not missing then you need to read logs for more information

### Alert Name: "CertManagerCertExpirySoon"

- Severity: Warning/Critical

- Duration: 1h

- Description: This alert will be triggered when certificate will be expired in 30 days or 7 days.

### Alert Name: "CertManagerCertNotReady"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when no valid cert is found.

- Actions:

      # Get certificate request
      kubectl get certificaterequests -A

      # If you find READY column return False then
      kubectl delete certificaterequests < certificaterequests_name > -n < namespace >

### Alert Name: "CertManagerHittingRateLimits"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when certmanager is hitting rate limit of Letsencrypt.

- Actions:

      # Letsencrypt rate limit is 50 per week and maximum of 300 New Orders per account per 3 hours.
      # Get certificate request
      kubectl get certificaterequests -A

      # If you find READY column return False then
      kubectl delete certificaterequests < certificaterequests_name > -n < namespace >

## Prometheus

### Alert Name: "PrometheusTenantDisappeared"

- Severity: Critical

- Duration: 10m

- Description: This alert will be triggered when Prometheus tenant has disappeared from Mimir for more than 15 minutes.

- Actions:

      # Check if Prometheus is running correctly
      kubectl get pod --namespace monitoring | grep prometheus

      # If still running then check if Prometheus has errors in logs
      kubectl --namespace monitoring logs <prometheus pod>

# App

## Common Application Alerts

### Alert Name: "AppExecutionSlow"

- Severity: Warning

- Duration: 0m

- Description: This alert will be triggered when pod has slow execution than 3s. Class will be included in alert message for further checks.

### Alert Name: "KafkaClientHasLostConnections"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when kafka client fails to connection with kafka clusters.

- Actions:

      # Check application logs based on label app found in alert description

### Alert Name: "KafkaClientProducerException"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when kafka client producer failed to connect Kafka cluster.

- Actions:

      # Check application logs based on label app found in alert description
      # Try this Prometheus query to observe of connections aren't back
      kafka_producer_connection_count{app=~"invitation-client|proxymessaging|message-tracking"}
      # Restart app is required if connections aren't recoverable

### Alert Name: "KafkaClientConsumerException"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when kafka client consumer failed to connect Kafka cluster.

- Actions:

      # Check application logs based on label app found in alert description
      # Try this Prometheus query to observe of connections aren't back
      kafka_consumer_connection_count{app=~"events|externalcommunication|invitation-client|message-rules|message-tracking|proxymessaging|search"}
      # Restart app is required if connections aren't recoverable

### Alert Name: "RedisClientHasLostConnections"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when kafka client fails to connection with kafka clusters.

- Actions:

      # Check application logs based on label app found in alert description

### Alert Name: "MongodbClientHasLostConnections"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when kafka client fails to connection with kafka clusters.

- Actions:

      # Check application logs based on label app found in alert description
      # Restart pod follow by this docs https://leap-expert.atlassian.net/wiki/spaces/DOC/pages/13434881/Kafka+Topics

### Alert Name: "ServiceErrorLogs"

- Severity: Critical

- Duration: 30m-60m

- Description: This alert will be triggered when a service has more than 1000 error logs for 30m-60m.

- Actions:

      # Check metrics query with PromQL
      sum by (app,cluster,namespace,product,version) (promtail_custom_fmop_logs_by_level{level="ERROR",app="<app_name>"}) > 1000
      # Check metrics query with LogQL
      {level="ERROR", app="<app_name>"}

## Application Alerts

### API-Server Service

#### Alert Name: "SSOLoginFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when api-server has many failed SSO login request

- Actions:

      # Execute PromQL query
      increase(sso_user_login_total{app="authentication",success="false"}[5m])
      # Execute LogQL queries for more information.
      {container="authentication",level="ERROR"}

### Audit Service

#### Alert Name: "AuditExportResultsFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when audit fails to export to specific transtport.

- Actions:

      # Find company ID that has failed export task
      db.DBCompany.find()

      # Check Export Task with given company ID
      db.ExportTask.find({"companyId": ObjectId("<company_id>")})

      # Check export in given duration with specific task ID
      db.DBExportTaskStatus.find({"taskId" : ObjectId("<task_id>"), "creationTimestamp": {$gte: ISODate("2023-06-01T00:00:00.000Z"),$lt: ISODate("2023-06-16T00:00:00.000Z")} }).pretty()

      # If you don't have task ID then you can check it as below
      db.DBExportTaskStatus.find({"status":"FAILED", "creationTimestamp": {$gte: ISODate("2023-06-01T00:00:00.000Z"),$lt: ISODate("2023-06-16T00:00:00.000Z")} }).pretty()

      # Note: update time duration. Ref ISODate

#### Alert Name: "AuditRecoverMatrixRoomRequestFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when audit fails to recover mamtrix request due to data currupted in collect DBMatrixRoom.

### Data Retention

#### Alert Name: "AuditDataRetentionIsDelayed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when data has not been deleted even after past retention age.

- Actions:

      1. Inform customer, if they have such process of manual alerting on delay
      2. Check data retention config
            db.DBProfile.find({"companyId":ObjectId("<tenant_id>")}).pretty()
         Look for these attributes
         - com.leapxpert.data-retention.enabled
         - com.leapxpert.data-retention.age-in-days
         - com.leapxpert.data-retention.alert-delay.enabled
         - com.leapxpert.data-retention.alert-delay.hours
      3. Check if jobs are stuck in PENDING or RUNNING or FAILED state
            db.DBRetentionJob.find(
            {
                  "companyId": "<companyId>",
                  "status": {
                        $in: ["PENDING","RUNNING","FAILED","PARTIALLY_FAILED"]
                  }
            }).sort({"dataEndTime": -1}).limit(1)
      4. Check whether redis queue is stuck with multiple pending jobs
            redis-cli
            LRANGE data-retention-jobs-queue 0 -1
      5. Call the cursor API of each job data type, to find out the actual delayed time
            curl -X GET "https://<api_domain>/v1/data-retention/cursor?type=DB_AUDIT_LOG" \
                  -H "Accept: application/json" \
                  -H "Authorization: Bearer <jwt>"
            curl -X GET  "https://<api_domain>/v1/data-retention/cursor?type=DB_AUDIT_LOG" \
                  -H "Accept: application/json" \
                  -H "X-API-KEY: <api_key>"
          Example output will show expectedDeletion and actualDeletion and you can compare with attributes in step 2:
          {
              "message": "Success",
              "code": 0,
              "expectedDeletion": {
                  "endTime": "2023-07-11T03:15:57.410Z"
              },
              "actualDeletion": {
                  "endTime": "2023-07-11T00:19:33.087Z"
              },
              "success": true
          }
      6. Loop BE for further investigation

      # Extra steps if you find the following messaging from step 3:
      7. If you find message "Failed to trigger purging room history". Execute blow queries to check data on room
            synapse=> select * from events where room_id = '<room_id>';
            synapse=> select * from event_json where room_id = '<room_id>';
      8. If step #5 returns empty result, then we can set job manually to SUCCESS
            db.DBRetentionJob.update(
                  {_id:ObjectId("<job_id>")},
                  {
                        $set: {
                              status: "SUCCESS",
                              lastUpdateTimestamp: ISODate("2023-07-27T07:06:44")
                              }
                  }
            )

#### Alert Name: "AuditPeriodicPollNotWorking"

- Severity: Critical

- Duration: 15m

- Description: This alert will be triggered when audit has no new polls since last poll.

- Actions:

      # Check configure poll-interval-min with default value is 5 (5m)
      kubectl get cm audit -n default -o jsonpath="{.data.env\.conf}" | grep poll-interval-min

      # Check audit pod log
      kubectl logs pod/<audit_pod> -n <audit_pod_namespace> -f

#### Alert Name: "AuditDataRetentionJobFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when audit data retention has failed job.

- Actions:

      # Check data retention job status
      db.DBRetentionJob.find({
            "companyId": "<tenantId>",
            "status": "FAILED"}).sort({ "lastUpdateTimestamp": -1 })

      # Check application log pattern
      - ERROR: "Got an error while running data retention job {}"
      - WARN: "Job {} number of errors = {}, which exceeds failure threshold {}, setting job status to FAILED"

      # Once the issue is fixed, manually trigger the job to retry, by calling API
      curl -X POST "https://<api_domain>/v1/data-retention/run" \
            -H "Accept: application/json" \
            -H "Authorization: Bearer <jwt>"
            -d @job.json
      ## Content of job.json will be collected from MongoDB query above

      # Keep monitoring the DBRetentionJob until the status turns to SUCCESS.

#### Alert Name: "AuditDataRetentionJobPartiallyFailed"

- Severity: Warning

- Duration: 0m

- Description: This alert will be triggered when audit data retention has failed job.

- Actions:

      # Check data retention job status
      db.DBRetentionJob.find({
            "companyId": "<tenantId>",
            "status": "PARTIALLY_FAILED"}).sort({ "lastUpdateTimestamp": -1 })

      # Check application log pattern
      - ERROR: "Failed to remove DBAuditLog, audit id: {}"
      - ERROR: "Got an error while processing for audit {}"
      - WARN: "Removing ES docs partially failed. audit log ids: {}, entityIds: {}, original entity count: {}, removed entity count: {}, updatedCount: {}". Check search service and elastic search for any error when deleting document
      - ERROR: "Failed to send dummy event, room id: {}". Check proxymessaging & synapse for any error
      - ERROR: "Failed to trigger purging room history, room id: {}, error: {}". Check proxymessaging & synapse for any error

      # Once the issue is fixed, manually trigger the job to retry, by calling API
      curl -X POST "https://<api_domain>/v1/data-retention/run" \
            -H "Accept: application/json" \
            -H "Authorization: Bearer <jwt>"
            -d @job.json
      ## Content of job.json will be collected from MongoDB query above

      # Keep monitoring the DBRetentionJob until the status turns to SUCCESS.

#### Alert Name: "AuditDataRetentionPendingJobs"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when audit has no new polls since last poll.

- Actions:

      # Check audit pod log
      kubectl logs pod/<audit_pod> -n <audit_pod_namespace> -f

      # RetentionJobBlockingConsumer logger:

      - DEBUG: "Started retention job receiver on redis list named". Should be printed upon audit service start
      - DEBUG: "Stopped retention job receiver on redis list named". Should be printed only upon audit service stop
      - ERROR: "pop exception, keep looping". Error when running blpop from redis, service should retry blpop forever
      - DEBUG: "Popped from redis queue, job id:". Service has successfully popped a job from the redis list

      # RedisListManager logger:

      - DEBUG: "Getting connection". Should be printed upon audit service start
      - DEBUG: "Created connection pool for instance". Should be printed upon audit service start
      - ERROR: "Failed connecting to REDIS server, will retry". Should retry connecting to redis every 30 seconds
      - ERROR: "Error acquiring redis connection from connection pool". Redis connection exception when performing rpush or llen, operation has failed
      - ERROR: "blpop exception". Error when running blpop from redis, service should retry blpop forever

      # RetentionJobDispatcher logger:

      - DEBUG: "Going to blocking Ask worker actor for job id {} attempt id {}".Successfully started a blocking operation to run the retention job
      - INFO: "Timeout when blocking Ask worker actor for job id {} attempt id {}, move onto next job". Timeout when waiting for the operation, will trigger consuming the next element from redis list

      # If above application logs indicate that jobs are running successfully, however the queue is piling up, then we may need to increase the number of workers to handle retention job.
      ## Edit configmap akka.conf
      /retentionJobWorkerActor {
            router = round-robin-pool
            nr-of-instances = 10
      }

#### Alert Name: "AuditDataRetentionMediaFileFailed"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when audit data retention has minio file deletion failure.

- Actions:

      # Check application log pattern
      - ERROR: "Failed deleting file {}"
      - ERROR: "Failed deleting thumbnail file {}"

      # Check data retention job status
      db.DBRetentionJob.find({
      "dataType": "AUDIT_MEDIA_FILE",
      "status": { $in: [ "PARTIALLY_FAILED", "FAILED" ] }
      })
      .sort({ "lastUpdateTimestamp": -1 })

      # Check Minio server for any errors

#### Alert Name: "L2AuditContainerOOMKilled"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when OOMKilled event is detected on audit container.

- Actions:

      # Get the stuck export tasks in "RUNNING" state with the "startTime" before audit container restart time

      # Retry export for the stuck export tasks
      Refer: https://leap-expert.atlassian.net/wiki/spaces/DE/pages/2486272927/How+to+run+Retry+API+for+an+Export+Task+runId

#### Alert Name: "SearchDataRetentionDocsDeletionFailed"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when search service has document deletion failure.

- Actions:

      # Check metric label "error" for any clue to the error.

      # Check application log pattern
      - ERROR: "Returning error response in status {}"
      - ERROR: "Processing request error {}"
      - ERROR: "Timeout when calling ES server, reason: {}"
      - ERROR: "IOException Error from ES Server, reason = {}"
      - ERROR: "Alias is not found, full response: {}"
      - ERROR: "ES throws ElasticsearchException"
      - ERROR: "Unexpected exception on Elasticsearch operation"

      # Check elasticsearch cluster for any errors

#### Alert Name: "ProxymessagingDataRetentionPurgeMartrixRoomFailed"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when proxymessaging failed to call synapse purge

- Actions:

      # Check metric label "error" for any clue to the error.

      # Check application log pattern
      - ERROR: "Processing request error {}"
      - Search by keyword "429 Too Many Requests", requests may be rate limited.

      # Check synapse for any errors

#### Alert Name: "AuditDataRetentionMatrixRoomPurgeFailed"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when proxymessaging failed to call synapse purge.

- Actions:

      # Check metric label "error" for any clue to the error.

      # Check application log pattern
      - ERROR: "Failed to query purging status, purge id: {}, error: {}"

      # Check proxymessaging & synapse for any error
      ## Search by keyword "429 Too Many Requests", requests may be rate limited

#### Alert Name: "AuditDataRetentionDeleteEntityFailed"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when calling the delete entity API encounters frequent errors.

- Actions:

      # Check metric "exception" label for any clue to the error

      # Check audit service application log pattern
      - ERROR: "Error handling dataRetentionDeleteEntity"

      # Check all below metrics related to data retention, since this API triggers the same data retention application flow
      - audit_minio_file_delete
      - search_delete_es_document_request
      - proxymessaging_redact_room_event_request

      # Inform customer, if they have such process of manual alerting on delay, since the not being able to delete data in time may cause compliance breach.

#### Alert Name: "ProxymessagingDataRetentionRedactEventFailed"

- Severity: Warning

- Duration: 2m

- Description: This alert will be triggered when proxymessaging calls synapse to send redact message API keeps failing.

- Actions:

      # Check metric label "error" for any clue to the error

      # Check application log pattern
      - ERROR: Processing request error {}
      - ERROR: Failed redacting room {} event id {}, error code {}

      # Check synapse for any error

### Authentication Service

#### Alert Name: "AuthenticationLoginFailed"

- Severity: Warning/Critical

- Duration: 2-5m

- Description: This alert will be triggered when authentication has many failed login

- Actions:

      # Execute PromQL query
      increase(login_request_total{app="authentication",success="false"}[5m])
      # Execute LogQL queries for more information.
      {container="authentication",level="ERROR"}
      ****{container="authentication"} |= "Failed authenticating user role"

#### Alert Name: "AuthorizationRequestFailed"

- Severity: Warning/Critical

- Duration: 2-5m

- Description: This alert will be triggered when authentication has many failed authorization requests.

- Actions:

      # Execute PromQL query
      increase(authorization_request_total{app="authentication",success="false"}[5m])
      # Execute LogQL queries:
      {container="authentication"} |= "Received authorization request with content userIdentifier|Authorizing for user role|Replying to authorization request with id"

#### Alert Name: "AuthenticationVaultRequestFailed"

- Severity: Warning/Critical

- Duration: 2-5m

- Description: This alert will be triggered when authentication has many failed requests to Vault.

- Actions:

      # Execute PromQL query
      increase(authentication_request_to_vault_total{app="authentication",success="false"}[5m])
      # Execute LogQL query
      {container="authentication"} |= "Vault responded with HTTP status code:"

#### Alert Name: "AuthenticationKeycloakRequestFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when authentication has many failed requests to Keycloak.

- Actions:

      # Execute PromQL query
      increase(authentication_request_to_keycloak_total{app="authentication",success="false"}[5m])
      # Execute LogQL query
      {container="authentication"} |= "KeycloakServiceClient"

### Whatsapp Archived Gateway Service

#### Alert Name: "WAGClientOutdated"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when WAG detected the WhatsApp client outdated.

### Whatsapp Integration Archived Service

#### Alert Name: "WAAEmailRegistrationInstructionFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when WAA detected AM failed to follow email instruction.

#### Alert Name: "WAAImportMessageMaxRetryExceeded"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when WAA has failed imported message after max retry.

- Actions:

      # Execute PromQL query
      (increase(waa_failed_imported_message_after_max_retry_total{app="whatsappintegration-archived"}[5m:]))
      # Execute LogQL queries:
      {app="whatsappintegration-archived"}

### Whatsapp Native Integration Service

#### Alert Name: "WhatsappNativeSendMediaTemplateFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when the media template triggers failed has been failed to be triggered more than 2 times in the last 1d.

- Actions:
      # Execute LogQL queries:
      {app="whatsapp-native-integration"}

#### Alert Name: "WhatsappNativeSendCloudMessageError"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when Whatsapp Cloud API returns errors.

- Actions:

      # Check the error code on: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/
      # Report the issue to Delivery Team

#### Alert Name: "WhatsappNativeSendCloudMessage2xxError"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when Whatsapp Cloud API returns API Permission errors.

- Actions:

      # Check the error code on: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/
      # These errors are returned when there was a problem with the access token you are using for the API call.
      # Verify the Meta app access token, need to generate a new one if token doesn’t have access to the permissions.

### Wechat Native Integration Service

#### Alert Name: "WechatNativeEnableIntegrationFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the enable integration requests failed.

#### Alert Name: "WechatNativeDisableIntegrationFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the disable integration requests failed

#### Alert Name: "WechatNativeCompleteIntegrationFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the complete integration requests failed

#### Alert Name: "WechatNativeOnboardingTriggerOtpFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the onboarding trigger OTP requests failed

#### Alert Name: "WechatNativeOnboardingVerifyOtpFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the onboarding verify OTP requests failed

#### Alert Name: "WechatNativeWechatServerApiCallFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when wechat native fails to make api call to wechat server.

### Wechat Miniap Integration Service

#### Alert Name: "WechatMiniappEnableIntegrationFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the enable integration requests failed.

#### Alert Name: "WechatMiniappDisableIntegrationFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the disable integration requests failed.

#### Alert Name: "WechatMiniappClientAuthenticationFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the client authentication requests failed.

#### Alert Name: "WechatMiniappTriggerOTPFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the client OTP triggers failed.

#### Alert Name: "WechatMiniappVerifyOTPFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the client OTP verifies failed.

#### Alert Name: "WechatMiniappGetOAFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the official account gets failed.

#### Alert Name: "WechatMiniappGetWechatMiniappAccountFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the wechat miniapp account gets failed.

#### Alert Name: "WechatMiniappCallAPIServerFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the call wechat API server gets failed.

### Wecom Integration Service

#### Alert Name: "WecomSsoLoginStartFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when user has SSO start login failed.

#### Alert Name: "WecomSsoLoginCompleteFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when user has SSO complete login failed.

#### Alert Name: "WecomContactUserCreateFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when service has failed request for user account creation.

#### Alert Name: "WecomContactClientCreateFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when service has failed request for client account creation.

#### Alert Name: "WecomClientVerificationStartFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when wecom client failed to trigger SMS OTP.

#### Alert Name: "WecomClientVerificationCompleteFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when wecom client failed to complete the verification.

#### Alert Name: "WecomTencentPlatformApiCallFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when wecom integration has failed requests to Tencent platform.

- Actions:

      # Error code can be found here https://developer.work.weixin.qq.com/document/path/90313
      # Collection log from wecom-integration pod

#### Alert Name: "WecomTencentLicenseExpired"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when Wecom license is expired.

- Actions:

      # Error code can be found here https://developer.work.weixin.qq.com/document/path/90313
      # Code 40001 indicates that wecom license has expired. We need to renew in next 5 days.
      # If the license renewal is after 5 days from alert time then all the new messages will be archived.

#### Alert Name: "WecomTencentWhitelistIPMismatched"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the requests to Wecom are failed because public IP is not whitelisted.

- Actions:

      # Error code can be found here https://developer.work.weixin.qq.com/document/path/90313
      # Code 301042 indicates that the requested IP is not within the set whitelist range.
      # Need to contact customer for public IP whitelisting in Wecom Enterprise Portal.

#### Alert Name: "WecomTencentInvalidSecret"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when the requests are failed due to invalid secret.

- Actions:

      # Error code can be found here https://developer.work.weixin.qq.com/document/path/90313
      # Code 40001 indicates that wecom requests are failed due to invalid secret.
      # We need to check to see if secret in vault is correctly or not.

### Customer Model Sync Service

#### Alert Name: "CustomerModelSyncGraphAPIFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when customermodelsync has detected failed events from Microsoft Graph API.

- Actions:

      # Check logs of pod
      kubectl logs <pod> --namespace <namespace>

#### Alert Name: "CustomerModelSyncAntiphonyFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when customermodelsync has failed periodical sync events with Antiphony.

- Actions:

      # Check logs of pod
      kubectl logs <pod> --namespace <namespace>

#### Alert Name: "CustomerModelSyncAADFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when customermodelsync has failed periodical sync events with Microsoft AAD.

#### Alert Name: "CustomerModelSyncMosaicFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when customermodelsync has failed periodical sync events with Mosaic.

- Actions:

      # Check logs of pod
      kubectl logs <pod> --namespace <namespace>-

#### Alert Name: "CustomerModelSyncSalesforcePullChangesFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when customermodelsync has failed pull changes from Mosaic.

- Actions:

      # Check logs of pod
      kubectl logs <pod> --namespace <namespace>

#### Alert Name: "CustomerModelSyncSalesforceOauthFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when customermodelsync has failed OAuth with Salesforce.

- Actions:

      # Check logs of pod
      kubectl logs <pod> --namespace <namespace>

#### Alert Name: "CustomerModelSyncSalesforceQueryFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when customermodelsync has failed query from Salesforce.

- Actions:

      # Check logs of pod
      kubectl logs <pod> --namespace <namespace>


### SMS Integration Service

#### Alert Name: "SMSRegisterAccountFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when smsintegration service failed to register account.

#### Alert Name: "SMSUnregisterAccountFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when smsintegration service failed to unregister account.

#### Alert Name: "SMSSendMessageFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when smsintegration service failed to send message.

#### Alert Name: "SMSReceiveMessageFailed"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when smsintegration service failed to receive message.

#### Alert Name: "SMSSendMessageLatency"

- Severity: Critical

- Duration: 2m

- Description: This alert will be triggered when smsintegration service smsintegration service experienced 95th percentile message sending latency.

### iMessage Archiving Integration

#### Alert Name: "ImessageNumberOfIncomingMessageFailedDaily"

- Severity: Critical

- Duration: 3h

- Description: This alert will be triggered when the total handled incoming message have been failed in the last 24 hours higher than 100.

- Actions:

      # Get log off containers for more information
      kubectl logs -f < pod_name > -n < namespace > -c < container_name >

#### Alert Name: "ImessageTranscodeImageFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when the total fails of image transcoding are higher than 5 in last 1 hour.

- Actions:

      # Check the health of the transcoder service and logs.
      kubectl describe <transcoder_pod_name> -n <namespace>

      # Get log off container imessage-archiving-integration for more information
      kubectl logs -f < pod_name > -n < namespace > -c imessage-archiving-integration

#### Alert Name: "ImessageTranscodeAudioFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when the total fails of audio transcoding are higher than 5 in last 1 hour.

- Actions:

      # Check the health of the transcoder service and logs.
      kubectl describe <transcoder_pod_name> -n <namespace>

      # Get log off container imessage-archiving-integration for more information
      kubectl logs -f < pod_name > -n < namespace > -c imessage-archiving-integration

#### Alert Name: "ImessageGenerateThumbnailFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when the total fails of thumbnail generating are higher than 5 in last 1 hour.

- Actions:

      # Check the health of the transcoder service and logs.
      kubectl describe <transcoder_pod_name> -n <namespace>

      # Get log off container imessage-archiving-integration for more information
      kubectl logs -f < pod_name > -n < namespace > -c imessage-archiving-integration

#### Alert Name: "ImessageIncomingMessagesFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when the incoming messages are failed in specific message type has been failed for 3h.

- Actions:

      # Get log off container for more information
      kubectl logs -f < pod_name > -n < namespace > -c imessage-archiving-integration

#### Alert Name: "ImessageDownstreamServiceFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when the imessage-archiving-integration has 5 requests calling to downstream service in 1h.

- Actions:

      # Get log off container for more information
      kubectl logs -f < pod_name > -n < namespace > -c imessage-archiving-integration

### Teams2B Integration Service

#### Alert Name: "Teams2bRefreshSubscriptionWebhookFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when refreshing subscription triggered by webhook gets failed.

#### Alert Name: "Teams2bRefreshSubscriptionCronJobFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when refreshing subscription triggered by cronjob gets failed.

#### Alert Name: "Teams2bIncomingTrafficDroppedWorkingDays"

- Severity: Critical

- Duration: 1h

- Description: This alert will be triggered when the incoming traffic of Teams2b service dropped more than 50% compared to the previous week.

#### Alert Name: "Teams2bNoIncommingTrafficWorkingDays"

- Severity: Critical

- Duration: 1d

- Description: This alert will be triggered when there's no incoming traffic to Teams2b service for the last 24 hours during working days.

#### Alert Name: "Teams2bOutgoingTrafficDroppedWorkingDays"

- Severity: Critical

- Duration: 1h

- Description: This alert will be triggered when the outgoing traffic of Teams2b service dropped more than 50% compared to the previous week.

#### Alert Name: "Teams2bNoOutgoingTrafficWorkingDays"

- Severity: Critical

- Duration: 1d

- Description: This alert will be triggered when there's no outgoing traffic to Teams2b service for the last 24 hours during working days.

## Others

### Alert Name: "KubeContainerOOMKilled"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when OOMKilled/Evicted event is detected on container.

- Actions:

      # Get log off containers for more information
      kubectl logs -f < pod_name > -n < namespace > -c < container_name >

### Alert Name: "KubeInitContainerOOMKilled"

- Severity: Critical

- Duration: 5m

- Description: This alert will be triggered when OOMKilled/Evicted event is detected on init container.

- Actions:

      # Get log off containers for more information
      kubectl logs -f < pod_name > -n < namespace > -c < init_container_name >

### Alert Name: "KubeContainerLivenessProbeFailed"

- Severity: Critical

- Duration: 0m

- Description: This alert will be triggered when liveness probe failed event is detected on container.

- Actions:

      # Get log off containers for more information
      kubectl describe pod < pod_name > -n < namespace >

      # Restart pod if needed
      kubectl rollout restart deploy/<deployment_name>

### Alert Name: "KubeManyNodesNotReady"

- Severity: Critical

- Duration: 1m

- Description: This alert will be triggered when many worker nodes are in NotReady status.

- Actions:

      # Get event of worker nodes
      kubectl describe node < node_name >

### Alert Name: "KubePodMemUsageHigh"

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when pod memory usage is over 90% of memory limits.

### Alert Name: "KubePodCpuUsageHigh

- Severity: Warning

- Duration: 5m

- Description: This alert will be triggered when pod cpu usage is over 90% of cpu limits.

### Alert Name: "KubePodFailedToPullImage"

- Severity: critical

- Duration: 5m

- Description: The alert is triggered when the image for a container is failed to download.

- Actions:

      # Describe pod to see the state
      kubectl describe pod <pod_name> -n <namespace>
      # Check image pull secret to make sure that pull secret is correct
      kubectl get secret lxp-docker-registry-key -o yaml

# Grafana Agent

## AgentTracingReceiverErrors

- Severity: warning/critial

- Duration: 15m

- Description: The alert is triggered when refused spans percentage on particular receiver increases more than 10%. This indicates that agent itself refuses spans due to many reasons (e.g Kubernetes worker node down, CNI down, etc).

- Actions:

      # Check if any grafana agent pods experiences downtime.
      # Check if any Kubernetes worker nodes experiences not ready state.

## AgentTracingExporterErrors

- Severity: warning/critial

- Duration: 15m

- Description: The alert is triggered when refused spans percentage on particular exporter increases more than 10%. This indicates that agent has failed to send trace to tracing system and requires operator to check tracing system.

- Actions:

      # Check if any problem with tempo that might cause the issue.

# Cloud Services Monitoring

## AWS Cloudwatch

### DocumentDBCPUUtilization

- Severity: warning/critical

- Duration: 15m

- Description: This alert is triggered when instance has cpu utilization reached more than 90% in last 15m.

- Actions:

      # Check if we have any releases recently
      # Capture spike from istio requests, high request rate might indicates high load against AWS DocumentDB
      sum by(source_workload, destination_workload) (increase(istio_requests_total{reporter="destination"}[1m]))
      # Double check disk IOPS, throughput and latency
      # Check log from AWS CloudWatch
      Access AWS CloudWatch > Log Groups > /aws/docdb/<docdb_cluster_name>/profiler > Select log stream > Filter ns "leapXpert.<collection_name>"
      # You will need to look at `planSummary`, `millis`, `durationMillis`
      # Check indexes on database collections `db.<collection_name>.getIndexes()`

### DocumentDBLowMemNumOperationsThrottled

- Severity: critical

- Duration: 5m

- Description: This alert is triggered when instance has the queue depth for requests that are throttled due to low available memory taken at a one-minute frequency higher than 10 in last 5m.

- Actions:

      # This requires to take actions immediately
      # Check if we have any releases recently
      # Capture spike from istio requests, high request rate might indicates high load against AWS DocumentDB
      sum by(source_workload, destination_workload) (increase(istio_requests_total{reporter="destination"}[1m]))
      # Need to check number of database connections, high connections will consume more memory on the instance
      # Check log from AWS CloudWatch
      Access AWS CloudWatch > Log Groups > /aws/docdb/<docdb_cluster_name>/profiler > Select log stream > Filter ns "leapXpert.<collection_name>"
      # You will need to look at `planSummary`, `millis`, `durationMillis`
      # Check indexes on database collections `db.<collection_name>.getIndexes()`

### DocumentDBLowMemThrottleQueueDepth

- Severity: critical

- Duration: 5m

- Description: This alert is triggered when instance has the queue depth for requests that are throttled due to low available memory taken at a one-minute frequency higher than 10 in last 5m.

- Actions:

      # This requires to take actions immediately
      # Check if we have any releases recently
      # Capture spike from istio requests, high request rate might indicates high load against AWS DocumentDB
      sum by(source_workload, destination_workload) (increase(istio_requests_total{reporter="destination"}[1m]))
      # Need to check number of database connections, high connections will consume more memory on the instance
      # Check log from AWS CloudWatch
      Access AWS CloudWatch > Log Groups > /aws/docdb/<docdb_cluster_name>/profiler > Select log stream > Filter ns "leapXpert.<collection_name>"
      # You will need to look at `planSummary`, `millis`, `durationMillis`
      # Check indexes on database collections `db.<collection_name>.getIndexes()`

### DocumentDBLowMemThrottleMaxQueueDepth

- Severity: warning/critical

- Duration: 5m

- Description: This alert is triggered when instance has the maximum queue depth for requests that are throttled due to low available memory in a one-minute period higher than 10 in last 5m.

- Actions:

      # This requires to take actions immediately
      # Check if we have any releases recently
      # Capture spike from istio requests, high request rate might indicates high load against AWS DocumentDB
      sum by(source_workload, destination_workload) (increase(istio_requests_total{reporter="destination"}[1m]))
      # Need to check number of database connections, high connections will consume more memory on the instance
      # Check log from AWS CloudWatch
      Access AWS CloudWatch > Log Groups > /aws/docdb/<docdb_cluster_name>/profiler > Select log stream > Filter ns "leapXpert.<collection_name>"
      # You will need to look at `planSummary`, `millis`, `durationMillis`
      # Check indexes on database collections `db.<collection_name>.getIndexes()`

### DocumentDBDatabaseConnections

- Severity: critical

- Duration: 5m

- Description: This alert is triggered when instance has more than 1000 connections in last 10m. This requires to check instance connection limit <https://docs.aws.amazon.com/documentdb/latest/developerguide/limits.html>

- Actions:

      # Check if we have any releases recently
      # Capture spike from istio requests, high request rate might indicates high load against AWS DocumentDB
      sum by(source_workload, destination_workload) (increase(istio_requests_total{reporter="destination"}[1m]))
      # Query metrics to check mongodb client connections to see to if which application creates high connections against AWS DocumentDB, below is metric name
      sum by (app,server_address,lxp_version) (mongodb_driver_pool_size)

### DocumentDBBufferCacheHitRatio

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when instance storage has cache hit rate less than 95% in last 15m.

- Actions:

      # Run a command similar to the following to view a breakdown of how often each index is accessed:
      db.<collection_name>.aggregate([{$indexStats:{}}]).pretty()
      # Run the following command to view the total number of scans that were performed with indexes (index scans). This count is compared to the number of scans performed without an index (collection scans). You can then analyze how often indexes are used during the operations performed on a collection
      db.collection.stats()
      # Run a command similar to the following to view more details about open cursors.
      db.runCommand("listCursors")

### DocumentDBIndexBufferCacheHitRatio

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when instance has index cache hit rate less than 95% in last 15m.

- Actions:

      # Run a command similar to the following to view a breakdown of how often each index is accessed:
      db.<collection_name>.aggregate([{$indexStats:{}}]).pretty()
      # Run the following command to view the total number of scans that were performed with indexes (index scans). This count is compared to the number of scans performed without an index (collection scans). You can then analyze how often indexes are used during the operations performed on a collection
      db.collection.stats()
      # Run a command similar to the following to view more details about open cursors.
      db.runCommand("listCursors")

### DocumentDBDatabaseCursors

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when instance is more than 300 open cursors in last 15m. This requires to check instance cursor limit <https://docs.aws.amazon.com/documentdb/latest/developerguide/limits.html>

- Actions:

      # Run a command similar to the following to view more details about open cursors.
      db.runCommand("listCursors")

### DocumentDBDBClusterReplicaLagMaximum

- Severity: warning/critical

- Duration: 15m

- Description: This alert is triggered when replication lag between mongo primary and secondary is higher than 10m.

- Actions:

      # Check database actual replication lag
      rs.printSecondaryReplicationInfo()
      # Check network latency, disk throughtput
      # Check long-running operation by changing `secs_running`
      db.currentOp(
        {
          "active" : true,
          "secs_running" : { "$gt" : 3 },
          "ns" : "leapXpert"
        }
      )

### ElasticacheEngineCPUUtilization

- Severity: warning/critical

- Duration: 15m

- Description: This alert is triggered when ElastiCache engine has CPU utilization higher than 80/90% for 15m.

- Actions:

      # Check if there are long-running commands using Redis Slow log.
      redis-cli -h <elasticache_host> -p 6379
      elasticache_host:6379> SLOWLOG GET
      # Check command statistic using LXP / Cloudwatch Metric > Amazon ElastiCache > Check the following graphs
      - Command: if there are command bursts, or if latency is increasing.
      - Save In Progress: if backup or replication is occurring.
      - Connections: High number of NewConnections: Establishing a TCP connection is a computationally expensive operation.
      - Reclaimed & Eviction Keys:
        - Evictions: Redis evicts keys according to the maxmemory-policy parameter. Eviction happens when the cache doesn't have enough memory to hold new data. If eviction volume is high.
        - Reclaimed:  To free up memory, Redis samples and then deletes any keys that have reached their timeout expiration. This process is called "reclaim." If there is a high number of expirations.

### ElasticacheCurrConnections

- Severity: warning/critical

- Duration: 15m

- Description: This alert is triggered when concurrent connections reached to 80-90% of limit 65000 connections by AWS ElastiCache. A constant increase of CurrConnections may lead to the exhaustion of the 65,000 available connections. This type of increase may indicate an issue on the application side and connections improperly closed leaving the connection established on the server side.

- Actions:

      # List connected client connections
      redis-cli -h <elasticache_host> -p 6379
      elasticache_host:6379> CLIENT LIST

### ElasticacheMemoryUsagePercentage

- Severity: warning/critical

- Duration: 15m

- Description: This alert is triggered when ElastiCache engine has memory utilization higher than 80/90% for 15m.

- Actions:

      # Check if there are long-running commands using Redis Slow log.
      redis-cli -h <elasticache_host> -p 6379
      elasticache_host:6379> SLOWLOG GET
      # Check command statistic using LXP / Cloudwatch Metric > Amazon ElastiCache > Check the following graphs
      - Command: if there are command bursts, or if latency is increasing.
      - Save In Progress: if backup or replication is occurring.
      - Connections: High number of NewConnections: Establishing a TCP connection is a computationally expensive operation.
      - Reclaimed & Eviction Keys:
        - Evictions: Redis evicts keys according to the maxmemory-policy parameter. Eviction happens when the cache doesn't have enough memory to hold new data. If eviction volume is high.
        - Reclaimed:  To free up memory, Redis samples and then deletes any keys that have reached their timeout expiration. This process is called "reclaim." If there is a high number of expirations.

### ElasticacheAuthenticationFailures

- Severity: critical

- Duration: 5m

- Description: This alert is triggered when there are authentications attempts.

- Actions:

      # Check application log for more information
      # You can get list of applications that connect to Redis by this Prometheus query
      sum by (app) (redis_cache_connected)

### ElasticacheReplicationLag

- Severity: warning/critical

- Duration: 15m

- Description: This alert is triggered when ElastiCache engine has replication lag higher than 30-60s for 15m.

- Actions:

      # Check if there are long-running commands using Redis Slow log.
      redis-cli -h <elasticache_host> -p 6379
      elasticache_host:6379> SLOWLOG GET
      # Check command statistic using LXP / Cloudwatch Metric > Amazon ElastiCache > Check the following graphs
      - Command: if there are command bursts, or if latency is increasing.
      - Save In Progress: if backup or replication is occurring.
      - Connections: High number of NewConnections: Establishing a TCP connection is a computationally expensive operation.
      - Reclaimed & Eviction Keys:
        - Evictions: Redis evicts keys according to the maxmemory-policy parameter. Eviction happens when the cache doesn't have enough memory to hold new data. If eviction volume is high.
        - Reclaimed:  To free up memory, Redis samples and then deletes any keys that have reached their timeout expiration. This process is called "reclaim." If there is a high number of expirations.

### OpenSearchClusterStatusRed

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when AWS Opensearch cluster has status red.

- Actions:

      # List unassigned shards
      $ curl -XGET '<domain_endpoint>/_cat/shards?h=index,shard,prirep,state,unassigned.reason' | grep UNASSIGNED
      # Retrieve the details for why the shard is unassigned
      $ curl -XGET '<domain_endpoint>/_cluster/allocation/explain?pretty' -H 'Content-Type:application/json' -d'{
            "index": "<index name>",
            "shard": <shardId>,
            "primary": <true or false>
      }
      # Ref. <https://repost.aws/knowledge-center/opensearch-red-yellow-status>

### OpenSearchClusterStatusYellow

- Severity: warning

- Duration: 10m

- Description: This alert is triggered when AWS Opensearch cluster has status yellow.

- Actions:

      # List unassigned shards
      $ curl -XGET '<domain_endpoint>/_cat/shards?h=index,shard,prirep,state,unassigned.reason' | grep UNASSIGNED
      # Retrieve the details for why the shard is unassigned
      $ curl -XGET '<domain_endpoint>/_cluster/allocation/explain?pretty' -H 'Content-Type:application/json' -d'{
            "index": "<index name>",
            "shard": <shardId>,
            "primary": <true or false>
      }
      # Ref. <https://repost.aws/knowledge-center/opensearch-red-yellow-status>

### OpenSearchFreeStorageSpace

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when instance storage usage is lower than 1-15GB.

- Actions:

      # Increase storage size
      # Remove unused indices

### OpenSearchClusterIndexWritesBlocked

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when opensearch cluster blocks write requests.

- Actions:

      # Check free storage usage
      # Check resource memory usage

### OpenSearchCPUUtilization

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when instance storage usage is higher than 90%.

- Actions:

      # The nodes hot threads API acts as a task manager, showing you the breakdown of all resource-intensive threads that are running on your cluster.
      curl -XGET '<domain_endpoint>/_nodes/hot_threads'
      # A search thread pool that consumes high CPU indicates that search queries are overwhelming your OpenSearch Service cluster.
      # Your cluster can be overwhelmed by a single long-running query. An increase in queries performed by your cluster can also affect your search thread pool.
      curl -XGET '<domain_endpoint>/_tasks?actions=*search&detailed'
      # Ref. <https://repost.aws/knowledge-center/opensearch-troubleshoot-high-cpu>

### OpenSearchShardsActive

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when opensearch cluster has more than 1000 shards. This can lead to more memory consumption.

- Actions:

      # List shards
      curl -XGET '<domain_endpoint>/_cat/shards?v'
      # Example output
      index-000001 0 p STARTED      3014 31.1mb 192.168.56.10 H5dfFeA
      index-000001 0 r INITIALIZING    0 14.3mb 192.168.56.30 bGG90GE

### OpenSearchMasterReachableFromNode

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when leader node of opensearch cluster is down.

- Actions:

      # Raise ticket to AWS Support

### OpenSearchThreadpoolWriteQueue

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when Opensearch cluster has high number of queued tasks in the write thread pool. This alert tells you whether a request is being rejected because of high CPU usage or high indexing concurrency.

- Actions:

      # Check threadpool
      curl -XGET '<domain_endpoint>/_cat/thread_pool?v'
      # Example output
      node_name        name                      active queue rejected
      opensearch-node1 ad-batch-task-threadpool    0     0        0
      opensearch-node1 ad-threadpool               0     0        0
      opensearch-node1 analyze                     0     0        0

### OpenSearchThreadpoolWriteRejected

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when Opensearch cluster has has high number of rejected tasks in the write thread pool for 15m.

- Actions:

      #  If this number continually grows, then consider scaling cluster.

### OpenSearchDiskQueueDepth

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when instance has the number of I/O requests higher than 100. that are queued at a time against the storage. This could indicate a surge in requests or Amazon EBS throttling, resulting in increased latency.

- Actions:

      # Check the output for the following metrics
      sum by (region,client_id,domain_name) (aws_es_read_iops_average)
      sum by (region,client_id,domain_name) (aws_es_read_latency_average)
      sum by (region,client_id,domain_name) (aws_es_read_throughput_average)
      sum by (region,client_id,domain_name) (aws_es_write_iops_average)
      sum by (region,client_id,domain_name) (aws_es_write_latency_average)
      sum by (region,client_id,domain_name) (aws_es_write_throughput_average)
      # Check EBS limit <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html>

### RDSDatabaseConnections

- Severity: warning/critical

- Duration: 15m

- Description: This alert is triggered when database instance has more than 1000-2000 connections for 15m.

- Actions:

      # Calculate current usage by select instance type <https://aws.amazon.com/vi/rds/instance-types/>
      # For example max connections on instance db.t3.large (2vCPUs, 8GB Memory)
      # will be calulated as below. Ref <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html>. LEAST({DBInstanceClassMemory/9531392}, 5000)
      8*1024*1024*1024 / 9531392 = 901 connections
      # To view the connections for each database for your RDS for PostgreSQL instance
      SELECT datname, numbackends FROM pg_stat_database;
      # Investigate why application client opens many connections.

### RDSFreeableMemory

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when instance free memory is less than 515MB-1GB

- Actions:

      # Need to check active connections
      # To view the connections for each database for your RDS for PostgreSQL instance
      SELECT datname, numbackends FROM pg_stat_database;
      # Investigate why application client opens many connections.

### RDSFreeStorageSpace

- Severity: warning/critical

- Duration: 5m

- Description: This alert is triggered when instance free storage usage is lower than 15GB to 1GB.

- Actions:

      # Check database size, example output as below
      psql> \l+
      +-------+--------+----------+-------------+-------------+-------------------+---------+------------+-------------+
      | Name  | Owner  | Encoding |   Collate   |    Ctype    | Access privileges |  Size   | Tablespace | Description |
      +-------+--------+----------+-------------+-------------+-------------------+---------+------------+-------------+
      | sample | barney | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                   | 8225 kB | pg_default |            |
      +-------+--------+----------+-------------+-------------+-------------------+---------+------------+-------------+
      # Check database size
      psql> \c <database_name>
      psql>
      SELET table_name, pg_size_pretty( pg_relation_size(quote_ident(table_name)))
      FROM information_schema.tables
      WHERE table_schema = 'public'
      ORDER BY pg_relation_size(quote_ident(table_name)) desc
      # Example Output
      table_name   pg_size_pretty
      ---------------------------
      database_1   96 GB
      database_2   46 GB
      database_3   5725 MB
      database_4   5112 MB

### RDSCPUUtilization

- Severity: warning/critical

- Duration: 5m

- Description: This alert is triggered when instance CPU Utilization is higher than 90-95%

- Actions:

      # Need to check active connections
      # To view the connections for each database for your RDS for PostgreSQL instance
      SELECT datname, numbackends FROM pg_stat_database;
      # Investigate why application client opens many connections.

### RDSDiskLatency

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when instance has disk read/write latency more than 250ms.

- Actions:

      # Check instance disk IOPS and throughput
      - IOPS bottleneck at the instance level
      - IOPS bottleneck at the volume level
      - Throughput bottleneck at the instance level
      - Throughput bottleneck at the volume level
      # Ref. <https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck>

### MSKHasNoActiveController

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when MSK cluster has no active controller.

- Actions:

      # Check Zookeeper current state with below Prometheus query
      aws_kafka_zoo_keeper_session_state_maximum offset 5m != 1
      # Detailed connection state
      - NOT_CONNECTED: '0.0'
      - ASSOCIATING: '0.1'
      - CONNECTING: '0.5'
      - CONNECTEDREADONLY: '0.8'
      - CONNECTED: '1.0'
      - CLOSED: '5.0'
      - AUTH_FAILED: '10.0'
      # Follow steps to check the issue https://repost.aws/knowledge-center/msk-cluster-connection-issues
      # Raise ticket to AWS support for further investigation if above steps don't work

### MSKOfflinePartitionCount

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when AWS MSK cluster has offline partitions. Number of offline partitions that don’t have an active leader and aren't writable or readable.

- Actions:

      # Check disk space because these can be symptoms of low disk space.
      Ref. https://docs.aws.amazon.com/msk/latest/developerguide/troubleshooting.html#troubleshooting-offlinepartitions-outofsyncreplicas

### MSKZooKeeperSessionState

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when AWS MSK cluster has connection status to ZooKeepr with state other than CONNECTED for 10m.

- Actions:

      # Check current state and raise ticket to AWS for further investigation
      - NOT_CONNECTED: '0.0'
      - ASSOCIATING: '0.1'
      - CONNECTING: '0.5'
      - CONNECTEDREADONLY: '0.8'
      - CONNECTED: '1.0'
      - CLOSED: '5.0'
      - AUTH_FAILED: '10.0'

### MSKCPUUtilization

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when MSK cluster has CPU utlization more than 90%.

- Actions:

      # If these metrics for a broker have high values, then the broker might be experiencing a high CPU usage.
      sum by (region,broker_id,cluster_name) (aws_kafka_bytes_in_per_sec_average)
      sum by (region,broker_id,cluster_name) (aws_kafka_bytes_out_per_sec_average)
      sum by (region,broker_id,cluster_name) (aws_kafka_messages_in_per_sec_average)
      # Number of partitions per broker was exceeded <https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html>
      ## Having too many partitions causes performance degradation because of high CPU utilization.
      # If the number of connections to the client is high, then the broker might be experiencing a high CPU usage.
      sum by (region,broker_id,cluster_name) (aws_kafka_connection_count_average)
      sum by (region,broker_id,cluster_name) (aws_kafka_connection_creation_rate_average)
      sum by (region,broker_id,cluster_name) (aws_kafka_connection_close_rate_average)

### MSKMemoryUtilization

- Severity: critical

- Duration: 15m

- Description: This alert is triggered when instance memory usage is over 90%.

- Actions:

      # Need to check metrics HeapMemoryAfterGC to see if gabage collection working properly.
      sum by (broker_id,region,cluster_name) (aws_kafka_heap_memory_after_gc_average)

### MSKUnderReplicatedPartition

- Severity: warning/critical

- Duration: 10m

- Description: This alert will be triggered when a MSK broker has partitions that are under replication. A healthy cluster has no under replicated partitions. This under replication will add latency as consumers don't receive their needed data until messages are replicated. If cluster many have under replicated partitions, it typically points to a problem with one or more brokers. Need to find root cause the problem immediately to avoid any data loss.

- Actions:

      # Follow AWS docs to check the issue
      https://docs.aws.amazon.com/msk/latest/developerguide/troubleshooting.html#troubleshooting-urp

### MSKConsumerGroupLag

- Severity: critical

- Duration: 5m

- Description: This alert will be triggered when a kafka consumergroup has many lag messages.

- Actions:

      # Based on consumergroup check log of relative service (e.g)
      kubectl logs -f <pod_name> -n <namespace>
      # Rollout restart application base on consumergroup name


## Azure Metrics

### Alert Name: "AzureDatabasePostgresFlexibleStorageUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when instance storage usage is over 80-90%.

- Actions:

      # Need to review current storage size configuration
      # Ref. https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-scale-compute-storage-portal#scaling-storage-size

### Alert Name: "AzureDatabasePostgresFlexibleCpuUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when instance CPU usage is over 80-90%.

- Actions:

      # Need to review instance specs to scale properly
      # Ref. https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-scale-compute-storage-portal#scaling-the-compute-tier-and-size

### Alert Name: "AzureDatabasePostgresFlexibleMemoryUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when instance memory usage is over 80-90%.

- Actions:

      # Need to review instance specs to scale properly
      # Ref. https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-scale-compute-storage-portal#scaling-the-compute-tier-and-size

### Alert Name: "AzureDatabasePostgresFlexibleMaxConnections"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when 80% percent of active connections is higher than max connections.

- Actions:

      # Query Prometheus to check what the client connections are increasing.
      sum by (app,cluster,resourceName,dimension) (azure_metrics_database_postgresql_flexible_maximum_db_client_connections_active_count)
      # Check service logs for relevant services that connection to database name
      # which is founcd from above query.

### Alert Name: "AzureDatabasePostgresFlexibleNoConnections"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when Postgresql flexible server has no connections continuously for the last 10m.

- Actions:

      # - Check if all service pods are running correctly.
      # - Check if service logs for any related errors.
      # - Check database connection string is set correctly.

### Alert Name: "AzureDatabasePostgresFlexibleDeadlocks"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when there are deadlocks detected in a database.

- Actions:

      # - Create ticket for Microsoft to check.

### Alert Name: "AzureDatabasePostgresFlexibleDbNotAlive"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when the database is not alive.

- Actions:

      # - Create ticket for Microsoft to check.

### Alert Name: "AzureDatabasePostgresFlexibleFailedConnections"

- Severity: critical

- Duration: 30m

- Description: This alert is triggered when Postgresql flexible server has failed connections.

- Actions:

      # - Create ticket for Microsoft to check.

### Alert Name: "AzureEventhubNamespaceCpuUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when Azure Eventhub namespace CPU usage is over 80-90%.

- Actions:

      # Need to check Eventhub namespace metrics to see which topic has high CPU usage
      # Ref. https://learn.microsoft.com/en-us/azure/event-hubs/monitor-event-hubsing-the-compute-tier-and-size

### Alert Name: "AzureEventhubNamespaceMemoryUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when Azure Eventhub namespace memory usage is over 80-90%.

- Actions:

      # Need to check Eventhub namespace metrics to see which topic has high memory usage
      # Ref. https://learn.microsoft.com/en-us/azure/event-hubs/monitor-event-hubsing-the-compute-tier-and-size

### Alert Name: "AzureEventhubServerErrors"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when Azure Eventhub has server errors.

- Actions:

      # Need to check Eventhub namespace metrics to see which topic has server errors
      # Ref. https://learn.microsoft.com/en-us/azure/event-hubs/monitor-event-hubs-reference#error-metrics

### Alert Name: "AzureEventhubThrottledRequests"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when Azure Eventhub has throttled requests.

- Actions:

      # Eventhub usage may be exceeded. Consider increasing EventHub Throughput Unit (TU) if needed.
      # Ref. https://learn.microsoft.com/en-us/azure/event-hubs/monitor-event-hubs-reference#request-metrics

### Alert Name: "AzureEventhubQuotaExceededErrors"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when Azure Eventhub has quota exceeded errors

- Actions:

      # Eventhub quota may be exceeded. Consider increasing quota if needed.
      # Ref. https://learn.microsoft.com/en-us/azure/event-hubs/monitor-event-hubs-reference#error-metrics

### Alert Name: "AzureCacheRedisCpuUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when Azure Cache for Redis CPU usage is over 80-90%.

- Actions:

      # Need to check Azure Cache for Redis has high load on which ShardId
      # Work with BE to indentify the issue and collect error log on whole FMOP services
      # Ref. https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-how-to-monitor

### Alert Name: "AzureCacheRedisMemoryUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when Azure Cache for Redis memory usage is over 80-90%.

- Actions:

      # Need to check Azure Cache for Redis has high load on which ShardId
      # Work with BE to indentify the issue and collect error log on whole FMOP services
      # Ref. https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-how-to-monitor

### Alert Name: "AzureCacheRedisServerLoadUsage"

- Severity: warning/critical

- Duration: 10m

- Description: This alert is triggered when Azure Cache for Redis server load usage is over 80-90%.

- Actions:

      # Need to check Azure Cache for Redis has high load on which ShardId
      # Work with BE to indentify the issue and collect error log on whole FMOP services
      # Ref. https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-how-to-monitor

### Alert Name: "AzureCacheRedisErrorOperations"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when Azure Cache for Redis has high error count more than 10.

- Actions:

      # Need to check Azure Cache for Redis has high load on which ShardId, ErrorType
      # Work with BE to indentify the issue and collect error log on whole FMOP services
      # Ref. https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-how-to-monitor

### Alert Name: "AzureCacheRedisHighConnectedClients"

- Severity: critical

- Duration: 10m

- Description: This alert is triggered when there is high connected clients on specific shard ID on Azure Cache for Redis Server.

- Actions:

      # Need to check Azure Cache for Redis has high load on which ShardId, ErrorType
      # Work with BE to indentify the issue and collect error log on whole FMOP services
      # Ref. https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-how-to-monitor
      # Ref. https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-cache-for-redis-limits

### Alert Name: "AzureCosmoMongodbOperationLatency"

- Severity: critical

- Duration: 5m

- Description: The alert is triggered when Azure CosmosDB for Mongo latency on specific operation is higher than 30s.

- Actions:

      # Need to check Azure CosmosDB metrics for to capture timestamp having latency increase.
      # Insight information to check DatabaseName, CollectionName, Region, ConnectionMode, OperationType, PublicAPIType
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/monitor?tabs=azure-diagnostics


### Alert Name: "AzureCosmoMongodbPhysicalPartitionSize16GB"

- Severity: Critical

- Duration: 10m

- Description: The alert is triggered when Azure CosmosDB physical partition size higher than 16GB.

- Actions:

      # If Azure CosmosDB physical partition size keeps increased, this can lead to data loss from FMOP side.
      # Increase physical volume size to 30GB as maximum threshold allowed by Azure
      # Follow up with relevant team for quick actions.
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits#provisioned-throughput
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview

### Alert Name: "AzureCosmoMongodbPhysicalPartitionSize18GB"

- Severity: Critical

- Duration: 10m

- Description: The alert is triggered when Azure CosmosDB physical partition size higher than 18GB.

- Actions:

      # If Azure CosmosDB physical partition size keeps increased, this can lead to data loss from FMOP side.
      # Increase physical volume size to 30GB as maximum threshold allowed by Azure
      # Follow up with relevant team for quick actions.
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits#provisioned-throughput
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview

### Alert Name: "AzureCosmoMongodbPhysicalPartitionSize26GB"

- Severity: Critical

- Duration: 10m

- Description: The alert is triggered when Azure CosmosDB physical partition size higher than 26GB.

- Actions:

      # If Azure CosmosDB physical partition size reaches 30GB, this can lead to data loss from FMOP side.
      # Also when the limit has been increased from 20GB to 30GB, the SLA of CosmosDB service is not guaranteed by Azure.
      # Follow up with relevant teams for to resolve the issue ASAP.
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits#provisioned-throughput
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview

### Alert Name: "AzureCosmoMongodbPhysicalPartitionSize28GB"

- Severity: Critical

- Duration: 10m

- Description: The alert is triggered when Azure CosmosDB physical partition size higher than 28GB.

- Actions:

      # If Azure CosmosDB physical partition size reaches 30GB, this can lead to data loss from FMOP side.
      # Also when the limit has been increased from 20GB to 30GB, the SLA of CosmosDB service is not guaranteed by Azure.
      # Follow up with relevant teams to resolve the issue ASAP.
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits#provisioned-throughput
      # Ref. https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview

### Alert Name: "AzureCosmoMongodbCollectionUnhealthy"

- Severity: Critical

- Duration: 90m

- Description: The alert is triggered when Azure CosmosDB has a collection that disappeared from Prometheus for more than 90 mins. Possibly the collection has become unhealthy.

- Actions:

      # Try to connect to MongoDB and perform a query on the collection. For example: `db.wan_DBEmailInstructionIntegrationRequest.find({})`
      # If the query timed out then the collection might have crashed.
      # You can verify more by going to Azure portal -> CosmosDB instance -> Data Explorer -> Choose the collection -> Settings
      # The settings of the collection should not be accessible.
      # At this moment we need to create a ticket for Microsoft to fix.

### Alert Name: "AzureCosmoMongodbErrorRequests"

- Severity: Critical

- Duration: 10m

- Description: The alert is triggered when Azure CosmosDB has many error requests for more than 10m.

- Actions:

      # - Check the error code here: https://aka.ms/mongo-db-error-codes

### Alert Name: "AzureCosmoMongodbServiceAvailability"

- Severity: Critical

- Duration: 10m

- Description: The alert is triggered when Azure CosmosDB has service availability less than 90% for more than 10 minutes.

- Actions:

      # - This indicates that Microsoft might have violated their SLA and that may affect our services. We can check with them to make sure the SLA is guaranteed.

## Event Hubs

### Alert Name: "EventHubsConsumerGroupLag"

- Severity: critical

- Duration: 10m

- Description: The alert is triggered when a consumer group has a lag of more than 100 for more than 10m.

- Actions:

      # Check if consuming service is OOMKilled or in CrashLoopBackOff or Error state. Also check if the service CPU is being throttled.

### Alert Name: "EventHubsNumberOfTopicsLimit"

- Severity: critical

- Duration: 0m

- Description: The alert is triggered when the number of topics (Event Hubs) will reach the limit of 100 soon.

- Actions:

      # Check immediately with BE or DevOps team.

## Frontdoor

### Alert Name: "AzureFrontdoorBackendLatency"

- Severity: critical

- Duration: 10m

- Description: The alert is triggered when Azure Frontdoor has high latency more than 30s to backend.

- Actions:

      # Check backend latency from Azure Frontdoor to backends from LXP / Azure Metrics dashboard
      # Check istio request latency metrics to ensure system response is stable or not
      # Follow up with DevOps team for further actions with Azure Support if needed

### Alert Name: "AzureFrontdoorBackendRequestFailed"

- Severity: critical

- Duration: 10m

- Description: The alert is triggered when Azure Frontdoor has many failed requests to the specific backends.

- Actions:

      # Check service logs from the specific backends based on API paths
      # Double check backend latency from Azure Frontdoor to backends from LXP / Azure Metrics dashboard

### Alert Name: "AzureFrontdoorClientRequestFailed"

- Severity: critical

- Duration: 10m

- Description: The alert is triggered when client encounters failed requests to Azure Frontdoor.

- Actions:

      # Check service logs from the specific backends based on API paths
      # Double check backend latency from Azure Frontdoor to backends from LXP / Azure Metrics dashboard

# Integration

## MacOS Node Exporter

### Alert Name: "MacInstanceDown1H"

- Severity: critical

- Duration: 1h

- Description: This alert will be triggered when imessage Mac instance has been down for 1h.

- Actions:

      # You can find instance ID, public IP and domain of this instance in alert description.
      # Check instance status on AWS EC2 console and try to SSH/VNC to the instance
      # Note: if the instance is in scrubbing workflow then the downtime can be up to 50m to 110m depending on processor architecture
      # Ref. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-stop

### Alert Name: "MacInstanceDownTimes1D"

- Severity: critical


- Description: This alert will be triggered when imessage Mac instance has been down more than 3 times for the last 1 day.

- Actions:

      # You can find instance ID, public IP and domain of this instance in alert description.
      # Check instance status on AWS EC2 console and try to SSH/VNC to the instance
      # Note: if the instance is in scrubbing workflow then the downtime can be up to 50m to 110m depending on processor architecture
      # Ref. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-stop

### Alert Name: "MacInstanceCpuHigh"

- Severity: warning

- Duration: 5m

- Description: This alert will be triggered when iMessage Mac instance has CPU usage more than 80%.

- Actions:

      # SSH to the instance and check storage usage
      # Use top command to check which process cosumes high CPU usage

### Alert Name: "MacInstanceMemoryHigh"

- Severity: warning

- Duration: 5m

- Description: This alert will be triggered when iMessage Mac instance has memory usage more than 80%.

- Actions:

      # SSH to the instance and check storage usage
      # Use top command to check which process cosumes high memory usage

## iGateway

### Alert Name: "iMessageLargeFileAttachment"

- Severity: warning

- Duration: 0m

- Description: The attachment file is larger than 25MB and will not be archived in the FMOP.

- Actions:

      # Warning the end user about the maximum attachment file size for sending and archiving

### Alert Name: "iMessageRetryMessage"

- Severity: critical

- Duration: 20m

- Description: The FMOP failed to retry message for archiving in 20m.

- Actions:

      # SSH to the instance and check the instance status

### Alert Name: "iMessageRotationDisabled"

- Severity: critical

- Duration: 60m

- Description: The rotation is currently disabled in the mac instance.

- Actions:

      # Enable the rotation for agents, using such API call:
      curl --location -g --request PUT 'https://<igateway domain>/imessage/v1/rotation/status' \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "rotationStatus": 1
      }'

### Alert Name: "iMessageRotationStuck"

- Severity: critical

- Duration: 30m

- Description: Rotation is stuck on a Mac instance.

- Actions:

      # Turn off rotation, make sure all agents get logged out
      # Login into gateway-lxp or launcher-lxp. Consult Delivery team for the login password
      # Open System Preferences → System Preferences →  Security & Privacy -> Privacy → Accessibility
      # Authenticate with a user has sudo permission
      # Click on + button to add a new one
      # From Finder, press: Shift + Command + . to show hidden files
      # Navigate to /System/Library/CoreServices/
      # Choose System Events
      # Then start rotation

### Alert Name: "iGatewayUnauthorizedAccess"

- Severity: critical

- Duration: 0m

- Description: There are unauthorized users logging in to the Mac instance when rotation/self-onboarding is initializing.

- Actions:
      # Please notify the Delivery team for further investigation.

### Alert Name: "igatewayAgentSqliteDbCorrupted"

- Severity: critical

- Duration: 0m

- Description: Database sqlite on iGateway agent has been corrupted.

- Actions:

      # Check iGateway log with message AGENT_SQLITE_DB_CORRUPTED
      # In the log, you should find the agent that is having the issue.
      # Recover database with below steps
      ## SSH to the Mac
      ## Swicth to the agent corrupted:
      $ sudo su - [agent_name]
      $ cd ~/Library/Application\ Support/LXP/imessage
      #Backup the agent DB
      $ cp lxp-agent.db lxp-agent.db.bk   # Backup the original (corrupted) DB file
      $ sqlite3 lxp-agent.db .recover > recovered_data.sql   # Export recoverable data to SQL file
      $ sqlite3 recovered.db < recovered_data.sql   # Import recovered data to a new DB file
      $ rm lxp-agent.db   # Remove corrupted DB file
      $ mv recovered.db lxp-agent.db   # Set recovered DB file as the new LXP DB file
      ## [Optional] Remove backup/recovered files
      $ rm recovered_data.sql lxp-agent.db.bk.20240102

## WhatsApp

### Alert Name: "WhatsappApiError"

- Severity: critical

- Duration: 2m

- Description: The alert is triggered when one or more WhatsApp services has errors.

- Actions:

      # Need to get the affected Whatsapp pod/service using this query: `whatsapp_client_endpoint_requests{result!="ok"}`, then check https://developers.facebook.com/docs/whatsapp/on-premises/errors for the error code.

### Alert Name: "WhatsappApiErrorTemplateGetBanned"

- Severity: critical

- Duration: 0m

- Description: The alert is triggered when one or more WhatsApp services has errors.

- Actions:

      # Need to get the affected Whatsapp pod/service using this query: `whatsapp_client_endpoint_requests{result!="ok"}`, then check https://developers.facebook.com/docs/whatsapp/on-premises/errors for the error code.
      # Report the issue to Delivery Team

### Alert Name: "WhatsappApiErrorParameterValueIsNotValid"

- Severity: critical

- Duration: 0m

- Description: The alert is triggered when one or more WhatsApp services has errors.

- Actions:

      # Need to get the affected Whatsapp pod/service using this query: `whatsapp_client_endpoint_requests{result!="ok"}`, then check https://developers.facebook.com/docs/whatsapp/on-premises/errors for the error code.
      # Report the issue to Delivery Team

### Alert Name: "WhatsappVersionExpired"

- Severity: critical

- Duration: 0m

- Description: The alert is triggered when one or more WhatsApp pods using an expired version.

- Actions:

      # Contact Delivery team to upgrade the version.

### Alert Name: "WhatsappVersionExpiry15Days"

- Severity: critical

- Duration: 0m

- Description: The alert is triggered when one or more WhatsApp pods using a version that is expiring soon.

- Actions:

      # Contact Delivery team to upgrade the version.

### Alert Name: "WhatsappVersionExpiry7Days"

- Severity: critical

- Duration: 0m

- Description: The alert is triggered when one or more WhatsApp pods using a version that is expiring soon.

- Actions:

      # Contact Delivery team to upgrade the version.

### Alert Name: "WhatsappOutMessageError"

- Severity: critical

- Duration: 2m

- Description: The alert is triggered when a Whatsapp pod is having out message error.

- Actions:

      # Contact Delivery team for the error.

# Endpoints Monitor

## Probe

### Alert Name: "BlackboxExporterHTTPEndpointDown"

- Severity: critical

- Duration: 5m

- Description: The alert is triggered when http endpoint is unreachable for 5m.

- Actions:

      # Try to access endpoint from your browser
      # These endpoint will not require authenticate or input params

### Alert Name: "BlackboxExporterFmopBeUrlEndpointDown"

- Severity: critical

- Duration: 2m

- Description: The alert is triggered when FMOP backend app readiness endpoint is unreachable for 2m.

- Actions:

      # Check pod status to see if any pod issue
      kubectl get pod -A | grep < service_name >


### Alert Name: "BlackboxExporteriMessageHTTPEndpointDown"

- Severity: critical

- Duration: 15m

- Description: The alert is triggered when imessage http endpoint is unreachable for 15m.

- Actions:

      # Try to access endpoint from your browser
      # These endpoint will not require authenticate or input params

### Alert Name: "BlackboxExporterWhatsappEndpointDown"

- Severity: critical

- Duration: 10m

- Description: The alert is triggered when Whatapps endpoints are unreachable for 10m.

- Actions:

      # First port forward:
      kubectl port-forward pod/<affected whatsapp pod> -n <whatsapp_namespace> 2080

      #Then check gateway status:
      curl http://localhost:2080/v1/health

      # If status is unregistered, forward the alert to Delivery team.
      # If status is disconnected, try restarting Whatsapp pod.
      # If status is uninitialized, try restarting Whatsapp pod.
      # If you cannot check the status, escalate to Delivery Team or SRE team.

### Alert Name: "BlackboxExporterEndpointCertificateExpiry"

- Severity: warning/critical

- Duration: 0m

- Description: The alert is triggered when certificate is about to expire in next 7/15 days

- Actions:

      # These endpoint will need api token to access
      # Escalate to Delivery Team or SRE team

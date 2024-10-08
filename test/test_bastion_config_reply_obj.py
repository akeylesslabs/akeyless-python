# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.bastion_config_reply_obj import BastionConfigReplyObj  # noqa: E501
from akeyless.rest import ApiException

class TestBastionConfigReplyObj(unittest.TestCase):
    """BastionConfigReplyObj unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BastionConfigReplyObj
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.bastion_config_reply_obj.BastionConfigReplyObj()  # noqa: E501
        if include_optional :
            return BastionConfigReplyObj(
                api_gateway_url = '0', 
                cluster_id = '0', 
                gator_cluster_id = 56, 
                _global = akeyless.models.bastion_global_conf.BastionGlobalConf(
                    allowed_bastion_urls = [
                        '0'
                        ], 
                    legacy_signing_alg = True, 
                    rdp_username_sub_claim = '0', 
                    ssh_username_sub_claim = '0', ), 
                ssh_bastion = akeyless.models.ssh_bastion_conf.SshBastionConf(
                    hide_session_recording = True, 
                    kexalgs = '0', 
                    log_forwarding = akeyless.models.log_forwarding_config_part.LogForwardingConfigPart(
                        aws_s3_config = akeyless.models.aws_s3_log_forwarding_config.AwsS3LogForwardingConfig(
                            aws_access_id = '0', 
                            aws_access_key = '0', 
                            aws_auth_type = '0', 
                            aws_region = '0', 
                            aws_role_arn = '0', 
                            aws_use_gateway_cloud_identity = True, 
                            bucket_name = '0', 
                            log_folder = '0', ), 
                        azure_analytics_config = akeyless.models.azure_log_analytics_forwarding_config.AzureLogAnalyticsForwardingConfig(
                            azure_workspace_id = '0', 
                            azure_workspace_key = '0', ), 
                        datadog_config = akeyless.models.datadog_forwarding_config.DatadogForwardingConfig(
                            datadog_api_key = '0', 
                            datadog_host = '0', 
                            datadog_log_service = '0', 
                            datadog_log_source = '0', 
                            datadog_log_tags = '0', ), 
                        elasticsearch_config = akeyless.models.elasticsearch_log_forwarding_config.ElasticsearchLogForwardingConfig(
                            elasticsearch_api_key = '0', 
                            elasticsearch_auth_type = '0', 
                            elasticsearch_cloud_id = '0', 
                            elasticsearch_enable_tls = True, 
                            elasticsearch_index = '0', 
                            elasticsearch_nodes = '0', 
                            elasticsearch_password = '0', 
                            elasticsearch_server_type = '0', 
                            elasticsearch_tls_certificate = '0', 
                            elasticsearch_user_name = '0', ), 
                        google_chronicle_config = akeyless.models.google_chronicle_forwarding_config.GoogleChronicleForwardingConfig(
                            customer_id = '0', 
                            log_type = '0', 
                            region = '0', 
                            service_account_key = '0', ), 
                        json_output = True, 
                        logan_enable = True, 
                        logan_url = '0', 
                        logstash_config = akeyless.models.logstash_log_forwarding_config.LogstashLogForwardingConfig(
                            logstash_dns = '0', 
                            logstash_enable_tls = True, 
                            logstash_protocol = '0', 
                            logstash_tls_certificate = '0', ), 
                        logz_io_config = akeyless.models.logz_io_log_forwarding_config.LogzIoLogForwardingConfig(
                            target_logz_io_protocol = '0', 
                            target_logz_io_token = '0', ), 
                        pull_interval_sec = '0', 
                        splunk_config = akeyless.models.splunk_log_forwarding_config.SplunkLogForwardingConfig(
                            splunk_enable_tls = True, 
                            splunk_index = '0', 
                            splunk_source = '0', 
                            splunk_sourcetype = '0', 
                            splunk_tls_certificate = '0', 
                            splunk_token = '0', 
                            splunk_url = '0', ), 
                        sumo_logic_config = akeyless.models.sumologic_log_forwarding_config.SumologicLogForwardingConfig(
                            sumo_logic_endpoint = '0', 
                            sumo_logic_host = '0', 
                            sumo_logic_tags = '0', ), 
                        syslog_config = akeyless.models.syslog_log_forwarding_config.SyslogLogForwardingConfig(
                            syslog_enable_tls = True, 
                            syslog_formatter = '0', 
                            syslog_host = '0', 
                            syslog_network = '0', 
                            syslog_target_tag = '0', 
                            syslog_tls_certificate = '0', ), 
                        target_log_type = '0', ), 
                    session_termination = akeyless.models.ssh_bastion_session_termination.SshBastionSessionTermination(
                        api_password = '0', 
                        api_token = '0', 
                        api_url = '0', 
                        api_username = '0', 
                        enabled = True, ), ), 
                web_bastion = akeyless.models.web_bastion_conf.WebBastionConf(
                    guacamole = akeyless.models.web_bastion_guacamole.WebBastionGuacamole(
                        keyboard_layout = '0', ), 
                    rdp_record = akeyless.models.web_bastion_rdp_record.WebBastionRdpRecord(
                        aws = akeyless.models.aws_storage.AwsStorage(
                            access_key_id = '0', 
                            access_key_secret = '0', 
                            auth_type = '0', 
                            bucket = '0', 
                            prefix = '0', 
                            region = '0', ), 
                        azure = akeyless.models.azure_storage.AzureStorage(
                            auth_type = '0', 
                            client_id = '0', 
                            client_secret = '0', 
                            storage_account = '0', 
                            storage_container_name = '0', 
                            tenant_id = '0', ), 
                        storage_type = '0', ), )
            )
        else :
            return BastionConfigReplyObj(
        )

    def testBastionConfigReplyObj(self):
        """Test BastionConfigReplyObj"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

# AkeylessGatewayConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admins** | [**AdminsConfigPart**](AdminsConfigPart.md) |  | [optional] 
**ca_certificates** | [**CaCertificatesConfigPart**](CaCertificatesConfigPart.md) |  | [optional] 
**cache** | [**CacheConfigPart**](CacheConfigPart.md) |  | [optional] 
**cf** | [**CFConfigPart**](CFConfigPart.md) |  | [optional] 
**config_protection_key_name** | **str** |  | [optional] 
**general** | [**GeneralConfigPart**](GeneralConfigPart.md) |  | [optional] 
**k8s_auths** | [**K8SAuthsConfigPart**](K8SAuthsConfigPart.md) |  | [optional] 
**kerberos** | [**KerberosConfigPart**](KerberosConfigPart.md) |  | [optional] 
**kmip_clients** | [**KMIPConfigPart**](KMIPConfigPart.md) |  | [optional] 
**ldap** | [**LdapConfigPart**](LdapConfigPart.md) |  | [optional] 
**leadership** | [**LeadershipConfigPart**](LeadershipConfigPart.md) |  | [optional] 
**log_forwarding** | [**LogForwardingConfigPart**](LogForwardingConfigPart.md) |  | [optional] 
**message_queue_info** | [**GatewayMessageQueueInfo**](GatewayMessageQueueInfo.md) |  | [optional] 
**migrations** | [**MigrationsConfigPart**](MigrationsConfigPart.md) |  | [optional] 
**producers** | [**ProducersConfigPart**](ProducersConfigPart.md) |  | [optional] 
**rotators** | [**RotatorsConfigPart**](RotatorsConfigPart.md) |  | [optional] 
**saml** | [**DefaultConfigPart**](DefaultConfigPart.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from akeyless.models.akeyless_gateway_config import AkeylessGatewayConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AkeylessGatewayConfig from a JSON string
akeyless_gateway_config_instance = AkeylessGatewayConfig.from_json(json)
# print the JSON string representation of the object
print(AkeylessGatewayConfig.to_json())

# convert the object into a dict
akeyless_gateway_config_dict = akeyless_gateway_config_instance.to_dict()
# create an instance of AkeylessGatewayConfig from a dict
akeyless_gateway_config_from_dict = AkeylessGatewayConfig.from_dict(akeyless_gateway_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



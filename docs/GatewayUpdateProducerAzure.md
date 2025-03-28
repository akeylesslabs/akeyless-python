# GatewayUpdateProducerAzure

gatewayUpdateProducerAzure is a command that updates azure producer [Deprecated: Use dynamic-secret-update-azure command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_obj_id** | **str** | Azure App Object Id | [optional] 
**azure_client_id** | **str** | Azure Client ID | [optional] 
**azure_client_secret** | **str** | Azure Client Secret | [optional] 
**azure_tenant_id** | **str** | Azure Tenant ID | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**fixed_user_claim_keyname** | **str** | FixedUserClaimKeyname | [optional] [default to 'false']
**fixed_user_only** | **bool** | Fixed user | [optional] [default to False]
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic secret encryption key | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to True]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_group_obj_id** | **str** | User Group Object Id | [optional] 
**user_portal_access** | **bool** | Azure User portal access | [optional] [default to False]
**user_principal_name** | **str** | User Principal Name | [optional] 
**user_programmatic_access** | **bool** | Azure User programmatic access | [optional] [default to False]
**user_role_template_id** | **str** | User Role Template Id | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.gateway_update_producer_azure import GatewayUpdateProducerAzure

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerAzure from a JSON string
gateway_update_producer_azure_instance = GatewayUpdateProducerAzure.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerAzure.to_json())

# convert the object into a dict
gateway_update_producer_azure_dict = gateway_update_producer_azure_instance.to_dict()
# create an instance of GatewayUpdateProducerAzure from a dict
gateway_update_producer_azure_from_dict = GatewayUpdateProducerAzure.from_dict(gateway_update_producer_azure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



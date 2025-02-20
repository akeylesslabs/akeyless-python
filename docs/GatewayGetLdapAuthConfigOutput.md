# GatewayGetLdapAuthConfigOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_access_id** | **str** |  | [optional] 
**ldap_anonymous_search** | **bool** |  | [optional] 
**ldap_bind_dn** | **str** |  | [optional] 
**ldap_bind_password** | **str** |  | [optional] 
**ldap_cert** | **str** |  | [optional] 
**ldap_enable** | **bool** |  | [optional] 
**ldap_group_attr** | **str** |  | [optional] 
**ldap_group_dn** | **str** |  | [optional] 
**ldap_group_filter** | **str** |  | [optional] 
**ldap_private_key** | **str** |  | [optional] 
**ldap_token_expiration** | **str** |  | [optional] 
**ldap_url** | **str** |  | [optional] 
**ldap_user_attr** | **str** |  | [optional] 
**ldap_user_dn** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_get_ldap_auth_config_output import GatewayGetLdapAuthConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayGetLdapAuthConfigOutput from a JSON string
gateway_get_ldap_auth_config_output_instance = GatewayGetLdapAuthConfigOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayGetLdapAuthConfigOutput.to_json())

# convert the object into a dict
gateway_get_ldap_auth_config_output_dict = gateway_get_ldap_auth_config_output_instance.to_dict()
# create an instance of GatewayGetLdapAuthConfigOutput from a dict
gateway_get_ldap_auth_config_output_from_dict = GatewayGetLdapAuthConfigOutput.from_dict(gateway_get_ldap_auth_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GatewayGetLdapAuthConfig

gatewayGetLdapAuth is a command that gets ldap auth config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_get_ldap_auth_config import GatewayGetLdapAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayGetLdapAuthConfig from a JSON string
gateway_get_ldap_auth_config_instance = GatewayGetLdapAuthConfig.from_json(json)
# print the JSON string representation of the object
print(GatewayGetLdapAuthConfig.to_json())

# convert the object into a dict
gateway_get_ldap_auth_config_dict = gateway_get_ldap_auth_config_instance.to_dict()
# create an instance of GatewayGetLdapAuthConfig from a dict
gateway_get_ldap_auth_config_from_dict = GatewayGetLdapAuthConfig.from_dict(gateway_get_ldap_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



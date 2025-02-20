# GatewayUpdateLdapAuthConfigOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.gateway_update_ldap_auth_config_output import GatewayUpdateLdapAuthConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLdapAuthConfigOutput from a JSON string
gateway_update_ldap_auth_config_output_instance = GatewayUpdateLdapAuthConfigOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLdapAuthConfigOutput.to_json())

# convert the object into a dict
gateway_update_ldap_auth_config_output_dict = gateway_update_ldap_auth_config_output_instance.to_dict()
# create an instance of GatewayUpdateLdapAuthConfigOutput from a dict
gateway_update_ldap_auth_config_output_from_dict = GatewayUpdateLdapAuthConfigOutput.from_dict(gateway_update_ldap_auth_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



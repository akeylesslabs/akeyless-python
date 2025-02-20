# GatewayUpdateLdapAuthConfig

gatewayUpdateLdapAuth is a command that updates ldap auth config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | The access ID of the Ldap auth method | [optional] 
**bind_dn** | **str** | Bind DN | [optional] 
**bind_dn_password** | **str** | Bind DN Password | [optional] 
**group_attr** | **str** | Group Attr | [optional] 
**group_dn** | **str** | Group Dn | [optional] 
**group_filter** | **str** | Group Filter | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**ldap_ca_cert** | **str** | LDAP CA Certificate (base64 encoded) | [optional] 
**ldap_enable** | **str** | Enable Ldap [true/false] | [optional] 
**ldap_url** | **str** | LDAP Server URL, e.g. ldap://planetexpress.com:389 | [optional] 
**signing_key_data** | **str** | The private key (base64 encoded), associated with the public key defined in the Ldap auth | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_attribute** | **str** | User Attribute | [optional] 
**user_dn** | **str** | User DN | [optional] 

## Example

```python
from akeyless.models.gateway_update_ldap_auth_config import GatewayUpdateLdapAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLdapAuthConfig from a JSON string
gateway_update_ldap_auth_config_instance = GatewayUpdateLdapAuthConfig.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLdapAuthConfig.to_json())

# convert the object into a dict
gateway_update_ldap_auth_config_dict = gateway_update_ldap_auth_config_instance.to_dict()
# create an instance of GatewayUpdateLdapAuthConfig from a dict
gateway_update_ldap_auth_config_from_dict = GatewayUpdateLdapAuthConfig.from_dict(gateway_update_ldap_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



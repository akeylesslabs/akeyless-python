# DynamicSecretUpdateLdap

dynamicSecretUpdateLdap is a command that updates ldap dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] 
**bind_dn** | **str** | Bind DN | [optional] 
**bind_dn_password** | **str** | Bind DN Password | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**external_username** | **str** | Externally provided username [true/false] | [optional] [default to 'false']
**fixed_user_claim_keyname** | **str** | For externally provided users, denotes the key-name of IdP claim to extract the username from (relevant only for external-username&#x3D;true) | [optional] [default to 'ext_username']
**group_dn** | **str** | Group DN which the temporary user should be added | [optional] 
**host_provider** | **str** | Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**ldap_ca_cert** | **str** | CA Certificate File Content | [optional] 
**ldap_url** | **str** | LDAP Server URL | [optional] 
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **List[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_rd_gateway_server** | **str** | RD Gateway server | [optional] 
**secure_access_rdp_domain** | **str** | Required when the Dynamic Secret is used for a domain user | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target** | **List[str]** | A list of linked targets to be associated, Relevant only for Secure Remote Access for ssh cert issuer, ldap rotated secret and ldap dynamic secret, To specify multiple targets use argument multiple times | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_expiration** | **str** | Token expiration | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_attribute** | **str** | User Attribute | [optional] 
**user_dn** | **str** | User DN | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.dynamic_secret_update_ldap import DynamicSecretUpdateLdap

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretUpdateLdap from a JSON string
dynamic_secret_update_ldap_instance = DynamicSecretUpdateLdap.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretUpdateLdap.to_json())

# convert the object into a dict
dynamic_secret_update_ldap_dict = dynamic_secret_update_ldap_instance.to_dict()
# create an instance of DynamicSecretUpdateLdap from a dict
dynamic_secret_update_ldap_from_dict = DynamicSecretUpdateLdap.from_dict(dynamic_secret_update_ldap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



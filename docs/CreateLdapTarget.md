# CreateLdapTarget

createldapTarget is a command that creates a new target. [Deprecated: Use target-create-ldap command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_dn** | **str** | Bind DN | 
**bind_dn_password** | **str** | Bind DN Password | 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**ldap_ca_cert** | **str** | CA Certificate File Content | [optional] 
**ldap_url** | **str** | LDAP Server URL | 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**server_type** | **str** | Set Ldap server type, Options:[OpenLDAP, ActiveDirectory]. Default is OpenLDAP | [optional] [default to 'OpenLDAP']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_expiration** | **str** | Token expiration | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_ldap_target import CreateLdapTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLdapTarget from a JSON string
create_ldap_target_instance = CreateLdapTarget.from_json(json)
# print the JSON string representation of the object
print(CreateLdapTarget.to_json())

# convert the object into a dict
create_ldap_target_dict = create_ldap_target_instance.to_dict()
# create an instance of CreateLdapTarget from a dict
create_ldap_target_from_dict = CreateLdapTarget.from_dict(create_ldap_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



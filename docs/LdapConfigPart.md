# LdapConfigPart


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
from akeyless.models.ldap_config_part import LdapConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of LdapConfigPart from a JSON string
ldap_config_part_instance = LdapConfigPart.from_json(json)
# print the JSON string representation of the object
print(LdapConfigPart.to_json())

# convert the object into a dict
ldap_config_part_dict = ldap_config_part_instance.to_dict()
# create an instance of LdapConfigPart from a dict
ldap_config_part_from_dict = LdapConfigPart.from_dict(ldap_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



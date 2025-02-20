# LdapTargetDetails

LdapTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**implementation_type** | **str** |  | [optional] 
**ldap_audience** | **str** |  | [optional] 
**ldap_bind_dn** | **str** |  | [optional] 
**ldap_bind_password** | **str** |  | [optional] 
**ldap_certificate** | **str** |  | [optional] 
**ldap_token_expiration** | **str** |  | [optional] 
**ldap_url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.ldap_target_details import LdapTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LdapTargetDetails from a JSON string
ldap_target_details_instance = LdapTargetDetails.from_json(json)
# print the JSON string representation of the object
print(LdapTargetDetails.to_json())

# convert the object into a dict
ldap_target_details_dict = ldap_target_details_instance.to_dict()
# create an instance of LdapTargetDetails from a dict
ldap_target_details_from_dict = LdapTargetDetails.from_dict(ldap_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



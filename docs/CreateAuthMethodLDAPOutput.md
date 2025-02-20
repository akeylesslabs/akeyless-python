# CreateAuthMethodLDAPOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**prv_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_auth_method_ldap_output import CreateAuthMethodLDAPOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodLDAPOutput from a JSON string
create_auth_method_ldap_output_instance = CreateAuthMethodLDAPOutput.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodLDAPOutput.to_json())

# convert the object into a dict
create_auth_method_ldap_output_dict = create_auth_method_ldap_output_instance.to_dict()
# create an instance of CreateAuthMethodLDAPOutput from a dict
create_auth_method_ldap_output_from_dict = CreateAuthMethodLDAPOutput.from_dict(create_auth_method_ldap_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



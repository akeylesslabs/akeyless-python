# CreateLdapTargetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int** |  | [optional] 

## Example

```python
from akeyless.models.create_ldap_target_output import CreateLdapTargetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLdapTargetOutput from a JSON string
create_ldap_target_output_instance = CreateLdapTargetOutput.from_json(json)
# print the JSON string representation of the object
print(CreateLdapTargetOutput.to_json())

# convert the object into a dict
create_ldap_target_output_dict = create_ldap_target_output_instance.to_dict()
# create an instance of CreateLdapTargetOutput from a dict
create_ldap_target_output_from_dict = CreateLdapTargetOutput.from_dict(create_ldap_target_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



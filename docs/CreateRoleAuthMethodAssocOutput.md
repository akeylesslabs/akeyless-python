# CreateRoleAuthMethodAssocOutput

CreateRoleAuthMethodAssocOutput defines output of CreateRoleAuthMethodAssoc operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_role_auth_method_assoc_output import CreateRoleAuthMethodAssocOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleAuthMethodAssocOutput from a JSON string
create_role_auth_method_assoc_output_instance = CreateRoleAuthMethodAssocOutput.from_json(json)
# print the JSON string representation of the object
print(CreateRoleAuthMethodAssocOutput.to_json())

# convert the object into a dict
create_role_auth_method_assoc_output_dict = create_role_auth_method_assoc_output_instance.to_dict()
# create an instance of CreateRoleAuthMethodAssocOutput from a dict
create_role_auth_method_assoc_output_from_dict = CreateRoleAuthMethodAssocOutput.from_dict(create_role_auth_method_assoc_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



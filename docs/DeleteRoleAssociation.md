# DeleteRoleAssociation

deleteRoleAssociation is a command that deletes an association between role and auth method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** | The association id to be deleted | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_role_association import DeleteRoleAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoleAssociation from a JSON string
delete_role_association_instance = DeleteRoleAssociation.from_json(json)
# print the JSON string representation of the object
print(DeleteRoleAssociation.to_json())

# convert the object into a dict
delete_role_association_dict = delete_role_association_instance.to_dict()
# create an instance of DeleteRoleAssociation from a dict
delete_role_association_from_dict = DeleteRoleAssociation.from_dict(delete_role_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



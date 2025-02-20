# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_date** | **datetime** |  | [optional] 
**access_date_display** | **str** |  | [optional] 
**client_permissions** | **List[str]** |  | [optional] 
**comment** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**delete_protection** | **bool** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**role_auth_methods_assoc** | [**List[RoleAuthMethodAssociation]**](RoleAuthMethodAssociation.md) |  | [optional] 
**role_name** | **str** |  | [optional] 
**rules** | [**Rules**](Rules.md) |  | [optional] 

## Example

```python
from akeyless.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



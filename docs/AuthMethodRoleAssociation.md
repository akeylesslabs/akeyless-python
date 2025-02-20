# AuthMethodRoleAssociation

AuthMethodRoleAssociation includes details of an association between an auth method and a role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_ops** | **List[str]** |  | [optional] 
**assoc_id** | **str** |  | [optional] 
**auth_method_sub_claims** | **Dict[str, List[str]]** |  | [optional] 
**is_sub_claims_case_sensitive** | **bool** |  | [optional] 
**is_subclaims_with_operator** | **bool** |  | [optional] 
**role_id** | **int** |  | [optional] 
**role_name** | **str** |  | [optional] 
**rules** | [**Rules**](Rules.md) |  | [optional] 

## Example

```python
from akeyless.models.auth_method_role_association import AuthMethodRoleAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodRoleAssociation from a JSON string
auth_method_role_association_instance = AuthMethodRoleAssociation.from_json(json)
# print the JSON string representation of the object
print(AuthMethodRoleAssociation.to_json())

# convert the object into a dict
auth_method_role_association_dict = auth_method_role_association_instance.to_dict()
# create an instance of AuthMethodRoleAssociation from a dict
auth_method_role_association_from_dict = AuthMethodRoleAssociation.from_dict(auth_method_role_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



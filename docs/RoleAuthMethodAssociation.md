# RoleAuthMethodAssociation

RoleAuthMethodAssociation includes details of an association between a role and an auth method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** |  | [optional] 
**auth_method_access_id** | **str** |  | [optional] 
**auth_method_name** | **str** |  | [optional] 
**auth_method_sub_claims** | **Dict[str, List[str]]** |  | [optional] 
**is_subclaims_with_operator** | **bool** |  | [optional] 
**sub_claims_case_sensitive** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.role_auth_method_association import RoleAuthMethodAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAuthMethodAssociation from a JSON string
role_auth_method_association_instance = RoleAuthMethodAssociation.from_json(json)
# print the JSON string representation of the object
print(RoleAuthMethodAssociation.to_json())

# convert the object into a dict
role_auth_method_association_dict = role_auth_method_association_instance.to_dict()
# create an instance of RoleAuthMethodAssociation from a dict
role_auth_method_association_from_dict = RoleAuthMethodAssociation.from_dict(role_auth_method_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



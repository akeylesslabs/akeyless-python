# RoleAssociationDetails

RoleAssociationDetails includes details of an association between a role and an auth method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** |  | [optional] 
**auth_method_name** | **str** |  | [optional] 
**auth_method_sub_claims** | **Dict[str, List[str]]** |  | [optional] 
**is_subclaims_with_operator** | **bool** |  | [optional] 
**role_name** | **str** |  | [optional] 
**sub_claims_case_sensitive** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.role_association_details import RoleAssociationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssociationDetails from a JSON string
role_association_details_instance = RoleAssociationDetails.from_json(json)
# print the JSON string representation of the object
print(RoleAssociationDetails.to_json())

# convert the object into a dict
role_association_details_dict = role_association_details_instance.to_dict()
# create an instance of RoleAssociationDetails from a dict
role_association_details_from_dict = RoleAssociationDetails.from_dict(role_association_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



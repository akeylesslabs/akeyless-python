# AuthMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_date** | **datetime** |  | [optional] 
**access_date_display** | **str** |  | [optional] 
**access_info** | [**AuthMethodAccessInfo**](AuthMethodAccessInfo.md) |  | [optional] 
**account_id** | **str** |  | [optional] 
**associated_gw_ids** | **List[int]** |  | [optional] 
**auth_method_access_id** | **str** |  | [optional] 
**auth_method_additional_data** | [**AuthMethodAdditionalData**](AuthMethodAdditionalData.md) |  | [optional] 
**auth_method_name** | **str** |  | [optional] 
**auth_method_roles_assoc** | [**List[AuthMethodRoleAssociation]**](AuthMethodRoleAssociation.md) |  | [optional] 
**client_permissions** | **List[str]** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**delete_protection** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**expiration_events** | [**List[AuthExpirationEvent]**](AuthExpirationEvent.md) |  | [optional] 
**is_approved** | **bool** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 

## Example

```python
from akeyless.models.auth_method import AuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethod from a JSON string
auth_method_instance = AuthMethod.from_json(json)
# print the JSON string representation of the object
print(AuthMethod.to_json())

# convert the object into a dict
auth_method_dict = auth_method_instance.to_dict()
# create an instance of AuthMethod from a dict
auth_method_from_dict = AuthMethod.from_dict(auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



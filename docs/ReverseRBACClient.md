# ReverseRBACClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assocs** | [**List[AuthMethodRoleAssociation]**](AuthMethodRoleAssociation.md) |  | [optional] 
**auth_method_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.reverse_rbac_client import ReverseRBACClient

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseRBACClient from a JSON string
reverse_rbac_client_instance = ReverseRBACClient.from_json(json)
# print the JSON string representation of the object
print(ReverseRBACClient.to_json())

# convert the object into a dict
reverse_rbac_client_dict = reverse_rbac_client_instance.to_dict()
# create an instance of ReverseRBACClient from a dict
reverse_rbac_client_from_dict = ReverseRBACClient.from_dict(reverse_rbac_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



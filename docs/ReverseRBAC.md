# ReverseRBAC

reverseRBAC is a command that shows which auth methods have access to a particular object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | Path to an object | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Type of object (item, am, role) | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.reverse_rbac import ReverseRBAC

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseRBAC from a JSON string
reverse_rbac_instance = ReverseRBAC.from_json(json)
# print the JSON string representation of the object
print(ReverseRBAC.to_json())

# convert the object into a dict
reverse_rbac_dict = reverse_rbac_instance.to_dict()
# create an instance of ReverseRBAC from a dict
reverse_rbac_from_dict = ReverseRBAC.from_dict(reverse_rbac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



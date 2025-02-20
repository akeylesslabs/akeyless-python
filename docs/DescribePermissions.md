# DescribePermissions

describePermissions is a command that shows which permissions your have to a particular path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | Path to an object | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Type of object (item, am, role, target) | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.describe_permissions import DescribePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of DescribePermissions from a JSON string
describe_permissions_instance = DescribePermissions.from_json(json)
# print the JSON string representation of the object
print(DescribePermissions.to_json())

# convert the object into a dict
describe_permissions_dict = describe_permissions_instance.to_dict()
# create an instance of DescribePermissions from a dict
describe_permissions_from_dict = DescribePermissions.from_dict(describe_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



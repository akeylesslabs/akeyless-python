# DescribePermissionsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_permissions** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.describe_permissions_output import DescribePermissionsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DescribePermissionsOutput from a JSON string
describe_permissions_output_instance = DescribePermissionsOutput.from_json(json)
# print the JSON string representation of the object
print(DescribePermissionsOutput.to_json())

# convert the object into a dict
describe_permissions_output_dict = describe_permissions_output_instance.to_dict()
# create an instance of DescribePermissionsOutput from a dict
describe_permissions_output_from_dict = DescribePermissionsOutput.from_dict(describe_permissions_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReverseRBACOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**Dict[str, ReverseRBACClient]**](ReverseRBACClient.md) |  | [optional] 

## Example

```python
from akeyless.models.reverse_rbac_output import ReverseRBACOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseRBACOutput from a JSON string
reverse_rbac_output_instance = ReverseRBACOutput.from_json(json)
# print the JSON string representation of the object
print(ReverseRBACOutput.to_json())

# convert the object into a dict
reverse_rbac_output_dict = reverse_rbac_output_instance.to_dict()
# create an instance of ReverseRBACOutput from a dict
reverse_rbac_output_from_dict = ReverseRBACOutput.from_dict(reverse_rbac_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



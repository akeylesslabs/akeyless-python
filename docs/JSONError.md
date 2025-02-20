# JSONError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 

## Example

```python
from akeyless.models.json_error import JSONError

# TODO update the JSON string below
json = "{}"
# create an instance of JSONError from a JSON string
json_error_instance = JSONError.from_json(json)
# print the JSON string representation of the object
print(JSONError.to_json())

# convert the object into a dict
json_error_dict = json_error_instance.to_dict()
# create an instance of JSONError from a dict
json_error_from_dict = JSONError.from_dict(json_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



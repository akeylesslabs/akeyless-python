# Unconfigure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**profile** | **str** | The profile name to be removed | [optional] [default to 'default']

## Example

```python
from akeyless.models.unconfigure import Unconfigure

# TODO update the JSON string below
json = "{}"
# create an instance of Unconfigure from a JSON string
unconfigure_instance = Unconfigure.from_json(json)
# print the JSON string representation of the object
print(Unconfigure.to_json())

# convert the object into a dict
unconfigure_dict = unconfigure_instance.to_dict()
# create an instance of Unconfigure from a dict
unconfigure_from_dict = Unconfigure.from_dict(unconfigure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



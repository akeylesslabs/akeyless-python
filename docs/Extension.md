# Extension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from akeyless.models.extension import Extension

# TODO update the JSON string below
json = "{}"
# create an instance of Extension from a JSON string
extension_instance = Extension.from_json(json)
# print the JSON string representation of the object
print(Extension.to_json())

# convert the object into a dict
extension_dict = extension_instance.to_dict()
# create an instance of Extension from a dict
extension_from_dict = Extension.from_dict(extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



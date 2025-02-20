# WindowsServiceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.windows_service_attributes import WindowsServiceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WindowsServiceAttributes from a JSON string
windows_service_attributes_instance = WindowsServiceAttributes.from_json(json)
# print the JSON string representation of the object
print(WindowsServiceAttributes.to_json())

# convert the object into a dict
windows_service_attributes_dict = windows_service_attributes_instance.to_dict()
# create an instance of WindowsServiceAttributes from a dict
windows_service_attributes_from_dict = WindowsServiceAttributes.from_dict(windows_service_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



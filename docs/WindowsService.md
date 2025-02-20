# WindowsService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**WindowsServiceAttributes**](WindowsServiceAttributes.md) |  | [optional] 
**host** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.windows_service import WindowsService

# TODO update the JSON string below
json = "{}"
# create an instance of WindowsService from a JSON string
windows_service_instance = WindowsService.from_json(json)
# print the JSON string representation of the object
print(WindowsService.to_json())

# convert the object into a dict
windows_service_dict = windows_service_instance.to_dict()
# create an instance of WindowsService from a dict
windows_service_from_dict = WindowsService.from_dict(windows_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



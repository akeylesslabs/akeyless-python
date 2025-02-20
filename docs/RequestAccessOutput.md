# RequestAccessOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** |  | [optional] 

## Example

```python
from akeyless.models.request_access_output import RequestAccessOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAccessOutput from a JSON string
request_access_output_instance = RequestAccessOutput.from_json(json)
# print the JSON string representation of the object
print(RequestAccessOutput.to_json())

# convert the object into a dict
request_access_output_dict = request_access_output_instance.to_dict()
# create an instance of RequestAccessOutput from a dict
request_access_output_from_dict = RequestAccessOutput.from_dict(request_access_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



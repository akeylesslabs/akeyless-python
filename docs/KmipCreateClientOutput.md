# KmipCreateClientOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kmip_create_client_output import KmipCreateClientOutput

# TODO update the JSON string below
json = "{}"
# create an instance of KmipCreateClientOutput from a JSON string
kmip_create_client_output_instance = KmipCreateClientOutput.from_json(json)
# print the JSON string representation of the object
print(KmipCreateClientOutput.to_json())

# convert the object into a dict
kmip_create_client_output_dict = kmip_create_client_output_instance.to_dict()
# create an instance of KmipCreateClientOutput from a dict
kmip_create_client_output_from_dict = KmipCreateClientOutput.from_dict(kmip_create_client_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



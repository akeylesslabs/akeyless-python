# KmipSetServerStateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.kmip_set_server_state_output import KmipSetServerStateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of KmipSetServerStateOutput from a JSON string
kmip_set_server_state_output_instance = KmipSetServerStateOutput.from_json(json)
# print the JSON string representation of the object
print(KmipSetServerStateOutput.to_json())

# convert the object into a dict
kmip_set_server_state_output_dict = kmip_set_server_state_output_instance.to_dict()
# create an instance of KmipSetServerStateOutput from a dict
kmip_set_server_state_output_from_dict = KmipSetServerStateOutput.from_dict(kmip_set_server_state_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KmipMoveServerOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_root** | **str** |  | [optional] 
**old_root** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kmip_move_server_output import KmipMoveServerOutput

# TODO update the JSON string below
json = "{}"
# create an instance of KmipMoveServerOutput from a JSON string
kmip_move_server_output_instance = KmipMoveServerOutput.from_json(json)
# print the JSON string representation of the object
print(KmipMoveServerOutput.to_json())

# convert the object into a dict
kmip_move_server_output_dict = kmip_move_server_output_instance.to_dict()
# create an instance of KmipMoveServerOutput from a dict
kmip_move_server_output_from_dict = KmipMoveServerOutput.from_dict(kmip_move_server_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



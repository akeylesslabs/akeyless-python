# CreatePasskeyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classic_key_id** | **str** |  | [optional] 
**classic_key_name** | **str** |  | [optional] 
**classic_key_type** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_passkey_output import CreatePasskeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasskeyOutput from a JSON string
create_passkey_output_instance = CreatePasskeyOutput.from_json(json)
# print the JSON string representation of the object
print(CreatePasskeyOutput.to_json())

# convert the object into a dict
create_passkey_output_dict = create_passkey_output_instance.to_dict()
# create an instance of CreatePasskeyOutput from a dict
create_passkey_output_from_dict = CreatePasskeyOutput.from_dict(create_passkey_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateClassicKeyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classic_key_id** | **str** |  | [optional] 
**classic_key_name** | **str** |  | [optional] 
**classic_key_type** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_classic_key_output import CreateClassicKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClassicKeyOutput from a JSON string
create_classic_key_output_instance = CreateClassicKeyOutput.from_json(json)
# print the JSON string representation of the object
print(CreateClassicKeyOutput.to_json())

# convert the object into a dict
create_classic_key_output_dict = create_classic_key_output_instance.to_dict()
# create an instance of CreateClassicKeyOutput from a dict
create_classic_key_output_from_dict = CreateClassicKeyOutput.from_dict(create_classic_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



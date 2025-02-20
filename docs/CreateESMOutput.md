# CreateESMOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_secret_manager_id** | **int** |  | [optional] 
**external_secret_manager_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_esm_output import CreateESMOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateESMOutput from a JSON string
create_esm_output_instance = CreateESMOutput.from_json(json)
# print the JSON string representation of the object
print(CreateESMOutput.to_json())

# convert the object into a dict
create_esm_output_dict = create_esm_output_instance.to_dict()
# create an instance of CreateESMOutput from a dict
create_esm_output_from_dict = CreateESMOutput.from_dict(create_esm_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



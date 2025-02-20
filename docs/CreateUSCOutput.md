# CreateUSCOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**universal_secrets_connector_id** | **int** |  | [optional] 
**universal_secrets_connector_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_usc_output import CreateUSCOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUSCOutput from a JSON string
create_usc_output_instance = CreateUSCOutput.from_json(json)
# print the JSON string representation of the object
print(CreateUSCOutput.to_json())

# convert the object into a dict
create_usc_output_dict = create_usc_output_instance.to_dict()
# create an instance of CreateUSCOutput from a dict
create_usc_output_from_dict = CreateUSCOutput.from_dict(create_usc_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



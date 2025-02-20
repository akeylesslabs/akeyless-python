# ProducersConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producers** | [**List[Producer]**](Producer.md) |  | [optional] 

## Example

```python
from akeyless.models.producers_config_part import ProducersConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of ProducersConfigPart from a JSON string
producers_config_part_instance = ProducersConfigPart.from_json(json)
# print the JSON string representation of the object
print(ProducersConfigPart.to_json())

# convert the object into a dict
producers_config_part_dict = producers_config_part_instance.to_dict()
# create an instance of ProducersConfigPart from a dict
producers_config_part_from_dict = ProducersConfigPart.from_dict(producers_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



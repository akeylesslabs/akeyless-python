# SumologicLogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sumo_logic_endpoint** | **str** |  | [optional] 
**sumo_logic_host** | **str** |  | [optional] 
**sumo_logic_tags** | **str** |  | [optional] 

## Example

```python
from akeyless.models.sumologic_log_forwarding_config import SumologicLogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SumologicLogForwardingConfig from a JSON string
sumologic_log_forwarding_config_instance = SumologicLogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(SumologicLogForwardingConfig.to_json())

# convert the object into a dict
sumologic_log_forwarding_config_dict = sumologic_log_forwarding_config_instance.to_dict()
# create an instance of SumologicLogForwardingConfig from a dict
sumologic_log_forwarding_config_from_dict = SumologicLogForwardingConfig.from_dict(sumologic_log_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



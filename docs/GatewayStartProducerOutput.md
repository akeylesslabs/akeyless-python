# GatewayStartProducerOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_start_producer_output import GatewayStartProducerOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayStartProducerOutput from a JSON string
gateway_start_producer_output_instance = GatewayStartProducerOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayStartProducerOutput.to_json())

# convert the object into a dict
gateway_start_producer_output_dict = gateway_start_producer_output_instance.to_dict()
# create an instance of GatewayStartProducerOutput from a dict
gateway_start_producer_output_from_dict = GatewayStartProducerOutput.from_dict(gateway_start_producer_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



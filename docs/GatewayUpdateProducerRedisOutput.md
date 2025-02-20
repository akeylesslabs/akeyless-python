# GatewayUpdateProducerRedisOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_update_producer_redis_output import GatewayUpdateProducerRedisOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerRedisOutput from a JSON string
gateway_update_producer_redis_output_instance = GatewayUpdateProducerRedisOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerRedisOutput.to_json())

# convert the object into a dict
gateway_update_producer_redis_output_dict = gateway_update_producer_redis_output_instance.to_dict()
# create an instance of GatewayUpdateProducerRedisOutput from a dict
gateway_update_producer_redis_output_from_dict = GatewayUpdateProducerRedisOutput.from_dict(gateway_update_producer_redis_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



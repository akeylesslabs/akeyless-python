# GatewayCreateProducerChefOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_create_producer_chef_output import GatewayCreateProducerChefOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerChefOutput from a JSON string
gateway_create_producer_chef_output_instance = GatewayCreateProducerChefOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerChefOutput.to_json())

# convert the object into a dict
gateway_create_producer_chef_output_dict = gateway_create_producer_chef_output_instance.to_dict()
# create an instance of GatewayCreateProducerChefOutput from a dict
gateway_create_producer_chef_output_from_dict = GatewayCreateProducerChefOutput.from_dict(gateway_create_producer_chef_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



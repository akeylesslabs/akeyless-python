# GatewayCreateProducerGkeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_create_producer_gke_output import GatewayCreateProducerGkeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerGkeOutput from a JSON string
gateway_create_producer_gke_output_instance = GatewayCreateProducerGkeOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerGkeOutput.to_json())

# convert the object into a dict
gateway_create_producer_gke_output_dict = gateway_create_producer_gke_output_instance.to_dict()
# create an instance of GatewayCreateProducerGkeOutput from a dict
gateway_create_producer_gke_output_from_dict = GatewayCreateProducerGkeOutput.from_dict(gateway_create_producer_gke_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



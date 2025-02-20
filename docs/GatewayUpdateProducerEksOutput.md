# GatewayUpdateProducerEksOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_update_producer_eks_output import GatewayUpdateProducerEksOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerEksOutput from a JSON string
gateway_update_producer_eks_output_instance = GatewayUpdateProducerEksOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerEksOutput.to_json())

# convert the object into a dict
gateway_update_producer_eks_output_dict = gateway_update_producer_eks_output_instance.to_dict()
# create an instance of GatewayUpdateProducerEksOutput from a dict
gateway_update_producer_eks_output_from_dict = GatewayUpdateProducerEksOutput.from_dict(gateway_update_producer_eks_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



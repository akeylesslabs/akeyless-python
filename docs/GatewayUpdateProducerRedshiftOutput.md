# GatewayUpdateProducerRedshiftOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_update_producer_redshift_output import GatewayUpdateProducerRedshiftOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerRedshiftOutput from a JSON string
gateway_update_producer_redshift_output_instance = GatewayUpdateProducerRedshiftOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerRedshiftOutput.to_json())

# convert the object into a dict
gateway_update_producer_redshift_output_dict = gateway_update_producer_redshift_output_instance.to_dict()
# create an instance of GatewayUpdateProducerRedshiftOutput from a dict
gateway_update_producer_redshift_output_from_dict = GatewayUpdateProducerRedshiftOutput.from_dict(gateway_update_producer_redshift_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



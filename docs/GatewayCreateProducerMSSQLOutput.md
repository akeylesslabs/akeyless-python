# GatewayCreateProducerMSSQLOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_create_producer_mssql_output import GatewayCreateProducerMSSQLOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerMSSQLOutput from a JSON string
gateway_create_producer_mssql_output_instance = GatewayCreateProducerMSSQLOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerMSSQLOutput.to_json())

# convert the object into a dict
gateway_create_producer_mssql_output_dict = gateway_create_producer_mssql_output_instance.to_dict()
# create an instance of GatewayCreateProducerMSSQLOutput from a dict
gateway_create_producer_mssql_output_from_dict = GatewayCreateProducerMSSQLOutput.from_dict(gateway_create_producer_mssql_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



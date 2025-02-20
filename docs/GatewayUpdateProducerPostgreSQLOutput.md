# GatewayUpdateProducerPostgreSQLOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_update_producer_postgre_sql_output import GatewayUpdateProducerPostgreSQLOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerPostgreSQLOutput from a JSON string
gateway_update_producer_postgre_sql_output_instance = GatewayUpdateProducerPostgreSQLOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerPostgreSQLOutput.to_json())

# convert the object into a dict
gateway_update_producer_postgre_sql_output_dict = gateway_update_producer_postgre_sql_output_instance.to_dict()
# create an instance of GatewayUpdateProducerPostgreSQLOutput from a dict
gateway_update_producer_postgre_sql_output_from_dict = GatewayUpdateProducerPostgreSQLOutput.from_dict(gateway_update_producer_postgre_sql_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



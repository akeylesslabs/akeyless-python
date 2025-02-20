# GatewayMigrationCreateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_migration_create_output import GatewayMigrationCreateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayMigrationCreateOutput from a JSON string
gateway_migration_create_output_instance = GatewayMigrationCreateOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayMigrationCreateOutput.to_json())

# convert the object into a dict
gateway_migration_create_output_dict = gateway_migration_create_output_instance.to_dict()
# create an instance of GatewayMigrationCreateOutput from a dict
gateway_migration_create_output_from_dict = GatewayMigrationCreateOutput.from_dict(gateway_migration_create_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



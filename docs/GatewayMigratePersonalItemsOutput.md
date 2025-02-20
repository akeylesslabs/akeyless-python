# GatewayMigratePersonalItemsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_items** | [**MigrationItems**](MigrationItems.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_migrate_personal_items_output import GatewayMigratePersonalItemsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayMigratePersonalItemsOutput from a JSON string
gateway_migrate_personal_items_output_instance = GatewayMigratePersonalItemsOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayMigratePersonalItemsOutput.to_json())

# convert the object into a dict
gateway_migrate_personal_items_output_dict = gateway_migrate_personal_items_output_instance.to_dict()
# create an instance of GatewayMigratePersonalItemsOutput from a dict
gateway_migrate_personal_items_output_from_dict = GatewayMigratePersonalItemsOutput.from_dict(gateway_migrate_personal_items_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



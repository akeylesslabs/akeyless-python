# GatewaySyncMigration

gatewaySyncMigration is a command that sync migration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Migration name | 
**start_sync** | **bool** | true, for starting synchronization, false for stopping | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_sync_migration import GatewaySyncMigration

# TODO update the JSON string below
json = "{}"
# create an instance of GatewaySyncMigration from a JSON string
gateway_sync_migration_instance = GatewaySyncMigration.from_json(json)
# print the JSON string representation of the object
print(GatewaySyncMigration.to_json())

# convert the object into a dict
gateway_sync_migration_dict = gateway_sync_migration_instance.to_dict()
# create an instance of GatewaySyncMigration from a dict
gateway_sync_migration_from_dict = GatewaySyncMigration.from_dict(gateway_sync_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



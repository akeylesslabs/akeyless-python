# GatewayStatusMigration

gatewayStatusMigration is a command that get migration status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Migration ID | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Migration name to display | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_status_migration import GatewayStatusMigration

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayStatusMigration from a JSON string
gateway_status_migration_instance = GatewayStatusMigration.from_json(json)
# print the JSON string representation of the object
print(GatewayStatusMigration.to_json())

# convert the object into a dict
gateway_status_migration_dict = gateway_status_migration_instance.to_dict()
# create an instance of GatewayStatusMigration from a dict
gateway_status_migration_from_dict = GatewayStatusMigration.from_dict(gateway_status_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GatewayListMigration

gatewayListMigration is a command that list migration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_list_migration import GatewayListMigration

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayListMigration from a JSON string
gateway_list_migration_instance = GatewayListMigration.from_json(json)
# print the JSON string representation of the object
print(GatewayListMigration.to_json())

# convert the object into a dict
gateway_list_migration_dict = gateway_list_migration_instance.to_dict()
# create an instance of GatewayListMigration from a dict
gateway_list_migration_from_dict = GatewayListMigration.from_dict(gateway_list_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



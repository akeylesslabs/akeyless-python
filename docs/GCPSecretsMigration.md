# GCPSecretsMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**GCPPayload**](GCPPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.gcp_secrets_migration import GCPSecretsMigration

# TODO update the JSON string below
json = "{}"
# create an instance of GCPSecretsMigration from a JSON string
gcp_secrets_migration_instance = GCPSecretsMigration.from_json(json)
# print the JSON string representation of the object
print(GCPSecretsMigration.to_json())

# convert the object into a dict
gcp_secrets_migration_dict = gcp_secrets_migration_instance.to_dict()
# create an instance of GCPSecretsMigration from a dict
gcp_secrets_migration_from_dict = GCPSecretsMigration.from_dict(gcp_secrets_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



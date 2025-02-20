# AWSSecretsMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**AWSPayload**](AWSPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.aws_secrets_migration import AWSSecretsMigration

# TODO update the JSON string below
json = "{}"
# create an instance of AWSSecretsMigration from a JSON string
aws_secrets_migration_instance = AWSSecretsMigration.from_json(json)
# print the JSON string representation of the object
print(AWSSecretsMigration.to_json())

# convert the object into a dict
aws_secrets_migration_dict = aws_secrets_migration_instance.to_dict()
# create an instance of AWSSecretsMigration from a dict
aws_secrets_migration_from_dict = AWSSecretsMigration.from_dict(aws_secrets_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



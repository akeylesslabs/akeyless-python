# K8SMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**K8SPayload**](K8SPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.k8_s_migration import K8SMigration

# TODO update the JSON string below
json = "{}"
# create an instance of K8SMigration from a JSON string
k8_s_migration_instance = K8SMigration.from_json(json)
# print the JSON string representation of the object
print(K8SMigration.to_json())

# convert the object into a dict
k8_s_migration_dict = k8_s_migration_instance.to_dict()
# create an instance of K8SMigration from a dict
k8_s_migration_from_dict = K8SMigration.from_dict(k8_s_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



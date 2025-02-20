# AdminsConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admins_migration_status** | **int** |  | [optional] 
**allowed_access** | [**Dict[str, AllowedAccessOld]**](AllowedAccessOld.md) |  | [optional] 

## Example

```python
from akeyless.models.admins_config_part import AdminsConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of AdminsConfigPart from a JSON string
admins_config_part_instance = AdminsConfigPart.from_json(json)
# print the JSON string representation of the object
print(AdminsConfigPart.to_json())

# convert the object into a dict
admins_config_part_dict = admins_config_part_instance.to_dict()
# create an instance of AdminsConfigPart from a dict
admins_config_part_from_dict = AdminsConfigPart.from_dict(admins_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



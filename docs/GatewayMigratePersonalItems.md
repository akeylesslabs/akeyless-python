# GatewayMigratePersonalItems

gatewayMigratePersonalItems is a command that migrate personal items from external vault

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1password_email** | **str** | 1Password user email to connect to the API | [optional] 
**var_1password_password** | **str** | 1Password user password to connect to the API | [optional] 
**var_1password_secret_key** | **str** | 1Password user secret key to connect to the API | [optional] 
**var_1password_url** | **str** | 1Password api container url | [optional] 
**var_1password_vaults** | **List[str]** | 1Password list of vault to get the items from | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**protection_key** | **str** | The name of a key that used to encrypt the secret value | [optional] 
**target_location** | **str** | Target location in your Akeyless personal folder for migrated secrets | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Migration type for now only 1password. | [optional] [default to '1password']
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_migrate_personal_items import GatewayMigratePersonalItems

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayMigratePersonalItems from a JSON string
gateway_migrate_personal_items_instance = GatewayMigratePersonalItems.from_json(json)
# print the JSON string representation of the object
print(GatewayMigratePersonalItems.to_json())

# convert the object into a dict
gateway_migrate_personal_items_dict = gateway_migrate_personal_items_instance.to_dict()
# create an instance of GatewayMigratePersonalItems from a dict
gateway_migrate_personal_items_from_dict = GatewayMigratePersonalItems.from_dict(gateway_migrate_personal_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



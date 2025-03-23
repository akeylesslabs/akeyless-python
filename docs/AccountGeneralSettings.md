# AccountGeneralSettings

AccountGeneralSettings describes general settings for an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_default_key_item_id** | **int** | AccountDefaultKeyItemID is the item ID of the DFC key item configured as the default protection key | [optional] 
**account_default_key_name** | **str** | AccountDefaultKeyName is the name of the DFC key item configured as the default key This is here simply for the response to include the item name in addition to the display ID so the client can properly show this to the user. It will not be saved to the DB, only the AccountDefaultKeyItemID will. | [optional] 
**allowed_clients_ips** | [**AllowedIpSettings**](AllowedIpSettings.md) |  | [optional] 
**allowed_gateways_ips** | [**AllowedIpSettings**](AllowedIpSettings.md) |  | [optional] 
**auth_usage_event** | [**UsageEventSetting**](UsageEventSetting.md) |  | [optional] 
**data_protection_section** | [**DataProtectionSection**](DataProtectionSection.md) |  | [optional] 
**default_home_page** | [**DefaultHomePage**](DefaultHomePage.md) |  | [optional] 
**dynamic_secret_max_ttl** | [**DynamicSecretMaxTtl**](DynamicSecretMaxTtl.md) |  | [optional] 
**enable_request_for_access** | **bool** |  | [optional] 
**invalid_characters** | **str** | InvalidCharacters is the invalid characters for items/targets/roles/auths/notifier_forwarder naming convention | [optional] 
**item_usage_event** | [**UsageEventSetting**](UsageEventSetting.md) |  | [optional] 
**lock_default_key** | **bool** | LockDefaultKey determines whether the configured default key can be updated by end-users on a per-request basis true - all requests use the configured default key false - every request can determine its protection key (default) nil - change nothing (every request can determine its protection key (default)) This parameter is only relevant if AccountDefaultKeyItemID is not empty | [optional] 
**password_expiration_info** | [**PasswordExpirationInfo**](PasswordExpirationInfo.md) |  | [optional] 
**password_policy** | [**PasswordPolicyInfo**](PasswordPolicyInfo.md) |  | [optional] 
**password_score** | [**PasswordScoreSetting**](PasswordScoreSetting.md) |  | [optional] 
**protect_items_by_default** | **bool** |  | [optional] 
**rotation_secret_max_interval** | [**RotationSecretMaxInterval**](RotationSecretMaxInterval.md) |  | [optional] 
**sharing_policy** | [**SharingPolicyInfo**](SharingPolicyInfo.md) |  | [optional] 

## Example

```python
from akeyless.models.account_general_settings import AccountGeneralSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGeneralSettings from a JSON string
account_general_settings_instance = AccountGeneralSettings.from_json(json)
# print the JSON string representation of the object
print(AccountGeneralSettings.to_json())

# convert the object into a dict
account_general_settings_dict = account_general_settings_instance.to_dict()
# create an instance of AccountGeneralSettings from a dict
account_general_settings_from_dict = AccountGeneralSettings.from_dict(account_general_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



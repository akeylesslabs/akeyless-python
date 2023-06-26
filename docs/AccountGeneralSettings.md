# AccountGeneralSettings

AccountGeneralSettings describes general settings for an account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_default_key_item_id** | **int** | AccountDefaultKeyItemID is the item ID of the DFC key item configured as the default protection key | [optional] 
**account_default_key_name** | **str** | AccountDefaultKeyName is the name of the DFC key item configured as the default key This is here simply for the response to include the item name in addition to the display ID so the client can properly show this to the user. It will not be saved to the DB, only the AccountDefaultKeyItemID will. | [optional] 
**data_protection_section** | [**DataProtectionSection**](DataProtectionSection.md) |  | [optional] 
**enable_request_for_access** | **bool** |  | [optional] 
**password_policy** | [**PasswordPolicyInfo**](PasswordPolicyInfo.md) |  | [optional] 
**protect_items_by_default** | **bool** |  | [optional] 
**sharing_policy** | [**SharingPolicyInfo**](SharingPolicyInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



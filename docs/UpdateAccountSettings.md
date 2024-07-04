# UpdateAccountSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address | [optional] 
**bound_ips** | **list[str]** | A default list of comma-separated CIDR block that are allowed to authenticate. | [optional] 
**city** | **str** | City | [optional] 
**company_name** | **str** | Company name | [optional] 
**country** | **str** | Country | [optional] 
**default_key_name** | **str** | Set the account default key based on the DFC key name. Use \&quot;set-original-akeyless-default-key\&quot; to revert to using the original default key of the account. | [optional] 
**default_share_link_ttl_minutes** | **str** | Set the default ttl in minutes for sharing item number between 60 and 43200 | [optional] 
**default_versioning** | **str** | If set to true, new versions is enabled by default | [optional] 
**dp_enable_classic_key_protection** | **str** | Set to update protection with classic keys state [true/false] | [optional] 
**dynamic_secret_max_ttl** | **int** | Set the maximum ttl for dynamic secrets | [optional] 
**dynamic_secret_max_ttl_enable** | **str** | Set a maximum ttl for dynamic secrets [true/false] | [optional] 
**enable_item_sharing** | **str** | Enable sharing items [true/false] | [optional] 
**force_new_versions** | **str** | If set to true, new version will be created on update | [optional] 
**gw_bound_ips** | **list[str]** | A default list of comma-separated CIDR block that acts as a trusted Gateway entity. | [optional] 
**invalid_characters** | **str** | Characters that cannot be used for items/targets/roles/auths/event_forwarder names. Empty string will enforce nothing. | [optional] [default to 'notReceivedInvalidCharacter']
**item_type** | **str** | VersionSettingsObjectType defines object types for account version settings | [optional] 
**items_deletion_protection** | **str** | Set or unset the default behaviour of items deletion protection [true/false] | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl_default** | **int** | Default ttl | [optional] 
**jwt_ttl_max** | **int** | Maximum ttl | [optional] 
**jwt_ttl_min** | **int** | Minimum ttl | [optional] 
**lock_bound_ips** | **str** | Lock bound-ips setting globally in the account. | [optional] 
**lock_default_key** | **str** | Lock the account&#39;s default protection key, if set - users will not be able to use a different protection key, relevant only if default-key-name is configured [true/false] | [optional] 
**lock_gw_bound_ips** | **str** | Lock gw-bound-ips setting in the account. | [optional] 
**max_rotation_interval** | **int** | Set the maximum rotation interval for rotated secrets auto rotation settings | [optional] 
**max_rotation_interval_enable** | **str** | Set a maximum rotation interval for rotated secrets auto rotation settings [true/false] | [optional] 
**max_versions** | **str** | Max versions | [optional] 
**password_length** | **int** | Password length between 5 - to 50 characters | [optional] 
**phone** | **str** | Phone number | [optional] 
**postal_code** | **str** | Postal code | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usage_event_enable** | **str** | Enable event for objects that have not been used or changed [true/false] | [optional] 
**usage_event_interval** | **int** | Interval by days for unused objects. Default and minimum interval is 90 days | [optional] 
**usage_event_object_type** | **str** | Usage event is supported for auth method or secrets-and-keys [auth/item] | [optional] 
**use_lower_letters** | **str** | Password must contain lower case letters [true/false] | [optional] 
**use_numbers** | **str** | Password must contain numbers [true/false] | [optional] 
**use_special_characters** | **str** | Password must contain special characters [true/false] | [optional] 
**use_capital_letters** | **str** | Password must contain capital letters [true/false] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



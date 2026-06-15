# RotatedSecretUpdateGcp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**authentication_credentials** | **str** | The credentials to connect with use-user-creds/use-target-creds | [optional] [default to 'use-user-creds']
**auto_rotate** | **str** |  | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_metadata']
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**gcp_service_account_email** | **str** | The email of the gcp service account to rotate | [optional] 
**gcp_service_account_key_id** | **str** | The key id of the gcp service account to rotate | [optional] 
**grace_rotation** | **str** | Enable graceful rotation (keep both versions temporarily). When enabled, a new secret version is created while the previous version is kept for the grace period, so both versions exist for a limited time. [true/false] | [optional] 
**grace_rotation_hour** | **int** | The Hour of the grace rotation in UTC | [optional] 
**grace_rotation_interval** | **str** | The number of days to wait before deleting the old key (must be bigger than rotation-interval) | [optional] 
**grace_rotation_timing** | **str** | When to create the new version relative to the rotation date [after/before] | [optional] 
**input_rule** | **list[str]** | Agentic input rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Sanitize input) | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** |  | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Rotated secret name | 
**new_name** | **str** | New item name | [optional] 
**output_rule** | **list[str]** | Agentic output rule in name&#x3D;...,rule&#x3D;... format (e.g. name&#x3D;rule1,rule&#x3D;Mask secrets) | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotation_event_in** | **list[str]** | How many days before the rotation of the item would you like to be notified | [optional] 
**rotation_hour** | **int** |  | [optional] 
**rotation_interval** | **str** |  | [optional] 
**rotator_type** | **str** | The rotator type. options: [target/service-account-rotator] | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_capital_letters** | **str** | Specifies whether the generated temporary password must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z). [true/false] | [optional] 
**use_lower_letters** | **str** | Specifies whether the generated temporary password must contain at least one lowercase character from the ISO basic Latin alphabet (a to z). [true/false] | [optional] 
**use_numbers** | **str** | Specifies whether the generated temporary password must contain at least one numeric character (0 to 9). [true/false] | [optional] 
**use_special_characters** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



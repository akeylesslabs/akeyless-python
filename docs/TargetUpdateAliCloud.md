# TargetUpdateAliCloud

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | AliCloud RAM access key secret | [optional] 
**access_key_id** | **str** | AliCloud RAM access key ID | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**generate_external_id** | **bool** | A unique auto-generated value used in your AliCloud account when configuring the RAM role trust policy to securely delegate access to Akeyless. Relevant only when using GW cloud ID | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**lock_on_read** | **str** | Lock this secret after each successful value read | [optional] 
**lock_ttl** | **str** | Lock TTL in minutes | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**region** | **str** | AliCloud region. Selects the regional STS endpoint. If empty, the global STS endpoint is used | [optional] 
**role_arn** | **str** | AliCloud RAM role ARN that the Gateway will assume in your AliCloud account (acs:ram::&lt;account-id&gt;:role/&lt;role-name&gt;), relevant only when using external ID | [optional] 
**rotate_on_unlock** | **str** | Rotate this secret after it is unlocked | [optional] 
**session_token** | **str** | Required only for temporary security credentials retrieved using STS | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_cloud_identity** | **bool** | Use the Gateway cloud identity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



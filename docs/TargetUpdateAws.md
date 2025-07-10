# TargetUpdateAws

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | AWS secret access key | 
**access_key_id** | **str** | AWS access key ID | 
**description** | **str** | Description of the object | [optional] 
**generate_external_id** | **bool** | A unique auto-generated value used in your AWS account when configuring your AWS IAM role to securely delegate access to Akeyless. Relevant only when using GW cloud ID | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**region** | **str** | AWS region | [optional] [default to 'us-east-2']
**role_arn** | **str** | AWS IAM role identifier that Gateway will assume in your AWS account, relevant only when using external ID | [optional] 
**session_token** | **str** | Required only for temporary security credentials retrieved using STS | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_cloud_identity** | **bool** | Use the GW&#39;s Cloud IAM | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GatewayCreateProducerAws

gatewayCreateProducerAws is a command that creates aws producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Access Key ID | 
**access_mode** | **str** |  | [optional] 
**access_secret_key** | **str** | Secret Access Key | 
**admin_rotation_interval_days** | **int** | Admin credentials rotation interval (days) | [optional] [default to 0]
**aws_role_arns** | **str** | AWS Role ARNs to be used in the Assume Role operation (relevant only for assume_role mode) | [optional] 
**aws_user_console_access** | **bool** | AWS User console access | [optional] [default to False]
**aws_user_groups** | **str** | AWS User groups | [optional] 
**aws_user_policies** | **str** | AWS User policies | [optional] 
**aws_user_programmatic_access** | **bool** | AWS User programmatic access | [optional] [default to True]
**enable_admin_rotation** | **bool** | Automatic admin credentials rotation | [optional] [default to False]
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**region** | **str** | Region | [optional] [default to 'us-east-2']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



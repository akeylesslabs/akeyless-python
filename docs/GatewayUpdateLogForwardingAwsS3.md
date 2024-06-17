# GatewayUpdateLogForwardingAwsS3

gatewayUpdateLogForwardingAwsS3 is a command that updates log forwarding config (aws-s3 target)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | AWS access id relevant for access_key auth-type | [optional] 
**access_key** | **str** | AWS access key relevant for access_key auth-type | [optional] 
**auth_type** | **str** | AWS auth type [access_key/cloud_id/assume_role] | [optional] 
**bucket_name** | **str** | AWS S3 bucket name | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**log_folder** | **str** | AWS S3 destination folder for logs | [optional] [default to 'use-existing']
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**region** | **str** | AWS region | [optional] 
**role_arn** | **str** | AWS role arn relevant for assume_role auth-type | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



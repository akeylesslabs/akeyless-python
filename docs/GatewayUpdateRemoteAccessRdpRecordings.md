# GatewayUpdateRemoteAccessRdpRecordings

gatewayUpdateRemoteAccessRdpRecordings is a command that update remote access rdp recording config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_storage_access_key_id** | **str** | AWS access key id. For more information refer to https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html | [optional] 
**aws_storage_bucket_name** | **str** | The AWS bucket name. For more information refer to https://docs.aws.amazon.com/s3/ | [optional] 
**aws_storage_bucket_prefix** | **str** | The folder name in S3 bucket. For more information refer to https://docs.aws.amazon.com/s3/ | [optional] 
**aws_storage_region** | **str** | The region where the storage is located | [optional] 
**aws_storage_secret_access_key** | **str** | AWS secret access key. For more information refer to https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html | [optional] 
**azure_storage_account_name** | **str** | Azure account name. For more information refer to https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview | [optional] 
**azure_storage_client_id** | **str** | Azure client id. For more information refer to https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info?tabs&#x3D;portal | [optional] 
**azure_storage_client_secret** | **str** | Azure client secret. For more information refer to https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info?tabs&#x3D;portal | [optional] 
**azure_storage_container_name** | **str** | Azure container name. For more information refer to https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata | [optional] 
**azure_storage_tenant_id** | **str** | Azure tenant id. For more information refer to https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**rdp_session_recording** | **str** | Enable recording of rdp session [true/false] | [optional] 
**rdp_session_recording_compress** | **bool** | Whether to compress recording files before upload | [optional] 
**rdp_session_recording_encryption_key** | **str** | If provided, this key will be used to encrypt uploaded recordings. | [optional] 
**rdp_session_recording_quality** | **str** | RDP session recording quality [low/medium/high] | [optional] 
**rdp_session_storage** | **str** | Rdp session recording storage destination [local/aws/azure] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



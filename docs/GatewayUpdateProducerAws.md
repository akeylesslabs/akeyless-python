# GatewayUpdateProducerAws

gatewayUpdateProducerAws is a command that Updates aws producer [Deprecated: Use dynamic-secret-update-aws command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mode** | **str** |  | [optional] 
**admin_rotation_interval_days** | **int** | Admin credentials rotation interval (days) | [optional] [default to 0]
**aws_access_key_id** | **str** | Access Key ID | [optional] 
**aws_access_secret_key** | **str** | Secret Access Key | [optional] 
**aws_role_arns** | **str** | AWS Role ARNs to be used in the Assume Role operation (relevant only for assume_role mode) | [optional] 
**aws_user_console_access** | **bool** | AWS User console access | [optional] [default to False]
**aws_user_groups** | **str** | AWS User groups | [optional] 
**aws_user_policies** | **str** | AWS User policies | [optional] 
**aws_user_programmatic_access** | **bool** | Enable AWS User programmatic access | [optional] [default to True]
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**enable_admin_rotation** | **bool** | Automatic admin credentials rotation | [optional] [default to False]
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**region** | **str** | Region | [optional] [default to 'us-east-2']
**secure_access_aws_account_id** | **str** | The AWS account id | [optional] 
**secure_access_aws_native_cli** | **bool** | The AWS native cli | [optional] 
**secure_access_bastion_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Bastion | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to True]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless Web Access Bastion | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless Web Access Bastion | [optional] [default to False]
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



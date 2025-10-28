# GatewayUpdateProducerAws

gatewayUpdateProducerAws is a command that Updates aws producer [Deprecated: Use dynamic-secret-update-aws command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mode** | **str** |  | [optional] 
**admin_rotation_interval_days** | **int** | Admin credentials rotation interval (days) | [optional] [default to 0]
**aws_access_key_id** | **str** | Access Key ID | [optional] 
**aws_access_secret_key** | **str** | Secret Access Key | [optional] 
**aws_external_id** | **str** | The AWS External ID associated with the AWS role (relevant only for assume_role mode) | [optional] 
**aws_role_arns** | **str** | AWS Role ARNs to be used in the Assume Role operation (relevant only for assume_role mode) | [optional] 
**aws_user_console_access** | **bool** | AWS User console access | [optional] [default to False]
**aws_user_groups** | **str** | AWS User groups | [optional] 
**aws_user_policies** | **str** | AWS User policies | [optional] 
**aws_user_programmatic_access** | **bool** | Enable AWS User programmatic access | [optional] [default to True]
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**enable_admin_rotation** | **bool** | Automatic admin credentials rotation | [optional] [default to False]
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**region** | **str** | Region | [optional] [default to 'us-east-2']
**secure_access_aws_account_id** | **str** | The AWS account id | [optional] 
**secure_access_aws_native_cli** | **bool** | The AWS native cli | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to True]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**session_tags** | **str** | String of Key value session tags comma separated, relevant only for Assumed Role | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**transitive_tag_keys** | **str** | String of transitive tag keys space separated, relevant only for Assumed Role | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



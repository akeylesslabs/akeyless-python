# UpdateWindowsTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA) | [optional] 
**description** | **str** | Description of the object | [optional] 
**domain** | **str** | User domain name | [optional] 
**hostname** | **str** | Server hostname | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**password** | **str** | Privileged user password | 
**port** | **str** | Server WinRM port | [optional] [default to '5986']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_version** | **bool** | Deprecated | [optional] 
**use_tls** | **str** | Enable/Disable TLS for WinRM over HTTPS [true/false] | [optional] [default to 'true']
**username** | **str** | Privileged username | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



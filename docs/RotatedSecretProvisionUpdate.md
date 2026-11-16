# RotatedSecretProvisionUpdate

provision-on-rotation provisions this target after a successful key rotation and is only supported for rotator type key-rotator. Omit the flag to keep the current value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Rotated secret name | 
**new_target_name** | **str** | New target name when retargeting the provisioning association | [optional] 
**private_key_passphrase** | **str** | Passphrase used to encrypt the private key file (omit to keep current; requires Read) | [optional] 
**private_key_remote_path** | **str** | Remote path for the private key (omit to keep current) | [optional] 
**provision_keys** | **str** | Keys to provision: public-key or private-key (omit to keep current) | [optional] 
**provision_on_rotation** | **bool** | When true, provision keys to this target after a successful key rotation. Only supported for rotator type key-rotator. Omit to keep the current value. Set false to turn it off. | [optional] 
**public_key_remote_path** | **str** | Remote path for the public key (omit to keep current) | [optional] 
**target_name** | **str** | Target name of the provisioning association to update | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



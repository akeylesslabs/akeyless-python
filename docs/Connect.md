# Connect

Connect is a command that performs secure remote access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helper** | [**object**](.md) |  | [optional] 
**rc_file_override** | **str** | used to override .akeyless-connect.rc in tests | [optional] 
**bastion_ctrl_path** | **str** | The Bastion API path | [optional] 
**bastion_ctrl_port** | **str** | The Bastion API Port | [optional] [default to '9900']
**bastion_ctrl_proto** | **str** | The Bastion API protocol | [optional] [default to 'http']
**bastion_ctrl_subdomain** | **str** | The Bastion API prefix | [optional] 
**cert_issuer_name** | **str** | The Akeyless certificate issuer name | [optional] 
**identity_file** | **str** | The file from which the identity (private key) for public key authentication is read | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**justification** | **str** |  | [optional] 
**name** | **str** | The Secret name (for database and AWS producers - producer name) | [optional] 
**ssh_command** | **str** | Path to SSH executable. e.g. /usr/bin/ssh | [optional] 
**ssh_extra_args** | **str** | Additional SSH arguments (except -i) | [optional] 
**ssh_legacy_signing_alg** | **bool** | Set this option to output legacy (&#39;ssh-rsa-cert-v01@openssh.com&#39;) signing algorithm name in the ssh certificate. | [optional] [default to False]
**target** | **str** | The target | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_ssh_agent** | **bool** | Enable ssh-agent | [optional] 
**via_bastion** | **str** | The jump box server | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



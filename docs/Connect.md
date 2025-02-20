# Connect

Connect is a command that performs secure remote access

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helper** | **object** |  | [optional] 
**rc_file_override** | **str** | used to override .akeyless-connect.rc in tests | [optional] 
**bastion_ctrl_path** | **str** | Deprecated. use bastion-ctrl-path | [optional] 
**bastion_ctrl_port** | **str** | Deprecated. use sra-ctrl-port | [optional] 
**bastion_ctrl_proto** | **str** | Deprecated. use sra-ctrl-proto | [optional] 
**bastion_ctrl_subdomain** | **str** | Deprecated. use sra-ctrl-subdomain | [optional] 
**cert_issuer_name** | **str** | The Akeyless certificate issuer name | [optional] 
**gateway_url** | **str** | The Gateway URL (configuration management) address, e.g. http://localhost:8000 | [optional] 
**identity_file** | **str** | The file from which the identity (private key) for public key authentication is read | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**justification** | **str** |  | [optional] 
**name** | **str** | The Secret name (for database and AWS producers - producer name) | [optional] 
**sra_ctrl_path** | **str** | The Bastion API path | [optional] 
**sra_ctrl_port** | **str** | The Bastion API Port | [optional] [default to '9900']
**sra_ctrl_proto** | **str** | The SRA API protocol | [optional] [default to 'http']
**sra_ctrl_subdomain** | **str** | The SRA API prefix | [optional] 
**ssh_command** | **str** | Path to SSH executable. e.g. /usr/bin/ssh | [optional] 
**ssh_extra_args** | **str** | Additional SSH arguments (except -i) | [optional] 
**ssh_legacy_signing_alg** | **bool** | Set this option to output legacy (&#39;ssh-rsa-cert-v01@openssh.com&#39;) signing algorithm name in the ssh certificate. | [optional] [default to False]
**target** | **str** | The target | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_ssh_agent** | **bool** | Enable ssh-agent | [optional] 
**via_bastion** | **str** | Deprecated. Use via-sra | [optional] 
**via_sra** | **str** | The jump box server | [optional] 

## Example

```python
from akeyless.models.connect import Connect

# TODO update the JSON string below
json = "{}"
# create an instance of Connect from a JSON string
connect_instance = Connect.from_json(json)
# print the JSON string representation of the object
print(Connect.to_json())

# convert the object into a dict
connect_dict = connect_instance.to_dict()
# create an instance of Connect from a dict
connect_from_dict = Connect.from_dict(connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GatewayUpdateRemoteAccess

gatewayUpdateRemoteAccess is a command that update remote access config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_urls** | **str** | List of valid URLs to redirect from the Portal back to the remote access server (in a comma-delimited list) | [optional] [default to 'use-existing']
**hide_session_recording** | **str** | Specifies whether to show/hide if the session is currently recorded [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**kexalgs** | **str** | Decide which algorithm will be used as part of the SSH initial hand-shake process | [optional] [default to 'use-existing']
**keyboard_layout** | **str** | Enable support for additional keyboard layouts | [optional] [default to 'use-existing']
**legacy_ssh_algorithm** | **str** | Signs SSH certificates using legacy ssh-rsa-cert-01@openssh.com signing algorithm [true/false] | [optional] 
**rdp_target_configuration** | **str** | Specify the usernameSubClaim that exists inside the IDP JWT, e.g. email | [optional] [default to 'use-existing']
**ssh_target_configuration** | **str** | Specify the usernameSubClaim that exists inside the IDP JWT, e.g. email | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_remote_access import GatewayUpdateRemoteAccess

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateRemoteAccess from a JSON string
gateway_update_remote_access_instance = GatewayUpdateRemoteAccess.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateRemoteAccess.to_json())

# convert the object into a dict
gateway_update_remote_access_dict = gateway_update_remote_access_instance.to_dict()
# create an instance of GatewayUpdateRemoteAccess from a dict
gateway_update_remote_access_from_dict = GatewayUpdateRemoteAccess.from_dict(gateway_update_remote_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



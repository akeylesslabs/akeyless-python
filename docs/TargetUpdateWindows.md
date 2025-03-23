# TargetUpdateWindows

GatewayUpdateProducerWindowsCmd is a command that updates an existing windows target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA) | [optional] 
**connection_type** | **str** | Type of connection to Windows Server [credentials/parent-target] | [optional] [default to 'credentials']
**description** | **str** | Description of the object | [optional] 
**domain** | **str** | User domain name | [optional] 
**hostname** | **str** | Server hostname | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**parent_target_name** | **str** | Name of the parent target, relevant only when connection-type is parent-target | [optional] 
**password** | **str** | Privileged user password | [default to 'dummy_value']
**port** | **str** | Server WinRM port | [optional] [default to '5986']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_tls** | **str** | Enable/Disable TLS for WinRM over HTTPS [true/false] | [optional] [default to 'true']
**username** | **str** | Privileged username | [default to 'dummy_value']

## Example

```python
from akeyless.models.target_update_windows import TargetUpdateWindows

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpdateWindows from a JSON string
target_update_windows_instance = TargetUpdateWindows.from_json(json)
# print the JSON string representation of the object
print(TargetUpdateWindows.to_json())

# convert the object into a dict
target_update_windows_dict = target_update_windows_instance.to_dict()
# create an instance of TargetUpdateWindows from a dict
target_update_windows_from_dict = TargetUpdateWindows.from_dict(target_update_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



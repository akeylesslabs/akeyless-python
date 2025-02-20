# TargetCreateWindows

GatewayCreateProducerWindowsCmd is a command that creates a new windows target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA) | [optional] 
**description** | **str** | Description of the object | [optional] 
**domain** | **str** | User domain name | [optional] 
**hostname** | **str** | Server hostname | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**password** | **str** | Privileged user password | 
**port** | **str** | Server WinRM port | [optional] [default to '5986']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_tls** | **str** | Enable/Disable TLS for WinRM over HTTPS [true/false] | [optional] [default to 'true']
**username** | **str** | Privileged username | 

## Example

```python
from akeyless.models.target_create_windows import TargetCreateWindows

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateWindows from a JSON string
target_create_windows_instance = TargetCreateWindows.from_json(json)
# print the JSON string representation of the object
print(TargetCreateWindows.to_json())

# convert the object into a dict
target_create_windows_dict = target_create_windows_instance.to_dict()
# create an instance of TargetCreateWindows from a dict
target_create_windows_from_dict = TargetCreateWindows.from_dict(target_create_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



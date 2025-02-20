# GatewayListRotatedSecrets

gatewayListRotatedSecrets is a command that returns a list of rotated secrets. [Deprecated: Use rotated-secret list command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_list_rotated_secrets import GatewayListRotatedSecrets

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayListRotatedSecrets from a JSON string
gateway_list_rotated_secrets_instance = GatewayListRotatedSecrets.from_json(json)
# print the JSON string representation of the object
print(GatewayListRotatedSecrets.to_json())

# convert the object into a dict
gateway_list_rotated_secrets_dict = gateway_list_rotated_secrets_instance.to_dict()
# create an instance of GatewayListRotatedSecrets from a dict
gateway_list_rotated_secrets_from_dict = GatewayListRotatedSecrets.from_dict(gateway_list_rotated_secrets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



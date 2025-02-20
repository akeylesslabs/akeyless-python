# GatewayGetK8SAuthConfig

gatewayGetK8SAuth is a command that gets k8s auth config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | K8S Auth config name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_get_k8_s_auth_config import GatewayGetK8SAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayGetK8SAuthConfig from a JSON string
gateway_get_k8_s_auth_config_instance = GatewayGetK8SAuthConfig.from_json(json)
# print the JSON string representation of the object
print(GatewayGetK8SAuthConfig.to_json())

# convert the object into a dict
gateway_get_k8_s_auth_config_dict = gateway_get_k8_s_auth_config_instance.to_dict()
# create an instance of GatewayGetK8SAuthConfig from a dict
gateway_get_k8_s_auth_config_from_dict = GatewayGetK8SAuthConfig.from_dict(gateway_get_k8_s_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GatewayUpdateTlsCert

gatewayUpdateTlsCert is a command that updates Gateway TLS certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_data** | **str** | TLS Certificate (base64 encoded) | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_data** | **str** | TLS Private Key (base64 encoded) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_tls_cert import GatewayUpdateTlsCert

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateTlsCert from a JSON string
gateway_update_tls_cert_instance = GatewayUpdateTlsCert.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateTlsCert.to_json())

# convert the object into a dict
gateway_update_tls_cert_dict = gateway_update_tls_cert_instance.to_dict()
# create an instance of GatewayUpdateTlsCert from a dict
gateway_update_tls_cert_from_dict = GatewayUpdateTlsCert.from_dict(gateway_update_tls_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



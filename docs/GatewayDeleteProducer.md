# GatewayDeleteProducer

gatewayDeleteProducer is a command that deletes producer [Deprecated: Use dynamic-secret-delete command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_delete_producer import GatewayDeleteProducer

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDeleteProducer from a JSON string
gateway_delete_producer_instance = GatewayDeleteProducer.from_json(json)
# print the JSON string representation of the object
print(GatewayDeleteProducer.to_json())

# convert the object into a dict
gateway_delete_producer_dict = gateway_delete_producer_instance.to_dict()
# create an instance of GatewayDeleteProducer from a dict
gateway_delete_producer_from_dict = GatewayDeleteProducer.from_dict(gateway_delete_producer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



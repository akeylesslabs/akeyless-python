# GatewayStopProducer

gatewayStopProducer is a command that stops producer [Deprecated: Use set-item-state command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_stop_producer import GatewayStopProducer

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayStopProducer from a JSON string
gateway_stop_producer_instance = GatewayStopProducer.from_json(json)
# print the JSON string representation of the object
print(GatewayStopProducer.to_json())

# convert the object into a dict
gateway_stop_producer_dict = gateway_stop_producer_instance.to_dict()
# create an instance of GatewayStopProducer from a dict
gateway_stop_producer_from_dict = GatewayStopProducer.from_dict(gateway_stop_producer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



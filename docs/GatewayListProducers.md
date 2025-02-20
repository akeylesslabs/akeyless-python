# GatewayListProducers

gatewayListProducers is a command that returns a list of producers [Deprecated: Use dynamic-secret-list command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_list_producers import GatewayListProducers

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayListProducers from a JSON string
gateway_list_producers_instance = GatewayListProducers.from_json(json)
# print the JSON string representation of the object
print(GatewayListProducers.to_json())

# convert the object into a dict
gateway_list_producers_dict = gateway_list_producers_instance.to_dict()
# create an instance of GatewayListProducers from a dict
gateway_list_producers_from_dict = GatewayListProducers.from_dict(gateway_list_producers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



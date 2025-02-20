# GatewayCreateProducerChef

gatewayCreateProducerChef is a command that creates chef producer [Deprecated: Use dynamic-secret-create-chef command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chef_orgs** | **str** | Organizations | [optional] 
**chef_server_key** | **str** | Server key | [optional] 
**chef_server_url** | **str** | Server URL | [optional] 
**chef_server_username** | **str** | Server username | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**skip_ssl** | **bool** | Skip SSL | [optional] [default to True]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.gateway_create_producer_chef import GatewayCreateProducerChef

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerChef from a JSON string
gateway_create_producer_chef_instance = GatewayCreateProducerChef.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerChef.to_json())

# convert the object into a dict
gateway_create_producer_chef_dict = gateway_create_producer_chef_instance.to_dict()
# create an instance of GatewayCreateProducerChef from a dict
gateway_create_producer_chef_from_dict = GatewayCreateProducerChef.from_dict(gateway_create_producer_chef_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



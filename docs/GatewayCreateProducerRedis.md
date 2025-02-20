# GatewayCreateProducerRedis

gatewayCreateProducerRedis is a command that creates Redis producer [Deprecated: Use dynamic-secret-create-redis command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl_rules** | **str** | A JSON array list of redis ACL rules to attach to the created user. For available rules see the ACL CAT command https://redis.io/commands/acl-cat By default the user will have permissions to read all keys &#39;[\&quot;~*\&quot;, \&quot;+@read\&quot;]&#39; | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**host** | **str** | Redis Host | [optional] [default to '127.0.0.1']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**password** | **str** | Redis Password | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**port** | **str** | Redis Port | [optional] [default to '6379']
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**ssl** | **bool** | Enable/Disable SSL [true/false] | [optional] [default to False]
**ssl_certificate** | **str** | SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA) | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Redis Username | [optional] 

## Example

```python
from akeyless.models.gateway_create_producer_redis import GatewayCreateProducerRedis

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerRedis from a JSON string
gateway_create_producer_redis_instance = GatewayCreateProducerRedis.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerRedis.to_json())

# convert the object into a dict
gateway_create_producer_redis_dict = gateway_create_producer_redis_instance.to_dict()
# create an instance of GatewayCreateProducerRedis from a dict
gateway_create_producer_redis_from_dict = GatewayCreateProducerRedis.from_dict(gateway_create_producer_redis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



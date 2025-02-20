# CreateRabbitMQTarget

createRabbitMQTarget is a command that creates a new target. [Deprecated: Use target-create-rabbitmq command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**rabbitmq_server_password** | **str** |  | [optional] 
**rabbitmq_server_uri** | **str** |  | [optional] 
**rabbitmq_server_user** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_rabbit_mq_target import CreateRabbitMQTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRabbitMQTarget from a JSON string
create_rabbit_mq_target_instance = CreateRabbitMQTarget.from_json(json)
# print the JSON string representation of the object
print(CreateRabbitMQTarget.to_json())

# convert the object into a dict
create_rabbit_mq_target_dict = create_rabbit_mq_target_instance.to_dict()
# create an instance of CreateRabbitMQTarget from a dict
create_rabbit_mq_target_from_dict = CreateRabbitMQTarget.from_dict(create_rabbit_mq_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



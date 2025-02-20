# UpdateRabbitMQTarget

updateRabbitMQTarget is a command that updates a new target. [Deprecated: Use target-update-rabbitmq command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**rabbitmq_server_password** | **str** |  | [optional] 
**rabbitmq_server_uri** | **str** |  | [optional] 
**rabbitmq_server_user** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_version** | **bool** | Deprecated | [optional] 

## Example

```python
from akeyless.models.update_rabbit_mq_target import UpdateRabbitMQTarget

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRabbitMQTarget from a JSON string
update_rabbit_mq_target_instance = UpdateRabbitMQTarget.from_json(json)
# print the JSON string representation of the object
print(UpdateRabbitMQTarget.to_json())

# convert the object into a dict
update_rabbit_mq_target_dict = update_rabbit_mq_target_instance.to_dict()
# create an instance of UpdateRabbitMQTarget from a dict
update_rabbit_mq_target_from_dict = UpdateRabbitMQTarget.from_dict(update_rabbit_mq_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



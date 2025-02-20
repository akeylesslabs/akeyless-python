# RabbitMQTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rabbitmq_server_password** | **str** |  | [optional] 
**rabbitmq_server_uri** | **str** |  | [optional] 
**rabbitmq_server_user** | **str** |  | [optional] 

## Example

```python
from akeyless.models.rabbit_mq_target_details import RabbitMQTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RabbitMQTargetDetails from a JSON string
rabbit_mq_target_details_instance = RabbitMQTargetDetails.from_json(json)
# print the JSON string representation of the object
print(RabbitMQTargetDetails.to_json())

# convert the object into a dict
rabbit_mq_target_details_dict = rabbit_mq_target_details_instance.to_dict()
# create an instance of RabbitMQTargetDetails from a dict
rabbit_mq_target_details_from_dict = RabbitMQTargetDetails.from_dict(rabbit_mq_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



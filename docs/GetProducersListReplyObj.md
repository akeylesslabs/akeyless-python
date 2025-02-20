# GetProducersListReplyObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producers** | [**List[Producer]**](Producer.md) |  | [optional] 
**producers_errors** | **object** |  | [optional] 

## Example

```python
from akeyless.models.get_producers_list_reply_obj import GetProducersListReplyObj

# TODO update the JSON string below
json = "{}"
# create an instance of GetProducersListReplyObj from a JSON string
get_producers_list_reply_obj_instance = GetProducersListReplyObj.from_json(json)
# print the JSON string representation of the object
print(GetProducersListReplyObj.to_json())

# convert the object into a dict
get_producers_list_reply_obj_dict = get_producers_list_reply_obj_instance.to_dict()
# create an instance of GetProducersListReplyObj from a dict
get_producers_list_reply_obj_from_dict = GetProducersListReplyObj.from_dict(get_producers_list_reply_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



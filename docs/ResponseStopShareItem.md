# ResponseStopShareItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[EmailError]**](EmailError.md) |  | [optional] 
**item_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.response_stop_share_item import ResponseStopShareItem

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseStopShareItem from a JSON string
response_stop_share_item_instance = ResponseStopShareItem.from_json(json)
# print the JSON string representation of the object
print(ResponseStopShareItem.to_json())

# convert the object into a dict
response_stop_share_item_dict = response_stop_share_item_instance.to_dict()
# create an instance of ResponseStopShareItem from a dict
response_stop_share_item_from_dict = ResponseStopShareItem.from_dict(response_stop_share_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



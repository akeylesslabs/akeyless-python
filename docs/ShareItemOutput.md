# ShareItemOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_error** | **Dict[str, str]** |  | [optional] 
**items_error** | [**List[ResponseStopShareItem]**](ResponseStopShareItem.md) |  | [optional] 
**s_token** | **str** |  | [optional] 
**shared_users** | **List[str]** |  | [optional] 
**shared_users_full_info** | [**List[SharingItemFullInfo]**](SharingItemFullInfo.md) |  | [optional] 
**sharing_url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.share_item_output import ShareItemOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ShareItemOutput from a JSON string
share_item_output_instance = ShareItemOutput.from_json(json)
# print the JSON string representation of the object
print(ShareItemOutput.to_json())

# convert the object into a dict
share_item_output_dict = share_item_output_instance.to_dict()
# create an instance of ShareItemOutput from a dict
share_item_output_from_dict = ShareItemOutput.from_dict(share_item_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



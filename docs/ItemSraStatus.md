# ItemSraStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_by_host_info** | **Dict[str, int]** |  | [optional] 
**count_info** | **Dict[str, Dict[str, int]]** |  | [optional] 
**hosts_in_use** | **List[str]** |  | [optional] 
**is_in_use** | **bool** |  | [optional] 
**last_used_item** | **datetime** |  | [optional] 

## Example

```python
from akeyless.models.item_sra_status import ItemSraStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSraStatus from a JSON string
item_sra_status_instance = ItemSraStatus.from_json(json)
# print the JSON string representation of the object
print(ItemSraStatus.to_json())

# convert the object into a dict
item_sra_status_dict = item_sra_status_instance.to_dict()
# create an instance of ItemSraStatus from a dict
item_sra_status_from_dict = ItemSraStatus.from_dict(item_sra_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



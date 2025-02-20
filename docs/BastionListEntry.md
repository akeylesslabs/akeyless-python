# BastionListEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**allowed_access_ids** | **List[str]** |  | [optional] 
**allowed_urls** | **List[str]** |  | [optional] 
**allowed_urls_per_instance** | **Dict[str, List[str]]** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**has_gateway_identity** | **bool** |  | [optional] 
**last_report** | **datetime** |  | [optional] 

## Example

```python
from akeyless.models.bastion_list_entry import BastionListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BastionListEntry from a JSON string
bastion_list_entry_instance = BastionListEntry.from_json(json)
# print the JSON string representation of the object
print(BastionListEntry.to_json())

# convert the object into a dict
bastion_list_entry_dict = bastion_list_entry_instance.to_dict()
# create an instance of BastionListEntry from a dict
bastion_list_entry_from_dict = BastionListEntry.from_dict(bastion_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



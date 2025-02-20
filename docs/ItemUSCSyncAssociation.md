# ItemUSCSyncAssociation

ItemUSCSyncAssociation includes details of usc sync associations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_id** | **str** |  | [optional] 
**attributes** | [**RemoteSecretInfo**](RemoteSecretInfo.md) |  | [optional] 
**item_id** | **int** |  | [optional] 
**item_name** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.item_usc_sync_association import ItemUSCSyncAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ItemUSCSyncAssociation from a JSON string
item_usc_sync_association_instance = ItemUSCSyncAssociation.from_json(json)
# print the JSON string representation of the object
print(ItemUSCSyncAssociation.to_json())

# convert the object into a dict
item_usc_sync_association_dict = item_usc_sync_association_instance.to_dict()
# create an instance of ItemUSCSyncAssociation from a dict
item_usc_sync_association_from_dict = ItemUSCSyncAssociation.from_dict(item_usc_sync_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



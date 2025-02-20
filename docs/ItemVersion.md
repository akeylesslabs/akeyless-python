# ItemVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_date** | **datetime** |  | [optional] 
**access_date_display** | **str** |  | [optional] 
**certificate_version_info** | [**CertificateVersionInfo**](CertificateVersionInfo.md) |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**customer_fragment_id** | **str** |  | [optional] 
**deletion_date** | **datetime** |  | [optional] 
**item_version_state** | **str** | ItemState defines the different states an Item can be in | [optional] 
**modification_date** | **datetime** |  | [optional] 
**protection_key_name** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**with_customer_fragment** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.item_version import ItemVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ItemVersion from a JSON string
item_version_instance = ItemVersion.from_json(json)
# print the JSON string representation of the object
print(ItemVersion.to_json())

# convert the object into a dict
item_version_dict = item_version_instance.to_dict()
# create an instance of ItemVersion from a dict
item_version_from_dict = ItemVersion.from_dict(item_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



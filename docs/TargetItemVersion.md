# TargetItemVersion


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
**latest_version** | **bool** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**protection_key_name** | **str** |  | [optional] 
**target_name** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**with_customer_fragment** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.target_item_version import TargetItemVersion

# TODO update the JSON string below
json = "{}"
# create an instance of TargetItemVersion from a JSON string
target_item_version_instance = TargetItemVersion.from_json(json)
# print the JSON string representation of the object
print(TargetItemVersion.to_json())

# convert the object into a dict
target_item_version_dict = target_item_version_instance.to_dict()
# create an instance of TargetItemVersion from a dict
target_item_version_from_dict = TargetItemVersion.from_dict(target_item_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CfInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.cf_info import CfInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CfInfo from a JSON string
cf_info_instance = CfInfo.from_json(json)
# print the JSON string representation of the object
print(CfInfo.to_json())

# convert the object into a dict
cf_info_dict = cf_info_instance.to_dict()
# create an instance of CfInfo from a dict
cf_info_from_dict = CfInfo.from_dict(cf_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



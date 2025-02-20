# SraInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sla** | **str** |  | [optional] 
**tier** | **str** | Tier represents a level of extensibility the account will have, defined by various limits for different resources of Akeyless e.g - A StarterTier may have a limit of 3 Client resources and 50 Secret resources | [optional] 
**user_type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.sra_info import SraInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SraInfo from a JSON string
sra_info_instance = SraInfo.from_json(json)
# print the JSON string representation of the object
print(SraInfo.to_json())

# convert the object into a dict
sra_info_dict = sra_info_instance.to_dict()
# create an instance of SraInfo from a dict
sra_info_from_dict = SraInfo.from_dict(sra_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SmInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sla** | **str** |  | [optional] 
**tier** | **str** | Tier represents a level of extensibility the account will have, defined by various limits for different resources of Akeyless e.g - A StarterTier may have a limit of 3 Client resources and 50 Secret resources | [optional] 

## Example

```python
from akeyless.models.sm_info import SmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SmInfo from a JSON string
sm_info_instance = SmInfo.from_json(json)
# print the JSON string representation of the object
print(SmInfo.to_json())

# convert the object into a dict
sm_info_dict = sm_info_instance.to_dict()
# create an instance of SmInfo from a dict
sm_info_from_dict = SmInfo.from_dict(sm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



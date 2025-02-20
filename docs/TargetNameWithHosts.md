# TargetNameWithHosts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** |  | [optional] 
**target_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.target_name_with_hosts import TargetNameWithHosts

# TODO update the JSON string below
json = "{}"
# create an instance of TargetNameWithHosts from a JSON string
target_name_with_hosts_instance = TargetNameWithHosts.from_json(json)
# print the JSON string representation of the object
print(TargetNameWithHosts.to_json())

# convert the object into a dict
target_name_with_hosts_dict = target_name_with_hosts_instance.to_dict()
# create an instance of TargetNameWithHosts from a dict
target_name_with_hosts_from_dict = TargetNameWithHosts.from_dict(target_name_with_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



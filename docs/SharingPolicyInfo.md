# SharingPolicyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_share_link_ttl** | **int** |  | [optional] 
**enable** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.sharing_policy_info import SharingPolicyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SharingPolicyInfo from a JSON string
sharing_policy_info_instance = SharingPolicyInfo.from_json(json)
# print the JSON string representation of the object
print(SharingPolicyInfo.to_json())

# convert the object into a dict
sharing_policy_info_dict = sharing_policy_info_instance.to_dict()
# create an instance of SharingPolicyInfo from a dict
sharing_policy_info_from_dict = SharingPolicyInfo.from_dict(sharing_policy_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



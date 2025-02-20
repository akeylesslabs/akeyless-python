# HuaweiAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_endpoint** | **str** | The auth URL. | [optional] 
**domain_id** | **List[str]** | The list of domain ids that the login is restricted to. | [optional] 
**domain_name** | **List[str]** | The list of domainNames that the login is restricted to. | [optional] 
**tenant_id** | **List[str]** | The list of tenantIDs  that the login is restricted to. | [optional] 
**tenant_name** | **List[str]** | The list of tenantNames  that the login is restricted to. | [optional] 
**user_id** | **List[str]** | The list of user ids that the login is restricted to. | [optional] 
**user_name** | **List[str]** | The list of user names that the login is restricted to. | [optional] 

## Example

```python
from akeyless.models.huawei_access_rules import HuaweiAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of HuaweiAccessRules from a JSON string
huawei_access_rules_instance = HuaweiAccessRules.from_json(json)
# print the JSON string representation of the object
print(HuaweiAccessRules.to_json())

# convert the object into a dict
huawei_access_rules_dict = huawei_access_rules_instance.to_dict()
# create an instance of HuaweiAccessRules from a dict
huawei_access_rules_from_dict = HuaweiAccessRules.from_dict(huawei_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



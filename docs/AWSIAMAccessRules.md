# AWSIAMAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **List[str]** | The list of account ids that the login is restricted to. | [optional] 
**arn** | **List[str]** | The list of ARNs that the login is restricted to. | [optional] 
**resource_id** | **List[str]** | The list of resource ids that the login is restricted to. | [optional] 
**role_id** | **List[str]** | The list of role ids that the login is restricted to. | [optional] 
**role_name** | **List[str]** | The list of role names that the login is restricted to. | [optional] 
**sts_endpoint** | **str** | The sts URL. | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 
**user_id** | **List[str]** | The list of user ids that the login is restricted to. | [optional] 
**user_name** | **List[str]** | The list of user names that the login is restricted to. | [optional] 

## Example

```python
from akeyless.models.awsiam_access_rules import AWSIAMAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of AWSIAMAccessRules from a JSON string
awsiam_access_rules_instance = AWSIAMAccessRules.from_json(json)
# print the JSON string representation of the object
print(AWSIAMAccessRules.to_json())

# convert the object into a dict
awsiam_access_rules_dict = awsiam_access_rules_instance.to_dict()
# create an instance of AWSIAMAccessRules from a dict
awsiam_access_rules_from_dict = AWSIAMAccessRules.from_dict(awsiam_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



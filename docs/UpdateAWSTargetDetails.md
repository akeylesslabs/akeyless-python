# UpdateAWSTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | The aws secret access key | [optional] 
**access_key_id** | **str** | The aws access key id | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**name** | **str** | Target name | 
**new_version** | **bool** | Deprecated | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**region** | **str** | The aws region | [optional] [default to 'us-east-2']
**session_token** | **str** | Required only for temporary security credentials retrieved via STS, otherwise it can be an empty string | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_aws_target_details import UpdateAWSTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAWSTargetDetails from a JSON string
update_aws_target_details_instance = UpdateAWSTargetDetails.from_json(json)
# print the JSON string representation of the object
print(UpdateAWSTargetDetails.to_json())

# convert the object into a dict
update_aws_target_details_dict = update_aws_target_details_instance.to_dict()
# create an instance of UpdateAWSTargetDetails from a dict
update_aws_target_details_from_dict = UpdateAWSTargetDetails.from_dict(update_aws_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TargetCreateAws


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | AWS secret access key | 
**access_key_id** | **str** | AWS access key ID | 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**region** | **str** | AWS region | [optional] [default to 'us-east-2']
**session_token** | **str** | Required only for temporary security credentials retrieved using STS | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_cloud_identity** | **bool** | Use the GW&#39;s Cloud IAM | [optional] 

## Example

```python
from akeyless.models.target_create_aws import TargetCreateAws

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateAws from a JSON string
target_create_aws_instance = TargetCreateAws.from_json(json)
# print the JSON string representation of the object
print(TargetCreateAws.to_json())

# convert the object into a dict
target_create_aws_dict = target_create_aws_instance.to_dict()
# create an instance of TargetCreateAws from a dict
target_create_aws_from_dict = TargetCreateAws.from_dict(target_create_aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



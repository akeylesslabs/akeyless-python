# TargetUpdateGitlab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**gitlab_access_token** | **str** | Gitlab access token | [optional] 
**gitlab_certificate** | **str** | Gitlab tls certificate (base64 encoded) | [optional] 
**gitlab_url** | **str** | Gitlab base url | [optional] [default to 'https://gitlab.com/']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_update_gitlab import TargetUpdateGitlab

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpdateGitlab from a JSON string
target_update_gitlab_instance = TargetUpdateGitlab.from_json(json)
# print the JSON string representation of the object
print(TargetUpdateGitlab.to_json())

# convert the object into a dict
target_update_gitlab_dict = target_update_gitlab_instance.to_dict()
# create an instance of TargetUpdateGitlab from a dict
target_update_gitlab_from_dict = TargetUpdateGitlab.from_dict(target_update_gitlab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



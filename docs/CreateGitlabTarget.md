# CreateGitlabTarget

createGitlabTarget is a command that creates a new target. [Deprecated: Use target-create-gitlab command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**gitlab_access_token** | **str** | Gitlab access token | [optional] 
**gitlab_certificate** | **str** | Gitlab tls certificate (base64 encoded) | [optional] 
**gitlab_url** | **str** | Gitlab base url | [optional] [default to 'https://gitlab.com/']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_gitlab_target import CreateGitlabTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGitlabTarget from a JSON string
create_gitlab_target_instance = CreateGitlabTarget.from_json(json)
# print the JSON string representation of the object
print(CreateGitlabTarget.to_json())

# convert the object into a dict
create_gitlab_target_dict = create_gitlab_target_instance.to_dict()
# create an instance of CreateGitlabTarget from a dict
create_gitlab_target_from_dict = CreateGitlabTarget.from_dict(create_gitlab_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



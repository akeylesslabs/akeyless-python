# DynamicSecretCreateGitlab

dynamicSecretCreateGitlab is a command that creates gitlab dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**gitlab_access_token** | **str** | Gitlab access token | [optional] 
**gitlab_access_type** | **str** | Gitlab access token type [project,group] | 
**gitlab_certificate** | **str** | Gitlab tls certificate (base64 encoded) | [optional] 
**gitlab_role** | **str** | Gitlab role | [optional] 
**gitlab_token_scopes** | **str** | Comma-separated list of access token scopes to grant | 
**gitlab_url** | **str** | Gitlab base url | [optional] [default to 'https://gitlab.com/']
**group_name** | **str** | Gitlab group name, required for access-type&#x3D;group | [optional] 
**installation_organization** | **str** | Gitlab project name, required for access-type&#x3D;project | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **str** | Access Token TTL | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_create_gitlab import DynamicSecretCreateGitlab

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretCreateGitlab from a JSON string
dynamic_secret_create_gitlab_instance = DynamicSecretCreateGitlab.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretCreateGitlab.to_json())

# convert the object into a dict
dynamic_secret_create_gitlab_dict = dynamic_secret_create_gitlab_instance.to_dict()
# create an instance of DynamicSecretCreateGitlab from a dict
dynamic_secret_create_gitlab_from_dict = DynamicSecretCreateGitlab.from_dict(dynamic_secret_create_gitlab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



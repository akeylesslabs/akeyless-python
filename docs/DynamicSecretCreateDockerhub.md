# DynamicSecretCreateDockerhub

dynamicSecretCreateDockerhub is a command that creates a DOCKERHUB dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**dockerhub_password** | **str** | DockerhubPassword is either the user&#39;s password access token to manage the repository | [optional] 
**dockerhub_token_scopes** | **str** | Access token scopes list (comma-separated) to give the dynamic secret valid options are in \&quot;repo:admin\&quot;, \&quot;repo:write\&quot;, \&quot;repo:read\&quot;, \&quot;repo:public_read\&quot; | [optional] 
**dockerhub_username** | **str** | DockerhubUsername is the name of the user in dockerhub | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.dynamic_secret_create_dockerhub import DynamicSecretCreateDockerhub

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretCreateDockerhub from a JSON string
dynamic_secret_create_dockerhub_instance = DynamicSecretCreateDockerhub.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretCreateDockerhub.to_json())

# convert the object into a dict
dynamic_secret_create_dockerhub_dict = dynamic_secret_create_dockerhub_instance.to_dict()
# create an instance of DynamicSecretCreateDockerhub from a dict
dynamic_secret_create_dockerhub_from_dict = DynamicSecretCreateDockerhub.from_dict(dynamic_secret_create_dockerhub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



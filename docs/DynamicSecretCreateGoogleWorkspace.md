# DynamicSecretCreateGoogleWorkspace

dynamicSecretCreateGoogleWorkspace is a command that creates Google Workspace dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mode** | **str** |  | 
**admin_email** | **str** | Admin user email | 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**fixed_user_claim_keyname** | **str** | For externally provided users, denotes the key-name of IdP claim to extract the username from | [optional] [default to 'ext_email']
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**group_email** | **str** | A group email, relevant only for group access-mode | [optional] 
**group_role** | **str** |  | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**role_name** | **str** | Name of the admin role to assign to the user, relevant only for role access-mode | [optional] 
**role_scope** | **str** |  | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to True]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Name of existing target to use in dynamic secret creation | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.dynamic_secret_create_google_workspace import DynamicSecretCreateGoogleWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretCreateGoogleWorkspace from a JSON string
dynamic_secret_create_google_workspace_instance = DynamicSecretCreateGoogleWorkspace.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretCreateGoogleWorkspace.to_json())

# convert the object into a dict
dynamic_secret_create_google_workspace_dict = dynamic_secret_create_google_workspace_instance.to_dict()
# create an instance of DynamicSecretCreateGoogleWorkspace from a dict
dynamic_secret_create_google_workspace_from_dict = DynamicSecretCreateGoogleWorkspace.from_dict(dynamic_secret_create_google_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SystemAccessCredentialsReplyObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**auth_creds** | **str** | Temporary credentials for accessing Auth | [optional] 
**expiry** | **int** | Credentials expiration date | [optional] 
**kfm_creds** | **str** | Temporary credentials for accessing the KFMs instances | [optional] 
**need_mfa_app_first_config** | **bool** | If the user didn&#39;t complete to configure the MFA app | [optional] 
**required_mfa** | **str** |  | [optional] 
**token** | **str** | Credentials tmp token | [optional] 
**uam_creds** | **str** | Temporary credentials for accessing the UAM service | [optional] 

## Example

```python
from akeyless.models.system_access_credentials_reply_obj import SystemAccessCredentialsReplyObj

# TODO update the JSON string below
json = "{}"
# create an instance of SystemAccessCredentialsReplyObj from a JSON string
system_access_credentials_reply_obj_instance = SystemAccessCredentialsReplyObj.from_json(json)
# print the JSON string representation of the object
print(SystemAccessCredentialsReplyObj.to_json())

# convert the object into a dict
system_access_credentials_reply_obj_dict = system_access_credentials_reply_obj_instance.to_dict()
# create an instance of SystemAccessCredentialsReplyObj from a dict
system_access_credentials_reply_obj_from_dict = SystemAccessCredentialsReplyObj.from_dict(system_access_credentials_reply_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateSalesforceTarget

updateSalesforceTarget is a command that updates a new target. [Deprecated: Use target-update-salesforce command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_private_key_data** | **str** | Base64 encoded PEM of the connected app private key (relevant for JWT auth only) | [optional] 
**auth_flow** | **str** | type of the auth flow (&#39;jwt&#39; / &#39;user-password&#39;) | 
**ca_cert_data** | **str** | Base64 encoded PEM cert to use when uploading a new key to Salesforce | [optional] 
**ca_cert_name** | **str** | name of the certificate in Salesforce tenant to use when uploading new key | [optional] 
**client_id** | **str** | Client ID of the oauth2 app to use for connecting to Salesforce | 
**client_secret** | **str** | Client secret of the oauth2 app to use for connecting to Salesforce (required for password flow) | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**email** | **str** | The email of the user attached to the oauth2 app used for connecting to Salesforce | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**password** | **str** | The password of the user attached to the oauth2 app used for connecting to Salesforce (required for user-password flow) | [optional] 
**security_token** | **str** | The security token of the user attached to the oauth2 app used for connecting to Salesforce  (required for user-password flow) | [optional] 
**tenant_url** | **str** | Url of the Salesforce tenant | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_version** | **bool** | Deprecated | [optional] 

## Example

```python
from akeyless.models.update_salesforce_target import UpdateSalesforceTarget

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSalesforceTarget from a JSON string
update_salesforce_target_instance = UpdateSalesforceTarget.from_json(json)
# print the JSON string representation of the object
print(UpdateSalesforceTarget.to_json())

# convert the object into a dict
update_salesforce_target_dict = update_salesforce_target_instance.to_dict()
# create an instance of UpdateSalesforceTarget from a dict
update_salesforce_target_from_dict = UpdateSalesforceTarget.from_dict(update_salesforce_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



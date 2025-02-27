# UpdateSecretVal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**custom_field** | **Dict[str, str]** | For Password Management use, additional fields | [optional] 
**format** | **str** | Secret format [text/json/key-value] (relevant only for type &#39;generic&#39;) | [optional] [default to 'text']
**inject_url** | **List[str]** | For Password Management use, reflect the website context | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**last_version** | **int** | The last version number before the update | [optional] 
**multiline** | **bool** | The provided value is a multiline value (separated by &#39;\\n&#39;) | [optional] 
**name** | **str** | Secret name | 
**new_version** | **bool** | Deprecated | [optional] 
**password** | **str** | For Password Management use, additional fields | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | For Password Management use | [optional] 
**value** | **str** | The secret value (relevant only for type &#39;generic&#39;) | 

## Example

```python
from akeyless.models.update_secret_val import UpdateSecretVal

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSecretVal from a JSON string
update_secret_val_instance = UpdateSecretVal.from_json(json)
# print the JSON string representation of the object
print(UpdateSecretVal.to_json())

# convert the object into a dict
update_secret_val_dict = update_secret_val_instance.to_dict()
# create an instance of UpdateSecretVal from a dict
update_secret_val_from_dict = UpdateSecretVal.from_dict(update_secret_val_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SignGPG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the key to use in the encryption process | [optional] 
**item_id** | **int** | The item id of the key to use in the encryption process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the encryption process | 
**message** | **str** | The message to be signed in base64 format | 
**passphrase** | **str** | Passphrase that was used to generate the key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.sign_gpg import SignGPG

# TODO update the JSON string below
json = "{}"
# create an instance of SignGPG from a JSON string
sign_gpg_instance = SignGPG.from_json(json)
# print the JSON string representation of the object
print(SignGPG.to_json())

# convert the object into a dict
sign_gpg_dict = sign_gpg_instance.to_dict()
# create an instance of SignGPG from a dict
sign_gpg_from_dict = SignGPG.from_dict(sign_gpg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreatePasskey

CreatePasskey is a command that creates a new passkey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**alg** | **str** | Passkey type; options: [EC256, EC384, EC512] | [default to 'EC256']
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | ClassicKey name | 
**origin_url** | **List[str]** | Originating websites for this passkey | [optional] 
**protection_key_name** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | For Password Management use | [optional] 

## Example

```python
from akeyless.models.create_passkey import CreatePasskey

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasskey from a JSON string
create_passkey_instance = CreatePasskey.from_json(json)
# print the JSON string representation of the object
print(CreatePasskey.to_json())

# convert the object into a dict
create_passkey_dict = create_passkey_instance.to_dict()
# create an instance of CreatePasskey from a dict
create_passkey_from_dict = CreatePasskey.from_dict(create_passkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



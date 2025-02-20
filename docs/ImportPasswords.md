# ImportPasswords

importPasswords is a command that import passwords

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'personal']
**format** | **str** | Password format type [LastPass/Chrome/Firefox/1password/keeper/bitwarden/dashlane] | [optional] [default to 'LastPass']
**import_path** | **str** | File path | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**protection_key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**target_folder** | **str** | Target folder for imported passwords | [optional] [default to '/']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_mode** | **str** |  | [optional] 

## Example

```python
from akeyless.models.import_passwords import ImportPasswords

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPasswords from a JSON string
import_passwords_instance = ImportPasswords.from_json(json)
# print the JSON string representation of the object
print(ImportPasswords.to_json())

# convert the object into a dict
import_passwords_dict = import_passwords_instance.to_dict()
# create an instance of ImportPasswords from a dict
import_passwords_from_dict = ImportPasswords.from_dict(import_passwords_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



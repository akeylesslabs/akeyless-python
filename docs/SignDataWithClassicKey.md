# SignDataWithClassicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Data | 
**display_id** | **str** | The name of the key to use in the sign data process | 
**hashed** | **bool** | Defines whether the data should be hashed as part of the signing. If true, the data will not be hashed | [optional] [default to False]
**hashing_method** | **str** | HashingMethod | [optional] [default to 'SHA256']
**ignore_cache** | **str** | Retrieve the Secret value without checking the Gateway&#39;s cache [true/false]. This flag is only relevant when using the RestAPI | [optional] [default to 'false']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | ClassicKey name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | classic key version | 

## Example

```python
from akeyless.models.sign_data_with_classic_key import SignDataWithClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of SignDataWithClassicKey from a JSON string
sign_data_with_classic_key_instance = SignDataWithClassicKey.from_json(json)
# print the JSON string representation of the object
print(SignDataWithClassicKey.to_json())

# convert the object into a dict
sign_data_with_classic_key_dict = sign_data_with_classic_key_instance.to_dict()
# create an instance of SignDataWithClassicKey from a dict
sign_data_with_classic_key_from_dict = SignDataWithClassicKey.from_dict(sign_data_with_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



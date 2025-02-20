# Hmac


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the key to use in the encryption process | [optional] 
**hash_function** | **str** | Hash function [sha-256,sha-512] | [optional] [default to 'sha-256']
**input_format** | **str** | Select default assumed format for any plaintext input. Currently supported options: [base64] | [optional] 
**item_id** | **int** | The item id of the key to use in the encryption process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the encryption process | 
**plaintext** | **str** | Data to perform hmac on | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.hmac import Hmac

# TODO update the JSON string below
json = "{}"
# create an instance of Hmac from a JSON string
hmac_instance = Hmac.from_json(json)
# print the JSON string representation of the object
print(Hmac.to_json())

# convert the object into a dict
hmac_dict = hmac_instance.to_dict()
# create an instance of Hmac from a dict
hmac_from_dict = Hmac.from_dict(hmac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



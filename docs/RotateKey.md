# RotateKey

of it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Key name | 
**new_cert_pem_data** | **str** | The new pem encoded certificate for the classic key. relevant only for keys provided by user (&#39;bring-your-own-key&#39;) | [optional] 
**new_key_data** | **str** | The new base64 encoded value for the classic key. relevant only for keys provided by user (&#39;bring-your-own-key&#39;) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.rotate_key import RotateKey

# TODO update the JSON string below
json = "{}"
# create an instance of RotateKey from a JSON string
rotate_key_instance = RotateKey.from_json(json)
# print the JSON string representation of the object
print(RotateKey.to_json())

# convert the object into a dict
rotate_key_dict = rotate_key_instance.to_dict()
# create an instance of RotateKey from a dict
rotate_key_from_dict = RotateKey.from_dict(rotate_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



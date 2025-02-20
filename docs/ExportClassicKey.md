# ExportClassicKey

ExportClassicKey is a command that returns the classic key material

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**export_public_key** | **bool** | Use this option to output only public key | [optional] [default to False]
**ignore_cache** | **str** | Retrieve the Secret value without checking the Gateway&#39;s cache [true/false]. This flag is only relevant when using the RestAPI | [optional] [default to 'false']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | ClassicKey name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Classic key version | [optional] 
**wrapping_key_name** | **str** | Classic key name to wrap the key material with | [optional] 

## Example

```python
from akeyless.models.export_classic_key import ExportClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of ExportClassicKey from a JSON string
export_classic_key_instance = ExportClassicKey.from_json(json)
# print the JSON string representation of the object
print(ExportClassicKey.to_json())

# convert the object into a dict
export_classic_key_dict = export_classic_key_instance.to_dict()
# create an instance of ExportClassicKey from a dict
export_classic_key_from_dict = ExportClassicKey.from_dict(export_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



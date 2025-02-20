# GetRSAPublic

getRSAPublic is a command that obtains the public key from a specific RSA private key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Name of RSA key to extract the public key from | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_rsa_public import GetRSAPublic

# TODO update the JSON string below
json = "{}"
# create an instance of GetRSAPublic from a JSON string
get_rsa_public_instance = GetRSAPublic.from_json(json)
# print the JSON string representation of the object
print(GetRSAPublic.to_json())

# convert the object into a dict
get_rsa_public_dict = get_rsa_public_instance.to_dict()
# create an instance of GetRSAPublic from a dict
get_rsa_public_from_dict = GetRSAPublic.from_dict(get_rsa_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



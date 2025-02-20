# GenerateAcmeEab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_name** | **str** | The name of the PKI certificate issuer | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.generate_acme_eab import GenerateAcmeEab

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAcmeEab from a JSON string
generate_acme_eab_instance = GenerateAcmeEab.from_json(json)
# print the JSON string representation of the object
print(GenerateAcmeEab.to_json())

# convert the object into a dict
generate_acme_eab_dict = generate_acme_eab_instance.to_dict()
# create an instance of GenerateAcmeEab from a dict
generate_acme_eab_from_dict = GenerateAcmeEab.from_dict(generate_acme_eab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



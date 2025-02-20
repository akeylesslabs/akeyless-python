# GetCertificateValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_name** | **str** | The parent PKI Certificate Issuer&#39;s name of the certificate, required when used with display-id and token | [optional] 
**display_id** | **str** | Certificate display ID | [optional] 
**ignore_cache** | **str** | Retrieve the Secret value without checking the Gateway&#39;s cache [true/false]. This flag is only relevant when using the RestAPI | [optional] [default to 'false']
**issuance_token** | **str** | Token for getting the issued certificate | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Certificate name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Certificate version | [optional] 

## Example

```python
from akeyless.models.get_certificate_value import GetCertificateValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetCertificateValue from a JSON string
get_certificate_value_instance = GetCertificateValue.from_json(json)
# print the JSON string representation of the object
print(GetCertificateValue.to_json())

# convert the object into a dict
get_certificate_value_dict = get_certificate_value_instance.to_dict()
# create an instance of GetCertificateValue from a dict
get_certificate_value_from_dict = GetCertificateValue.from_dict(get_certificate_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



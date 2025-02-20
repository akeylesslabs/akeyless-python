# ProvisionCertificate

provisionCertificate is a command that provisions a certificate content to a target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | Certificate display ID | [optional] 
**item_id** | **int** | Certificate item ID | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Certificate name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.provision_certificate import ProvisionCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionCertificate from a JSON string
provision_certificate_instance = ProvisionCertificate.from_json(json)
# print the JSON string representation of the object
print(ProvisionCertificate.to_json())

# convert the object into a dict
provision_certificate_dict = provision_certificate_instance.to_dict()
# create an instance of ProvisionCertificate from a dict
provision_certificate_from_dict = ProvisionCertificate.from_dict(provision_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



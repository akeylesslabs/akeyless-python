# CertificateStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_pem** | **str** |  | [optional] 
**common_name** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.certificate_store import CertificateStore

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateStore from a JSON string
certificate_store_instance = CertificateStore.from_json(json)
# print the JSON string representation of the object
print(CertificateStore.to_json())

# convert the object into a dict
certificate_store_dict = certificate_store_instance.to_dict()
# create an instance of CertificateStore from a dict
certificate_store_from_dict = CertificateStore.from_dict(certificate_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



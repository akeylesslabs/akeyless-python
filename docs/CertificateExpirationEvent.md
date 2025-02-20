# CertificateExpirationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds_before** | **int** |  | [optional] 

## Example

```python
from akeyless.models.certificate_expiration_event import CertificateExpirationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateExpirationEvent from a JSON string
certificate_expiration_event_instance = CertificateExpirationEvent.from_json(json)
# print the JSON string representation of the object
print(CertificateExpirationEvent.to_json())

# convert the object into a dict
certificate_expiration_event_dict = certificate_expiration_event_instance.to_dict()
# create an instance of CertificateExpirationEvent from a dict
certificate_expiration_event_from_dict = CertificateExpirationEvent.from_dict(certificate_expiration_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



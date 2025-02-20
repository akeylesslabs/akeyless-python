# CertificateChainInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew_certificate** | **bool** |  | [optional] 
**certificate_chain** | [**List[CertificateInfo]**](CertificateInfo.md) |  | [optional] 
**certificate_format** | **str** |  | [optional] 
**certificate_has_private_key** | **bool** |  | [optional] 
**certificate_issuer_gw_cluster_id** | **int** |  | [optional] 
**certificate_issuer_gw_cluster_url** | **str** |  | [optional] 
**certificate_issuer_item_id** | **int** |  | [optional] 
**certificate_issuer_name** | **str** |  | [optional] 
**certificate_pem** | **str** |  | [optional] 
**certificate_status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**expiration_events** | [**List[CertificateExpirationEvent]**](CertificateExpirationEvent.md) |  | [optional] 
**renew_before_expiration_in_days** | **int** |  | [optional] 

## Example

```python
from akeyless.models.certificate_chain_info import CertificateChainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateChainInfo from a JSON string
certificate_chain_info_instance = CertificateChainInfo.from_json(json)
# print the JSON string representation of the object
print(CertificateChainInfo.to_json())

# convert the object into a dict
certificate_chain_info_dict = certificate_chain_info_instance.to_dict()
# create an instance of CertificateChainInfo from a dict
certificate_chain_info_from_dict = CertificateChainInfo.from_dict(certificate_chain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



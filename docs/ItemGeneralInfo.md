# ItemGeneralInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issue_details** | [**CertificateIssueInfo**](CertificateIssueInfo.md) |  | [optional] 
**certificate_chain_info** | [**CertificateChainInfo**](CertificateChainInfo.md) |  | [optional] 
**certificate_format** | **str** |  | [optional] 
**certificates_template_info** | [**CertificateTemplateInfo**](CertificateTemplateInfo.md) |  | [optional] 
**classic_key_details** | [**ClassicKeyDetailsInfo**](ClassicKeyDetailsInfo.md) |  | [optional] 
**cluster_gw_url** | **str** |  | [optional] 
**display_metadata** | **str** |  | [optional] 
**dynamic_secret_producer_details** | [**DynamicSecretProducerInfo**](DynamicSecretProducerInfo.md) |  | [optional] 
**expiration_events** | [**List[CertificateExpirationEvent]**](CertificateExpirationEvent.md) |  | [optional] 
**importer_info** | [**ImporterInfo**](ImporterInfo.md) |  | [optional] 
**next_rotation_events** | [**List[NextAutoRotationEvent]**](NextAutoRotationEvent.md) |  | [optional] 
**oidc_client_info** | [**OidcClientInfo**](OidcClientInfo.md) |  | [optional] 
**password_policy** | [**PasswordPolicyInfo**](PasswordPolicyInfo.md) |  | [optional] 
**rotated_secret_details** | [**RotatedSecretDetailsInfo**](RotatedSecretDetailsInfo.md) |  | [optional] 
**secure_remote_access_details** | [**SecureRemoteAccess**](SecureRemoteAccess.md) |  | [optional] 
**static_secret_info** | [**StaticSecretDetailsInfo**](StaticSecretDetailsInfo.md) |  | [optional] 
**tokenizer_info** | [**TokenizerInfo**](TokenizerInfo.md) |  | [optional] 

## Example

```python
from akeyless.models.item_general_info import ItemGeneralInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ItemGeneralInfo from a JSON string
item_general_info_instance = ItemGeneralInfo.from_json(json)
# print the JSON string representation of the object
print(ItemGeneralInfo.to_json())

# convert the object into a dict
item_general_info_dict = item_general_info_instance.to_dict()
# create an instance of ItemGeneralInfo from a dict
item_general_info_from_dict = ItemGeneralInfo.from_dict(item_general_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



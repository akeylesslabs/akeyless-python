# AcmeAccount

AcmeAccount is copied without the jwk as it seems like it has issues with sdk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountId is the ACME account id, not Akeyless account id | [optional] 
**key_digest** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from akeyless.models.acme_account import AcmeAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AcmeAccount from a JSON string
acme_account_instance = AcmeAccount.from_json(json)
# print the JSON string representation of the object
print(AcmeAccount.to_json())

# convert the object into a dict
acme_account_dict = acme_account_instance.to_dict()
# create an instance of AcmeAccount from a dict
acme_account_from_dict = AcmeAccount.from_dict(acme_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



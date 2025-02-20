# DeactivateAcmeAccount

deactivateAcmeAccount is a command that Deactivates \\ Deletes an acme external account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_account_id** | **str** | The acme account id to deactivate | 
**cert_issuer_name** | **str** | The name of the PKI certificate issuer | 
**delete_account** | **bool** | Delete the account | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.deactivate_acme_account import DeactivateAcmeAccount

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivateAcmeAccount from a JSON string
deactivate_acme_account_instance = DeactivateAcmeAccount.from_json(json)
# print the JSON string representation of the object
print(DeactivateAcmeAccount.to_json())

# convert the object into a dict
deactivate_acme_account_dict = deactivate_acme_account_instance.to_dict()
# create an instance of DeactivateAcmeAccount from a dict
deactivate_acme_account_from_dict = DeactivateAcmeAccount.from_dict(deactivate_acme_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# WalletDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_type** | **str** |  | [optional] 
**p12_data_base64** | **str** |  | [optional] 
**sso_data_base64** | **str** |  | [optional] 

## Example

```python
from akeyless.models.wallet_details import WalletDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletDetails from a JSON string
wallet_details_instance = WalletDetails.from_json(json)
# print the JSON string representation of the object
print(WalletDetails.to_json())

# convert the object into a dict
wallet_details_dict = wallet_details_instance.to_dict()
# create an instance of WalletDetails from a dict
wallet_details_from_dict = WalletDetails.from_dict(wallet_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



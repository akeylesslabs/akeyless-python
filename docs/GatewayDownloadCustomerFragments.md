# GatewayDownloadCustomerFragments

gatewayDownloadCustomerFragments is a command that downloads customer fragments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_download_customer_fragments import GatewayDownloadCustomerFragments

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDownloadCustomerFragments from a JSON string
gateway_download_customer_fragments_instance = GatewayDownloadCustomerFragments.from_json(json)
# print the JSON string representation of the object
print(GatewayDownloadCustomerFragments.to_json())

# convert the object into a dict
gateway_download_customer_fragments_dict = gateway_download_customer_fragments_instance.to_dict()
# create an instance of GatewayDownloadCustomerFragments from a dict
gateway_download_customer_fragments_from_dict = GatewayDownloadCustomerFragments.from_dict(gateway_download_customer_fragments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



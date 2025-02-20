# ZeroSSLTargetDetails

ZeroSSLTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**imap_fqdn** | **str** |  | [optional] 
**imap_password** | **str** |  | [optional] 
**imap_port** | **str** |  | [optional] 
**imap_user** | **str** |  | [optional] 
**timeout** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**validation_email** | **str** |  | [optional] 

## Example

```python
from akeyless.models.zero_ssl_target_details import ZeroSSLTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ZeroSSLTargetDetails from a JSON string
zero_ssl_target_details_instance = ZeroSSLTargetDetails.from_json(json)
# print the JSON string representation of the object
print(ZeroSSLTargetDetails.to_json())

# convert the object into a dict
zero_ssl_target_details_dict = zero_ssl_target_details_instance.to_dict()
# create an instance of ZeroSSLTargetDetails from a dict
zero_ssl_target_details_from_dict = ZeroSSLTargetDetails.from_dict(zero_ssl_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



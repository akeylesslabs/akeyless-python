# WebHookNotiForwarderPublicDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**username** | **str** | Auth type - User Password | [optional] 

## Example

```python
from akeyless.models.web_hook_noti_forwarder_public_details import WebHookNotiForwarderPublicDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookNotiForwarderPublicDetails from a JSON string
web_hook_noti_forwarder_public_details_instance = WebHookNotiForwarderPublicDetails.from_json(json)
# print the JSON string representation of the object
print(WebHookNotiForwarderPublicDetails.to_json())

# convert the object into a dict
web_hook_noti_forwarder_public_details_dict = web_hook_noti_forwarder_public_details_instance.to_dict()
# create an instance of WebHookNotiForwarderPublicDetails from a dict
web_hook_noti_forwarder_public_details_from_dict = WebHookNotiForwarderPublicDetails.from_dict(web_hook_noti_forwarder_public_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



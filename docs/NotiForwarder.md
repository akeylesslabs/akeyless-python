# NotiForwarder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** |  | [optional] 
**client_id** | **str** | Auth - JWT | [optional] 
**client_permissions** | **List[str]** |  | [optional] 
**comment** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**event_types** | **List[str]** |  | [optional] 
**gateway_cluster_id** | **int** |  | [optional] 
**include_error** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**last_version** | **int** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**noti_forwarder_id** | **int** |  | [optional] 
**noti_forwarder_name** | **str** |  | [optional] 
**noti_forwarder_type** | **str** |  | [optional] 
**noti_forwarder_versions** | [**List[ItemVersion]**](ItemVersion.md) |  | [optional] 
**override_url** | **str** |  | [optional] 
**paths** | **List[str]** |  | [optional] 
**protection_key** | **str** |  | [optional] 
**runner_type** | **str** |  | [optional] 
**slack_noti_forwarder_public_details** | **object** |  | [optional] 
**timespan_in_seconds** | **int** |  | [optional] 
**to_emails** | [**List[EmailEntry]**](EmailEntry.md) |  | [optional] 
**user_email** | **str** |  | [optional] 
**username** | **str** | Auth - User Password | [optional] 
**webhook_noti_forwarder_public_details** | [**WebHookNotiForwarderPublicDetails**](WebHookNotiForwarderPublicDetails.md) |  | [optional] 
**with_customer_fragment** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.noti_forwarder import NotiForwarder

# TODO update the JSON string below
json = "{}"
# create an instance of NotiForwarder from a JSON string
noti_forwarder_instance = NotiForwarder.from_json(json)
# print the JSON string representation of the object
print(NotiForwarder.to_json())

# convert the object into a dict
noti_forwarder_dict = noti_forwarder_instance.to_dict()
# create an instance of NotiForwarder from a dict
noti_forwarder_from_dict = NotiForwarder.from_dict(noti_forwarder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



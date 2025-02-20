# UpdateRDPTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_name** | **str** | The admin name | [optional] 
**admin_pwd** | **str** | The admin password | [optional] 
**host_name** | **str** | The rdp host name | [optional] 
**host_port** | **str** | The rdp port | [optional] [default to '22']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**name** | **str** | Target name | 
**new_version** | **bool** | Deprecated | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_rdp_target_details import UpdateRDPTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRDPTargetDetails from a JSON string
update_rdp_target_details_instance = UpdateRDPTargetDetails.from_json(json)
# print the JSON string representation of the object
print(UpdateRDPTargetDetails.to_json())

# convert the object into a dict
update_rdp_target_details_dict = update_rdp_target_details_instance.to_dict()
# create an instance of UpdateRDPTargetDetails from a dict
update_rdp_target_details_from_dict = UpdateRDPTargetDetails.from_dict(update_rdp_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



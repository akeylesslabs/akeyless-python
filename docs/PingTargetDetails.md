# PingTargetDetails

PingTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_port** | **str** |  | [optional] 
**authorization_port** | **str** |  | [optional] 
**ping_url** | **str** |  | [optional] 
**privileged_user** | **str** |  | [optional] 
**user_password** | **str** |  | [optional] 

## Example

```python
from akeyless.models.ping_target_details import PingTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PingTargetDetails from a JSON string
ping_target_details_instance = PingTargetDetails.from_json(json)
# print the JSON string representation of the object
print(PingTargetDetails.to_json())

# convert the object into a dict
ping_target_details_dict = ping_target_details_instance.to_dict()
# create an instance of PingTargetDetails from a dict
ping_target_details_from_dict = PingTargetDetails.from_dict(ping_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



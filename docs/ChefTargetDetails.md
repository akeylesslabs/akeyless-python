# ChefTargetDetails

ChefTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chef_server_host_name** | **str** |  | [optional] 
**chef_server_key** | **str** |  | [optional] 
**chef_server_port** | **str** |  | [optional] 
**chef_server_url** | **str** |  | [optional] 
**chef_server_username** | **str** |  | [optional] 
**chef_skip_ssl** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.chef_target_details import ChefTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ChefTargetDetails from a JSON string
chef_target_details_instance = ChefTargetDetails.from_json(json)
# print the JSON string representation of the object
print(ChefTargetDetails.to_json())

# convert the object into a dict
chef_target_details_dict = chef_target_details_instance.to_dict()
# create an instance of ChefTargetDetails from a dict
chef_target_details_from_dict = ChefTargetDetails.from_dict(chef_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



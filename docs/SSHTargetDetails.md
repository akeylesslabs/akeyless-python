# SSHTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**private_key_password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from akeyless.models.ssh_target_details import SSHTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SSHTargetDetails from a JSON string
ssh_target_details_instance = SSHTargetDetails.from_json(json)
# print the JSON string representation of the object
print(SSHTargetDetails.to_json())

# convert the object into a dict
ssh_target_details_dict = ssh_target_details_instance.to_dict()
# create an instance of SSHTargetDetails from a dict
ssh_target_details_from_dict = SSHTargetDetails.from_dict(ssh_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



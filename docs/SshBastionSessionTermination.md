# SshBastionSessionTermination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_password** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
**api_url** | **str** |  | [optional] 
**api_username** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.ssh_bastion_session_termination import SshBastionSessionTermination

# TODO update the JSON string below
json = "{}"
# create an instance of SshBastionSessionTermination from a JSON string
ssh_bastion_session_termination_instance = SshBastionSessionTermination.from_json(json)
# print the JSON string representation of the object
print(SshBastionSessionTermination.to_json())

# convert the object into a dict
ssh_bastion_session_termination_dict = ssh_bastion_session_termination_instance.to_dict()
# create an instance of SshBastionSessionTermination from a dict
ssh_bastion_session_termination_from_dict = SshBastionSessionTermination.from_dict(ssh_bastion_session_termination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



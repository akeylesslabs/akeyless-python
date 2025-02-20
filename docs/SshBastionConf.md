# SshBastionConf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hide_session_recording** | **bool** |  | [optional] 
**kexalgs** | **str** |  | [optional] 
**log_forwarding** | [**LogForwardingConfigPart**](LogForwardingConfigPart.md) |  | [optional] 
**session_termination** | [**SshBastionSessionTermination**](SshBastionSessionTermination.md) |  | [optional] 

## Example

```python
from akeyless.models.ssh_bastion_conf import SshBastionConf

# TODO update the JSON string below
json = "{}"
# create an instance of SshBastionConf from a JSON string
ssh_bastion_conf_instance = SshBastionConf.from_json(json)
# print the JSON string representation of the object
print(SshBastionConf.to_json())

# convert the object into a dict
ssh_bastion_conf_dict = ssh_bastion_conf_instance.to_dict()
# create an instance of SshBastionConf from a dict
ssh_bastion_conf_from_dict = SshBastionConf.from_dict(ssh_bastion_conf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



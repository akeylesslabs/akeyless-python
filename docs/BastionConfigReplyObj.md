# BastionConfigReplyObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_gateway_url** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**gator_cluster_id** | **int** |  | [optional] 
**var_global** | [**BastionGlobalConf**](BastionGlobalConf.md) |  | [optional] 
**ssh_bastion** | [**SshBastionConf**](SshBastionConf.md) |  | [optional] 
**web_bastion** | [**WebBastionConf**](WebBastionConf.md) |  | [optional] 

## Example

```python
from akeyless.models.bastion_config_reply_obj import BastionConfigReplyObj

# TODO update the JSON string below
json = "{}"
# create an instance of BastionConfigReplyObj from a JSON string
bastion_config_reply_obj_instance = BastionConfigReplyObj.from_json(json)
# print the JSON string representation of the object
print(BastionConfigReplyObj.to_json())

# convert the object into a dict
bastion_config_reply_obj_dict = bastion_config_reply_obj_instance.to_dict()
# create an instance of BastionConfigReplyObj from a dict
bastion_config_reply_obj_from_dict = BastionConfigReplyObj.from_dict(bastion_config_reply_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



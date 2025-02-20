# WebBastionConf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guacamole** | [**WebBastionGuacamole**](WebBastionGuacamole.md) |  | [optional] 
**rdp_record** | [**WebBastionRdpRecord**](WebBastionRdpRecord.md) |  | [optional] 

## Example

```python
from akeyless.models.web_bastion_conf import WebBastionConf

# TODO update the JSON string below
json = "{}"
# create an instance of WebBastionConf from a JSON string
web_bastion_conf_instance = WebBastionConf.from_json(json)
# print the JSON string representation of the object
print(WebBastionConf.to_json())

# convert the object into a dict
web_bastion_conf_dict = web_bastion_conf_instance.to_dict()
# create an instance of WebBastionConf from a dict
web_bastion_conf_from_dict = WebBastionConf.from_dict(web_bastion_conf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



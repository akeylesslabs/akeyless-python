# BastionGlobalConf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_bastion_urls** | **List[str]** |  | [optional] 
**legacy_signing_alg** | **bool** |  | [optional] 
**rdp_username_sub_claim** | **str** |  | [optional] 
**ssh_username_sub_claim** | **str** |  | [optional] 

## Example

```python
from akeyless.models.bastion_global_conf import BastionGlobalConf

# TODO update the JSON string below
json = "{}"
# create an instance of BastionGlobalConf from a JSON string
bastion_global_conf_instance = BastionGlobalConf.from_json(json)
# print the JSON string representation of the object
print(BastionGlobalConf.to_json())

# convert the object into a dict
bastion_global_conf_dict = bastion_global_conf_instance.to_dict()
# create an instance of BastionGlobalConf from a dict
bastion_global_conf_from_dict = BastionGlobalConf.from_dict(bastion_global_conf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



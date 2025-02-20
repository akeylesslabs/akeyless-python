# KmipClientSetRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **List[str]** | Access capabilities | 
**client_id** | **str** |  | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** |  | [optional] 
**path** | **str** | Access path | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_client_set_rule import KmipClientSetRule

# TODO update the JSON string below
json = "{}"
# create an instance of KmipClientSetRule from a JSON string
kmip_client_set_rule_instance = KmipClientSetRule.from_json(json)
# print the JSON string representation of the object
print(KmipClientSetRule.to_json())

# convert the object into a dict
kmip_client_set_rule_dict = kmip_client_set_rule_instance.to_dict()
# create an instance of KmipClientSetRule from a dict
kmip_client_set_rule_from_dict = KmipClientSetRule.from_dict(kmip_client_set_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



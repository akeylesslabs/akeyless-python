# CFConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_fragements** | **Dict[str, str]** |  | [optional] 

## Example

```python
from akeyless.models.cf_config_part import CFConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of CFConfigPart from a JSON string
cf_config_part_instance = CFConfigPart.from_json(json)
# print the JSON string representation of the object
print(CFConfigPart.to_json())

# convert the object into a dict
cf_config_part_dict = cf_config_part_instance.to_dict()
# create an instance of CFConfigPart from a dict
cf_config_part_from_dict = CFConfigPart.from_dict(cf_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



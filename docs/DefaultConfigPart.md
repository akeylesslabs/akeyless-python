# DefaultConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_access_id** | **str** |  | [optional] 
**default_protection_key_id** | **int** |  | [optional] 
**default_secret_location** | **str** |  | [optional] 
**oidc_access_id** | **str** |  | [optional] 
**saml_access_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.default_config_part import DefaultConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultConfigPart from a JSON string
default_config_part_instance = DefaultConfigPart.from_json(json)
# print the JSON string representation of the object
print(DefaultConfigPart.to_json())

# convert the object into a dict
default_config_part_dict = default_config_part_instance.to_dict()
# create an instance of DefaultConfigPart from a dict
default_config_part_from_dict = DefaultConfigPart.from_dict(default_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



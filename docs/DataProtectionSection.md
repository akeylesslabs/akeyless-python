# DataProtectionSection

We need the fields to be pointers as we use the same struct for partial updates as well

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_classic_key_protection** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.data_protection_section import DataProtectionSection

# TODO update the JSON string below
json = "{}"
# create an instance of DataProtectionSection from a JSON string
data_protection_section_instance = DataProtectionSection.from_json(json)
# print the JSON string representation of the object
print(DataProtectionSection.to_json())

# convert the object into a dict
data_protection_section_dict = data_protection_section_instance.to_dict()
# create an instance of DataProtectionSection from a dict
data_protection_section_from_dict = DataProtectionSection.from_dict(data_protection_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



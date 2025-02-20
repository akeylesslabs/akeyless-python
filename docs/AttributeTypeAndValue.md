# AttributeTypeAndValue

AttributeTypeAndValue mirrors the ASN.1 structure of the same name in RFC 5280, Section 4.1.2.4.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[int]** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from akeyless.models.attribute_type_and_value import AttributeTypeAndValue

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeTypeAndValue from a JSON string
attribute_type_and_value_instance = AttributeTypeAndValue.from_json(json)
# print the JSON string representation of the object
print(AttributeTypeAndValue.to_json())

# convert the object into a dict
attribute_type_and_value_dict = attribute_type_and_value_instance.to_dict()
# create an instance of AttributeTypeAndValue from a dict
attribute_type_and_value_from_dict = AttributeTypeAndValue.from_dict(attribute_type_and_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



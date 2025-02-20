# Name

Name represents an X.509 distinguished name. This only includes the common elements of a DN. Note that Name is only an approximation of the X.509 structure. If an accurate representation is needed, asn1.Unmarshal the raw subject or issuer as an [RDNSequence].

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **List[str]** |  | [optional] 
**extra_names** | [**List[AttributeTypeAndValue]**](AttributeTypeAndValue.md) | ExtraNames contains attributes to be copied, raw, into any marshaled distinguished names. Values override any attributes with the same OID. The ExtraNames field is not populated when parsing, see Names. | [optional] 
**locality** | **List[str]** |  | [optional] 
**names** | [**List[AttributeTypeAndValue]**](AttributeTypeAndValue.md) | Names contains all parsed attributes. When parsing distinguished names, this can be used to extract non-standard attributes that are not parsed by this package. When marshaling to RDNSequences, the Names field is ignored, see ExtraNames. | [optional] 
**serial_number** | **str** |  | [optional] 
**street_address** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.name import Name

# TODO update the JSON string below
json = "{}"
# create an instance of Name from a JSON string
name_instance = Name.from_json(json)
# print the JSON string representation of the object
print(Name.to_json())

# convert the object into a dict
name_dict = name_instance.to_dict()
# create an instance of Name from a dict
name_from_dict = Name.from_dict(name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



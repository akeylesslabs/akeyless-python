# SAMLAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.saml_attribute import SAMLAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLAttribute from a JSON string
saml_attribute_instance = SAMLAttribute.from_json(json)
# print the JSON string representation of the object
print(SAMLAttribute.to_json())

# convert the object into a dict
saml_attribute_dict = saml_attribute_instance.to_dict()
# create an instance of SAMLAttribute from a dict
saml_attribute_from_dict = SAMLAttribute.from_dict(saml_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



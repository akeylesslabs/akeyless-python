# UniversalIdentityDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_depth** | **int** |  | [optional] 
**number_of_tokens** | **int** |  | [optional] 
**root** | [**UIDTokenDetails**](UIDTokenDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.universal_identity_details import UniversalIdentityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UniversalIdentityDetails from a JSON string
universal_identity_details_instance = UniversalIdentityDetails.from_json(json)
# print the JSON string representation of the object
print(UniversalIdentityDetails.to_json())

# convert the object into a dict
universal_identity_details_dict = universal_identity_details_instance.to_dict()
# create an instance of UniversalIdentityDetails from a dict
universal_identity_details_from_dict = UniversalIdentityDetails.from_dict(universal_identity_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



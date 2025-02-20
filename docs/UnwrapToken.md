# UnwrapToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**shared_token** | **str** | The shared token | 

## Example

```python
from akeyless.models.unwrap_token import UnwrapToken

# TODO update the JSON string below
json = "{}"
# create an instance of UnwrapToken from a JSON string
unwrap_token_instance = UnwrapToken.from_json(json)
# print the JSON string representation of the object
print(UnwrapToken.to_json())

# convert the object into a dict
unwrap_token_dict = unwrap_token_instance.to_dict()
# create an instance of UnwrapToken from a dict
unwrap_token_from_dict = UnwrapToken.from_dict(unwrap_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



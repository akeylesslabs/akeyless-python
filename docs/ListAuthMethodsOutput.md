# ListAuthMethodsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_methods** | [**List[AuthMethod]**](AuthMethod.md) |  | [optional] 
**next_page** | **str** |  | [optional] 

## Example

```python
from akeyless.models.list_auth_methods_output import ListAuthMethodsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuthMethodsOutput from a JSON string
list_auth_methods_output_instance = ListAuthMethodsOutput.from_json(json)
# print the JSON string representation of the object
print(ListAuthMethodsOutput.to_json())

# convert the object into a dict
list_auth_methods_output_dict = list_auth_methods_output_instance.to_dict()
# create an instance of ListAuthMethodsOutput from a dict
list_auth_methods_output_from_dict = ListAuthMethodsOutput.from_dict(list_auth_methods_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



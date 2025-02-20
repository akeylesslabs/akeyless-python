# GetRotatedSecretValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Get rotated secret value of specific Host (relevant only for Linked Target) | [optional] 
**ignore_cache** | **str** | Retrieve the Secret value without checking the Gateway&#39;s cache [true/false]. This flag is only relevant when using the RestAPI | [optional] [default to 'false']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**names** | **str** | Secret name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Secret version | [optional] 

## Example

```python
from akeyless.models.get_rotated_secret_value import GetRotatedSecretValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetRotatedSecretValue from a JSON string
get_rotated_secret_value_instance = GetRotatedSecretValue.from_json(json)
# print the JSON string representation of the object
print(GetRotatedSecretValue.to_json())

# convert the object into a dict
get_rotated_secret_value_dict = get_rotated_secret_value_instance.to_dict()
# create an instance of GetRotatedSecretValue from a dict
get_rotated_secret_value_from_dict = GetRotatedSecretValue.from_dict(get_rotated_secret_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



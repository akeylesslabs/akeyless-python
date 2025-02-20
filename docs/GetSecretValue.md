# GetSecretValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**ignore_cache** | **str** | Retrieve the Secret value without checking the Gateway&#39;s cache [true/false]. This flag is only relevant when using the RestAPI | [optional] [default to 'false']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**names** | **List[str]** | Secret name | 
**pretty_print** | **bool** | Print the secret value with json-pretty-print (not relevent to SDK) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Secret version, if negative value N is provided the last N versions will return (maximum 20) | [optional] 

## Example

```python
from akeyless.models.get_secret_value import GetSecretValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetSecretValue from a JSON string
get_secret_value_instance = GetSecretValue.from_json(json)
# print the JSON string representation of the object
print(GetSecretValue.to_json())

# convert the object into a dict
get_secret_value_dict = get_secret_value_instance.to_dict()
# create an instance of GetSecretValue from a dict
get_secret_value_from_dict = GetSecretValue.from_dict(get_secret_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



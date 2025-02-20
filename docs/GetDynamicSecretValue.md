# GetDynamicSecretValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** | Optional arguments as key&#x3D;value pairs or JSON strings, e.g - \\\&quot;--args&#x3D;csr&#x3D;base64_encoded_csr --args&#x3D;common_name&#x3D;bar\\\&quot; or args&#x3D;&#39;{\\\&quot;csr\\\&quot;:\\\&quot;base64_encoded_csr\\\&quot;}. It is possible to combine both formats.&#39; | [optional] 
**host** | **str** | Host | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**target** | **str** | Target Name | [optional] 
**timeout** | **int** | Timeout in seconds | [optional] [default to 15]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_dynamic_secret_value import GetDynamicSecretValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetDynamicSecretValue from a JSON string
get_dynamic_secret_value_instance = GetDynamicSecretValue.from_json(json)
# print the JSON string representation of the object
print(GetDynamicSecretValue.to_json())

# convert the object into a dict
get_dynamic_secret_value_dict = get_dynamic_secret_value_instance.to_dict()
# create an instance of GetDynamicSecretValue from a dict
get_dynamic_secret_value_from_dict = GetDynamicSecretValue.from_dict(get_dynamic_secret_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



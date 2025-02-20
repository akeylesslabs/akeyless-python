# CreateAuthMethodSAMLOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_auth_method_saml_output import CreateAuthMethodSAMLOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodSAMLOutput from a JSON string
create_auth_method_saml_output_instance = CreateAuthMethodSAMLOutput.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodSAMLOutput.to_json())

# convert the object into a dict
create_auth_method_saml_output_dict = create_auth_method_saml_output_instance.to_dict()
# create an instance of CreateAuthMethodSAMLOutput from a dict
create_auth_method_saml_output_from_dict = CreateAuthMethodSAMLOutput.from_dict(create_auth_method_saml_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



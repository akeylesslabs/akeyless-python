# CreateAuthMethodOIDCOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_auth_method_oidc_output import CreateAuthMethodOIDCOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodOIDCOutput from a JSON string
create_auth_method_oidc_output_instance = CreateAuthMethodOIDCOutput.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodOIDCOutput.to_json())

# convert the object into a dict
create_auth_method_oidc_output_dict = create_auth_method_oidc_output_instance.to_dict()
# create an instance of CreateAuthMethodOIDCOutput from a dict
create_auth_method_oidc_output_from_dict = CreateAuthMethodOIDCOutput.from_dict(create_auth_method_oidc_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



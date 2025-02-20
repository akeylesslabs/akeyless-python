# CreateOidcAppOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_oidc_app_output import CreateOidcAppOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOidcAppOutput from a JSON string
create_oidc_app_output_instance = CreateOidcAppOutput.from_json(json)
# print the JSON string representation of the object
print(CreateOidcAppOutput.to_json())

# convert the object into a dict
create_oidc_app_output_dict = create_oidc_app_output_instance.to_dict()
# create an instance of CreateOidcAppOutput from a dict
create_oidc_app_output_from_dict = CreateOidcAppOutput.from_dict(create_oidc_app_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



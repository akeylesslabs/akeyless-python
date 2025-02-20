# RotateOidcClientOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_secret** | **str** |  | [optional] 

## Example

```python
from akeyless.models.rotate_oidc_client_output import RotateOidcClientOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RotateOidcClientOutput from a JSON string
rotate_oidc_client_output_instance = RotateOidcClientOutput.from_json(json)
# print the JSON string representation of the object
print(RotateOidcClientOutput.to_json())

# convert the object into a dict
rotate_oidc_client_output_dict = rotate_oidc_client_output_instance.to_dict()
# create an instance of RotateOidcClientOutput from a dict
rotate_oidc_client_output_from_dict = RotateOidcClientOutput.from_dict(rotate_oidc_client_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



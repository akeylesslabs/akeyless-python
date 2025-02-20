# StaticCredsAuthOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from akeyless.models.static_creds_auth_output import StaticCredsAuthOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StaticCredsAuthOutput from a JSON string
static_creds_auth_output_instance = StaticCredsAuthOutput.from_json(json)
# print the JSON string representation of the object
print(StaticCredsAuthOutput.to_json())

# convert the object into a dict
static_creds_auth_output_dict = static_creds_auth_output_instance.to_dict()
# create an instance of StaticCredsAuthOutput from a dict
static_creds_auth_output_from_dict = StaticCredsAuthOutput.from_dict(static_creds_auth_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



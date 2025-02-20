# StaticCredsAuth

staticCredsAuth is a command that creates a temporary access profile using the provided static credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Akeyless JWT token | [optional] 
**admin_email** | **str** | Akeyless JWT token | [optional] 
**creds** | **str** | Akeyless JWT token | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]

## Example

```python
from akeyless.models.static_creds_auth import StaticCredsAuth

# TODO update the JSON string below
json = "{}"
# create an instance of StaticCredsAuth from a JSON string
static_creds_auth_instance = StaticCredsAuth.from_json(json)
# print the JSON string representation of the object
print(StaticCredsAuth.to_json())

# convert the object into a dict
static_creds_auth_dict = static_creds_auth_instance.to_dict()
# create an instance of StaticCredsAuth from a dict
static_creds_auth_from_dict = StaticCredsAuth.from_dict(static_creds_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



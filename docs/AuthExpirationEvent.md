# AuthExpirationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds_before** | **int** |  | [optional] 

## Example

```python
from akeyless.models.auth_expiration_event import AuthExpirationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthExpirationEvent from a JSON string
auth_expiration_event_instance = AuthExpirationEvent.from_json(json)
# print the JSON string representation of the object
print(AuthExpirationEvent.to_json())

# convert the object into a dict
auth_expiration_event_dict = auth_expiration_event_instance.to_dict()
# create an instance of AuthExpirationEvent from a dict
auth_expiration_event_from_dict = AuthExpirationEvent.from_dict(auth_expiration_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



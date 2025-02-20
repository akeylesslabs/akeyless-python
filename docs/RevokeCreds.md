# RevokeCreds

revokeCreds will permanently revoke the credentials associated with the provided token or profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.revoke_creds import RevokeCreds

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeCreds from a JSON string
revoke_creds_instance = RevokeCreds.from_json(json)
# print the JSON string representation of the object
print(RevokeCreds.to_json())

# convert the object into a dict
revoke_creds_dict = revoke_creds_instance.to_dict()
# create an instance of RevokeCreds from a dict
revoke_creds_from_dict = RevokeCreds.from_dict(revoke_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



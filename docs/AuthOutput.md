# AuthOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete_auth_link** | **str** |  | [optional] 
**creds** | [**SystemAccessCredentialsReplyObj**](SystemAccessCredentialsReplyObj.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from akeyless.models.auth_output import AuthOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AuthOutput from a JSON string
auth_output_instance = AuthOutput.from_json(json)
# print the JSON string representation of the object
print(AuthOutput.to_json())

# convert the object into a dict
auth_output_dict = auth_output_instance.to_dict()
# create an instance of AuthOutput from a dict
auth_output_from_dict = AuthOutput.from_dict(auth_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



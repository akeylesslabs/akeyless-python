# UidRotateToken

uidRotateToken is a command that rotates an Akeyless Universal Identity token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fork** | **bool** | Create a new child token with default parameters | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**send_manual_ack_token** | **str** | The new rotated token to send manual ack for (with uid-token&#x3D;the-orig-token) | [optional] 
**uid_token** | **str** | The Universal identity token | [optional] 
**with_manual_ack** | **bool** | Disable automatic ack | [optional] 

## Example

```python
from akeyless.models.uid_rotate_token import UidRotateToken

# TODO update the JSON string below
json = "{}"
# create an instance of UidRotateToken from a JSON string
uid_rotate_token_instance = UidRotateToken.from_json(json)
# print the JSON string representation of the object
print(UidRotateToken.to_json())

# convert the object into a dict
uid_rotate_token_dict = uid_rotate_token_instance.to_dict()
# create an instance of UidRotateToken from a dict
uid_rotate_token_from_dict = UidRotateToken.from_dict(uid_rotate_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



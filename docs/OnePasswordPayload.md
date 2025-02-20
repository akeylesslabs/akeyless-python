# OnePasswordPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vaults** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.one_password_payload import OnePasswordPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OnePasswordPayload from a JSON string
one_password_payload_instance = OnePasswordPayload.from_json(json)
# print the JSON string representation of the object
print(OnePasswordPayload.to_json())

# convert the object into a dict
one_password_payload_dict = one_password_payload_instance.to_dict()
# create an instance of OnePasswordPayload from a dict
one_password_payload_from_dict = OnePasswordPayload.from_dict(one_password_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



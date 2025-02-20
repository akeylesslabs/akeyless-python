# UIDTokenDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**Dict[str, UIDTokenDetails]**](UIDTokenDetails.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**deny_inheritance** | **bool** |  | [optional] 
**deny_rotate** | **bool** |  | [optional] 
**depth** | **int** |  | [optional] 
**expired_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_rotate** | **str** |  | [optional] 
**revoked** | **bool** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from akeyless.models.uid_token_details import UIDTokenDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UIDTokenDetails from a JSON string
uid_token_details_instance = UIDTokenDetails.from_json(json)
# print the JSON string representation of the object
print(UIDTokenDetails.to_json())

# convert the object into a dict
uid_token_details_dict = uid_token_details_instance.to_dict()
# create an instance of UIDTokenDetails from a dict
uid_token_details_from_dict = UIDTokenDetails.from_dict(uid_token_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



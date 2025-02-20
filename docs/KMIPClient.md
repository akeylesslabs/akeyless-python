# KMIPClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_keys_on_creation** | **bool** |  | [optional] 
**certificate_issue_date** | **datetime** |  | [optional] 
**certificate_ttl_in_seconds** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rules** | [**List[PathRule]**](PathRule.md) |  | [optional] 

## Example

```python
from akeyless.models.kmip_client import KMIPClient

# TODO update the JSON string below
json = "{}"
# create an instance of KMIPClient from a JSON string
kmip_client_instance = KMIPClient.from_json(json)
# print the JSON string representation of the object
print(KMIPClient.to_json())

# convert the object into a dict
kmip_client_dict = kmip_client_instance.to_dict()
# create an instance of KMIPClient from a dict
kmip_client_from_dict = KMIPClient.from_dict(kmip_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



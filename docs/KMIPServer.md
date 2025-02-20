# KMIPServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**ca** | **List[int]** |  | [optional] 
**certificate** | **List[int]** |  | [optional] 
**certificate_issue_date** | **datetime** |  | [optional] 
**certificate_ttl_in_seconds** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**root** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kmip_server import KMIPServer

# TODO update the JSON string below
json = "{}"
# create an instance of KMIPServer from a JSON string
kmip_server_instance = KMIPServer.from_json(json)
# print the JSON string representation of the object
print(KMIPServer.to_json())

# convert the object into a dict
kmip_server_dict = kmip_server_instance.to_dict()
# create an instance of KMIPServer from a dict
kmip_server_from_dict = KMIPServer.from_dict(kmip_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



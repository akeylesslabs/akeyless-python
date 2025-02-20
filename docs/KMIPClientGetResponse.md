# KMIPClientGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**KMIPClient**](KMIPClient.md) |  | [optional] 

## Example

```python
from akeyless.models.kmip_client_get_response import KMIPClientGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KMIPClientGetResponse from a JSON string
kmip_client_get_response_instance = KMIPClientGetResponse.from_json(json)
# print the JSON string representation of the object
print(KMIPClientGetResponse.to_json())

# convert the object into a dict
kmip_client_get_response_dict = kmip_client_get_response_instance.to_dict()
# create an instance of KMIPClientGetResponse from a dict
kmip_client_get_response_from_dict = KMIPClientGetResponse.from_dict(kmip_client_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



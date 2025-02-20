# AzurePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**tenant** | **str** |  | [optional] 

## Example

```python
from akeyless.models.azure_payload import AzurePayload

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePayload from a JSON string
azure_payload_instance = AzurePayload.from_json(json)
# print the JSON string representation of the object
print(AzurePayload.to_json())

# convert the object into a dict
azure_payload_dict = azure_payload_instance.to_dict()
# create an instance of AzurePayload from a dict
azure_payload_from_dict = AzurePayload.from_dict(azure_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



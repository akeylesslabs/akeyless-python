# HashiPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_as_json** | **bool** |  | [optional] 
**namespaces** | **List[str]** |  | [optional] 
**token** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.hashi_payload import HashiPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HashiPayload from a JSON string
hashi_payload_instance = HashiPayload.from_json(json)
# print the JSON string representation of the object
print(HashiPayload.to_json())

# convert the object into a dict
hashi_payload_dict = hashi_payload_instance.to_dict()
# create an instance of HashiPayload from a dict
hashi_payload_from_dict = HashiPayload.from_dict(hashi_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GCPPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_credentials_json** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gcp_payload import GCPPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GCPPayload from a JSON string
gcp_payload_instance = GCPPayload.from_json(json)
# print the JSON string representation of the object
print(GCPPayload.to_json())

# convert the object into a dict
gcp_payload_dict = gcp_payload_instance.to_dict()
# create an instance of GCPPayload from a dict
gcp_payload_from_dict = GCPPayload.from_dict(gcp_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



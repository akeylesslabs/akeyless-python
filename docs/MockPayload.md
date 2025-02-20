# MockPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vaults** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.mock_payload import MockPayload

# TODO update the JSON string below
json = "{}"
# create an instance of MockPayload from a JSON string
mock_payload_instance = MockPayload.from_json(json)
# print the JSON string representation of the object
print(MockPayload.to_json())

# convert the object into a dict
mock_payload_dict = mock_payload_instance.to_dict()
# create an instance of MockPayload from a dict
mock_payload_from_dict = MockPayload.from_dict(mock_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



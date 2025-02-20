# ListSraSessionsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_gateways** | [**List[GatewayNameInfo]**](GatewayNameInfo.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**sessions** | [**List[SraSessionEntryOut]**](SraSessionEntryOut.md) |  | [optional] 

## Example

```python
from akeyless.models.list_sra_sessions_output import ListSraSessionsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListSraSessionsOutput from a JSON string
list_sra_sessions_output_instance = ListSraSessionsOutput.from_json(json)
# print the JSON string representation of the object
print(ListSraSessionsOutput.to_json())

# convert the object into a dict
list_sra_sessions_output_dict = list_sra_sessions_output_instance.to_dict()
# create an instance of ListSraSessionsOutput from a dict
list_sra_sessions_output_from_dict = ListSraSessionsOutput.from_dict(list_sra_sessions_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



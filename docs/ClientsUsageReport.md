# ClientsUsageReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**clients** | [**List[ClientUsageInfo]**](ClientUsageInfo.md) |  | [optional] 
**product** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**total_clients** | **int** |  | [optional] 

## Example

```python
from akeyless.models.clients_usage_report import ClientsUsageReport

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsUsageReport from a JSON string
clients_usage_report_instance = ClientsUsageReport.from_json(json)
# print the JSON string representation of the object
print(ClientsUsageReport.to_json())

# convert the object into a dict
clients_usage_report_dict = clients_usage_report_instance.to_dict()
# create an instance of ClientsUsageReport from a dict
clients_usage_report_from_dict = ClientsUsageReport.from_dict(clients_usage_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UsageReportSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients_by_auth_method_types** | **Dict[str, int]** |  | [optional] 
**product** | **str** |  | [optional] 
**secrets_by_types** | **Dict[str, int]** |  | [optional] 
**time** | **int** |  | [optional] 
**total_clients** | **int** |  | [optional] 
**total_secrets** | **int** |  | [optional] 

## Example

```python
from akeyless.models.usage_report_summary import UsageReportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportSummary from a JSON string
usage_report_summary_instance = UsageReportSummary.from_json(json)
# print the JSON string representation of the object
print(UsageReportSummary.to_json())

# convert the object into a dict
usage_report_summary_dict = usage_report_summary_instance.to_dict()
# create an instance of UsageReportSummary from a dict
usage_report_summary_from_dict = UsageReportSummary.from_dict(usage_report_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



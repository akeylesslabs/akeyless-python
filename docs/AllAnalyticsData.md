# AllAnalyticsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics_data** | **Dict[str, List[List[str]]]** |  | [optional] 
**certificates_expiry_data** | [**CertificateAnalyticAggregation**](CertificateAnalyticAggregation.md) |  | [optional] 
**clients_usage_reports** | [**Dict[str, ClientsUsageReport]**](ClientsUsageReport.md) |  | [optional] 
**date_updated** | **int** |  | [optional] 
**usage_reports** | [**Dict[str, UsageReportSummary]**](UsageReportSummary.md) |  | [optional] 

## Example

```python
from akeyless.models.all_analytics_data import AllAnalyticsData

# TODO update the JSON string below
json = "{}"
# create an instance of AllAnalyticsData from a JSON string
all_analytics_data_instance = AllAnalyticsData.from_json(json)
# print the JSON string representation of the object
print(AllAnalyticsData.to_json())

# convert the object into a dict
all_analytics_data_dict = all_analytics_data_instance.to_dict()
# create an instance of AllAnalyticsData from a dict
all_analytics_data_from_dict = AllAnalyticsData.from_dict(all_analytics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



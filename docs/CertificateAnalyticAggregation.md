# CertificateAnalyticAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**ca_counts** | **Dict[str, int]** |  | [optional] 
**risk_counts** | **Dict[str, int]** |  | [optional] 

## Example

```python
from akeyless.models.certificate_analytic_aggregation import CertificateAnalyticAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateAnalyticAggregation from a JSON string
certificate_analytic_aggregation_instance = CertificateAnalyticAggregation.from_json(json)
# print the JSON string representation of the object
print(CertificateAnalyticAggregation.to_json())

# convert the object into a dict
certificate_analytic_aggregation_dict = certificate_analytic_aggregation_instance.to_dict()
# create an instance of CertificateAnalyticAggregation from a dict
certificate_analytic_aggregation_from_dict = CertificateAnalyticAggregation.from_dict(certificate_analytic_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



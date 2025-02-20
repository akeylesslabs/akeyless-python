# GetAnalyticsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_analytics_data import GetAnalyticsData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnalyticsData from a JSON string
get_analytics_data_instance = GetAnalyticsData.from_json(json)
# print the JSON string representation of the object
print(GetAnalyticsData.to_json())

# convert the object into a dict
get_analytics_data_dict = get_analytics_data_instance.to_dict()
# create an instance of GetAnalyticsData from a dict
get_analytics_data_from_dict = GetAnalyticsData.from_dict(get_analytics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



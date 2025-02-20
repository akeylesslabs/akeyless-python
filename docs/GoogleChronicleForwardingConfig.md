# GoogleChronicleForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**log_type** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**service_account_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.google_chronicle_forwarding_config import GoogleChronicleForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleChronicleForwardingConfig from a JSON string
google_chronicle_forwarding_config_instance = GoogleChronicleForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(GoogleChronicleForwardingConfig.to_json())

# convert the object into a dict
google_chronicle_forwarding_config_dict = google_chronicle_forwarding_config_instance.to_dict()
# create an instance of GoogleChronicleForwardingConfig from a dict
google_chronicle_forwarding_config_from_dict = GoogleChronicleForwardingConfig.from_dict(google_chronicle_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



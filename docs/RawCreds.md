# RawCreds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.raw_creds import RawCreds

# TODO update the JSON string below
json = "{}"
# create an instance of RawCreds from a JSON string
raw_creds_instance = RawCreds.from_json(json)
# print the JSON string representation of the object
print(RawCreds.to_json())

# convert the object into a dict
raw_creds_dict = raw_creds_instance.to_dict()
# create an instance of RawCreds from a dict
raw_creds_from_dict = RawCreds.from_dict(raw_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



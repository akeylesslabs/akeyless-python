# RefreshKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Key name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.refresh_key import RefreshKey

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshKey from a JSON string
refresh_key_instance = RefreshKey.from_json(json)
# print the JSON string representation of the object
print(RefreshKey.to_json())

# convert the object into a dict
refresh_key_dict = refresh_key_instance.to_dict()
# create an instance of RefreshKey from a dict
refresh_key_from_dict = RefreshKey.from_dict(refresh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



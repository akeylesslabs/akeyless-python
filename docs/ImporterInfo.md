# ImporterInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_item_id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from akeyless.models.importer_info import ImporterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImporterInfo from a JSON string
importer_info_instance = ImporterInfo.from_json(json)
# print the JSON string representation of the object
print(ImporterInfo.to_json())

# convert the object into a dict
importer_info_dict = importer_info_instance.to_dict()
# create an instance of ImporterInfo from a dict
importer_info_from_dict = ImporterInfo.from_dict(importer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



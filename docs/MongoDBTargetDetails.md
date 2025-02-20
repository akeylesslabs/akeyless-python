# MongoDBTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongodb_atlas_api_private_key** | **str** |  | [optional] 
**mongodb_atlas_api_public_key** | **str** |  | [optional] 
**mongodb_atlas_project_id** | **str** | mongodb atlas fields | [optional] 
**mongodb_db_name** | **str** | common fields | [optional] 
**mongodb_default_auth_db** | **str** |  | [optional] 
**mongodb_host_port** | **str** |  | [optional] 
**mongodb_is_atlas** | **bool** |  | [optional] 
**mongodb_password** | **str** |  | [optional] 
**mongodb_uri_connection** | **str** | mongodb fields | [optional] 
**mongodb_uri_options** | **str** |  | [optional] 
**mongodb_username** | **str** |  | [optional] 

## Example

```python
from akeyless.models.mongo_db_target_details import MongoDBTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBTargetDetails from a JSON string
mongo_db_target_details_instance = MongoDBTargetDetails.from_json(json)
# print the JSON string representation of the object
print(MongoDBTargetDetails.to_json())

# convert the object into a dict
mongo_db_target_details_dict = mongo_db_target_details_instance.to_dict()
# create an instance of MongoDBTargetDetails from a dict
mongo_db_target_details_from_dict = MongoDBTargetDetails.from_dict(mongo_db_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



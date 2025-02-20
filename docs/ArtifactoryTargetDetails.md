# ArtifactoryTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactory_admin_apikey** | **str** |  | [optional] 
**artifactory_admin_username** | **str** |  | [optional] 
**artifactory_base_url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.artifactory_target_details import ArtifactoryTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactoryTargetDetails from a JSON string
artifactory_target_details_instance = ArtifactoryTargetDetails.from_json(json)
# print the JSON string representation of the object
print(ArtifactoryTargetDetails.to_json())

# convert the object into a dict
artifactory_target_details_dict = artifactory_target_details_instance.to_dict()
# create an instance of ArtifactoryTargetDetails from a dict
artifactory_target_details_from_dict = ArtifactoryTargetDetails.from_dict(artifactory_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



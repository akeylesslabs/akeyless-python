# GitlabTargetDetails

GitlabTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gitlab_access_token** | **str** |  | [optional] 
**gitlab_certificate** | **str** |  | [optional] 
**gitlab_url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gitlab_target_details import GitlabTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GitlabTargetDetails from a JSON string
gitlab_target_details_instance = GitlabTargetDetails.from_json(json)
# print the JSON string representation of the object
print(GitlabTargetDetails.to_json())

# convert the object into a dict
gitlab_target_details_dict = gitlab_target_details_instance.to_dict()
# create an instance of GitlabTargetDetails from a dict
gitlab_target_details_from_dict = GitlabTargetDetails.from_dict(gitlab_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



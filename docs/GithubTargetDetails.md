# GithubTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_app_id** | **int** |  | [optional] 
**github_app_private_key** | **str** |  | [optional] 
**github_base_url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.github_target_details import GithubTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GithubTargetDetails from a JSON string
github_target_details_instance = GithubTargetDetails.from_json(json)
# print the JSON string representation of the object
print(GithubTargetDetails.to_json())

# convert the object into a dict
github_target_details_dict = github_target_details_instance.to_dict()
# create an instance of GithubTargetDetails from a dict
github_target_details_from_dict = GithubTargetDetails.from_dict(github_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



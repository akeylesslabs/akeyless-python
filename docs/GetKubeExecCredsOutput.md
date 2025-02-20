# GetKubeExecCredsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**status** | [**ClientData**](ClientData.md) |  | [optional] 

## Example

```python
from akeyless.models.get_kube_exec_creds_output import GetKubeExecCredsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetKubeExecCredsOutput from a JSON string
get_kube_exec_creds_output_instance = GetKubeExecCredsOutput.from_json(json)
# print the JSON string representation of the object
print(GetKubeExecCredsOutput.to_json())

# convert the object into a dict
get_kube_exec_creds_output_dict = get_kube_exec_creds_output_instance.to_dict()
# create an instance of GetKubeExecCredsOutput from a dict
get_kube_exec_creds_output_from_dict = GetKubeExecCredsOutput.from_dict(get_kube_exec_creds_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



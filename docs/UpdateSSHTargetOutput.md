# UpdateSSHTargetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int** |  | [optional] 

## Example

```python
from akeyless.models.update_ssh_target_output import UpdateSSHTargetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSSHTargetOutput from a JSON string
update_ssh_target_output_instance = UpdateSSHTargetOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateSSHTargetOutput.to_json())

# convert the object into a dict
update_ssh_target_output_dict = update_ssh_target_output_instance.to_dict()
# create an instance of UpdateSSHTargetOutput from a dict
update_ssh_target_output_from_dict = UpdateSSHTargetOutput.from_dict(update_ssh_target_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



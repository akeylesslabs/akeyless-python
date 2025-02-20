# CreateSSHTargetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int** |  | [optional] 

## Example

```python
from akeyless.models.create_ssh_target_output import CreateSSHTargetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSSHTargetOutput from a JSON string
create_ssh_target_output_instance = CreateSSHTargetOutput.from_json(json)
# print the JSON string representation of the object
print(CreateSSHTargetOutput.to_json())

# convert the object into a dict
create_ssh_target_output_dict = create_ssh_target_output_instance.to_dict()
# create an instance of CreateSSHTargetOutput from a dict
create_ssh_target_output_from_dict = CreateSSHTargetOutput.from_dict(create_ssh_target_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



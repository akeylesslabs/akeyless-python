# CreateEKSTargetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int** |  | [optional] 

## Example

```python
from akeyless.models.create_eks_target_output import CreateEKSTargetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEKSTargetOutput from a JSON string
create_eks_target_output_instance = CreateEKSTargetOutput.from_json(json)
# print the JSON string representation of the object
print(CreateEKSTargetOutput.to_json())

# convert the object into a dict
create_eks_target_output_dict = create_eks_target_output_instance.to_dict()
# create an instance of CreateEKSTargetOutput from a dict
create_eks_target_output_from_dict = CreateEKSTargetOutput.from_dict(create_eks_target_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



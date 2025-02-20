# CreateAWSTargetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int** |  | [optional] 

## Example

```python
from akeyless.models.create_aws_target_output import CreateAWSTargetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAWSTargetOutput from a JSON string
create_aws_target_output_instance = CreateAWSTargetOutput.from_json(json)
# print the JSON string representation of the object
print(CreateAWSTargetOutput.to_json())

# convert the object into a dict
create_aws_target_output_dict = create_aws_target_output_instance.to_dict()
# create an instance of CreateAWSTargetOutput from a dict
create_aws_target_output_from_dict = CreateAWSTargetOutput.from_dict(create_aws_target_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



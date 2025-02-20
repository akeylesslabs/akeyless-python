# RollbackSecretOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from akeyless.models.rollback_secret_output import RollbackSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackSecretOutput from a JSON string
rollback_secret_output_instance = RollbackSecretOutput.from_json(json)
# print the JSON string representation of the object
print(RollbackSecretOutput.to_json())

# convert the object into a dict
rollback_secret_output_dict = rollback_secret_output_instance.to_dict()
# create an instance of RollbackSecretOutput from a dict
rollback_secret_output_from_dict = RollbackSecretOutput.from_dict(rollback_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



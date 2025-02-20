# CreateSecretOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_secret_output import CreateSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecretOutput from a JSON string
create_secret_output_instance = CreateSecretOutput.from_json(json)
# print the JSON string representation of the object
print(CreateSecretOutput.to_json())

# convert the object into a dict
create_secret_output_dict = create_secret_output_instance.to_dict()
# create an instance of CreateSecretOutput from a dict
create_secret_output_from_dict = CreateSecretOutput.from_dict(create_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



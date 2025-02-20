# EsmListSecretsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets_list** | [**List[SecretInfo]**](SecretInfo.md) |  | [optional] 

## Example

```python
from akeyless.models.esm_list_secrets_output import EsmListSecretsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EsmListSecretsOutput from a JSON string
esm_list_secrets_output_instance = EsmListSecretsOutput.from_json(json)
# print the JSON string representation of the object
print(EsmListSecretsOutput.to_json())

# convert the object into a dict
esm_list_secrets_output_dict = esm_list_secrets_output_instance.to_dict()
# create an instance of EsmListSecretsOutput from a dict
esm_list_secrets_output_from_dict = EsmListSecretsOutput.from_dict(esm_list_secrets_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



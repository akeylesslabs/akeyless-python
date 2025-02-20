# UscListSecretsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets_list** | [**List[SecretInfo]**](SecretInfo.md) |  | [optional] 

## Example

```python
from akeyless.models.usc_list_secrets_output import UscListSecretsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UscListSecretsOutput from a JSON string
usc_list_secrets_output_instance = UscListSecretsOutput.from_json(json)
# print the JSON string representation of the object
print(UscListSecretsOutput.to_json())

# convert the object into a dict
usc_list_secrets_output_dict = usc_list_secrets_output_instance.to_dict()
# create an instance of UscListSecretsOutput from a dict
usc_list_secrets_output_from_dict = UscListSecretsOutput.from_dict(usc_list_secrets_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



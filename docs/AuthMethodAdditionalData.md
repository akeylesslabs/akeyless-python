# AuthMethodAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kerberos_data** | [**KerberosAuthMethodInfo**](KerberosAuthMethodInfo.md) |  | [optional] 

## Example

```python
from akeyless.models.auth_method_additional_data import AuthMethodAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodAdditionalData from a JSON string
auth_method_additional_data_instance = AuthMethodAdditionalData.from_json(json)
# print the JSON string representation of the object
print(AuthMethodAdditionalData.to_json())

# convert the object into a dict
auth_method_additional_data_dict = auth_method_additional_data_instance.to_dict()
# create an instance of AuthMethodAdditionalData from a dict
auth_method_additional_data_from_dict = AuthMethodAdditionalData.from_dict(auth_method_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



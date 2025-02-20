# KMIPConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**Dict[str, KMIPClient]**](KMIPClient.md) |  | [optional] 
**key_enc** | **List[int]** | Saves the private key of the cert issuer in encypted form | [optional] 
**server** | [**KMIPServer**](KMIPServer.md) |  | [optional] 
**server_enc** | **List[int]** | Saved for backward compatibility TODO: remove this after all clients upgrade | [optional] 

## Example

```python
from akeyless.models.kmip_config_part import KMIPConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of KMIPConfigPart from a JSON string
kmip_config_part_instance = KMIPConfigPart.from_json(json)
# print the JSON string representation of the object
print(KMIPConfigPart.to_json())

# convert the object into a dict
kmip_config_part_dict = kmip_config_part_instance.to_dict()
# create an instance of KMIPConfigPart from a dict
kmip_config_part_from_dict = KMIPConfigPart.from_dict(kmip_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



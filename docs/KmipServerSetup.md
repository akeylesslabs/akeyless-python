# KmipServerSetup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_ttl** | **int** | Server certificate TTL in days | [optional] [default to 90]
**hostname** | **str** | Hostname | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**root** | **str** | Root path of KMIP Resources | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_server_setup import KmipServerSetup

# TODO update the JSON string below
json = "{}"
# create an instance of KmipServerSetup from a JSON string
kmip_server_setup_instance = KmipServerSetup.from_json(json)
# print the JSON string representation of the object
print(KmipServerSetup.to_json())

# convert the object into a dict
kmip_server_setup_dict = kmip_server_setup_instance.to_dict()
# create an instance of KmipServerSetup from a dict
kmip_server_setup_from_dict = KmipServerSetup.from_dict(kmip_server_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



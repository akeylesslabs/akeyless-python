# KmipCreateClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_keys_on_creation** | **str** | If set to &#39;true&#39;, newly created keys on the client will be set to an &#39;active&#39; state | [optional] [default to 'false']
**certificate_ttl** | **int** | Client certificate TTL in days | [optional] [default to 90]
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Client name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_create_client import KmipCreateClient

# TODO update the JSON string below
json = "{}"
# create an instance of KmipCreateClient from a JSON string
kmip_create_client_instance = KmipCreateClient.from_json(json)
# print the JSON string representation of the object
print(KmipCreateClient.to_json())

# convert the object into a dict
kmip_create_client_dict = kmip_create_client_instance.to_dict()
# create an instance of KmipCreateClient from a dict
kmip_create_client_from_dict = KmipCreateClient.from_dict(kmip_create_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



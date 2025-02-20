# KmipDescribeClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_describe_client import KmipDescribeClient

# TODO update the JSON string below
json = "{}"
# create an instance of KmipDescribeClient from a JSON string
kmip_describe_client_instance = KmipDescribeClient.from_json(json)
# print the JSON string representation of the object
print(KmipDescribeClient.to_json())

# convert the object into a dict
kmip_describe_client_dict = kmip_describe_client_instance.to_dict()
# create an instance of KmipDescribeClient from a dict
kmip_describe_client_from_dict = KmipDescribeClient.from_dict(kmip_describe_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



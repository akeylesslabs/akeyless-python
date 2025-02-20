# DeleteGatewayAllowedAccessId

deleteGatewayAllowedAccessId is a command that deletes access-id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | The access id to be stripped of access to gateway | 
**cluster_name** | **str** | The name of the updated cluster, e.g. acc-abcd12345678/p-123456789012/defaultCluster | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_gateway_allowed_access_id import DeleteGatewayAllowedAccessId

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGatewayAllowedAccessId from a JSON string
delete_gateway_allowed_access_id_instance = DeleteGatewayAllowedAccessId.from_json(json)
# print the JSON string representation of the object
print(DeleteGatewayAllowedAccessId.to_json())

# convert the object into a dict
delete_gateway_allowed_access_id_dict = delete_gateway_allowed_access_id_instance.to_dict()
# create an instance of DeleteGatewayAllowedAccessId from a dict
delete_gateway_allowed_access_id_from_dict = DeleteGatewayAllowedAccessId.from_dict(delete_gateway_allowed_access_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AddGatewayAllowedAccessId

Responses:  default: errorResponse 200: addGatewayAllowedAccessIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | The access id that will be able to access to gateway | 
**cluster_name** | **str** | The name of the updated cluster, e.g. acc-abcd12345678/p-123456789012/defaultCluster | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**sub_claims** | **Dict[str, str]** | key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.add_gateway_allowed_access_id import AddGatewayAllowedAccessId

# TODO update the JSON string below
json = "{}"
# create an instance of AddGatewayAllowedAccessId from a JSON string
add_gateway_allowed_access_id_instance = AddGatewayAllowedAccessId.from_json(json)
# print the JSON string representation of the object
print(AddGatewayAllowedAccessId.to_json())

# convert the object into a dict
add_gateway_allowed_access_id_dict = add_gateway_allowed_access_id_instance.to_dict()
# create an instance of AddGatewayAllowedAccessId from a dict
add_gateway_allowed_access_id_from_dict = AddGatewayAllowedAccessId.from_dict(add_gateway_allowed_access_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



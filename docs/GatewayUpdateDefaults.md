# GatewayUpdateDefaults

gatewayUpdateDefaults is a command that updates defaults settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_access_id** | **str** | Default Certificate access id for UI login | [optional] [default to 'use-existing']
**event_on_status_change** | **str** | Trigger an event when Gateway status is changed [true/false] | [optional] 
**hvp_route_version** | **int** | Hvp route version to use [1/2] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of the gateway default encryption key | [optional] [default to 'Default']
**oidc_access_id** | **str** | Default OIDC access id for UI login | [optional] [default to 'use-existing']
**saml_access_id** | **str** | Default SAML access id for UI login | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_defaults import GatewayUpdateDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateDefaults from a JSON string
gateway_update_defaults_instance = GatewayUpdateDefaults.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateDefaults.to_json())

# convert the object into a dict
gateway_update_defaults_dict = gateway_update_defaults_instance.to_dict()
# create an instance of GatewayUpdateDefaults from a dict
gateway_update_defaults_from_dict = GatewayUpdateDefaults.from_dict(gateway_update_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GatewayCreateAllowedAccess

gatewayCreateAllowedAccess is a command that creates allowed access in Gator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_claims_case_insensitive** | **bool** |  | [optional] 
**access_id** | **str** | Access ID The access id to be attached to this allowed access. Auth method with this access id should already exist. | 
**case_sensitive** | **str** | Treat sub claims as case-sensitive [true/false] | [optional] [default to 'true']
**description** | **str** | Allowed access description | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Allowed access name | 
**permissions** | **str** | Permissions  Comma-seperated list of permissions for this allowed access. Available permissions: [defaults,targets,classic_keys,automatic_migration,ldap_auth,dynamic_secret,k8s_auth,log_forwarding,zero_knowledge_encryption,rotated_secret,caching,event_forwarding,admin,kmip,general] | [optional] 
**sub_claims** | **Dict[str, str]** | Sub claims key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_create_allowed_access import GatewayCreateAllowedAccess

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateAllowedAccess from a JSON string
gateway_create_allowed_access_instance = GatewayCreateAllowedAccess.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateAllowedAccess.to_json())

# convert the object into a dict
gateway_create_allowed_access_dict = gateway_create_allowed_access_instance.to_dict()
# create an instance of GatewayCreateAllowedAccess from a dict
gateway_create_allowed_access_from_dict = GatewayCreateAllowedAccess.from_dict(gateway_create_allowed_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OidcClientInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_permission_assignment** | [**List[AccessOrGroupPermissionAssignment]**](AccessOrGroupPermissionAssignment.md) |  | [optional] 
**audience** | **List[str]** |  | [optional] 
**client_id** | **str** |  | [optional] 
**grant_types** | **List[str]** |  | [optional] 
**issuer_url** | **str** |  | [optional] 
**logout_uris** | **List[str]** |  | [optional] 
**public** | **bool** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**response_types** | **List[str]** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.oidc_client_info import OidcClientInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OidcClientInfo from a JSON string
oidc_client_info_instance = OidcClientInfo.from_json(json)
# print the JSON string representation of the object
print(OidcClientInfo.to_json())

# convert the object into a dict
oidc_client_info_dict = oidc_client_info_instance.to_dict()
# create an instance of OidcClientInfo from a dict
oidc_client_info_from_dict = OidcClientInfo.from_dict(oidc_client_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



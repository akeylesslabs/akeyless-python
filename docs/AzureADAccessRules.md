# AzureADAccessRules

AzureADAccessRules contains access rules specific to Azure Active Directory authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_endpoint** | **str** | The audience in the JWT. | [optional] 
**bound_group_ids** | **List[str]** | The list of group ids that login is restricted to. | [optional] 
**bound_resource_groups** | **List[str]** | The list of resource groups that login is restricted to. | [optional] 
**bound_resource_ids** | **List[str]** | The list of full resource ids that the login is restricted to. | [optional] 
**bound_resource_names** | **List[str]** | The list of resource names that the login is restricted to (e.g, a virtual machine name, scale set name, etc). | [optional] 
**bound_resource_providers** | **List[str]** | The list of resource providers that login is restricted to (e.g, Microsoft.Compute, Microsoft.ManagedIdentity, etc). | [optional] 
**bound_resource_types** | **List[str]** | The list of resource types that login is restricted to  (e.g, virtualMachines, userAssignedIdentities, etc). | [optional] 
**bound_service_principal_ids** | **List[str]** | The list of service principal IDs that login is restricted to. | [optional] 
**bound_subscription_ids** | **List[str]** | The list of subscription IDs that login is restricted to. | [optional] 
**bound_tenant_id** | **str** | The tenants id for the Azure Active Directory organization. | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**jwks_uri** | **str** | The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

## Example

```python
from akeyless.models.azure_ad_access_rules import AzureADAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of AzureADAccessRules from a JSON string
azure_ad_access_rules_instance = AzureADAccessRules.from_json(json)
# print the JSON string representation of the object
print(AzureADAccessRules.to_json())

# convert the object into a dict
azure_ad_access_rules_dict = azure_ad_access_rules_instance.to_dict()
# create an instance of AzureADAccessRules from a dict
azure_ad_access_rules_from_dict = AzureADAccessRules.from_dict(azure_ad_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



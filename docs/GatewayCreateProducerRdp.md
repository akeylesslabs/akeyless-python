# GatewayCreateProducerRdp

gatewayCreateProducerRdp is a command that creates rdp producer [Deprecated: Use dynamic-secret-create-rdp command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_user_extend_session** | **int** | AllowUserExtendSession | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**fixed_user_claim_keyname** | **str** | For externally provided users, denotes the key-name of IdP claim to extract the username from (relevant only for fixed-user-only&#x3D;true) | [optional] [default to 'ext_username']
**fixed_user_only** | **str** | Allow access using externally (IdP) provided username [true/false] | [optional] [default to 'false']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**rdp_admin_name** | **str** | RDP Admin Name | [optional] 
**rdp_admin_pwd** | **str** | RDP Admin password | [optional] 
**rdp_host_name** | **str** | Hostname | [optional] 
**rdp_host_port** | **str** | Port | [optional] [default to '22']
**rdp_user_groups** | **str** | Groups | [optional] 
**secure_access_allow_external_user** | **bool** | Allow providing external user for a domain users | [optional] [default to False]
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **List[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_rd_gateway_server** | **str** | RD Gateway server | [optional] 
**secure_access_rdp_domain** | **str** | Required when the Dynamic Secret is used for a domain user | [optional] 
**secure_access_rdp_user** | **str** | Override the RDP Domain username | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**warn_user_before_expiration** | **int** | WarnBeforeUserExpiration | [optional] 

## Example

```python
from akeyless.models.gateway_create_producer_rdp import GatewayCreateProducerRdp

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerRdp from a JSON string
gateway_create_producer_rdp_instance = GatewayCreateProducerRdp.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerRdp.to_json())

# convert the object into a dict
gateway_create_producer_rdp_dict = gateway_create_producer_rdp_instance.to_dict()
# create an instance of GatewayCreateProducerRdp from a dict
gateway_create_producer_rdp_from_dict = GatewayCreateProducerRdp.from_dict(gateway_create_producer_rdp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



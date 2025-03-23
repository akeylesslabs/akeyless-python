# SecureRemoteAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**allow_port_forwarding** | **bool** |  | [optional] 
**allow_providing_external_username** | **bool** |  | [optional] 
**bastion_api** | **str** |  | [optional] 
**bastion_issuer** | **str** |  | [optional] 
**bastion_issuer_id** | **int** |  | [optional] 
**bastion_ssh** | **str** |  | [optional] 
**block_concurrent_connections** | **bool** |  | [optional] 
**block_concurrent_connections_level** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**connection_delay_seconds** | **int** |  | [optional] 
**dashboard_url** | **str** |  | [optional] 
**db_name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**enforce_hosts_restriction** | **bool** |  | [optional] 
**gw_cluster_id** | **int** |  | [optional] 
**host** | **List[str]** |  | [optional] 
**host_provider_type** | **str** |  | [optional] 
**is_cli** | **bool** |  | [optional] 
**is_web** | **bool** |  | [optional] 
**isolated** | **bool** |  | [optional] 
**native** | **bool** |  | [optional] 
**rd_gateway_server** | **str** |  | [optional] 
**rdp_user** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**rotate_after_disconnect** | **bool** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**ssh_password** | **bool** |  | [optional] 
**ssh_private_key** | **bool** |  | [optional] 
**ssh_user** | **str** |  | [optional] 
**status_info** | [**ItemSraStatus**](ItemSraStatus.md) |  | [optional] 
**target_hosts** | [**List[TargetNameWithHosts]**](TargetNameWithHosts.md) |  | [optional] 
**targets** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 
**use_internal_bastion** | **bool** |  | [optional] 
**web_proxy** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.secure_remote_access import SecureRemoteAccess

# TODO update the JSON string below
json = "{}"
# create an instance of SecureRemoteAccess from a JSON string
secure_remote_access_instance = SecureRemoteAccess.from_json(json)
# print the JSON string representation of the object
print(SecureRemoteAccess.to_json())

# convert the object into a dict
secure_remote_access_dict = secure_remote_access_instance.to_dict()
# create an instance of SecureRemoteAccess from a dict
secure_remote_access_from_dict = SecureRemoteAccess.from_dict(secure_remote_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



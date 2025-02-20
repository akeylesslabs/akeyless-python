# DbTargetDetails

DbTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_service_provider** | **str** |  | [optional] 
**cluster_mode** | **bool** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**db_client_id** | **str** |  | [optional] 
**db_client_secret** | **str** |  | [optional] 
**db_host_name** | **str** |  | [optional] 
**db_name** | **str** |  | [optional] 
**db_port** | **str** |  | [optional] 
**db_private_key** | **str** | (Optional) Private Key in PEM format | [optional] 
**db_private_key_passphrase** | **str** |  | [optional] 
**db_pwd** | **str** |  | [optional] 
**db_server_certificates** | **str** | (Optional) DBServerCertificates defines the set of root certificate authorities that clients use when verifying server certificates. If DBServerCertificates is empty, TLS uses the host&#39;s root CA set. | [optional] 
**db_server_name** | **str** | (Optional) ServerName is used to verify the hostname on the returned certificates unless InsecureSkipVerify is given. It is also included in the client&#39;s handshake to support virtual hosting unless it is an IP address. | [optional] 
**db_tenant_id** | **str** |  | [optional] 
**db_user_name** | **str** |  | [optional] 
**oracle_wallet_details** | [**WalletDetails**](WalletDetails.md) |  | [optional] 
**sf_account** | **str** |  | [optional] 
**ssl_connection_certificate** | **str** | (Optional) SSLConnectionCertificate defines the certificate for SSL connection. Must be base64 certificate loaded by UI using file loader field | [optional] 
**ssl_connection_mode** | **bool** | (Optional) SSLConnectionMode defines if SSL mode will be used to connect to DB | [optional] 

## Example

```python
from akeyless.models.db_target_details import DbTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DbTargetDetails from a JSON string
db_target_details_instance = DbTargetDetails.from_json(json)
# print the JSON string representation of the object
print(DbTargetDetails.to_json())

# convert the object into a dict
db_target_details_dict = db_target_details_instance.to_dict()
# create an instance of DbTargetDetails from a dict
db_target_details_from_dict = DbTargetDetails.from_dict(db_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



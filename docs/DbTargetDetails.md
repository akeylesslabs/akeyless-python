# DbTargetDetails

DbTargetDetails
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_certificate** | **str** | (Optional) ClientCertificate defines the client certificate for mutual TLS. Must be base64 certificate loaded by UI using file loader field | [optional] 
**client_key_passphrase** | **str** | (Optional) ClientKeyPassphrase defines the passphrase for the client private key | [optional] 
**client_private_key** | **str** | (Optional) ClientPrivateKey defines the client private key for mutual TLS. Must be base64 private key loaded by UI using file loader field | [optional] 
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
**enable_mtls** | **bool** | (Optional) EnableMTLS defines if mutual TLS will be used to connect to DB | [optional] 
**oracle_wallet_details** | [**WalletDetails**](WalletDetails.md) |  | [optional] 
**sf_account** | **str** |  | [optional] 
**skip_server_name_validation** | **str** | (Optional) SkipServerNameValidation disables server name verification while still validating the certificate chain. Postgres treats empty as legacy \&quot;skip hostname validation\&quot;; MySQL treats empty as false. | [optional] 
**ssl_connection_certificate** | **str** | (Optional) SSLConnectionCertificate defines the certificate for SSL connection. Must be base64 certificate loaded by UI using file loader field | [optional] 
**ssl_connection_mode** | **bool** | (Optional) SSLConnectionMode defines if SSL mode will be used to connect to DB | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TargetCreateAerospike

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_username** | **str** | Username of an account with the user-admin role | [optional] 
**aerospike_client_id** | **str** | Client ID for Aerospike Cloud authentication (relevant only for Aerospike Cloud) | [optional] 
**aerospike_client_secret** | **str** | Client secret for Aerospike Cloud authentication (relevant only for Aerospike Cloud) | [optional] 
**aerospike_cloud** | **bool** | Set to &#39;true&#39; for Aerospike Cloud deployments | [optional] 
**aerospike_cluster_id** | **str** | Cloud cluster ID (relevant only for Aerospike Cloud) | [optional] 
**client_certificate** | **str** | Client certificate for mTLS (mTLS only) | [optional] 
**client_private_key** | **str** | Client private key for mTLS (mTLS only) | [optional] 
**db_server_name** | **str** | TLS server name used to verify the certificate hostname. If empty, the Aerospike hostname is used. | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**enable_mtls** | **bool** | Enable mutual TLS authentication - requires --ssl&#x3D;true (true/false) | [optional] 
**hostname** | **str** | Aerospike host address and port (e.g. url.to.aerospike.db) | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**namespace** | **str** | Namespace name (relevant only for Aerospike db) | [optional] 
**password** | **str** | Password for the admin user | [optional] 
**port** | **str** | Database connection port | [optional] 
**skip_server_name_validation** | **str** | Skip server name verification while still validating the certificate chain (true/false). Empty means do not skip. | [optional] 
**ssl** | **bool** | Enable SSL encryption (true/false) | [optional] 
**ssl_certificate** | **str** | Base64-encoded SSL CA certificate from a trusted Certificate Authority (CA) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



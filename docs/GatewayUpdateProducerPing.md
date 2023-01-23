# GatewayUpdateProducerPing

gatewayUpdateProducerPing is a command that updates Ping producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**name** | **str** | Producer name | 
**new_name** | **str** | Producer New name | [optional] 
**ping_administrative_port** | **str** | Ping Federate administrative port | [optional] [default to '9999']
**ping_atm_id** | **str** | Set a specific Access Token Management (ATM) instance for the created OAuth Client by providing the ATM Id. If no explicit value is given, the default pingfederate server ATM will be set. | [optional] 
**ping_authorization_port** | **str** | Ping Federate authorization port | [optional] [default to '9031']
**ping_cert_subject_dn** | **str** | The subject DN of the client certificate. If no explicit value is given, the producer will create CA certificate and matched client certificate and return it as value. Used in conjunction with ping-issuer-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method) | [optional] 
**ping_client_authentication_type** | **str** | OAuth Client Authentication Type [CLIENT_SECRET, PRIVATE_KEY_JWT, CLIENT_TLS_CERTIFICATE] | [optional] [default to 'CLIENT_SECRET']
**ping_enforce_replay_prevention** | **str** | Determines whether PingFederate requires a unique signed JWT from the client for each action (relevant for PRIVATE_KEY_JWT authentication method) | [optional] 
**ping_grant_types** | **list[str]** | List of OAuth client grant types [IMPLICIT, AUTHORIZATION_CODE, CLIENT_CREDENTIALS, TOKEN_EXCHANGE, REFRESH_TOKEN, ASSERTION_GRANTS, PASSWORD, RESOURCE_OWNER_CREDENTIALS]. If no explicit value is given, AUTHORIZATION_CODE will be selected as default. | [optional] 
**ping_issuer_dn** | **str** | Issuer DN of trusted CA certificate that imported into Ping Federate server. You may select \\\&quot;Trust Any\\\&quot; to trust all the existing issuers in Ping Federate server. Used in conjunction with ping-cert-subject-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method) | [optional] 
**ping_jwks** | **str** | Base64-encoded JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT (Sign Algo: RS256) and return it as value (relevant for PRIVATE_KEY_JWT authentication method) | [optional] 
**ping_jwks_url** | **str** | The URL of the JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT and return it as value (relevant for PRIVATE_KEY_JWT authentication method) | [optional] 
**ping_password** | **str** | Ping Federate privileged user password | [optional] 
**ping_privileged_user** | **str** | Ping Federate privileged user | [optional] 
**ping_redirect_uris** | **list[str]** | List of URIs to which the OAuth authorization server may redirect the resource owner&#39;s user agent after authorization is obtained. At least one redirection URI is required for the AUTHORIZATION_CODE and IMPLICIT grant types. | [optional] 
**ping_restricted_scopes** | **list[str]** | Limit the OAuth client to specific scopes list | [optional] 
**ping_signing_algo** | **str** | The signing algorithm that the client must use to sign its request objects [RS256,RS384,RS512,ES256,ES384,ES512,PS256,PS384,PS512] If no explicit value is given, the client can use any of the supported signing algorithms (relevant for PRIVATE_KEY_JWT authentication method) | [optional] 
**ping_url** | **str** | Ping URL | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | The time from dynamic secret creation to expiration. | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GoogleTrustTargetDetails

GoogleTrustTargetDetails defines configuration for Google Trust Services ACME target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_key_pem** | **str** | ACME Account Private Key (PEM-encoded) Supports ECDSA (P-256, P-384, P-521), RSA (2048+), and Ed25519 Auto-generated as ECDSA P-256 during target creation bootstrap Stored encrypted, required for certificate operations and revocation | [optional] 
**account_url** | **str** | ACME Account URL (returned after registration with Google Trust Services) Used to retrieve existing account instead of re-registering | [optional] 
**acme_environment** | **str** | ACMEEnvironment defines Let&#39;s Encrypt ACME directory environment | [optional] 
**challenge_type** | **str** | ACMEChallengeType defines ACME challenge type for Let&#39;s Encrypt | [optional] 
**dns_target_name** | **str** | Name of DNS target (transient field - not stored in DB) Used by CLI to pass DNS target name to SDK for creating target_object_assoc Retrieved from target_object_assoc when reading target Required when ChallengeType is \&quot;dns\&quot; | [optional] 
**dns_target_type** | **str** |  | [optional] 
**dns_zone** | **str** | Cloudflare zone identifier Required when DNSTargetType is Cloudflare | [optional] 
**eab_hmac_key** | **str** | External Account Binding HMAC key (required for ACME account bootstrap on target creation) Not persisted after bootstrap | [optional] 
**eab_key_id** | **str** | External Account Binding key identifier (required for ACME account bootstrap on target creation) Not persisted after bootstrap | [optional] 
**email** | **str** | Email address for ACME account registration Required | [optional] 
**gcp_project** | **str** | GCP Cloud DNS: Project ID Optional - can be derived from service account | [optional] 
**hosted_zone** | **str** | AWS Route53: Hosted zone ID Required when DNSTargetType is AWS | [optional] 
**resource_group** | **str** | Azure DNS: Resource group name Required when DNSTargetType is Azure | [optional] 
**timeout** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



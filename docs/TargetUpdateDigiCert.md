# TargetUpdateDigiCert

targetUpdateDigiCert is a command that updates an existing DigiCert target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_challenge** | **str** | ACME challenge type. Options: [dns] | [optional] [default to 'dns']
**description** | **str** | Description of the object | [optional] 
**digicert_url** | **str** | DigiCert ACME endpoint selector. Options: [us-production/eu-production/us-demo/eu-demo] | [optional] [default to 'us-production']
**dns_target_creds** | **str** | Name of existing cloud target for DNS credentials. Required when challenge type is dns. Supported providers: AWS, Azure, GCP | [optional] 
**eab_hmac_key** | **str** | External Account Binding HMAC key (required for ACME account bootstrap on create) | [optional] 
**eab_key_id** | **str** | External Account Binding key identifier (required for ACME account bootstrap on create) | [optional] 
**email** | **str** | Email address for ACME account registration | 
**gcp_project** | **str** | GCP Cloud DNS project ID. Optional and can be derived from service account | [optional] 
**hosted_zone** | **str** | AWS Route53 hosted zone ID. Required when DNS credentials target is AWS | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**resource_group** | **str** | Azure resource group name. Required when DNS credentials target is Azure | [optional] 
**timeout** | **str** | Timeout for challenge validation | [optional] [default to '5m']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



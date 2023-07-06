# CreatePKICertIssuer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_any_name** | **bool** | If set, clients can request certificates for any CN | [optional] 
**allow_subdomains** | **bool** | If set, clients can request certificates for subdomains and wildcard subdomains of the allowed domains | [optional] 
**allowed_domains** | **str** | A list of the allowed domains that clients can request to be included in the certificate (in a comma-delimited list) | [optional] 
**allowed_uri_sans** | **str** | A list of the allowed URIs that clients can request to be included in the certificate as part of the URI Subject Alternative Names (in a comma-delimited list) | [optional] 
**ca_target** | **str** | The name of an existing CA target to attach this PKI Certificate Issuer to, required in Public CA mode | [optional] 
**client_flag** | **bool** | If set, certificates will be flagged for client auth use | [optional] 
**code_signing_flag** | **bool** | If set, certificates will be flagged for code signing use | [optional] 
**country** | **str** | A comma-separated list of countries that will be set in the issued certificate | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**destination_path** | **str** | A path in which to save generated certificates | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**gw_cluster_url** | **str** | The GW cluster URL to issue the certificate from, required in Public CA mode | [optional] 
**is_ca** | **bool** | If set, the basic constraints extension will be added to certificate | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_usage** | **str** | key-usage | [optional] [default to 'DigitalSignature,KeyAgreement,KeyEncipherment']
**locality** | **str** | A comma-separated list of localities that will be set in the issued certificate | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | PKI certificate issuer name | 
**not_enforce_hostnames** | **bool** | If set, any names are allowed for CN and SANs in the certificate and not only a valid host name | [optional] 
**not_require_cn** | **bool** | If set, clients can request certificates without a CN | [optional] 
**organizational_units** | **str** | A comma-separated list of organizational units (OU) that will be set in the issued certificate | [optional] 
**organizations** | **str** | A comma-separated list of organizations (O) that will be set in the issued certificate | [optional] 
**postal_code** | **str** | A comma-separated list of postal codes that will be set in the issued certificate | [optional] 
**protect_certificates** | **bool** | Whether to protect generated certificates from deletion | [optional] 
**province** | **str** | A comma-separated list of provinces that will be set in the issued certificate | [optional] 
**server_flag** | **bool** | If set, certificates will be flagged for server auth use | [optional] 
**signer_key_name** | **str** | A key to sign the certificate with, required in Private CA mode | [default to 'dummy_signer_key']
**street_address** | **str** | A comma-separated list of street addresses that will be set in the issued certificate | [optional] 
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | The maximum requested Time To Live for issued certificates, in seconds. In case of Public CA, this is based on the CA target&#39;s supported maximum TTLs | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



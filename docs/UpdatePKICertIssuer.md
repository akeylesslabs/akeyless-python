# UpdatePKICertIssuer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**allow_any_name** | **bool** | If set, clients can request certificates for any CN | [optional] 
**allow_copy_ext_from_csr** | **bool** | If set, will allow copying the extra extensions from the csr file (if given) | [optional] 
**allow_subdomains** | **bool** | If set, clients can request certificates for subdomains of the allowed domains | [optional] 
**allowed_domains** | **str** | A list of the allowed domains that clients can request to be included in the certificate (in a comma-delimited list) | [optional] 
**allowed_extra_extensions** | **str** | A json string containing the allowed extra extensions for the pki cert issuer | [optional] 
**allowed_ip_sans** | **str** | A list of the allowed CIDRs for ips that clients can request to be included in the certificate as part of the IP Subject Alternative Names (in a comma-delimited list) | [optional] 
**allowed_uri_sans** | **str** | A list of the allowed URIs that clients can request to be included in the certificate as part of the URI Subject Alternative Names (in a comma-delimited list) | [optional] 
**auto_renew** | **bool** | Automatically renew certificates before expiration | [optional] 
**client_flag** | **bool** | If set, certificates will be flagged for client auth use | [optional] 
**code_signing_flag** | **bool** | If set, certificates will be flagged for code signing use | [optional] 
**country** | **str** | A comma-separated list of countries that will be set in the issued certificate | [optional] 
**create_private_crl** | **bool** | Set this to allow the issuer will expose a CRL endpoint in the Gateway | [optional] 
**create_private_ocsp** | **bool** |  | [optional] 
**create_public_crl** | **bool** | Set this to allow the cert issuer will expose a public CRL endpoint | [optional] 
**create_public_ocsp** | **bool** |  | [optional] 
**critical_key_usage** | **str** | Mark key usage as critical [true/false] | [optional] [default to 'true']
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**destination_path** | **str** | A path in which to save generated certificates | [optional] 
**disable_wildcards** | **bool** | If set, generation of wildcard certificates will be disabled. | [optional] 
**enable_acme** | **bool** | If set, the cert issuer will support the acme protocol | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**gw_cluster_url** | **str** | The GW cluster URL to issue the certificate from. Required in Public CA mode, to allow CRLs on private CA, or to enable ACME | [optional] 
**is_ca** | **bool** | If set, the basic constraints extension will be added to certificate | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_usage** | **str** | key-usage | [optional] [default to 'DigitalSignature,KeyAgreement,KeyEncipherment']
**locality** | **str** | A comma-separated list of localities that will be set in the issued certificate | [optional] 
**max_path_len** | **int** | The maximum path length for the generated certificate. -1, means unlimited | [optional] [default to -1]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | PKI certificate issuer name | 
**new_name** | **str** | New item name | [optional] 
**not_enforce_hostnames** | **bool** | If set, any names are allowed for CN and SANs in the certificate and not only a valid host name | [optional] 
**not_require_cn** | **bool** | If set, clients can request certificates without a CN | [optional] 
**ocsp_ttl** | **str** |  | [optional] 
**organizational_units** | **str** | A comma-separated list of organizational units (OU) that will be set in the issued certificate | [optional] 
**organizations** | **str** | A comma-separated list of organizations (O) that will be set in the issued certificate | [optional] 
**postal_code** | **str** | A comma-separated list of postal codes that will be set in the issued certificate | [optional] 
**protect_certificates** | **bool** | Whether to protect generated certificates from deletion | [optional] 
**province** | **str** | A comma-separated list of provinces that will be set in the issued certificate | [optional] 
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**scheduled_renew** | **int** | Number of days before expiration to renew certificates | [optional] 
**server_flag** | **bool** | If set, certificates will be flagged for server auth use | [optional] 
**signer_key_name** | **str** | A key to sign the certificate with, required in Private CA mode | [optional] 
**street_address** | **str** | A comma-separated list of street addresses that will be set in the issued certificate | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **str** | The maximum requested Time To Live for issued certificates, in seconds. In case of Public CA, this is based on the CA target&#39;s supported maximum TTLs | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



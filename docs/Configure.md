# Configure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID | [optional] 
**access_key** | **str** | Access Key | [optional] 
**access_type** | **str** | Access Type (access_key/password/azure_ad/saml/oidc/aws_iam/gcp/k8s/cert) | [optional] [default to 'access_key']
**account_id** | **str** | Account id (relevant only for access-type&#x3D;password where the email address is associated with more than one account) | [optional] 
**admin_email** | **str** | Email (relevant only for access-type&#x3D;password) | [optional] 
**admin_password** | **str** | Password (relevant only for access-type&#x3D;password) | [optional] 
**azure_ad_object_id** | **str** | Azure Active Directory ObjectId (relevant only for access-type&#x3D;azure_ad) | [optional] 
**cert_data** | **str** | Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type&#x3D;cert in Curl Context) | [optional] 
**cert_issuer_name** | **str** | Certificate Issuer Name | [optional] 
**cert_username** | **str** | The username to sign in the SSH certificate (use a comma-separated list for more than one username) | [optional] 
**default_location_prefix** | **str** | Default path prefix for name of items, targets and auth methods | [optional] 
**disable_pafxfast** | **str** | Disable the FAST negotiation in the Kerberos authentication method | [optional] 
**gateway_spn** | **str** | The service principal name of the gateway as registered in LDAP (i.e., HTTP/gateway) | [optional] 
**gcp_audience** | **str** | GCP JWT audience | [optional] [default to 'akeyless.io']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_auth_config_name** | **str** | The K8S Auth config name (relevant only for access-type&#x3D;k8s) | [optional] 
**kerberos_username** | **str** | TThe username for the entry within the keytab to authenticate via Kerberos | [optional] 
**key_data** | **str** | Private key data encoded in base64. Used if file was not provided.(relevant only for access-type&#x3D;cert in Curl Context) | [optional] 
**keytab_data** | **str** | Base64-encoded content of a valid keytab file, containing the service account&#39;s entry. | [optional] 
**krb5_conf_data** | **str** | Base64-encoded content of a valid krb5.conf file, specifying the settings and parameters required for Kerberos authentication. | [optional] 
**legacy_signing_alg_name** | **bool** | Set this option to output legacy (&#39;ssh-rsa-cert-v01@openssh.com&#39;) signing algorithm name in the certificate. | [optional] 
**oci_auth_type** | **str** | The type of the OCI configuration to use [instance/apikey/resource] (relevant only for access-type&#x3D;oci) | [optional] [default to 'apikey']
**oci_group_ocid** | **list[str]** | A list of Oracle Cloud IDs groups (relevant only for access-type&#x3D;oci) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



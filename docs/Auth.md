# Auth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID | [optional] 
**access_key** | **str** | Access key (relevant only for access-type&#x3D;access_key) | [optional] 
**access_type** | **str** | Access Type (access_key/password/saml/ldap/k8s/azure_ad/oidc/aws_iam/universal_identity/jwt/gcp/cert/oci/kerberos) | [optional] [default to 'access_key']
**account_id** | **str** | Account id (relevant only for access-type&#x3D;password where the email address is associated with more than one account) | [optional] 
**admin_email** | **str** | Email (relevant only for access-type&#x3D;password) | [optional] 
**admin_password** | **str** | Password (relevant only for access-type&#x3D;password) | [optional] 
**cert_data** | **str** | Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type&#x3D;cert) | [optional] 
**cloud_id** | **str** | The cloud identity (relevant only for access-type&#x3D;azure_ad,aws_iam,gcp) | [optional] 
**debug** | **bool** |  | [optional] 
**disable_pafxfast** | **str** | Disable the FAST negotiation in the Kerberos authentication method | [optional] 
**gateway_spn** | **str** | The service principal name of the gateway as registered in LDAP (i.e., HTTP/gateway) | [optional] 
**gateway_url** | **str** | Gateway URL relevant only for access-type&#x3D;k8s/oauth2/saml/oidc | [optional] 
**gcp_audience** | **str** | GCP JWT audience | [optional] [default to 'akeyless.io']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt** | **str** | The Json Web Token (relevant only for access-type&#x3D;jwt/oidc) | [optional] 
**k8s_auth_config_name** | **str** | The K8S Auth config name (relevant only for access-type&#x3D;k8s) | [optional] 
**k8s_service_account_token** | **str** | The K8S service account token. (relevant only for access-type&#x3D;k8s) | [optional] 
**kerberos_token** | **str** | KerberosToken represents a Kerberos token generated for the gateway SPN (Service Principal Name). | [optional] 
**kerberos_username** | **str** | TThe username for the entry within the keytab to authenticate via Kerberos | [optional] 
**key_data** | **str** | Private key data encoded in base64. Used if file was not provided.(relevant only for access-type&#x3D;cert) | [optional] 
**keytab_data** | **str** | Base64-encoded content of a valid keytab file, containing the service account&#39;s entry. | [optional] 
**krb5_conf_data** | **str** | Base64-encoded content of a valid krb5.conf file, specifying the settings and parameters required for Kerberos authentication. | [optional] 
**ldap_password** | **str** | LDAP password (relevant only for access-type&#x3D;ldap) | [optional] 
**oci_auth_type** | **str** | The type of the OCI configuration to use [instance/apikey/resource] (relevant only for access-type&#x3D;oci) | [optional] [default to 'apikey']
**oci_group_ocid** | **list[str]** | A list of Oracle Cloud IDs groups (relevant only for access-type&#x3D;oci) | [optional] 
**otp** | **str** |  | [optional] 
**uid_token** | **str** | The universal_identity token (relevant only for access-type&#x3D;universal_identity) | [optional] 
**use_remote_browser** | **bool** | Returns a link to complete the authentication remotely (relevant only for access-type&#x3D;saml/oidc) | [optional] 
**username** | **str** | LDAP username (relevant only for access-type&#x3D;ldap) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



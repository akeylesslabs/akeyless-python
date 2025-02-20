# TargetCreateZeroSSL

targetCreateZeroSSL is a command that creates a new ZeroSSL target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API Key of the ZeroSSLTarget account | 
**description** | **str** | Description of the object | [optional] 
**imap_fqdn** | **str** | ImapFQDN of the IMAP service, FQDN or IPv4 address. Must be FQDN if the IMAP is using TLS | 
**imap_password** | **str** | ImapPassword to access the IMAP service | 
**imap_port** | **str** | ImapPort of the IMAP service | [optional] [default to '993']
**imap_target_email** | **str** | ImapValidationEmail to use when asking ZeroSSL to send a validation email, if empty will user imap-username | [optional] 
**imap_username** | **str** | ImapUsername to access the IMAP service | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**timeout** | **str** | Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h. | [optional] [default to '5m']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_create_zero_ssl import TargetCreateZeroSSL

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateZeroSSL from a JSON string
target_create_zero_ssl_instance = TargetCreateZeroSSL.from_json(json)
# print the JSON string representation of the object
print(TargetCreateZeroSSL.to_json())

# convert the object into a dict
target_create_zero_ssl_dict = target_create_zero_ssl_instance.to_dict()
# create an instance of TargetCreateZeroSSL from a dict
target_create_zero_ssl_from_dict = TargetCreateZeroSSL.from_dict(target_create_zero_ssl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



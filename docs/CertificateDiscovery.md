# CertificateDiscovery

CertificateDiscovery is a command that discovery certificates
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug** | **bool** | Debug mode | [optional] [default to False]
**expiration_event_in** | **list[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**hosts** | **str** | A comma separated list of IPs, CIDR ranges, or DNS names to discovery | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**port_ranges** | **str** | A comma separated list of port ranges Examples: \&quot;80,443\&quot; or \&quot;80,443,8080-8090\&quot; or \&quot;443\&quot; | [optional] [default to '443']
**protection_key** | **str** | The name of the key that protects the certificate value | [optional] 
**target_location** | **str** | The folder where the results will be saved | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



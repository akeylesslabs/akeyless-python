# GatewayUpdateProducerRedshift

gatewayUpdateProducerRedshift is a command that updates redshift producer [Deprecated: Use dynamic-secret-update-redshift command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_statements** | **str** | Redshift Creation statements | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key** | **str** | Dynamic producer encryption key | [optional] 
**redshift_db_name** | **str** | Redshift DB Name | [optional] 
**redshift_host** | **str** | Redshift Host | [optional] [default to '127.0.0.1']
**redshift_password** | **str** | Redshift Password | [optional] 
**redshift_port** | **str** | Redshift Port | [optional] [default to '5439']
**redshift_username** | **str** | Redshift Username | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **List[str]** | Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts) | [optional] 
**ssl** | **bool** | Enable/Disable SSL [true/false] | [optional] [default to False]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.gateway_update_producer_redshift import GatewayUpdateProducerRedshift

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerRedshift from a JSON string
gateway_update_producer_redshift_instance = GatewayUpdateProducerRedshift.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerRedshift.to_json())

# convert the object into a dict
gateway_update_producer_redshift_dict = gateway_update_producer_redshift_instance.to_dict()
# create an instance of GatewayUpdateProducerRedshift from a dict
gateway_update_producer_redshift_from_dict = GatewayUpdateProducerRedshift.from_dict(gateway_update_producer_redshift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



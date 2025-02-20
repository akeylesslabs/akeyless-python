# SalesforceTargetDetails

SalesforceTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_private_key** | **List[int]** | params needed for jwt auth AppPrivateKey is the rsa private key in PEM format | [optional] 
**auth_flow** | **str** |  | [optional] 
**ca_cert_data** | **List[int]** | CACertData is the rsa 4096 certificate data in PEM format | [optional] 
**ca_cert_name** | **str** | CACertName is the name of the certificate in SalesForce tenant | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** | params needed for password auth | [optional] 
**password** | **str** |  | [optional] 
**security_token** | **str** |  | [optional] 
**tenant_url** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.salesforce_target_details import SalesforceTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceTargetDetails from a JSON string
salesforce_target_details_instance = SalesforceTargetDetails.from_json(json)
# print the JSON string representation of the object
print(SalesforceTargetDetails.to_json())

# convert the object into a dict
salesforce_target_details_dict = salesforce_target_details_instance.to_dict()
# create an instance of SalesforceTargetDetails from a dict
salesforce_target_details_from_dict = SalesforceTargetDetails.from_dict(salesforce_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GatewayCreateProducerGithubOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_create_producer_github_output import GatewayCreateProducerGithubOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerGithubOutput from a JSON string
gateway_create_producer_github_output_instance = GatewayCreateProducerGithubOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerGithubOutput.to_json())

# convert the object into a dict
gateway_create_producer_github_output_dict = gateway_create_producer_github_output_instance.to_dict()
# create an instance of GatewayCreateProducerGithubOutput from a dict
gateway_create_producer_github_output_from_dict = GatewayCreateProducerGithubOutput.from_dict(gateway_create_producer_github_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateEKSTarget

createEKSTarget is a command that creates a new target. [Deprecated: Use target-create-eks command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**eks_access_key_id** | **str** | Access Key ID | 
**eks_cluster_ca_cert** | **str** | EKS cluster CA certificate | 
**eks_cluster_endpoint** | **str** | EKS cluster URL endpoint | 
**eks_cluster_name** | **str** | EKS cluster name | 
**eks_region** | **str** | Region | [optional] [default to 'us-east-2']
**eks_secret_access_key** | **str** | Secret Access Key | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.create_eks_target import CreateEKSTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEKSTarget from a JSON string
create_eks_target_instance = CreateEKSTarget.from_json(json)
# print the JSON string representation of the object
print(CreateEKSTarget.to_json())

# convert the object into a dict
create_eks_target_dict = create_eks_target_instance.to_dict()
# create an instance of CreateEKSTarget from a dict
create_eks_target_from_dict = CreateEKSTarget.from_dict(create_eks_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



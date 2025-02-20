# DeleteGwCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | Gateway Cluster, e.g. acc-abcd12345678/p-123456789012/defaultCluster | 
**force_deletion** | **bool** | Enforce deletion | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_gw_cluster import DeleteGwCluster

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGwCluster from a JSON string
delete_gw_cluster_instance = DeleteGwCluster.from_json(json)
# print the JSON string representation of the object
print(DeleteGwCluster.to_json())

# convert the object into a dict
delete_gw_cluster_dict = delete_gw_cluster_instance.to_dict()
# create an instance of DeleteGwCluster from a dict
delete_gw_cluster_from_dict = DeleteGwCluster.from_dict(delete_gw_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



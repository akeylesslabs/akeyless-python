# Producer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**failure_message** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**init** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.producer import Producer

# TODO update the JSON string below
json = "{}"
# create an instance of Producer from a JSON string
producer_instance = Producer.from_json(json)
# print the JSON string representation of the object
print(Producer.to_json())

# convert the object into a dict
producer_dict = producer_instance.to_dict()
# create an instance of Producer from a dict
producer_from_dict = Producer.from_dict(producer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



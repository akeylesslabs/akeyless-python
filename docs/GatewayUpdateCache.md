# GatewayUpdateCache

gatewayUpdateCache is a command that updates cache settings
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_interval** | **str** | Secure backup interval in minutes. To ensure service continuity in case of power cycle and network outage secrets will be backed up periodically per backup interval | [optional] [default to '1']
**enable_cache** | **str** | Enable cache [true/false] | [optional] 
**enable_proactive** | **str** | Enable proactive caching [true/false] | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**minimum_fetch_interval** | **str** | When using Cache or/and Proactive Cache, additional secrets will be fetched upon requesting a secret, based on the requestor&#39;s access policy. Define minimum fetching interval to avoid over fetching in a given time frame | [optional] [default to '5']
**stale_timeout** | **str** | Stale timeout in minutes, cache entries which are not accessed within timeout will be removed from cache | [optional] [default to '60']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



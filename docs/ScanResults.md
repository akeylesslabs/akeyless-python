# ScanResults

ScanResults contains detailed results from a certificate scan
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_existing** | **int** |  | [optional] 
**count_failed** | **int** |  | [optional] 
**count_hosts** | **int** |  | [optional] 
**count_new** | **int** |  | [optional] 
**count_subdomains** | **int** |  | [optional] 
**domain_coverage** | [**list[DomainCoverage]**](DomainCoverage.md) | DomainCoverage says, per public domain, how much of it subdomain discovery managed to cover. Clients that predate it ignore it, and a scan with no public domain omits it. | [optional] 
**error** | **str** |  | [optional] 
**failed_targets** | [**list[TargetError]**](TargetError.md) |  | [optional] 
**item_names** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



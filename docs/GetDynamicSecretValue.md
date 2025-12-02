# GetDynamicSecretValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Optional arguments as key&#x3D;value pairs or JSON strings, e.g - \\\&quot;--args&#x3D;csr&#x3D;base64_encoded_csr --args&#x3D;common_name&#x3D;bar\\\&quot; or args&#x3D;&#39;{\\\&quot;csr\\\&quot;:\\\&quot;base64_encoded_csr\\\&quot;}. It is possible to combine both formats.&#39; | [optional] 
**dbname** | **str** | DBName: Optional override DB name (works only if DS allows it. only relevant for MSSQL) | [optional] 
**host** | **str** | Host | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**target** | **str** | Target Name | [optional] 
**timeout** | **int** | Timeout in seconds | [optional] [default to 15]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateLinkedTarget

updateLinkedTarget is a command that updates an existing target. [Deprecated: Use target-update-linked command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_hosts** | **str** | A comma seperated list of new server hosts and server descriptions joined by semicolon &#39;;&#39; that will be added to the Linked Target hosts. | [optional] 
**description** | **str** | Description of the object | [optional] 
**hosts** | **str** | A comma seperated list of server hosts and server descriptions joined by semicolon &#39;;&#39; (i.e. &#39;server-dev.com;My Dev server,server-prod.com;My Prod server description&#39;) | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**name** | **str** | Linked Target name | 
**new_name** | **str** | New Linked Target name | [optional] 
**parent_target_name** | **str** | The parent Target name | [optional] 
**rm_hosts** | **str** | Comma separated list of existing hosts that will be removed from Linked Target hosts. | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Specifies the hosts type, relevant only when working without parent target | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



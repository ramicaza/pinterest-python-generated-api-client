# CatalogsRetailProductGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the catalog product group. | 
**filters** | [**CatalogsProductGroupFilters**](CatalogsProductGroupFilters.md) |  | 
**catalog_id** | **str** | Catalog id pertaining to the retail product group. | 
**feed_id** | **str, none_type** | id of the catalogs feed belonging to this catalog product group | 
**catalog_type** | **str** |  | defaults to "RETAIL"
**name** | **str** | Name of catalog product group | [optional] 
**description** | **str, none_type** |  | [optional] 
**is_featured** | **bool** | boolean indicator of whether the product group is being featured or not | [optional] 
**type** | [**CatalogsProductGroupType**](CatalogsProductGroupType.md) |  | [optional] 
**status** | [**CatalogsProductGroupStatus**](CatalogsProductGroupStatus.md) |  | [optional] 
**created_at** | **int** | Unix timestamp in seconds of when catalog product group was created. | [optional] 
**updated_at** | **int** | Unix timestamp in seconds of last time catalog product group was updated. | [optional] 
**country** | **str, none_type** |  | [optional] 
**locale** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



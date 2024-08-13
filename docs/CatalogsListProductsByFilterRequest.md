# CatalogsListProductsByFilterRequest

Request object to list products for a given product group filter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_id** | **str** | Catalog Feed id pertaining to the catalog product group filter. | [optional] 
**filters** | [**CatalogsProductGroupFilters**](CatalogsProductGroupFilters.md) |  | [optional] 
**catalog_type** | **str** |  | [optional]  if omitted the server will use the default value of "CREATIVE_ASSETS"
**catalog_id** | **str** | Catalog id pertaining to the creative assets product group. | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**locale** | [**CatalogsLocale**](CatalogsLocale.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



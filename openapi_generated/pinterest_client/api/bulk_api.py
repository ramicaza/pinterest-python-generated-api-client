"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.14.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_generated.pinterest_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_generated.pinterest_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_generated.pinterest_client.model.bulk_download_request import BulkDownloadRequest
from openapi_generated.pinterest_client.model.bulk_download_response import BulkDownloadResponse
from openapi_generated.pinterest_client.model.bulk_upsert_request import BulkUpsertRequest
from openapi_generated.pinterest_client.model.bulk_upsert_response import BulkUpsertResponse
from openapi_generated.pinterest_client.model.bulk_upsert_status_response import BulkUpsertStatusResponse
from openapi_generated.pinterest_client.model.error import Error


class BulkApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.bulk_download_create_endpoint = _Endpoint(
            settings={
                'response_type': (BulkDownloadResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/bulk/download',
                'operation_id': 'bulk_download_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'bulk_download_request',
                ],
                'required': [
                    'ad_account_id',
                    'bulk_download_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'bulk_download_request':
                        (BulkDownloadRequest,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'bulk_download_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.bulk_request_get_endpoint = _Endpoint(
            settings={
                'response_type': (BulkUpsertStatusResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/bulk/{bulk_request_id}',
                'operation_id': 'bulk_request_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'bulk_request_id',
                    'include_details',
                ],
                'required': [
                    'ad_account_id',
                    'bulk_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'bulk_request_id':
                        (str,),
                    'include_details':
                        (bool,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'bulk_request_id': 'bulk_request_id',
                    'include_details': 'include_details',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'bulk_request_id': 'path',
                    'include_details': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.bulk_upsert_create_endpoint = _Endpoint(
            settings={
                'response_type': (BulkUpsertResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/bulk/upsert',
                'operation_id': 'bulk_upsert_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'bulk_upsert_request',
                ],
                'required': [
                    'ad_account_id',
                    'bulk_upsert_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'bulk_upsert_request':
                        (BulkUpsertRequest,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'bulk_upsert_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def bulk_download_create(
        self,
        ad_account_id,
        bulk_download_request,
        **kwargs
    ):
        """Get advertiser entities in bulk  # noqa: E501

        Create an asynchronous report that may include information on campaigns, ad groups, product groups, ads, and/or keywords; can filter by campaigns. Though the entities may be active, archived, or paused, only active entities will return data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_download_create(ad_account_id, bulk_download_request, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            bulk_download_request (BulkDownloadRequest): Parameters to get ad entities in bulk

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BulkDownloadResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['bulk_download_request'] = \
            bulk_download_request
        return self.bulk_download_create_endpoint.call_with_http_info(**kwargs)

    def bulk_request_get(
        self,
        ad_account_id,
        bulk_request_id,
        **kwargs
    ):
        """Download advertiser entities in bulk  # noqa: E501

        Get the status of a bulk request by <code>request_id</code>, along with a download URL that will allow you to download the new or updated entity data (campaigns, ad groups, product groups, ads, or keywords).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_request_get(ad_account_id, bulk_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            bulk_request_id (str): Unique identifier of a bulk upsert request.

        Keyword Args:
            include_details (bool): if set to True then attach the errors/details to all the requests. [optional] if omitted the server will use the default value of False
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BulkUpsertStatusResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['bulk_request_id'] = \
            bulk_request_id
        return self.bulk_request_get_endpoint.call_with_http_info(**kwargs)

    def bulk_upsert_create(
        self,
        ad_account_id,
        bulk_upsert_request,
        **kwargs
    ):
        """Create/update ad entities in bulk  # noqa: E501

        Either create or update any combination of campaigns, ad groups, product groups, ads, or keywords. Note that this request will be processed asynchronously; the response will include a <code>request_id</code> that can be used to obtain the status of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_upsert_create(ad_account_id, bulk_upsert_request, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            bulk_upsert_request (BulkUpsertRequest): Parameters to get create/update ad entities in bulk

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BulkUpsertResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['bulk_upsert_request'] = \
            bulk_upsert_request
        return self.bulk_upsert_create_endpoint.call_with_http_info(**kwargs)


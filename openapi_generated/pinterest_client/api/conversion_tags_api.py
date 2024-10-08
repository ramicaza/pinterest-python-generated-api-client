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
from openapi_generated.pinterest_client.model.conversion_event_response import ConversionEventResponse
from openapi_generated.pinterest_client.model.conversion_tag_create import ConversionTagCreate
from openapi_generated.pinterest_client.model.conversion_tag_list_response import ConversionTagListResponse
from openapi_generated.pinterest_client.model.conversion_tag_response import ConversionTagResponse
from openapi_generated.pinterest_client.model.conversion_tags_ocpm_eligible_response import ConversionTagsOcpmEligibleResponse
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated


class ConversionTagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.conversion_tags_create_endpoint = _Endpoint(
            settings={
                'response_type': (ConversionTagResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/conversion_tags',
                'operation_id': 'conversion_tags_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'conversion_tag_create',
                ],
                'required': [
                    'ad_account_id',
                    'conversion_tag_create',
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
                    'conversion_tag_create':
                        (ConversionTagCreate,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'conversion_tag_create': 'body',
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
        self.conversion_tags_get_endpoint = _Endpoint(
            settings={
                'response_type': (ConversionTagResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/conversion_tags/{conversion_tag_id}',
                'operation_id': 'conversion_tags_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'conversion_tag_id',
                ],
                'required': [
                    'ad_account_id',
                    'conversion_tag_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                    'conversion_tag_id',
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
                    ('conversion_tag_id',): {
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
                    'conversion_tag_id':
                        (str,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'conversion_tag_id': 'conversion_tag_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'conversion_tag_id': 'path',
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
        self.conversion_tags_list_endpoint = _Endpoint(
            settings={
                'response_type': (ConversionTagListResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/conversion_tags',
                'operation_id': 'conversion_tags_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'filter_deleted',
                ],
                'required': [
                    'ad_account_id',
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
                    'filter_deleted':
                        (bool,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'filter_deleted': 'filter_deleted',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'filter_deleted': 'query',
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
        self.ocpm_eligible_conversion_tags_get_endpoint = _Endpoint(
            settings={
                'response_type': (ConversionTagsOcpmEligibleResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/conversion_tags/ocpm_eligible',
                'operation_id': 'ocpm_eligible_conversion_tags_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                ],
                'required': [
                    'ad_account_id',
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
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
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
        self.page_visit_conversion_tags_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/conversion_tags/page_visit',
                'operation_id': 'page_visit_conversion_tags_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'page_size',
                    'order',
                    'bookmark',
                ],
                'required': [
                    'ad_account_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'order',
                ],
                'validation': [
                    'ad_account_id',
                    'page_size',
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
                    ('page_size',): {

                        'inclusive_maximum': 250,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('order',): {

                        "ASCENDING": "ASCENDING",
                        "DESCENDING": "DESCENDING"
                    },
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'page_size':
                        (int,),
                    'order':
                        (str,),
                    'bookmark':
                        (str,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'page_size': 'page_size',
                    'order': 'order',
                    'bookmark': 'bookmark',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'page_size': 'query',
                    'order': 'query',
                    'bookmark': 'query',
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

    def conversion_tags_create(
        self,
        ad_account_id,
        conversion_tag_create,
        **kwargs
    ):
        """Create conversion tag  # noqa: E501

        Create a conversion tag, also known as <a href=\"https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag\" target=\"_blank\">Pinterest tag</a>, with the option to enable enhanced match.<p/> The Pinterest Tag tracks actions people take on the ad account’ s website after they view the ad account's ad on Pinterest. The advertiser needs to customize this tag to track conversions.<p/> For more information, see:<p/> <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag\">Set up the Pinterest tag</a><p/> <a class=\"reference external\" href=\"/docs/api-features/pinterest-tag/\">Pinterest Tag</a><p/> <a class=\"reference external\" href=\"/docs/api-features/pinterest-tag/#enhanced-match\">Enhanced match</a>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.conversion_tags_create(ad_account_id, conversion_tag_create, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            conversion_tag_create (ConversionTagCreate): Conversion Tag to create

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
            ConversionTagResponse
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
        kwargs['conversion_tag_create'] = \
            conversion_tag_create
        return self.conversion_tags_create_endpoint.call_with_http_info(**kwargs)

    def conversion_tags_get(
        self,
        ad_account_id,
        conversion_tag_id,
        **kwargs
    ):
        """Get conversion tag  # noqa: E501

        Get information about an existing conversion tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.conversion_tags_get(ad_account_id, conversion_tag_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            conversion_tag_id (str): Id of the conversion tag.

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
            ConversionTagResponse
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
        kwargs['conversion_tag_id'] = \
            conversion_tag_id
        return self.conversion_tags_get_endpoint.call_with_http_info(**kwargs)

    def conversion_tags_list(
        self,
        ad_account_id,
        **kwargs
    ):
        """Get conversion tags  # noqa: E501

        List conversion tags associated with an ad account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.conversion_tags_list(ad_account_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.

        Keyword Args:
            filter_deleted (bool): Filter out deleted tags.. [optional] if omitted the server will use the default value of False
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
            ConversionTagListResponse
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
        return self.conversion_tags_list_endpoint.call_with_http_info(**kwargs)

    def ocpm_eligible_conversion_tags_get(
        self,
        ad_account_id,
        **kwargs
    ):
        """Get Ocpm eligible conversion tags  # noqa: E501

        Get Ocpm eligible conversion tag events for an ad account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ocpm_eligible_conversion_tags_get(ad_account_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.

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
            ConversionTagsOcpmEligibleResponse
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
        return self.ocpm_eligible_conversion_tags_get_endpoint.call_with_http_info(**kwargs)

    def page_visit_conversion_tags_get(
        self,
        ad_account_id,
        **kwargs
    ):
        """Get page visit conversion tags  # noqa: E501

        Get all page visit conversion tag events for an ad account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.page_visit_conversion_tags_get(ad_account_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.

        Keyword Args:
            page_size (int): Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information.. [optional] if omitted the server will use the default value of 25
            order (str): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items.. [optional]
            bookmark (str): Cursor used to fetch the next page of items. [optional]
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
            bool, date, datetime, dict, float, int, list, str, none_type
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
        return self.page_visit_conversion_tags_get_endpoint.call_with_http_info(**kwargs)


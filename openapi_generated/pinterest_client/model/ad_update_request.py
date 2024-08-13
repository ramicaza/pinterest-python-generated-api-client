"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.14.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_generated.pinterest_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_generated.pinterest_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_generated.pinterest_client.model.ad_common import AdCommon
    from openapi_generated.pinterest_client.model.ad_update_request1 import AdUpdateRequest1
    from openapi_generated.pinterest_client.model.creative_type import CreativeType
    from openapi_generated.pinterest_client.model.entity_status import EntityStatus
    from openapi_generated.pinterest_client.model.grid_click_type import GridClickType
    from openapi_generated.pinterest_client.model.quiz_pin_data import QuizPinData
    from openapi_generated.pinterest_client.model.tracking_urls import TrackingUrls
    globals()['AdCommon'] = AdCommon
    globals()['AdUpdateRequest1'] = AdUpdateRequest1
    globals()['CreativeType'] = CreativeType
    globals()['EntityStatus'] = EntityStatus
    globals()['GridClickType'] = GridClickType
    globals()['QuizPinData'] = QuizPinData
    globals()['TrackingUrls'] = TrackingUrls


class AdUpdateRequest(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('customizable_cta_type',): {
            'None': None,
            'GET_OFFER': "GET_OFFER",
            'LEARN_MORE': "LEARN_MORE",
            'ORDER_NOW': "ORDER_NOW",
            'SHOP_NOW': "SHOP_NOW",
            'SIGN_UP': "SIGN_UP",
            'SUBSCRIBE': "SUBSCRIBE",
            'BUY_NOW': "BUY_NOW",
            'CONTACT_US': "CONTACT_US",
            'GET_QUOTE': "GET_QUOTE",
            'VISIT_SITE': "VISIT_SITE",
            'APPLY_NOW': "APPLY_NOW",
            'BOOK_NOW': "BOOK_NOW",
            'REQUEST_DEMO': "REQUEST_DEMO",
            'REGISTER_NOW': "REGISTER_NOW",
            'FIND_A_DEALER': "FIND_A_DEALER",
            'ADD_TO_CART': "ADD_TO_CART",
            'WATCH_NOW': "WATCH_NOW",
            'READ_MORE': "READ_MORE",
            'NULL': "null",
        },
    }

    validations = {
        ('id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('ad_group_id',): {
            'regex': {
                'pattern': r'^(AG)?\d+$',  # noqa: E501
            },
        },
        ('lead_form_id',): {
            'regex': {
                'pattern': r'^(AG)?\d+$',  # noqa: E501
            },
        },
        ('pin_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'ad_group_id': (str,),  # noqa: E501
            'android_deep_link': (str, none_type,),  # noqa: E501
            'carousel_android_deep_links': ([str], none_type,),  # noqa: E501
            'carousel_destination_urls': ([str], none_type,),  # noqa: E501
            'carousel_ios_deep_links': ([str], none_type,),  # noqa: E501
            'click_tracking_url': (str, none_type,),  # noqa: E501
            'creative_type': (CreativeType,),  # noqa: E501
            'destination_url': (str, none_type,),  # noqa: E501
            'ios_deep_link': (str, none_type,),  # noqa: E501
            'is_pin_deleted': (bool,),  # noqa: E501
            'is_removable': (bool,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'status': (EntityStatus,),  # noqa: E501
            'tracking_urls': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'view_tracking_url': (str, none_type,),  # noqa: E501
            'lead_form_id': (str, none_type,),  # noqa: E501
            'grid_click_type': (GridClickType,),  # noqa: E501
            'customizable_cta_type': (str, none_type,),  # noqa: E501
            'quiz_pin_data': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'pin_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'ad_group_id': 'ad_group_id',  # noqa: E501
        'android_deep_link': 'android_deep_link',  # noqa: E501
        'carousel_android_deep_links': 'carousel_android_deep_links',  # noqa: E501
        'carousel_destination_urls': 'carousel_destination_urls',  # noqa: E501
        'carousel_ios_deep_links': 'carousel_ios_deep_links',  # noqa: E501
        'click_tracking_url': 'click_tracking_url',  # noqa: E501
        'creative_type': 'creative_type',  # noqa: E501
        'destination_url': 'destination_url',  # noqa: E501
        'ios_deep_link': 'ios_deep_link',  # noqa: E501
        'is_pin_deleted': 'is_pin_deleted',  # noqa: E501
        'is_removable': 'is_removable',  # noqa: E501
        'name': 'name',  # noqa: E501
        'status': 'status',  # noqa: E501
        'tracking_urls': 'tracking_urls',  # noqa: E501
        'view_tracking_url': 'view_tracking_url',  # noqa: E501
        'lead_form_id': 'lead_form_id',  # noqa: E501
        'grid_click_type': 'grid_click_type',  # noqa: E501
        'customizable_cta_type': 'customizable_cta_type',  # noqa: E501
        'quiz_pin_data': 'quiz_pin_data',  # noqa: E501
        'pin_id': 'pin_id',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AdUpdateRequest - a model defined in OpenAPI

        Keyword Args:
            id (str): The ID of this ad.
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ad_group_id (str): ID of the ad group that contains the ad.. [optional]  # noqa: E501
            android_deep_link (str, none_type): Deep link URL for Android devices.. [optional]  # noqa: E501
            carousel_android_deep_links ([str], none_type): Comma-separated deep links for the carousel pin on Android.. [optional]  # noqa: E501
            carousel_destination_urls ([str], none_type): Comma-separated destination URLs for the carousel pin to promote.. [optional]  # noqa: E501
            carousel_ios_deep_links ([str], none_type): Comma-separated deep links for the carousel pin on iOS.. [optional]  # noqa: E501
            click_tracking_url (str, none_type): Tracking url for the ad clicks.. [optional]  # noqa: E501
            creative_type (CreativeType): [optional]  # noqa: E501
            destination_url (str, none_type): Destination URL.. [optional]  # noqa: E501
            ios_deep_link (str, none_type): Deep link URL for iOS devices.. [optional]  # noqa: E501
            is_pin_deleted (bool): Is original pin deleted?. [optional]  # noqa: E501
            is_removable (bool): Is pin repinnable?. [optional]  # noqa: E501
            name (str, none_type): Name of the ad - 255 chars max.. [optional]  # noqa: E501
            status (EntityStatus): [optional]  # noqa: E501
            tracking_urls ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            view_tracking_url (str, none_type): Tracking URL for ad impressions.. [optional]  # noqa: E501
            lead_form_id (str, none_type): Lead form ID for lead ad generation.. [optional]  # noqa: E501
            grid_click_type (GridClickType): [optional]  # noqa: E501
            customizable_cta_type (str, none_type): Select a call to action (CTA) to display below your ad. Available only for ads with direct links enabled. CTA options for consideration and conversion campaigns are LEARN_MORE, SHOP_NOW, BOOK_NOW, SIGN_UP, VISIT_SITE, BUY_NOW, GET_OFFER, ORDER_NOW, ADD_TO_CART (for conversion campaigns with add to cart conversion events only). [optional]  # noqa: E501
            quiz_pin_data ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Before creating a quiz ad, you must create an organic Pin using POST/Create Pin for each result in the quiz. Quiz ads cannot be saved by a Pinner. Quiz ad results can be saved.. [optional]  # noqa: E501
            pin_id (str, none_type): Pin ID. This field may only be updated for draft ads.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """AdUpdateRequest - a model defined in OpenAPI

        Keyword Args:
            id (str): The ID of this ad.
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ad_group_id (str): ID of the ad group that contains the ad.. [optional]  # noqa: E501
            android_deep_link (str, none_type): Deep link URL for Android devices.. [optional]  # noqa: E501
            carousel_android_deep_links ([str], none_type): Comma-separated deep links for the carousel pin on Android.. [optional]  # noqa: E501
            carousel_destination_urls ([str], none_type): Comma-separated destination URLs for the carousel pin to promote.. [optional]  # noqa: E501
            carousel_ios_deep_links ([str], none_type): Comma-separated deep links for the carousel pin on iOS.. [optional]  # noqa: E501
            click_tracking_url (str, none_type): Tracking url for the ad clicks.. [optional]  # noqa: E501
            creative_type (CreativeType): [optional]  # noqa: E501
            destination_url (str, none_type): Destination URL.. [optional]  # noqa: E501
            ios_deep_link (str, none_type): Deep link URL for iOS devices.. [optional]  # noqa: E501
            is_pin_deleted (bool): Is original pin deleted?. [optional]  # noqa: E501
            is_removable (bool): Is pin repinnable?. [optional]  # noqa: E501
            name (str, none_type): Name of the ad - 255 chars max.. [optional]  # noqa: E501
            status (EntityStatus): [optional]  # noqa: E501
            tracking_urls ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            view_tracking_url (str, none_type): Tracking URL for ad impressions.. [optional]  # noqa: E501
            lead_form_id (str, none_type): Lead form ID for lead ad generation.. [optional]  # noqa: E501
            grid_click_type (GridClickType): [optional]  # noqa: E501
            customizable_cta_type (str, none_type): Select a call to action (CTA) to display below your ad. Available only for ads with direct links enabled. CTA options for consideration and conversion campaigns are LEARN_MORE, SHOP_NOW, BOOK_NOW, SIGN_UP, VISIT_SITE, BUY_NOW, GET_OFFER, ORDER_NOW, ADD_TO_CART (for conversion campaigns with add to cart conversion events only). [optional]  # noqa: E501
            quiz_pin_data ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Before creating a quiz ad, you must create an organic Pin using POST/Create Pin for each result in the quiz. Quiz ads cannot be saved by a Pinner. Quiz ad results can be saved.. [optional]  # noqa: E501
            pin_id (str, none_type): Pin ID. This field may only be updated for draft ads.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [

          ],
          'oneOf': [
          ],
        }

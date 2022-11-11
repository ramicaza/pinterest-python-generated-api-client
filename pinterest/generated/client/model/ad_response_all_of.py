"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.7.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pinterest.generated.client.model_utils import (  # noqa: F401
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
from pinterest.generated.client.exceptions import ApiAttributeError


def lazy_import():
    from pinterest.generated.client.model.pin_promotion_summary_status import PinPromotionSummaryStatus
    globals()['PinPromotionSummaryStatus'] = PinPromotionSummaryStatus


class AdResponseAllOf(ModelNormal):
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
        ('rejected_reasons',): {
            'HASHTAGS': "HASHTAGS",
            'PROMOTIONS_AND_PRICES': "PROMOTIONS_AND_PRICES",
            'TARGETING': "TARGETING",
            'LANDING_PAGE': "LANDING_PAGE",
            'CAPS_AND_SYMBOLS': "CAPS_AND_SYMBOLS",
            'SHOCKING': "SHOCKING",
            'WEIGHT_LOSS': "WEIGHT_LOSS",
            'PROHIBITED_PRODUCT': "PROHIBITED_PRODUCT",
            'AUTHENTICITY': "AUTHENTICITY",
            'NUDITY': "NUDITY",
            'CONFUSING_DESIGN': "CONFUSING_DESIGN",
            'URGENCY': "URGENCY",
            'RATINGS': "RATINGS",
            'APP': "APP",
            'ALCOHOL': "ALCOHOL",
            'CONTESTS': "CONTESTS",
            'POLITICAL': "POLITICAL",
            'OTHER': "OTHER",
            'IMAGE': "IMAGE",
            'NAR': "NAR",
            'INCONSISTENT': "INCONSISTENT",
            'CLICKBAIT': "CLICKBAIT",
            'NO_DESCRIPTION': "NO_DESCRIPTION",
            'LOW_QUALITY': "LOW_QUALITY",
            'EXAGGERATED_CLAIMS': "EXAGGERATED_CLAIMS",
            'PINTEREST_BRAND': "PINTEREST_BRAND",
            'ALCOHOL_NO_SALE': "ALCOHOL_NO_SALE",
            'LANDING_PAGE_SPEED': "LANDING_PAGE_SPEED",
            'LANDING_PAGE_HARDWALL': "LANDING_PAGE_HARDWALL",
            'LANDING_PAGE_BROKEN': "LANDING_PAGE_BROKEN",
            'LANDING_PAGE_QUALITY': "LANDING_PAGE_QUALITY",
            'OUT_OF_STOCK': "OUT_OF_STOCK",
            'IMAGE_LOW_QUALITY': "IMAGE_LOW_QUALITY",
            'IMAGE_BUSY': "IMAGE_BUSY",
            'IMAGE_POORLY_EDITED': "IMAGE_POORLY_EDITED",
            'IMAGE_BEFORE_AFTER': "IMAGE_BEFORE_AFTER",
            'UGC': "UGC",
            'FAKE_BUTTONS': "FAKE_BUTTONS",
            'WEAPONS': "WEAPONS",
            'SENSITIVE': "SENSITIVE",
            'UNACCEPTABLE_BUSINESS': "UNACCEPTABLE_BUSINESS",
            'SUSPICIOUS_CLAIMS': "SUSPICIOUS_CLAIMS",
            'PHARMA': "PHARMA",
            'SUSPICIOUS_SUPPLEMENTS': "SUSPICIOUS_SUPPLEMENTS",
            'ILLEGAL_RECREATIONAL_DRUG': "ILLEGAL_RECREATIONAL_DRUG",
            'LOW_QUALITY_LANDING_PAGE': "LOW_QUALITY_LANDING_PAGE",
            'RESTRICTED_HEALTHCARE': "RESTRICTED_HEALTHCARE",
            'INCONSISTENT_LANG_FR': "INCONSISTENT_LANG_FR",
        },
        ('review_status',): {
            'OTHER': "OTHER",
            'PENDING': "PENDING",
            'REJECTED': "REJECTED",
            'APPROVED': "APPROVED",
        },
    }

    validations = {
        ('ad_account_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('campaign_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('id',): {
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
            'ad_account_id': (str,),  # noqa: E501
            'campaign_id': (str,),  # noqa: E501
            'collection_items_destination_url_template': (str, none_type,),  # noqa: E501
            'created_time': (int,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'rejected_reasons': ([str],),  # noqa: E501
            'rejection_labels': ([str],),  # noqa: E501
            'review_status': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'updated_time': (int,),  # noqa: E501
            'summary_status': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ad_account_id': 'ad_account_id',  # noqa: E501
        'campaign_id': 'campaign_id',  # noqa: E501
        'collection_items_destination_url_template': 'collection_items_destination_url_template',  # noqa: E501
        'created_time': 'created_time',  # noqa: E501
        'id': 'id',  # noqa: E501
        'rejected_reasons': 'rejected_reasons',  # noqa: E501
        'rejection_labels': 'rejection_labels',  # noqa: E501
        'review_status': 'review_status',  # noqa: E501
        'type': 'type',  # noqa: E501
        'updated_time': 'updated_time',  # noqa: E501
        'summary_status': 'summary_status',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AdResponseAllOf - a model defined in OpenAPI

        Keyword Args:
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
            ad_account_id (str): The ID of the advertiser that this ad belongs to.. [optional]  # noqa: E501
            campaign_id (str): ID of the ad campaign that contains this ad.. [optional]  # noqa: E501
            collection_items_destination_url_template (str, none_type): Destination URL template for all items within a collections drawer.. [optional]  # noqa: E501
            created_time (int): Pin creation time. Unix timestamp in seconds.. [optional]  # noqa: E501
            id (str): The ID of this ad.. [optional]  # noqa: E501
            rejected_reasons ([str]): Enum reason why the pin was rejected. Returned if <code>review_status</code> is \"REJECTED\".. [optional]  # noqa: E501
            rejection_labels ([str]): Text reason why the pin was rejected. Returned if <code>review_status</code> is \"REJECTED\".. [optional]  # noqa: E501
            review_status (str): Ad review status. [optional]  # noqa: E501
            type (str): Always \"ad\".. [optional]  # noqa: E501
            updated_time (int): Last update time. Unix timestamp in seconds.. [optional]  # noqa: E501
            summary_status (str): Ad summary status. [optional]  # noqa: E501
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
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
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """AdResponseAllOf - a model defined in OpenAPI

        Keyword Args:
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
            ad_account_id (str): The ID of the advertiser that this ad belongs to.. [optional]  # noqa: E501
            campaign_id (str): ID of the ad campaign that contains this ad.. [optional]  # noqa: E501
            collection_items_destination_url_template (str, none_type): Destination URL template for all items within a collections drawer.. [optional]  # noqa: E501
            created_time (int): Pin creation time. Unix timestamp in seconds.. [optional]  # noqa: E501
            id (str): The ID of this ad.. [optional]  # noqa: E501
            rejected_reasons ([str]): Enum reason why the pin was rejected. Returned if <code>review_status</code> is \"REJECTED\".. [optional]  # noqa: E501
            rejection_labels ([str]): Text reason why the pin was rejected. Returned if <code>review_status</code> is \"REJECTED\".. [optional]  # noqa: E501
            review_status (str): Ad review status. [optional]  # noqa: E501
            type (str): Always \"ad\".. [optional]  # noqa: E501
            updated_time (int): Last update time. Unix timestamp in seconds.. [optional]  # noqa: E501
            summary_status (str): Ad summary status. [optional]  # noqa: E501
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

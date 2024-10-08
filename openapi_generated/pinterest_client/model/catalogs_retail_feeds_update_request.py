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
    from openapi_generated.pinterest_client.model.catalogs_feed_credentials import CatalogsFeedCredentials
    from openapi_generated.pinterest_client.model.catalogs_feed_processing_schedule import CatalogsFeedProcessingSchedule
    from openapi_generated.pinterest_client.model.catalogs_format import CatalogsFormat
    from openapi_generated.pinterest_client.model.catalogs_status import CatalogsStatus
    from openapi_generated.pinterest_client.model.catalogs_type import CatalogsType
    from openapi_generated.pinterest_client.model.nullable_currency import NullableCurrency
    from openapi_generated.pinterest_client.model.product_availability_type import ProductAvailabilityType
    globals()['CatalogsFeedCredentials'] = CatalogsFeedCredentials
    globals()['CatalogsFeedProcessingSchedule'] = CatalogsFeedProcessingSchedule
    globals()['CatalogsFormat'] = CatalogsFormat
    globals()['CatalogsStatus'] = CatalogsStatus
    globals()['CatalogsType'] = CatalogsType
    globals()['NullableCurrency'] = NullableCurrency
    globals()['ProductAvailabilityType'] = ProductAvailabilityType


class CatalogsRetailFeedsUpdateRequest(ModelNormal):
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
    }

    validations = {
        ('location',): {
            'regex': {
                'pattern': r'^(http|https|ftp|sftp):\/\/',  # noqa: E501
            },
        },
    }

    additional_properties_type = None

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
            'catalog_type': (CatalogsType,),  # noqa: E501
            'default_currency': (NullableCurrency,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'format': (CatalogsFormat,),  # noqa: E501
            'credentials': (CatalogsFeedCredentials,),  # noqa: E501
            'location': (str,),  # noqa: E501
            'preferred_processing_schedule': (CatalogsFeedProcessingSchedule,),  # noqa: E501
            'status': (CatalogsStatus,),  # noqa: E501
            'default_availability': (ProductAvailabilityType,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'catalog_type': 'catalog_type',  # noqa: E501
        'default_currency': 'default_currency',  # noqa: E501
        'name': 'name',  # noqa: E501
        'format': 'format',  # noqa: E501
        'credentials': 'credentials',  # noqa: E501
        'location': 'location',  # noqa: E501
        'preferred_processing_schedule': 'preferred_processing_schedule',  # noqa: E501
        'status': 'status',  # noqa: E501
        'default_availability': 'default_availability',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, catalog_type, *args, **kwargs):  # noqa: E501
        """CatalogsRetailFeedsUpdateRequest - a model defined in OpenAPI

        Args:
            catalog_type (CatalogsType):

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
            default_currency (NullableCurrency): [optional]  # noqa: E501
            name (str): A human-friendly name associated to a given feed.. [optional]  # noqa: E501
            format (CatalogsFormat): [optional]  # noqa: E501
            credentials (CatalogsFeedCredentials): [optional]  # noqa: E501
            location (str): The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing.. [optional]  # noqa: E501
            preferred_processing_schedule (CatalogsFeedProcessingSchedule): [optional]  # noqa: E501
            status (CatalogsStatus): [optional]  # noqa: E501
            default_availability (ProductAvailabilityType): [optional]  # noqa: E501
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

        self.catalog_type = catalog_type
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
    def __init__(self, catalog_type, *args, **kwargs):  # noqa: E501
        """CatalogsRetailFeedsUpdateRequest - a model defined in OpenAPI

        Args:
            catalog_type (CatalogsType):

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
            default_currency (NullableCurrency): [optional]  # noqa: E501
            name (str): A human-friendly name associated to a given feed.. [optional]  # noqa: E501
            format (CatalogsFormat): [optional]  # noqa: E501
            credentials (CatalogsFeedCredentials): [optional]  # noqa: E501
            location (str): The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing.. [optional]  # noqa: E501
            preferred_processing_schedule (CatalogsFeedProcessingSchedule): [optional]  # noqa: E501
            status (CatalogsStatus): [optional]  # noqa: E501
            default_availability (ProductAvailabilityType): [optional]  # noqa: E501
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

        self.catalog_type = catalog_type
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

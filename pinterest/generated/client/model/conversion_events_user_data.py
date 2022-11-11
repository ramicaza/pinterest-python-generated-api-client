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
    from pinterest.generated.client.model.conversion_events_user_data_any_of import ConversionEventsUserDataAnyOf
    from pinterest.generated.client.model.conversion_events_user_data_any_of1 import ConversionEventsUserDataAnyOf1
    from pinterest.generated.client.model.conversion_events_user_data_any_of2 import ConversionEventsUserDataAnyOf2
    globals()['ConversionEventsUserDataAnyOf'] = ConversionEventsUserDataAnyOf
    globals()['ConversionEventsUserDataAnyOf1'] = ConversionEventsUserDataAnyOf1
    globals()['ConversionEventsUserDataAnyOf2'] = ConversionEventsUserDataAnyOf2


class ConversionEventsUserData(ModelComposed):
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
            'em': ([str],),  # noqa: E501
            'hashed_maids': ([str],),  # noqa: E501
            'client_ip_address': (str,),  # noqa: E501
            'client_user_agent': (str,),  # noqa: E501
            'ph': ([str],),  # noqa: E501
            'ge': ([str],),  # noqa: E501
            'db': ([str],),  # noqa: E501
            'ln': ([str],),  # noqa: E501
            'fn': ([str],),  # noqa: E501
            'ct': ([str],),  # noqa: E501
            'st': ([str],),  # noqa: E501
            'zp': ([str],),  # noqa: E501
            'country': ([str],),  # noqa: E501
            'external_id': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'em': 'em',  # noqa: E501
        'hashed_maids': 'hashed_maids',  # noqa: E501
        'client_ip_address': 'client_ip_address',  # noqa: E501
        'client_user_agent': 'client_user_agent',  # noqa: E501
        'ph': 'ph',  # noqa: E501
        'ge': 'ge',  # noqa: E501
        'db': 'db',  # noqa: E501
        'ln': 'ln',  # noqa: E501
        'fn': 'fn',  # noqa: E501
        'ct': 'ct',  # noqa: E501
        'st': 'st',  # noqa: E501
        'zp': 'zp',  # noqa: E501
        'country': 'country',  # noqa: E501
        'external_id': 'external_id',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ConversionEventsUserData - a model defined in OpenAPI

        Keyword Args:
            em ([str]): Sha256 hashes of lowercase version of user's email addresses. Used for matching.
            hashed_maids ([str]): Sha256 hashes of user's \"Google Advertising IDs\" (GAIDs) or \"Apple's Identifier for Advertisers\" (IDFAs). Used for matching.
            client_ip_address (str): The user's IP address, which can be either in IPv4 or IPv6 format. Used for matching.
            client_user_agent (str): The user agent string of the user's web browser.
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
            ph ([str]): Sha256 hashes of user's phone numbers, only digits with country code, area code, and number. Remove any symbols, letters, spaces and leading zeros.. [optional]  # noqa: E501
            ge ([str]): Sha256 hashes of user's gender, in lowercase. Either \"f\" or \"m\" or \"n\" for non-binary gender.. [optional]  # noqa: E501
            db ([str]): Sha256 hashes of user's date of birthday, given as year, month, and day.. [optional]  # noqa: E501
            ln ([str]): Sha256 hashes of user's last name, in lowercase.. [optional]  # noqa: E501
            fn ([str]): Sha256 hashes of user's first name, in lowercase.. [optional]  # noqa: E501
            ct ([str]): Sha256 hashes of user's city, in lowercase, and without spaces or punctuation.. [optional]  # noqa: E501
            st ([str]): Sha256 hashes of user's state, given as a two-letter code in lowercase.. [optional]  # noqa: E501
            zp ([str]): Sha256 hashes of user's zipcode, only digits.. [optional]  # noqa: E501
            country ([str]): Sha256 hashes of two-character ISO-3166 country code indicating the user's country, in lowercase.. [optional]  # noqa: E501
            external_id ([str]): Sha256 hashes of the unique id from the advertiser that identifies a user in their space, e.g. user id, loyalty id, etc.. [optional]  # noqa: E501
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
        """ConversionEventsUserData - a model defined in OpenAPI

        Keyword Args:
            em ([str]): Sha256 hashes of lowercase version of user's email addresses. Used for matching.
            hashed_maids ([str]): Sha256 hashes of user's \"Google Advertising IDs\" (GAIDs) or \"Apple's Identifier for Advertisers\" (IDFAs). Used for matching.
            client_ip_address (str): The user's IP address, which can be either in IPv4 or IPv6 format. Used for matching.
            client_user_agent (str): The user agent string of the user's web browser.
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
            ph ([str]): Sha256 hashes of user's phone numbers, only digits with country code, area code, and number. Remove any symbols, letters, spaces and leading zeros.. [optional]  # noqa: E501
            ge ([str]): Sha256 hashes of user's gender, in lowercase. Either \"f\" or \"m\" or \"n\" for non-binary gender.. [optional]  # noqa: E501
            db ([str]): Sha256 hashes of user's date of birthday, given as year, month, and day.. [optional]  # noqa: E501
            ln ([str]): Sha256 hashes of user's last name, in lowercase.. [optional]  # noqa: E501
            fn ([str]): Sha256 hashes of user's first name, in lowercase.. [optional]  # noqa: E501
            ct ([str]): Sha256 hashes of user's city, in lowercase, and without spaces or punctuation.. [optional]  # noqa: E501
            st ([str]): Sha256 hashes of user's state, given as a two-letter code in lowercase.. [optional]  # noqa: E501
            zp ([str]): Sha256 hashes of user's zipcode, only digits.. [optional]  # noqa: E501
            country ([str]): Sha256 hashes of two-character ISO-3166 country code indicating the user's country, in lowercase.. [optional]  # noqa: E501
            external_id ([str]): Sha256 hashes of the unique id from the advertiser that identifies a user in their space, e.g. user id, loyalty id, etc.. [optional]  # noqa: E501
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
              ConversionEventsUserDataAnyOf,
              ConversionEventsUserDataAnyOf1,
              ConversionEventsUserDataAnyOf2,
          ],
          'allOf': [

          ],
          'oneOf': [
          ],
        }

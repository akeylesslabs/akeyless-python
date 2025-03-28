# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from akeyless.models.attribute_type_and_value import AttributeTypeAndValue
from typing import Optional, Set
from typing_extensions import Self

class Name(BaseModel):
    """
    Name represents an X.509 distinguished name. This only includes the common elements of a DN. Note that Name is only an approximation of the X.509 structure. If an accurate representation is needed, asn1.Unmarshal the raw subject or issuer as an [RDNSequence].
    """ # noqa: E501
    country: Optional[List[StrictStr]] = Field(default=None, alias="Country")
    extra_names: Optional[List[AttributeTypeAndValue]] = Field(default=None, description="ExtraNames contains attributes to be copied, raw, into any marshaled distinguished names. Values override any attributes with the same OID. The ExtraNames field is not populated when parsing, see Names.", alias="ExtraNames")
    locality: Optional[List[StrictStr]] = Field(default=None, alias="Locality")
    names: Optional[List[AttributeTypeAndValue]] = Field(default=None, description="Names contains all parsed attributes. When parsing distinguished names, this can be used to extract non-standard attributes that are not parsed by this package. When marshaling to RDNSequences, the Names field is ignored, see ExtraNames.", alias="Names")
    serial_number: Optional[StrictStr] = Field(default=None, alias="SerialNumber")
    street_address: Optional[List[StrictStr]] = Field(default=None, alias="StreetAddress")
    __properties: ClassVar[List[str]] = ["Country", "ExtraNames", "Locality", "Names", "SerialNumber", "StreetAddress"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Name from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in extra_names (list)
        _items = []
        if self.extra_names:
            for _item_extra_names in self.extra_names:
                if _item_extra_names:
                    _items.append(_item_extra_names.to_dict())
            _dict['ExtraNames'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in names (list)
        _items = []
        if self.names:
            for _item_names in self.names:
                if _item_names:
                    _items.append(_item_names.to_dict())
            _dict['Names'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Name from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Country": obj.get("Country"),
            "ExtraNames": [AttributeTypeAndValue.from_dict(_item) for _item in obj["ExtraNames"]] if obj.get("ExtraNames") is not None else None,
            "Locality": obj.get("Locality"),
            "Names": [AttributeTypeAndValue.from_dict(_item) for _item in obj["Names"]] if obj.get("Names") is not None else None,
            "SerialNumber": obj.get("SerialNumber"),
            "StreetAddress": obj.get("StreetAddress")
        })
        return _obj



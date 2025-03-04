# coding: utf-8

"""
BrowserUp MitmProxy

___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___

The version of the OpenAPI document: 1.0.0
Contact: developers@browserup.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import conlist
from pydantic import Field
from pydantic import StrictStr

from BrowserUpMitmProxyClient.models.counter import Counter
from BrowserUpMitmProxyClient.models.error import Error
from BrowserUpMitmProxyClient.models.page_timings import PageTimings
from BrowserUpMitmProxyClient.models.verify_result import VerifyResult


class Page(BaseModel):
    """
    Page
    """

    started_date_time: datetime = Field(..., alias="startedDateTime")
    id: StrictStr = Field(...)
    title: StrictStr = Field(...)
    verifications: Optional[conlist(VerifyResult)] = Field(None, alias="_verifications")
    counters: Optional[conlist(Counter)] = Field(None, alias="_counters")
    errors: Optional[conlist(Error)] = Field(None, alias="_errors")
    page_timings: PageTimings = Field(..., alias="pageTimings")
    comment: Optional[StrictStr] = None
    additional_properties: dict[str, Any] = {}
    __properties = [
        "startedDateTime",
        "id",
        "title",
        "_verifications",
        "_counters",
        "_errors",
        "pageTimings",
        "comment",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Page:
        """Create an instance of Page from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True, exclude={"additional_properties"}, exclude_none=True
        )
        # override the default output from pydantic by calling `to_dict()` of each item in verifications (list)
        _items = []
        if self.verifications:
            for _item in self.verifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict["_verifications"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in counters (list)
        _items = []
        if self.counters:
            for _item in self.counters:
                if _item:
                    _items.append(_item.to_dict())
            _dict["_counters"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["_errors"] = _items
        # override the default output from pydantic by calling `to_dict()` of page_timings
        if self.page_timings:
            _dict["pageTimings"] = self.page_timings.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Page:
        """Create an instance of Page from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Page.parse_obj(obj)

        _obj = Page.parse_obj(
            {
                "started_date_time": obj.get("startedDateTime"),
                "id": obj.get("id"),
                "title": obj.get("title"),
                "verifications": [
                    VerifyResult.from_dict(_item) for _item in obj.get("_verifications")
                ]
                if obj.get("_verifications") is not None
                else None,
                "counters": [Counter.from_dict(_item) for _item in obj.get("_counters")]
                if obj.get("_counters") is not None
                else None,
                "errors": [Error.from_dict(_item) for _item in obj.get("_errors")]
                if obj.get("_errors") is not None
                else None,
                "page_timings": PageTimings.from_dict(obj.get("pageTimings"))
                if obj.get("pageTimings") is not None
                else None,
                "comment": obj.get("comment"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

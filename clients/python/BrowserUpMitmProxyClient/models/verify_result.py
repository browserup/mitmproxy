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
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictBool
from pydantic import StrictStr


class VerifyResult(BaseModel):
    """
    VerifyResult
    """

    result: Optional[StrictBool] = Field(None, description="Result True / False")
    name: Optional[StrictStr] = Field(None, description="Name")
    type: Optional[StrictStr] = Field(None, description="Type")
    __properties = ["result", "name", "type"]

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
    def from_json(cls, json_str: str) -> VerifyResult:
        """Create an instance of VerifyResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyResult:
        """Create an instance of VerifyResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VerifyResult.parse_obj(obj)

        _obj = VerifyResult.parse_obj(
            {
                "result": obj.get("result"),
                "name": obj.get("name"),
                "type": obj.get("type"),
            }
        )
        return _obj

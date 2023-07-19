# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .constant_value_chat_history_variable import ConstantValueChatHistoryVariable
from .constant_value_json_variable import ConstantValueJsonVariable
from .constant_value_string_variable import ConstantValueStringVariable


class TerminalNodeResultOutput_String(ConstantValueStringVariable):
    type: typing_extensions.Literal["STRING"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class TerminalNodeResultOutput_Json(ConstantValueJsonVariable):
    type: typing_extensions.Literal["JSON"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class TerminalNodeResultOutput_ChatHistory(ConstantValueChatHistoryVariable):
    type: typing_extensions.Literal["CHAT_HISTORY"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


TerminalNodeResultOutput = typing_extensions.Annotated[
    typing.Union[TerminalNodeResultOutput_String, TerminalNodeResultOutput_Json, TerminalNodeResultOutput_ChatHistory],
    pydantic.Field(discriminator="type"),
]

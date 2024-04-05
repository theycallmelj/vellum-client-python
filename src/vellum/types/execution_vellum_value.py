# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .execution_array_vellum_value import ExecutionArrayVellumValue
from .execution_chat_history_vellum_value import ExecutionChatHistoryVellumValue
from .execution_error_vellum_value import ExecutionErrorVellumValue
from .execution_function_call_vellum_value import ExecutionFunctionCallVellumValue
from .execution_json_vellum_value import ExecutionJsonVellumValue
from .execution_number_vellum_value import ExecutionNumberVellumValue
from .execution_search_results_vellum_value import ExecutionSearchResultsVellumValue
from .execution_string_vellum_value import ExecutionStringVellumValue


class ExecutionVellumValue_String(ExecutionStringVellumValue):
    type: typing.Literal["STRING"] = "STRING"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ExecutionVellumValue_Number(ExecutionNumberVellumValue):
    type: typing.Literal["NUMBER"] = "NUMBER"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ExecutionVellumValue_Json(ExecutionJsonVellumValue):
    type: typing.Literal["JSON"] = "JSON"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ExecutionVellumValue_ChatHistory(ExecutionChatHistoryVellumValue):
    type: typing.Literal["CHAT_HISTORY"] = "CHAT_HISTORY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ExecutionVellumValue_SearchResults(ExecutionSearchResultsVellumValue):
    type: typing.Literal["SEARCH_RESULTS"] = "SEARCH_RESULTS"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ExecutionVellumValue_Error(ExecutionErrorVellumValue):
    type: typing.Literal["ERROR"] = "ERROR"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ExecutionVellumValue_Array(ExecutionArrayVellumValue):
    type: typing.Literal["ARRAY"] = "ARRAY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ExecutionVellumValue_FunctionCall(ExecutionFunctionCallVellumValue):
    type: typing.Literal["FUNCTION_CALL"] = "FUNCTION_CALL"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


ExecutionVellumValue = typing.Union[
    ExecutionVellumValue_String,
    ExecutionVellumValue_Number,
    ExecutionVellumValue_Json,
    ExecutionVellumValue_ChatHistory,
    ExecutionVellumValue_SearchResults,
    ExecutionVellumValue_Error,
    ExecutionVellumValue_Array,
    ExecutionVellumValue_FunctionCall,
]

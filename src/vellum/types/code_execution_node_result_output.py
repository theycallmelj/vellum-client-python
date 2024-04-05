# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .code_execution_node_array_result import CodeExecutionNodeArrayResult
from .code_execution_node_chat_history_result import CodeExecutionNodeChatHistoryResult
from .code_execution_node_error_result import CodeExecutionNodeErrorResult
from .code_execution_node_function_call_result import CodeExecutionNodeFunctionCallResult
from .code_execution_node_json_result import CodeExecutionNodeJsonResult
from .code_execution_node_number_result import CodeExecutionNodeNumberResult
from .code_execution_node_search_results_result import CodeExecutionNodeSearchResultsResult
from .code_execution_node_string_result import CodeExecutionNodeStringResult


class CodeExecutionNodeResultOutput_String(CodeExecutionNodeStringResult):
    type: typing.Literal["STRING"] = "STRING"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class CodeExecutionNodeResultOutput_Number(CodeExecutionNodeNumberResult):
    type: typing.Literal["NUMBER"] = "NUMBER"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class CodeExecutionNodeResultOutput_Json(CodeExecutionNodeJsonResult):
    type: typing.Literal["JSON"] = "JSON"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class CodeExecutionNodeResultOutput_ChatHistory(CodeExecutionNodeChatHistoryResult):
    type: typing.Literal["CHAT_HISTORY"] = "CHAT_HISTORY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class CodeExecutionNodeResultOutput_SearchResults(CodeExecutionNodeSearchResultsResult):
    type: typing.Literal["SEARCH_RESULTS"] = "SEARCH_RESULTS"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class CodeExecutionNodeResultOutput_Error(CodeExecutionNodeErrorResult):
    type: typing.Literal["ERROR"] = "ERROR"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class CodeExecutionNodeResultOutput_Array(CodeExecutionNodeArrayResult):
    type: typing.Literal["ARRAY"] = "ARRAY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class CodeExecutionNodeResultOutput_FunctionCall(CodeExecutionNodeFunctionCallResult):
    type: typing.Literal["FUNCTION_CALL"] = "FUNCTION_CALL"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


CodeExecutionNodeResultOutput = typing.Union[
    CodeExecutionNodeResultOutput_String,
    CodeExecutionNodeResultOutput_Number,
    CodeExecutionNodeResultOutput_Json,
    CodeExecutionNodeResultOutput_ChatHistory,
    CodeExecutionNodeResultOutput_SearchResults,
    CodeExecutionNodeResultOutput_Error,
    CodeExecutionNodeResultOutput_Array,
    CodeExecutionNodeResultOutput_FunctionCall,
]

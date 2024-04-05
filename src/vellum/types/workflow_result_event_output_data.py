# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .workflow_result_event_output_data_array import WorkflowResultEventOutputDataArray
from .workflow_result_event_output_data_chat_history import WorkflowResultEventOutputDataChatHistory
from .workflow_result_event_output_data_error import WorkflowResultEventOutputDataError
from .workflow_result_event_output_data_function_call import WorkflowResultEventOutputDataFunctionCall
from .workflow_result_event_output_data_json import WorkflowResultEventOutputDataJson
from .workflow_result_event_output_data_number import WorkflowResultEventOutputDataNumber
from .workflow_result_event_output_data_search_results import WorkflowResultEventOutputDataSearchResults
from .workflow_result_event_output_data_string import WorkflowResultEventOutputDataString


class WorkflowResultEventOutputData_String(WorkflowResultEventOutputDataString):
    type: typing.Literal["STRING"] = "STRING"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowResultEventOutputData_Number(WorkflowResultEventOutputDataNumber):
    type: typing.Literal["NUMBER"] = "NUMBER"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowResultEventOutputData_Json(WorkflowResultEventOutputDataJson):
    type: typing.Literal["JSON"] = "JSON"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowResultEventOutputData_ChatHistory(WorkflowResultEventOutputDataChatHistory):
    type: typing.Literal["CHAT_HISTORY"] = "CHAT_HISTORY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowResultEventOutputData_SearchResults(WorkflowResultEventOutputDataSearchResults):
    type: typing.Literal["SEARCH_RESULTS"] = "SEARCH_RESULTS"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowResultEventOutputData_Array(WorkflowResultEventOutputDataArray):
    type: typing.Literal["ARRAY"] = "ARRAY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowResultEventOutputData_FunctionCall(WorkflowResultEventOutputDataFunctionCall):
    type: typing.Literal["FUNCTION_CALL"] = "FUNCTION_CALL"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowResultEventOutputData_Error(WorkflowResultEventOutputDataError):
    type: typing.Literal["ERROR"] = "ERROR"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


WorkflowResultEventOutputData = typing.Union[
    WorkflowResultEventOutputData_String,
    WorkflowResultEventOutputData_Number,
    WorkflowResultEventOutputData_Json,
    WorkflowResultEventOutputData_ChatHistory,
    WorkflowResultEventOutputData_SearchResults,
    WorkflowResultEventOutputData_Array,
    WorkflowResultEventOutputData_FunctionCall,
    WorkflowResultEventOutputData_Error,
]

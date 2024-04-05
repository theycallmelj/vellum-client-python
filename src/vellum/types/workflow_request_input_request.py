# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .workflow_request_chat_history_input_request import WorkflowRequestChatHistoryInputRequest
from .workflow_request_json_input_request import WorkflowRequestJsonInputRequest
from .workflow_request_number_input_request import WorkflowRequestNumberInputRequest
from .workflow_request_string_input_request import WorkflowRequestStringInputRequest


class WorkflowRequestInputRequest_String(WorkflowRequestStringInputRequest):
    type: typing.Literal["STRING"] = "STRING"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowRequestInputRequest_Json(WorkflowRequestJsonInputRequest):
    type: typing.Literal["JSON"] = "JSON"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowRequestInputRequest_ChatHistory(WorkflowRequestChatHistoryInputRequest):
    type: typing.Literal["CHAT_HISTORY"] = "CHAT_HISTORY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class WorkflowRequestInputRequest_Number(WorkflowRequestNumberInputRequest):
    type: typing.Literal["NUMBER"] = "NUMBER"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


WorkflowRequestInputRequest = typing.Union[
    WorkflowRequestInputRequest_String,
    WorkflowRequestInputRequest_Json,
    WorkflowRequestInputRequest_ChatHistory,
    WorkflowRequestInputRequest_Number,
]

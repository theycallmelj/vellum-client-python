# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .workflow_execution_node_result_event import WorkflowExecutionNodeResultEvent
from .workflow_execution_workflow_result_event import WorkflowExecutionWorkflowResultEvent


class WorkflowStreamEvent_Workflow(WorkflowExecutionWorkflowResultEvent):
    type: typing_extensions.Literal["WORKFLOW"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class WorkflowStreamEvent_Node(WorkflowExecutionNodeResultEvent):
    type: typing_extensions.Literal["NODE"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


WorkflowStreamEvent = typing_extensions.Annotated[
    typing.Union[WorkflowStreamEvent_Workflow, WorkflowStreamEvent_Node], pydantic.Field(discriminator="type")
]

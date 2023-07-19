# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .conditional_node_result import ConditionalNodeResult
from .deployment_node_result import DeploymentNodeResult
from .prompt_node_result import PromptNodeResult
from .sandbox_node_result import SandboxNodeResult
from .search_node_result import SearchNodeResult
from .terminal_node_result import TerminalNodeResult


class WorkflowNodeResultData_Prompt(PromptNodeResult):
    type: typing_extensions.Literal["PROMPT"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Sandbox(SandboxNodeResult):
    type: typing_extensions.Literal["SANDBOX"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Deployment(DeploymentNodeResult):
    type: typing_extensions.Literal["DEPLOYMENT"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Search(SearchNodeResult):
    type: typing_extensions.Literal["SEARCH"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Conditional(ConditionalNodeResult):
    type: typing_extensions.Literal["CONDITIONAL"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Terminal(TerminalNodeResult):
    type: typing_extensions.Literal["TERMINAL"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


WorkflowNodeResultData = typing_extensions.Annotated[
    typing.Union[
        WorkflowNodeResultData_Prompt,
        WorkflowNodeResultData_Sandbox,
        WorkflowNodeResultData_Deployment,
        WorkflowNodeResultData_Search,
        WorkflowNodeResultData_Conditional,
        WorkflowNodeResultData_Terminal,
    ],
    pydantic.Field(discriminator="type"),
]

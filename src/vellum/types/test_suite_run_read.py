# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .test_suite_run_exec_config import TestSuiteRunExecConfig
from .test_suite_run_state import TestSuiteRunState
from .test_suite_run_test_suite import TestSuiteRunTestSuite

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TestSuiteRunRead(pydantic.BaseModel):
    id: str
    created: dt.datetime
    test_suite: TestSuiteRunTestSuite
    state: TestSuiteRunState = pydantic.Field()
    """
    The current state of this run
    
    - `QUEUED` - Queued
    - `RUNNING` - Running
    - `COMPLETE` - Complete
    - `FAILED` - Failed
    - `CANCELLED` - Cancelled
    """

    exec_config: typing.Optional[TestSuiteRunExecConfig] = pydantic.Field(default=None)
    """
    Configuration that defines how the Test Suite should be run
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

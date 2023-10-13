# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .model_type_deprecated import ModelTypeDeprecated
from .model_version_build_config import ModelVersionBuildConfig
from .model_version_exec_config import ModelVersionExecConfig
from .model_version_read_status_enum import ModelVersionReadStatusEnum
from .provider_enum import ProviderEnum

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ModelVersionRead(pydantic.BaseModel):
    id: str = pydantic.Field(description="Vellum-generated ID that uniquely identifies this model version.")
    created: dt.datetime = pydantic.Field(description="Timestamp of when this model version was created.")
    label: str = pydantic.Field(description="Human-friendly name for this model version.")
    model_type: ModelTypeDeprecated
    provider: ProviderEnum = pydantic.Field(
        description=(
            "Which LLM provider this model version is associated with.\n"
            "\n"
            "* `ANTHROPIC` - Anthropic\n"
            "* `COHERE` - Cohere\n"
            "* `GOOGLE` - Google\n"
            "* `HOSTED` - Hosted\n"
            "* `MOSAICML` - MosaicML\n"
            "* `MYSTIC` - Mystic\n"
            "* `OPENAI` - OpenAI\n"
            "* `PYQ` - Pyq\n"
        )
    )
    external_id: str = pydantic.Field(
        description="The unique id of this model version as it exists in the above provider's system."
    )
    build_config: ModelVersionBuildConfig = pydantic.Field(
        description="Configuration used to build this model version."
    )
    exec_config: ModelVersionExecConfig = pydantic.Field(
        description="Configuration used to execute this model version."
    )
    status: typing.Optional[ModelVersionReadStatusEnum]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}

# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .search_filters_request import SearchFiltersRequest
from .search_result_merging_request import SearchResultMergingRequest
from .search_weights_request import SearchWeightsRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SearchRequestOptionsRequest(pydantic.BaseModel):
    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of results to return.
    """

    weights: typing.Optional[SearchWeightsRequest] = pydantic.Field(default=None)
    """
    The weights to use for the search. Must add up to 1.0.
    """

    result_merging: typing.Optional[SearchResultMergingRequest] = pydantic.Field(default=None)
    """
    The configuration for merging results.
    """

    filters: typing.Optional[SearchFiltersRequest] = pydantic.Field(default=None)
    """
    The filters to apply to the search.
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

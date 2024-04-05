# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...types.paginated_test_suite_run_execution_list import PaginatedTestSuiteRunExecutionList
from ...types.test_suite_run_exec_config_request import TestSuiteRunExecConfigRequest
from ...types.test_suite_run_read import TestSuiteRunRead

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestSuiteRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        test_suite_id: str,
        exec_config: TestSuiteRunExecConfigRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteRunRead:
        """
        Trigger a Test Suite and create a new Test Suite Run

        Parameters:
            - test_suite_id: str. The ID of the Test Suite to run

            - exec_config: TestSuiteRunExecConfigRequest. Configuration that defines how the Test Suite should be run

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum import (
            TestSuiteRunDeploymentReleaseTagExecConfigDataRequest,
            TestSuiteRunExecConfigRequest_DeploymentReleaseTag,
        )
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suite_runs.create(
            test_suite_id="string",
            exec_config=TestSuiteRunExecConfigRequest_DeploymentReleaseTag(
                data=TestSuiteRunDeploymentReleaseTagExecConfigDataRequest(
                    deployment_id="string",
                    tag="string",
                ),
                test_case_ids=["string"],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", "v1/test-suite-runs"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"test_suite_id": test_suite_id, "exec_config": exec_config})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"test_suite_id": test_suite_id, "exec_config": exec_config}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TestSuiteRunRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TestSuiteRunRead:
        """
        Retrieve a specific Test Suite Run by ID

        Parameters:
            - id: str. A UUID string identifying this test suite run.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suite_runs.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", f"v1/test-suite-runs/{jsonable_encoder(id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TestSuiteRunRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_executions(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTestSuiteRunExecutionList:
        """
        Parameters:
            - id: str. A UUID string identifying this test suite run.

            - limit: typing.Optional[int]. Number of results to return per page.

            - offset: typing.Optional[int]. The initial index from which to return the results.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suite_runs.list_executions(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suite-runs/{jsonable_encoder(id)}/executions",
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "limit": limit,
                        "offset": offset,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTestSuiteRunExecutionList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTestSuiteRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        test_suite_id: str,
        exec_config: TestSuiteRunExecConfigRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteRunRead:
        """
        Trigger a Test Suite and create a new Test Suite Run

        Parameters:
            - test_suite_id: str. The ID of the Test Suite to run

            - exec_config: TestSuiteRunExecConfigRequest. Configuration that defines how the Test Suite should be run

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum import (
            TestSuiteRunDeploymentReleaseTagExecConfigDataRequest,
            TestSuiteRunExecConfigRequest_DeploymentReleaseTag,
        )
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suite_runs.create(
            test_suite_id="string",
            exec_config=TestSuiteRunExecConfigRequest_DeploymentReleaseTag(
                data=TestSuiteRunDeploymentReleaseTagExecConfigDataRequest(
                    deployment_id="string",
                    tag="string",
                ),
                test_case_ids=["string"],
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", "v1/test-suite-runs"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"test_suite_id": test_suite_id, "exec_config": exec_config})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"test_suite_id": test_suite_id, "exec_config": exec_config}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TestSuiteRunRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TestSuiteRunRead:
        """
        Retrieve a specific Test Suite Run by ID

        Parameters:
            - id: str. A UUID string identifying this test suite run.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suite_runs.retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", f"v1/test-suite-runs/{jsonable_encoder(id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TestSuiteRunRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_executions(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTestSuiteRunExecutionList:
        """
        Parameters:
            - id: str. A UUID string identifying this test suite run.

            - limit: typing.Optional[int]. Number of results to return per page.

            - offset: typing.Optional[int]. The initial index from which to return the results.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suite_runs.list_executions(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suite-runs/{jsonable_encoder(id)}/executions",
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "limit": limit,
                        "offset": offset,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTestSuiteRunExecutionList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

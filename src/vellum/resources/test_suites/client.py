# This file was auto-generated by Fern from our API Definition.

import json
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...types.named_test_case_variable_value_request import NamedTestCaseVariableValueRequest
from ...types.paginated_test_suite_test_case_list import PaginatedTestSuiteTestCaseList
from ...types.test_suite_test_case import TestSuiteTestCase
from ...types.test_suite_test_case_bulk_operation_request import TestSuiteTestCaseBulkOperationRequest
from ...types.test_suite_test_case_bulk_result import TestSuiteTestCaseBulkResult

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestSuitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_test_suite_test_cases(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTestSuiteTestCaseList:
        """
        List the Test Cases associated with a Test Suite

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - limit: typing.Optional[int]. Number of results to return per page.

            - offset: typing.Optional[int]. The initial index from which to return the results.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suites.list_test_suite_test_cases(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases",
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
            return pydantic_v1.parse_obj_as(PaginatedTestSuiteTestCaseList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def upsert_test_suite_test_case(
        self,
        id: str,
        *,
        upsert_test_suite_test_case_request_id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        input_values: typing.Sequence[NamedTestCaseVariableValueRequest],
        evaluation_values: typing.Sequence[NamedTestCaseVariableValueRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteTestCase:
        """
        Upserts a new test case for a test suite, keying off of the optionally provided test case id.

        If an id is provided and has a match, the test case will be updated. If no id is provided or no match
        is found, a new test case will be appended to the end.

        Note that a full replacement of the test case is performed, so any fields not provided will be removed
        or overwritten with default values.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - upsert_test_suite_test_case_request_id: typing.Optional[str]. The ID of the Test Case to upsert. If specified and a match is found, the existing Test Case will be updated. If specified and no match is found, a Test Case will be created with the provided ID. If not provided, a new Test Case will be created with an auto-generated ID.

            - label: typing.Optional[str].

            - input_values: typing.Sequence[NamedTestCaseVariableValueRequest]. Values for each of the Test Case's input variables

            - evaluation_values: typing.Sequence[NamedTestCaseVariableValueRequest]. Values for each of the Test Case's evaluation variables

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suites.upsert_test_suite_test_case(
            id="id",
            input_values=[],
            evaluation_values=[],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"input_values": input_values, "evaluation_values": evaluation_values}
        if upsert_test_suite_test_case_request_id is not OMIT:
            _request["id"] = upsert_test_suite_test_case_request_id
        if label is not OMIT:
            _request["label"] = label
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
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
            return pydantic_v1.parse_obj_as(TestSuiteTestCase, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def test_suite_test_cases_bulk(
        self,
        id: str,
        *,
        request: typing.Sequence[TestSuiteTestCaseBulkOperationRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[typing.List[TestSuiteTestCaseBulkResult]]:
        """
        Created, replace, and delete Test Cases within the specified Test Suite in bulk

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - request: typing.Sequence[TestSuiteTestCaseBulkOperationRequest].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum import (
            BulkCreateTestSuiteTestCaseDataRequest,
            NamedTestCaseVariableValueRequest_String,
            TestSuiteTestCaseBulkOperationRequest_Create,
        )
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suites.test_suite_test_cases_bulk(
            id="string",
            request=[
                TestSuiteTestCaseBulkOperationRequest_Create(
                    id="string",
                    data=BulkCreateTestSuiteTestCaseDataRequest(
                        label="string",
                        input_values=[NamedTestCaseVariableValueRequest_String()],
                        evaluation_values=[NamedTestCaseVariableValueRequest_String()],
                    ),
                )
            ],
        )
        """
        with self._client_wrapper.httpx_client.stream(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases-bulk",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _text in _response.iter_lines():
                    if len(_text) == 0:
                        continue
                    yield pydantic_v1.parse_obj_as(typing.List[TestSuiteTestCaseBulkResult], json.loads(_text))  # type: ignore
                return
            _response.read()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_test_suite_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an existing test case for a test suite, keying off of the test case id.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - test_case_id: str. An id identifying the test case that you'd like to delete

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suites.delete_test_suite_test_case(
            id="id",
            test_case_id="test_case_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases/{jsonable_encoder(test_case_id)}",
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
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTestSuitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_test_suite_test_cases(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTestSuiteTestCaseList:
        """
        List the Test Cases associated with a Test Suite

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - limit: typing.Optional[int]. Number of results to return per page.

            - offset: typing.Optional[int]. The initial index from which to return the results.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suites.list_test_suite_test_cases(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases",
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
            return pydantic_v1.parse_obj_as(PaginatedTestSuiteTestCaseList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def upsert_test_suite_test_case(
        self,
        id: str,
        *,
        upsert_test_suite_test_case_request_id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        input_values: typing.Sequence[NamedTestCaseVariableValueRequest],
        evaluation_values: typing.Sequence[NamedTestCaseVariableValueRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteTestCase:
        """
        Upserts a new test case for a test suite, keying off of the optionally provided test case id.

        If an id is provided and has a match, the test case will be updated. If no id is provided or no match
        is found, a new test case will be appended to the end.

        Note that a full replacement of the test case is performed, so any fields not provided will be removed
        or overwritten with default values.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - upsert_test_suite_test_case_request_id: typing.Optional[str]. The ID of the Test Case to upsert. If specified and a match is found, the existing Test Case will be updated. If specified and no match is found, a Test Case will be created with the provided ID. If not provided, a new Test Case will be created with an auto-generated ID.

            - label: typing.Optional[str].

            - input_values: typing.Sequence[NamedTestCaseVariableValueRequest]. Values for each of the Test Case's input variables

            - evaluation_values: typing.Sequence[NamedTestCaseVariableValueRequest]. Values for each of the Test Case's evaluation variables

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suites.upsert_test_suite_test_case(
            id="id",
            input_values=[],
            evaluation_values=[],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"input_values": input_values, "evaluation_values": evaluation_values}
        if upsert_test_suite_test_case_request_id is not OMIT:
            _request["id"] = upsert_test_suite_test_case_request_id
        if label is not OMIT:
            _request["label"] = label
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
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
            return pydantic_v1.parse_obj_as(TestSuiteTestCase, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def test_suite_test_cases_bulk(
        self,
        id: str,
        *,
        request: typing.Sequence[TestSuiteTestCaseBulkOperationRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[typing.List[TestSuiteTestCaseBulkResult]]:
        """
        Created, replace, and delete Test Cases within the specified Test Suite in bulk

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - request: typing.Sequence[TestSuiteTestCaseBulkOperationRequest].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum import (
            BulkCreateTestSuiteTestCaseDataRequest,
            NamedTestCaseVariableValueRequest_String,
            TestSuiteTestCaseBulkOperationRequest_Create,
        )
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suites.test_suite_test_cases_bulk(
            id="string",
            request=[
                TestSuiteTestCaseBulkOperationRequest_Create(
                    id="string",
                    data=BulkCreateTestSuiteTestCaseDataRequest(
                        label="string",
                        input_values=[NamedTestCaseVariableValueRequest_String()],
                        evaluation_values=[NamedTestCaseVariableValueRequest_String()],
                    ),
                )
            ],
        )
        """
        async with self._client_wrapper.httpx_client.stream(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases-bulk",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _text in _response.aiter_lines():
                    if len(_text) == 0:
                        continue
                    yield pydantic_v1.parse_obj_as(typing.List[TestSuiteTestCaseBulkResult], json.loads(_text))  # type: ignore
                return
            await _response.aread()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_test_suite_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an existing test case for a test suite, keying off of the test case id.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - test_case_id: str. An id identifying the test case that you'd like to delete

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suites.delete_test_suite_test_case(
            id="id",
            test_case_id="test_case_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/",
                f"v1/test-suites/{jsonable_encoder(id)}/test-cases/{jsonable_encoder(test_case_id)}",
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
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.post_submodel_element_by_path_submodel_repo_extent import PostSubmodelElementByPathSubmodelRepoExtent
from ...models.post_submodel_element_by_path_submodel_repo_level import PostSubmodelElementByPathSubmodelRepoLevel
from ...models.result import Result
from ...models.submodel_element import SubmodelElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Client,
    json_body: SubmodelElement,
    level: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoLevel
    ] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Dict[str, Any]:
    url = "{}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}".format(
        client.base_url, submodelIdentifier=submodel_identifier, idShortPath=id_short_path
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_level: Union[Unset, None, str] = UNSET
    if not isinstance(level, Unset):
        json_level = level.value if level else None

    params["level"] = json_level

    json_extent: Union[Unset, None, str] = UNSET
    if not isinstance(extent, Unset):
        json_extent = extent.value if extent else None

    params["extent"] = json_extent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Result, SubmodelElement]]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Result.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Result.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = Result.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Result.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = Result.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SubmodelElement.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Result.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Result, SubmodelElement]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Client,
    json_body: SubmodelElement,
    level: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoLevel
    ] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Response[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
        json_body (SubmodelElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Result, SubmodelElement]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
        client=client,
        json_body=json_body,
        level=level,
        extent=extent,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Client,
    json_body: SubmodelElement,
    level: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoLevel
    ] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Optional[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
        json_body (SubmodelElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Result, SubmodelElement]
    """

    return sync_detailed(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
        client=client,
        json_body=json_body,
        level=level,
        extent=extent,
    ).parsed


async def asyncio_detailed(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Client,
    json_body: SubmodelElement,
    level: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoLevel
    ] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Response[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
        json_body (SubmodelElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Result, SubmodelElement]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
        client=client,
        json_body=json_body,
        level=level,
        extent=extent,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Client,
    json_body: SubmodelElement,
    level: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoLevel
    ] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, None, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Optional[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, None, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
        json_body (SubmodelElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Result, SubmodelElement]
    """

    return (
        await asyncio_detailed(
            submodel_identifier=submodel_identifier,
            id_short_path=id_short_path,
            client=client,
            json_body=json_body,
            level=level,
            extent=extent,
        )
    ).parsed

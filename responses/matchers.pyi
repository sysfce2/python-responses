from typing import (
    Any,
    Callable,
    Optional,
    Dict,
)

JSONDecodeError = ValueError


def _create_key_val_str(input_dict: Dict[Any, Any]) -> str: ...

def json_params_matcher(
    params: Optional[Dict[str, Any]]
) -> Callable[..., Any]: ...

def urlencoded_params_matcher(
    params: Optional[Dict[str, str]]
) -> Callable[..., Any]: ...

def query_param_matcher(
    params: Optional[Dict[str, str]]
) -> Callable[..., Any]: ...

def request_kwargs_matcher(
    kwargs: Optional[Dict[str, Any]]
) -> Callable[..., Any]: ...

def header_matcher(
    headers: Dict[str, str],
    strict_match: bool = ...
) -> Callable[..., Any]: ...
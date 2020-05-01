from typing import Dict, Any

class JSONRPCException(Exception):
    CODE = None
    MESSAGE = None

    def __init__(self, id: str = None, errors: dict = None) -> None:
        self._id = id
        self._errors = errors or {}

    @property
    def id(self):
        return self._id

    @property
    def errors(self):
        return self._errors


class JSONRPCMethodNotFoundException(JSONRPCException):
    CODE = -32601
    MESSAGE = "Method not found."


class JSONRPCInvalidParamsException(JSONRPCException):
    CODE = -32602
    MESSAGE = "Invalid params."


class JSONRPCInvalidRequestException(JSONRPCException):
    CODE = -32600
    MESSAGE = "Invalid Request."


class JSONRPCParseErrorException(JSONRPCException):
    CODE = -32700
    MESSAGE = "Parse error."

class JSONRPCServerErrorException(JSONRPCException):
    def __init__(self, id: str = None, errors: dict = None, code: int = -32000, msg: str = ""):
        super().__init__(id, errors)
        self.CODE = code
        self.MESSAGE = msg

class JSONRPCUserException(Exception):
    def __init__(self, code: int, msg: str, **kwargs):
        self.exception_info: Dict[str, Any] = {}
        self.exception_info["code"] = code
        self.exception_info["message"] = msg
        self.exception_info.update(**kwargs)

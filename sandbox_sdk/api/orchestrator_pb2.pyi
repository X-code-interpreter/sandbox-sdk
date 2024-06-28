from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SandboxConfig(_message.Message):
    __slots__ = ("templateID", "kernelVersion", "maxInstanceLength", "sandboxID", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    KERNELVERSION_FIELD_NUMBER: _ClassVar[int]
    MAXINSTANCELENGTH_FIELD_NUMBER: _ClassVar[int]
    SANDBOXID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    templateID: str
    kernelVersion: str
    maxInstanceLength: int
    sandboxID: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, templateID: _Optional[str] = ..., kernelVersion: _Optional[str] = ..., maxInstanceLength: _Optional[int] = ..., sandboxID: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SandboxCreateRequest(_message.Message):
    __slots__ = ("sandbox",)
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    sandbox: SandboxConfig
    def __init__(self, sandbox: _Optional[_Union[SandboxConfig, _Mapping]] = ...) -> None: ...

class SandboxCreateResponse(_message.Message):
    __slots__ = ("privateIP",)
    PRIVATEIP_FIELD_NUMBER: _ClassVar[int]
    privateIP: str
    def __init__(self, privateIP: _Optional[str] = ...) -> None: ...

class SandboxRequest(_message.Message):
    __slots__ = ("sandboxID",)
    SANDBOXID_FIELD_NUMBER: _ClassVar[int]
    sandboxID: str
    def __init__(self, sandboxID: _Optional[str] = ...) -> None: ...

class RunningSandbox(_message.Message):
    __slots__ = ("config", "startTime")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    config: SandboxConfig
    startTime: _timestamp_pb2.Timestamp
    def __init__(self, config: _Optional[_Union[SandboxConfig, _Mapping]] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SandboxListResponse(_message.Message):
    __slots__ = ("sandboxes",)
    SANDBOXES_FIELD_NUMBER: _ClassVar[int]
    sandboxes: _containers.RepeatedCompositeFieldContainer[RunningSandbox]
    def __init__(self, sandboxes: _Optional[_Iterable[_Union[RunningSandbox, _Mapping]]] = ...) -> None: ...

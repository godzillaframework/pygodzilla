#!/usr/bin/env python3

from typing import Any, Callable, Optional, Protocol, runtime_checkable
import zmq
import zmq.asyncio


@runtime_checkable
class GodzillaMQClient(Protocol):  
    @property
    def context(self) -> zmq.Context:
        ...

    def connect(self, address: str) -> None:
        ...

    def close(self) -> None:
        ...

    def send(self, message: bytes) -> None:
        ...

    def poll(self, timeout: int) -> bool:
        ...

    def recv(self) -> bytes:
        ...

    def request(self, message: bytes) -> Any:
        ...


@runtime_checkable
class AsyncGodzillaMQClient(Protocol):  
    @property
    def context(self) -> zmq.asyncio.Context:
        ...

    def connect(self, address: str) -> None:
        ...

    def close(self) -> None:
        ...

    async def send(self, message: bytes) -> None:
        ...

    async def poll(self, timeout: int) -> bool:
        ...

    async def recv(self) -> bytes:
        ...

    async def request(self, message: bytes) -> Any:
        ...


@runtime_checkable
class GodzillaMQBroker(Protocol):  
    def listen(self, address: str, channel: str) -> None:
        ...

    def close(self) -> None:
        ...


@runtime_checkable
class GodzillaMQWorker(Protocol):  
    def listen(
        self, address: str, msg_handler: Callable[[bytes], Optional[bytes]]
    ) -> None:
        ...

    def close(self) -> None:
        ...
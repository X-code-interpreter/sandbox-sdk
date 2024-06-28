# Sandbox SDK

This is a Python SDK for our code interpreter, which can be used to create secure sandboxes and interact with it.

Most of the interfaces and implementations in this SDK are ported from [e2b](https://github.com/e2b-dev/E2B/tree/main/packages/python-sdk), which is the SOTA of the open source sandbox project.

This is an async-based SDK, which is different from the e2b. It means almost all interfaces are coroutines and need to be used with [asyncio](https://docs.python.org/3/library/asyncio.html) library.
This reason why adopting coroutine is that the original e2b SDK is extremely slow (at least in my environment), e.g., it takes more than 10 seconds to start a process.

## Example

Do not forget to call `close`:

```python
from sandbox_sdk import Sandbox

sandbox = await Sandbox.create(cwd="/code/app")

proc = await sandbox.process.start("pwd")
output = await proc.wait()
assert output.stdout == "/code/app"
await sandbox.close()
```

We also support `with` statement:

```python
from sandbox_sdk.code_interpreter import CodeInterpreter

async with await CodeInterpreter.create() as sandbox:
    await sandbox.notebook.exec_cell("x = 1")

    result = await sandbox.notebook.exec_cell("x+=1; x")
    assert result.text == "2"
```

## Backend

Note that this SDK should not be used directly, it has to be used after depolyment of our sandbox backend.

The sandbox backend is also ported from [e2b infra](https://github.com/e2b-dev/infra) and remove some components which could be omitted in our small-scale depolyment.

For more about backend, please refer to the [corresponding repo](https://github.com/X-code-interpreter/sandbox-backend).

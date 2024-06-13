# Sandbox SDK

This is a Python SDK for our code interpreter, which can be used to create secure sandboxes and interact with it.

Most of the interfaces and implementations in this SDK are ported from [e2b](https://github.com/e2b-dev/E2B/tree/main/packages/python-sdk), which is the SOTA of the open source sandbox project.

Nearly all interfaces is compatiable with e2b, so please refer to their docs if you want to try it.

## Backend

Note that this SDK should not be used directly, it has to be used after depolyment of our sandbox backend.

The sandbox backend is also ported from [e2b infra](https://github.com/e2b-dev/infra) and remove some components which could be omitted in our small-scale depolyment.

For more about backend, please refer to the [corresponding repo](https://github.com/X-code-interpreter/sandbox-backend).

from sandbox_sdk.code_interpreter import CodeInterpreter
import logging


def test_basic(caplog):
    caplog.set_level(logging.DEBUG)
    with CodeInterpreter() as sandbox:
        result = sandbox.notebook.exec_cell("x =1; x")
        assert result.text == "1"

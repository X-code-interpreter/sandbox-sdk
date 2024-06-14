from sandbox_sdk.code_interpreter import CodeInterpreter


def test_bash():
    with CodeInterpreter() as sandbox:
        result = sandbox.notebook.exec_cell("!pwd")
        assert "".join(result.logs.stdout).strip() == "/home/user"

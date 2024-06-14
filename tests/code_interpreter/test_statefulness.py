from sandbox_sdk.code_interpreter import CodeInterpreter


def test_stateful():
    with CodeInterpreter() as sandbox:
        sandbox.notebook.exec_cell("x = 1")

        result = sandbox.notebook.exec_cell("x+=1; x")
        assert result.text == "2"

from typer.testing import CliRunner

from litcomp.cli import app


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert "literature-compiler" in result.output

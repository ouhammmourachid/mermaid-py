import tomllib
from pathlib import Path


def test_project_urls_are_defined_for_pypi_metadata():
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"

    with pyproject.open("rb") as fh:
        metadata = tomllib.load(fh)

    urls = metadata["project"].get("urls", {})
    classifiers = metadata["project"].get("classifiers", [])

    assert urls["Homepage"] == "https://github.com/ouhammmourachid/mermaid-py"
    assert urls["Repository"] == "https://github.com/ouhammmourachid/mermaid-py"
    assert urls["Issues"] == "https://github.com/ouhammmourachid/mermaid-py/issues"
    assert urls["Documentation"] == "https://github.com/ouhammmourachid/mermaid-py#readme"
    assert "Programming Language :: Python :: 3.9" in classifiers
    assert "Programming Language :: Python :: 3.12" in classifiers

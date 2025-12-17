# Mermaid-py

this package works as an interface for the famous mermaid-js library that uses scripts to create diagrams.

[![Code Coverage](https://codecov.io/gh/ouhammmourachid/mermaid-py/graph/badge.svg?token=732C2PA73Z)](https://codecov.io/gh/ouhammmourachid/mermaid-py)
[![GitHub LICENSE](https://img.shields.io/github/license/ouhammmourachid/mermaid-py)](https://github.com/ouhammmourachid/mermaid-py/blob/main/LICENSE)
[![Mounthly Download](https://img.shields.io/pypi/dm/mermaid-py)](https://pypistats.org/packages/mermaid-py)
[![latest version](https://img.shields.io/pypi/v/mermaid-py.svg?style=flat)](https://pypi.org/project/mermaid-py/)
[![supported python version](https://img.shields.io/pypi/pyversions/mermaid-py)](https://pypi.org/project/mermaid-py)
[![ruff badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mermaid-py on snyk](https://snyk.io/advisor/python/mermaid-py/badge.svg)](https://snyk.io/advisor/python/mermaid-py)


## Description

mermaid-py is a dynamic Python library designed to serve as a seamless interface for
the renowned Mermaid library. Built upon the powerful capabilities of Python, mermaid-py
empowers developers and data enthusiasts to effortlessly create stunning diagrams, flowcharts,
and visualizations directly within their Python environments.


## Examples

first install the package using pip:

```bash
pip install mermaid-py
```

- using `Mermaid` and `Graph` classes:
```python
import mermaid as md
from mermaid.graph import Graph

render = md.Mermaid("""
stateDiagram-v2
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
""")
render # !! note this only works in the notebook that rendered the html.
```

<p align="center">
   <img src="https://github.com/user-attachments/assets/8476ec24-b41f-4a88-9c30-a2478a2c0fd8" alt="Example Flowchart"
    style="width: 20%;">
</p>

- using `mermaidjs` magic function in a notebook first `import mermaid as md`:

```python
%%mermaidjs # with --img flag in case your notebook doesn't render HTML
flowchart LR
    A-->B
    B-->C
```

<p align="center">
    <img src="https://github.com/ouhammmourachid/mermaid-py/assets/93659459/d4d1b993-a33d-4eb0-82ae-2ad39bf30e90" alt="Example Flowchart"
    style="width: 20%;">
</p>

- using `FlowChart` etc ...

```python
from mermaid import *
from mermaid.flowchart import *

diagram = Mermaid(Flowchart(...))

diagram
```
- more examples on [mermaid](https://www.kaggle.com/code/ouhammourachid/mermaid-py) and [test-mermaid](https://www.kaggle.com/code/ouhammourachid/testing-mermaid-py)

## Server

By default, the library uses the mermaid.ink service [github](https://github.com/jihchi/mermaid.ink) for generating diagrams. The service can be run locally using docker, following instructions [here](https://github.com/jihchi/mermaid.ink?tab=readme-ov-file#launch-a-container).

The `MERMAID_INK_SERVER` environment variable can be used to specify the server to use, for example.

## List of Diagrames
- [x] [~~FlowChart~~](https://mermaid.js.org/syntax/flowchart.html)
- [x] [~~Sequence Diagram~~](https://mermaid.js.org/syntax/sequenceDiagram.html)
- [ ] [Class Diagram](https://mermaid.js.org/syntax/classDiagram.html)
- [x] [~~State Diagram~~](https://mermaid.js.org/syntax/stateDiagram.html)
- [x] [~~Entity Relationship Diagram~~](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)
- [x] [~~User Journey~~](https://mermaid.js.org/syntax/userJourney.html)
- [ ] [Gantt](https://mermaid.js.org/syntax/gantt.html)
- [x] [~~Pie Chart~~](https://mermaid.js.org/syntax/pie.html)
- [ ] [Quadrant Chart](https://mermaid.js.org/syntax/quadrantChart.html)
- [x] [~~Requirement Diagram~~](https://mermaid.js.org/syntax/requirementDiagram.html)
- [ ] [Gitgraph (Git) Diagram](https://mermaid.js.org/syntax/gitgraph.html)
- [ ] [C4 Diagram 🦺⚠️](https://mermaid.js.org/syntax/c4.html)
- [x] [~~Mindmaps~~](https://mermaid.js.org/syntax/mindmap.html)
- [ ] [Timeline](https://mermaid.js.org/syntax/timeline.html)
- [ ] [Zenuml](https://mermaid.js.org/syntax/zenuml.html)
- [ ] [Sankey](https://mermaid.js.org/syntax/sankey.html)
- [ ] [XYChart 🔥](https://mermaid.js.org/syntax/xyChart.html)
- [ ] [Block Diagram 🔥](https://mermaid.js.org/syntax/block.html)
- [ ] [Packet 🔥](https://mermaid.js.org/syntax/packet.html)
- [ ] [Kanban 🔥](https://mermaid.js.org/syntax/kanban.html)
- [ ] [Architecture 🔥](https://mermaid.js.org/syntax/architecture.html)
- [ ] [Radar 🔥](https://mermaid.js.org/syntax/radar.html)
- [ ] [Treemap 🔥](https://mermaid.js.org/syntax/treemap.html)

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or want to get in touch, you can reach out to me at [contact.ouhammou@gmail.com](contact.ouhammou@gmail.com).

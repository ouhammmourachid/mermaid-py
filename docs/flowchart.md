This module provides functionality for creating and rendering flowcharts.

Usage:
    1. Import the module: `import flowchart`
    2. Create a new flowchart object: `chart = flowchart.Flowchart()`
    3. Add nodes and connections to the flowchart:
        - `chart.add_node("Node 1")`
        - `chart.add_node("Node 2")`
        - `chart.add_connection("Node 1", "Node 2")`
    4. Render the flowchart: `chart.render()`

Note:
    - The flowchart is rendered using the Mermaid syntax.
    - To build the documentation, run `mkdocs build`.

Example:
    ```python
    import flowchart

    chart = flowchart.Flowchart()
    chart.add_node("Start")
    chart.add_node("End")
    chart.add_connection("Start", "End")
    chart.render()
    ```

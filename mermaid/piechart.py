from mermaid.graph import Graph


class PieChart(Graph):
    def __init__(self,
                 title: str,
                 data: dict[str, float],
                 show_data: bool = False):
        super().__init__(title, '')
        self.data: dict[str, float] = data
        self.show_data: bool = show_data
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        showData: str = ' showData' if self.show_data else ''
        script: str = f'\npie{showData}'

        for key, value in self.data.items():
            script += f'\n\t"{key}" : {value}'

        self.script += script + '\n'

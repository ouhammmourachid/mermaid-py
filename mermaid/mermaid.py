import base64
import uuid

import requests


class Mermaid:
    def __init__(self, diagram: str):
        """this is methode for creating an Mermaid object
        Parameters
        ----------
        diagram : str
            a string that contains the text of the diagrame like this one
            ```mermaid
            graph TD;
                A-->B;
                A-->C;
                B-->D;
                C-->D;
            ```
        """
        self._diagram = self._process_diagram(diagram)
        self._uid = uuid.uuid4()

    @staticmethod
    def _process_diagram(diagram: str) -> str:
        graphbytes = diagram.encode('utf8')
        base64_bytes = base64.b64encode(graphbytes)
        diagram = base64_bytes.decode('ascii')
        return diagram

    def _repr_html_(self) -> str:

        response = requests.get('https://mermaid.ink/svg/' + self._diagram)
        return response.text

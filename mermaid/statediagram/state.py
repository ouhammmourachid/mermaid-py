"""State module.

This module contains the classes to represent states in a state diagram.
"""
from typing import Optional

from mermaid import text_to_snake_case


class State:
    """State class.

    This class represents a state in a state diagram.

    Attributes:
        id_ (str): The ID of the state.
        content (str): The content of the state.
        sub_states (list[State]): The sub-states of the state.
    """
    def __init__(self,
                 id_: str,
                 content: str = '',
                 sub_states: Optional[list['State']] = None,
                 transitions: Optional[list['BaseTransition']] = None) -> None:
        """Initialize a new State.

        Args:
            id_ (str): The ID of the state.
            content (str): The content of the state.
            sub_states (Optional[list[State]]): The sub-states of the state.
        """
        self.id_: str = text_to_snake_case(id_)
        self.content: str = content if content else id_
        self.sub_states: list['State'] = sub_states if sub_states else []
        self.transitions: list['BaseTransition'] = transitions if transitions else []

    def __str__(self) -> str:
        """Return the string representation of the state.
        """
        string: str = f'{self.id_} : {self.content}'

        if len(self.sub_states):
            string += f'\nstate {self.id_} {{'
            for state in self.sub_states:
                string += f'\n\t{state}'
            
            for transition in self.transitions:
                string += f'\n\t{str(transition)}'

            string += '\n}'

        return string


class Start(State):
    """Start class.

    This class represents the start state in a state diagram.
    """
    def __init__(self) -> None:
        super().__init__(id_='[*]')
        self.id_: str = '[*]'

    def __str__(self) -> str:
        return f'{self.id_}'


class End(State):
    """End class.

    This class represents the end state in a state diagram.
    """
    def __init__(self) -> None:
        super().__init__(id_='[*]')
        self.id_: str = '[*]'

    def __str__(self) -> str:
        return f'{self.id_}'

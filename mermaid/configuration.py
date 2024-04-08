from enum import Enum


class Themes(Enum):
    """Enum class for themes

    args:
        Enum: Enum class

    methods:
        value: returns the value of the Enum class
    """
    DEFAULT = 'default'
    FOREST = 'forest'
    DARK = 'dark'
    NEUTRAL = 'neutral'
    BASE = 'base'


class Config:
    """Config class for mermaid diagrams

    args:
        theme: Themes = Themes.DEFAULT
        primary_color: Optional[str] = None
        primary_text_color: Optional[str] = None
        primary_border_color: Optional[str] = None
        line_color: Optional[str] = None
        secondary_color: Optional[str] = None
        tertiary_color: Optional[str] = None

    methods:
        __init__: initializes the class
        __str__: returns the string representation of the class
    """
    def __init__(self,
                 theme: Themes = Themes.DEFAULT,
                 primary_color: str | None = None,
                 primary_text_color: str | None = None,
                 primary_border_color: str | None = None,
                 line_color: str | None = None,
                 secondary_color: str | None = None,
                 tertiary_color: str | None = None) -> None:
        """Initializes the class

        args:
            theme: Themes = Themes.DEFAULT
            primary_color: Optional[str] = None
            primary_text_color: Optional[str] = None
            primary_border_color: Optional[str] = None
            line_color: Optional[str] = None
            secondary_color: Optional[str] = None
            tertiary_color: Optional[str] = None
        """
        self.theme: Themes = theme
        self.primary_color: str | None = primary_color
        self.primary_text_color: str | None = primary_text_color
        self.primary_border_color: str | None = primary_border_color
        self.line_color: str | None = line_color
        self.secondary_color: str | None = secondary_color
        self.tertiary_color: str | None = tertiary_color

    def __str__(self) -> str:
        """Returns the string representation of the class

        returns:
            str: string representation of the class
        """
        string: str = '%%{\n\tinit: {\n'

        string += f'\t\t"theme": "{self.theme.value}",\n\t\t"themeVariables": ' + '{\n'
        if self.primary_color:
            string += f'\t\t\t"primaryColor": "{self.primary_color}",\n'
        if self.primary_text_color:
            string += f'\t\t\t"primaryTextColor": "{self.primary_text_color}",\n'
        if self.primary_border_color:
            string += f'\t\t\t"primaryBorderColor": "{self.primary_border_color}",\n'
        if self.line_color:
            string += f'\t\t\t"lineColor": "{self.line_color}",\n'
        if self.secondary_color:
            string += f'\t\t\t"secondaryColor": "{self.secondary_color}",\n'
        if self.tertiary_color:
            string += f'\t\t\t"tertiaryColor": "{self.tertiary_color}",\n'
        if string.endswith(',\n'):
            string = string[:-2] + '\n'
        string += '\t\t}\n'
        string += '\t}\n}%%\n'
        return string

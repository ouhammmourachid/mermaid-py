from typing import Optional, Union


class Entity:
    def __init__(self,
                 name: str,
                 attributes: dict[str, Union[list[str], str]] = None) -> None:
        self.name: str = name
        self.attributes: dict[str, Union[
            list[str], str]] = attributes if attributes is not None else {}

    def __str__(self) -> str:
        string_attributes: str = self.build_attributes()
        string: str = ''.join([self.name, '{\n', string_attributes, '}'])
        return string

    def update_attributes(self, attributes: dict[str, str]) -> None:
        self.attributes.update(attributes)

    def add_attribute(self,
                      name: str,
                      type_: str,
                      constrint: Optional[str] = None,
                      comment: Optional[str] = None) -> None:
        attribute_def: list[str] = [type_]
        if constrint is not None:
            attribute_def.append(constrint)
        if comment is not None:
            attribute_def.append(comment)
        self.attributes[name] = attribute_def

    def build_attributes(self) -> str:
        string_attributes: str = ''
        for att_name, att_def in self.attributes.items():
            string: str = ''
            if isinstance(att_def, str):
                string = f'\t{att_def} {att_name}\n'
            else:
                if len(att_def) == 1:
                    string = f'{att_def[0]} {att_name}\n'
                elif len(att_def) == 2:
                    if att_def[1] in ['PK', 'FK', 'UK']:
                        string = f'\t{att_def[0]} {att_name} {att_def[1]}\n'
                    else:
                        string = f'\t{att_def[0]} {att_name} "{att_def[1]}"\n'
                else:
                    string = f'\t{att_def[0]} {att_name} {att_def[1]} "{att_def[2]}"\n'
            string_attributes += string
        return string_attributes

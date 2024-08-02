from dataclasses import dataclass


@dataclass
class Icon:
    name: str
    type_: str
    version: str = "v1"

    def __str__(self) -> str:
        if self.version == "v1":
            return f"{self.type_} {self.name}"
        elif self.version == "v2":
            return f"{self.type_}:{self.name}"
        return f" {self.type_}:{self.name} "

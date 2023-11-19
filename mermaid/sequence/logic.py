from mermaid.sequence.link import Link

class Loop:
    def __init__(self, condition:str, link:list[Link]):
        self.condition = condition
        self.link = link
    
    def __str__(self) -> str:
        return f'\tloop {self.condition}\n' + ''.join([str(link) for link in self.link]) + '\tend\n'

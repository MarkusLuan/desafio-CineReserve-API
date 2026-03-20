import enum

class AbstractEnum (enum.Enum):
    def __init__(self, ordinal: int, label: str=""):
        super().__init__()
        
        if not label:
            label = self.name.title()

        self.ordinal = ordinal
        self.label = label
    
    def __str__(self) -> str:
        return self.label
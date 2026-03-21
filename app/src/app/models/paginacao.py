from dataclasses import dataclass

@dataclass
class Paginacao:
    first_result: int
    max_results: int

    def __init__(self, first_result = 0, max_results = 20):
        self.first_result = first_result
        self.max_results = max_results
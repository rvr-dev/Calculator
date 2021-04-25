from dataclasses import dataclass


@dataclass
class Expression:
    """Expression data type for Calculator class"""
    sign: str = None
    result: float = None
    next_number: float = None

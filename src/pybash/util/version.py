from typing import Optional

class VersionInfo:
    def __init__(
            self,
            major: int,
            minor: int,
            micro: int,
            /,
            *,
            beta: Optional[bool] = None,
            alpha: Optional[bool] = None,
            ) -> None:
        self.major = major
        self.minor = minor
        self.micro = micro
        if beta and alpha:
            raise ValueError("can not mix beta and alpha")
        self.beta = beta
        self.alpha = alpha

    def __eq__(self, value) -> bool:
        if isinstance(value, str):
            value = value.split(".")

        try:
            return (self[0] == value[0]) and (self[1] == value[1]) and (self[2] == self[2]) and len(self) == len(value)
        except IndexError:
            return False

    def __repr__(self) -> str:
        _repr = f"{self.major}.{self.minor}.{self.micro}"
        if self.beta or self.alpha:
            _repr += " "
        if self.beta:
            return _repr + "beta"
        
        elif self.alpha:
            return _repr + "alpha"
        
        else:
            return _repr
    
    def __len__(self) -> int:
        return 3

    def __getitem__(self, index: int) -> int:
        if index == 0:
            return self.major
        
        if index == 1:
            return self.minor
        
        if index == 2:
            return self.micro
        
        raise IndexError("index out of range")
class VersionInfo:
    def __init__(self, major: int, minor: int, micro: int) -> None:
        self.major = major
        self.minor = minor
        self.micro = micro

    def __eq__(self, value) -> bool:
        if isinstance(value, str):
            value = value.split(".")

        return (self[0] == value[0]) and (self[1] == value[1]) and (self[2] == self[2])

    def __repr__(self):
        return f"{self.major}.{self.minor}.{self.micro}"

    def __getitem__(self, index: int):
        if index == 0:
            return self.major
        
        if index == 1:
            return self.minor
        
        if index == 2:
            return self.micro
        
        raise IndexError("index out of range")
class BaseModel:
    def to_dict(self):
        out = {}
        for keys, values in self.__dict__.items():
            out[keys] = values
        return out

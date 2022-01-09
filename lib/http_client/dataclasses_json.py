import dataclasses
import json


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def dumps(data):
    return json.dumps(data, cls=EnhancedJSONEncoder)


# example
if __name__ == '__main__':
    @dataclasses.dataclass
    class MyClass:
        id: int
        name: str


    my_class = MyClass(1, "zuzuka")
    js = dumps(my_class)
    print(js)

    print(dict(my_class))

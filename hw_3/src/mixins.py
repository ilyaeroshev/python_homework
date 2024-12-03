from copy import deepcopy
import numpy as np


class StrMixin:
    def __str__(self):
        return str(self.value)


class WritableMixin:
    def write(self, file):
        file.write(str(self))


class GetterSetterArrayMixin:
    @property
    def array(self):
        return deepcopy(self.value)

    @array.setter
    def array(self, next_value):
        self.value = deepcopy(next_value)


class ValueMixin:
    def __init__(self, value) -> None:
        self.value = value


class ArrayLike(
    ValueMixin,
    StrMixin,
    WritableMixin,
    GetterSetterArrayMixin,
    np.lib.mixins.NDArrayOperatorsMixin,
):
    _HANDLED_TYPES = (np.ndarray, list)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get("out", ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (ArrayLike,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, ArrayLike) else x for x in inputs)
        if out:
            kwargs["out"] = tuple(
                x.value if isinstance(x, ArrayLike) else x for x in out
            )
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == "at":
            return None
        else:
            return type(self)(result)


np.random.seed(0)

a = ArrayLike(np.random.randint(0, 10, (10, 10)))
b = ArrayLike(np.random.randint(0, 10, (10, 10)))

with open("../artifacts/3.2/matrix+.txt", "w") as file:
    (a + b).write(file)

with open("../artifacts/3.2/matrix*.txt", "w") as file:
    (a * b).write(file)

with open("../artifacts/3.2/matrix@.txt", "w") as file:
    (a @ b).write(file)

# Python - Inheritance

Class inheritance in Python: subclasses, `isinstance`, `issubclass`, `type`, `super()` and method overriding.

| File | Description |
| ---- | ----------- |
| `0-lookup.py` | `lookup(obj)` returns the list of attributes and methods of an object |
| `1-my_list.py` | `MyList`, a subclass of `list` with `print_sorted()` |
| `2-is_same_class.py` | `is_same_class(obj, a_class)`: is `obj` exactly an instance of `a_class`? |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)`: is `obj` an instance of `a_class` or one of its subclasses? |
| `4-inherits_from.py` | `inherits_from(obj, a_class)`: is `obj` an instance of a strict subclass of `a_class`? |
| `5-base_geometry.py` | An empty class `BaseGeometry` |
| `6-base_geometry.py` | `BaseGeometry.area()` raises an `Exception` |
| `7-base_geometry.py` | Adds `integer_validator(name, value)` |
| `8-rectangle.py` | `Rectangle(BaseGeometry)` with a validated private width and height |
| `9-rectangle.py` | Adds `area()` and `__str__()` to `Rectangle` |
| `10-square.py` | `Square(Rectangle)` with a validated private size |
| `11-square.py` | Adds `__str__()` that prints `[Square] <width>/<height>` |
| `tests/1-my_list.txt` | Doctests for `MyList` |
| `tests/7-base_geometry.txt` | Doctests for `BaseGeometry` |

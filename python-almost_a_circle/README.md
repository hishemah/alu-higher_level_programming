# Python - Almost a circle

A small object-oriented project: a `Base` class that manages ids and JSON/CSV serialization, a `Rectangle` that inherits from it, and a `Square` that inherits from `Rectangle`, all covered by unittests.

| File | Description |
| ---- | ----------- |
| `models/base.py` | `Base`: automatic ids, `to_json_string`, `from_json_string`, `save_to_file`, `load_from_file`, `create`, `save_to_file_csv`, `load_from_file_csv`, `draw` |
| `models/rectangle.py` | `Rectangle(Base)`: validated `width`, `height`, `x`, `y`; `area`, `display`, `__str__`, `update`, `to_dictionary` |
| `models/square.py` | `Square(Rectangle)`: `size`, `__str__`, `update`, `to_dictionary` |
| `tests/test_models/test_base.py` | Unittests for `Base` |
| `tests/test_models/test_rectangle.py` | Unittests for `Rectangle` |
| `tests/test_models/test_square.py` | Unittests for `Square` |

Run all the tests from this folder:

```bash
python3 -m unittest discover tests
```

# Python - Input/Output

Reading and writing files with the `with` statement, and serializing Python objects to and from JSON.

| File | Description |
| ---- | ----------- |
| `0-read_file.py` | `read_file(filename)` prints a UTF8 text file to stdout |
| `1-write_file.py` | `write_file(filename, text)` writes a string to a file and returns the number of characters written |
| `2-append_write.py` | `append_write(filename, text)` appends a string to a file and returns the number of characters added |
| `3-to_json_string.py` | `to_json_string(my_obj)` returns the JSON representation of an object |
| `4-from_json_string.py` | `from_json_string(my_str)` returns the object represented by a JSON string |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)` writes an object to a file as JSON |
| `6-load_from_json_file.py` | `load_from_json_file(filename)` creates an object from a JSON file |
| `7-add_item.py` | Adds all command-line arguments to a list saved in `add_item.json` |
| `8-class_to_json.py` | `class_to_json(obj)` returns the dictionary description of an object for JSON serialization |
| `9-student.py` | `Student` class with `to_json()` |
| `10-student.py` | `Student.to_json(attrs=None)` can filter the attributes returned |
| `11-student.py` | Adds `reload_from_json(json)` to replace all attributes of a `Student` |
| `12-pascal_triangle.py` | `pascal_triangle(n)` returns Pascal's triangle of `n` rows as a list of lists |

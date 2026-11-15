#!/usr/bin/python3
"""Module that defines the Base class of all the shapes of this project."""
import csv
import json


class Base:
    """Base of all the shapes: manages their id and their serialization.

    Attributes:
        __nb_objects (int): the number of instances created without an id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): the id of the new instance; when it is None, the
                next automatic id is used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by the JSON string json_string.

        Args:
            json_string (str): a JSON string of a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of list_objs to the file <Class name>.json.

        Args:
            list_objs (list): a list of instances that inherit from Base.
        """
        dictionaries = []
        if list_objs is not None:
            dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance with all its attributes set from dictionary.

        Args:
            **dictionary: the attribute names and values to set.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances read from the file <Class name>.json.

        An empty list is returned if the file doesn't exist.
        """
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                dictionaries = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in dictionaries]

    @classmethod
    def _csv_fields(cls):
        """Return the CSV column names for this class."""
        if cls.__name__ == "Square":
            return ["id", "size", "x", "y"]
        return ["id", "width", "height", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write list_objs to the file <Class name>.csv.

        A Rectangle row is id,width,height,x,y and a Square row is
        id,size,x,y.

        Args:
            list_objs (list): a list of instances that inherit from Base.
        """
        fields = cls._csv_fields()
        with open(cls.__name__ + ".csv", "w", newline="",
                  encoding="utf-8") as f:
            writer = csv.writer(f)
            for obj in list_objs or []:
                values = obj.to_dictionary()
                writer.writerow([values[name] for name in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances read from the file <Class name>.csv.

        An empty list is returned if the file doesn't exist.
        """
        fields = cls._csv_fields()
        try:
            with open(cls.__name__ + ".csv", newline="",
                      encoding="utf-8") as f:
                rows = list(csv.reader(f))
        except FileNotFoundError:
            return []
        return [cls.create(**dict(zip(fields, map(int, row))))
                for row in rows if row]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the rectangles and squares with the turtle module.

        Args:
            list_rectangles (list): Rectangle instances to draw.
            list_squares (list): Square instances to draw.
        """
        import turtle

        pen = turtle.Turtle()
        pen.screen.bgcolor("#f2f2f2")
        pen.pensize(3)
        for shapes, color in ((list_rectangles, "#2a6f97"),
                              (list_squares, "#c44536")):
            pen.color(color)
            for shape in shapes:
                pen.penup()
                pen.goto(shape.x, shape.y)
                pen.pendown()
                for _ in range(2):
                    pen.forward(shape.width)
                    pen.left(90)
                    pen.forward(shape.height)
                    pen.left(90)
        turtle.exitonclick()

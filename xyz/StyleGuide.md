# Style guide
## Variable, function and method naming
Use lower case for variable, function and method names. Use snake_case, i.e. underscore to separate composed words, e.g. `all_names = ['alice', 'bob']`

## Class naming
Start class names with a capital letter and use camel-case for composed words, e.g. `class GraduateStudent()`

## Comments
Focus on _why_ not _what_ comments, use `#` to start a comment

## Docstring
For each function/method, include a docstring with the following format:
```python
"""one line description, what does the function do?

attribute_name: description

returns: description
"""
```

## Type annotations
Use type annotations for function and method headers to indicate types of parameters and return value.

Generally, variables do not need type annotations.

## Examples
A function
```python
def remove_middle(text: str) -> str:
    """Removes middle character of odd length text, a copy otherwise.

    text: string to operate on

    return: even length version of text
    """
```

Additionally, for classes provide a description and list of attributes:
```python
class Point:
    """Represents a point in 2-D space.

    attributes: 
        x: x-coordinates of the point
        y: y-coordinates of the point
    """

    def get_distance_from_origin(self) -> float:
        """Returns distance of point from origin (0,0)"""
    
    def get_distance_to_point(self, other: Point) -> float:
        """Returns distance to other point"""
```

#!/usr/bin/python3

"define locked class"

class LockedClass:
    """
    prevent user form dynamically creating new instance
    except if the attribute is first_name
    """
    __slots__ = ["first_name"]

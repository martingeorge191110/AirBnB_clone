#!/usr/bin/env python3
"""User model class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class that will create attributies """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

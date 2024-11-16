#!/usr/bin/env python3
"""Review model class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class that will create attributies"""
    place_id = ""
    user_id = ""
    text = ""

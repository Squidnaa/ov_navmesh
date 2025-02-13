import omni.ui as ui
from omni.ui import color as cl

class NavGuiStyles:
    """Style sheet for navmesh extension GUI."""

    """Color scheme for GUI."""
    red = cl("#e52c39")
    yellow = cl("#e5d62c")
    green = cl("#1abc9c")

    """Styles for GUI elements."""
    

    solid_red_button = {
        "Button": {
            "background_color": red,
            "border_radius": 5,
        },
        "Button.Label": {
            "text_color": cl.black,
            "font_size": 14,
        }
    }


    solid_yellow_button = {
        "Button": {
            "background_color": yellow,
            "border_radius": 5,
        },
        "Button.Label": {
            "text_color": cl.black,
            "font_size": 14,
        }
    }

    solid_green_button = {
        "Button": {
            "background_color": green,
            "border_radius": 5,
        },
        "Button.Label": {
            "text_color": cl.black,
            "font_size": 14,
        }
    }
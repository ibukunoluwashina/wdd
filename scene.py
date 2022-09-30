# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.


    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")
# Call the main function so that
# this program will start executing.
main()
import arcade

def create_shapes(win_width, win_height):
    shape_list = []
    win_width = win_width/4
    rectangle = arcade.create_rectangle_filled(win_width, 350, 100, 200, arcade.color.BABY_PINK)
    circle = arcade.create_ellipse(win_width*3, 350, 50, 50, arcade.color.PUCE_RED)
    line = arcade.create_line(win_width, 650, win_width*3, 75, arcade.color.CANARY_YELLOW)
    shape_list.append(rectangle)
    shape_list.append(circle)
    shape_list.append(line)
    return shape_list

def create_more_shapes(current_shapes, win_height):
    poly_points = [(400, win_height - 50), (350, win_height-100), (450, win_height - 100)]
    triangle = arcade.create_polygon(poly_points, arcade.color.BLOND)
    current_shapes.append(triangle)

def main():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 700
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Demo with Functions")
    shapes_to_draw = create_shapes(WINDOW_WIDTH, WINDOW_HEIGHT)
    print(f"window size is{WINDOW_WIDTH}")
    arcade.start_render()
    for shapes in shapes_to_draw:
        shapes_to_draw
    arcade.finish_render()

    arcade.run()

main()
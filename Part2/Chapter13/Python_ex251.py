# Don't run.

# Painting figure
# without polymorphism
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
        a_shape.draw_circle()

# Paint figure
# with polymorphism
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    a_shape.draw()

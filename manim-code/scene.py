from manim import *


class VectorDrawing(VectorScene):
    def construct(self):

        # My stuff
        scalar = Dot(point=[-3, 0, 0], radius=.2, color=GREEN)
        arrow = Line(start=[2, 3, 0], end=[5,1, 0], color=YELLOW).add_tip()

        polygon_points = [
            [-1, -1, 0],
            [3, -2, 0],
            [2, 2, 0],
            [-2, 3, 0]
        ]
        bivector=Polygon(*polygon_points, color=RED, fill_color=RED, fill_opacity=1.)

        self.add_axes()
        self.add_plane()
        #plane = NumberPlane(x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=10, y_length=5)
        #basis = self.get_basis_vectors()
        #self.add(plane)
        

        self.play(Create(scalar))  # show the scalar
        self.play(Create(arrow))
        self.play(Create(bivector))
        #self.add_vector([4 ,2])

        self.wait()

# Call on CLI with:
# manim -pql --format=gif scene.py VectorDrawing
# to (p)lay after generating in (ql) low-quality and generate format=gif instead of mp4 default

# To only generate the last frame of the scene execute this:
#manim -sqh <file.py> SceneName
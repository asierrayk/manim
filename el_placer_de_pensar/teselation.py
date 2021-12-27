from manim import *
from el_placer_de_pensar import PortalPalette


class Teselation(Scene):
    def construct(self):
        title = Text("Teselaciones", color=BLACK)
        self.play(Write(title, run_time=1))
        self.wait()
        self.play(title.animate.to_corner(UL))
        definition = Text(
            "Una teselación es un conjunto de figuras que recubren el plano cumpliendo dos condiciones:",
            text2color={"teselación": PortalPalette.BLUE},
            color=BLACK
        )


        self.play(Write(definition, run_time=2))
        self.wait()

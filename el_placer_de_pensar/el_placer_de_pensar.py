from manim import *

class Palette:
    DARK = "#072448"
    BLUE = "#54d2d2"
    YELLOW = "#ffcb00"
    ORANGE = "#f8aa4b"
    RED = "#ff6150"

    GREEN = "#54d254"

class ElPlacerDePensarV1(Scene):
    def construct(self):
        self.wait()
        el_placer_de_pensar = Tex(
            "El Placer de Pensar"
        )
        self.play(Write(el_placer_de_pensar, run_time=1))
        self.wait(1)
        self.play(FadeOut(el_placer_de_pensar))
        self.wait()


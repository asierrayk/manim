from manim import *

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


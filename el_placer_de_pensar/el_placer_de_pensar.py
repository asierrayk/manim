from manim import *
import manimpango

class Palette:
    BACKGROUND = "#ece6e2"

class PortalPalette:
        LIGHT_ORANGE = "#ff9a00"
        ORANGE = "#ff5d00"
        BLACK = "#000000"
        BLUE = "#0065ff"
        LIGHT_BLUE = "#00a2ff"

class ElPlacerDePensarV1(Scene):
    def construct(self):
        # self.wait()
        # el_placer_de_pensar = Tex(
        #     "El $\mathbb{P}$lacer de $\mathbb{P}$ensar}", color=Palette.BLACK
        # )
        # self.play(Write(el_placer_de_pensar, run_time=1))
        # self.wait(1)
        # self.play(FadeOut(el_placer_de_pensar))
        # self.wait()


        placer = Text(
            "El Placer",
            color=BLACK,
            gradient=(PortalPalette.BLUE, PortalPalette.LIGHT_BLUE),
            font="TeX Gyre Pagella Math",
            # text2color={"El": PortalPalette.LIGHT_BLUE, " Placer": PortalPalette.BLUE}
        ).scale(2).move_to(LEFT)

        p = Text(
            "P",
            color=PortalPalette.LIGHT_BLUE,
            font="TeX Gyre Pagella Math",
        ).scale(3)

        pensar = Text(
            "de Pensar",
            color=BLACK,
            font="TeX Gyre Pagella Math",
            gradient=(PortalPalette.ORANGE, PortalPalette.LIGHT_ORANGE),
            # text2color={"de": PortalPalette.LIGHT_ORANGE, " Pensar": PortalPalette.ORANGE}
        ).scale(2).next_to(placer, RIGHT)
        circle = Circle(
            color=PortalPalette.LIGHT_BLUE,
            fill_color=PortalPalette.LIGHT_ORANGE,
            fill_opacity=1,
            gradient=(PortalPalette.LIGHT_BLUE, PortalPalette.LIGHT_ORANGE)
        ).surround(p, buffer_factor=1.5)

        VGroup(placer, pensar).move_to(ORIGIN)
        placer_copy = placer.copy()

        self.play(Write(placer), run_time=1)
        self.add(placer_copy)
        self.wait(0.5)
        self.play(TransformMatchingShapes(placer, pensar, run_time=2, path_arc=PI/2))
        self.wait(1)

        self.remove(placer_copy)
        self.play(
            TransformMatchingShapes(placer, p),
            Transform(pensar, circle),
            run_time=1.5
        )
        self.wait(5)

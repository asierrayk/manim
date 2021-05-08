from manim import *

from el_placer_de_pensar.el_placer_de_pensar import Palette


class Square5(Scene):
    AMOUNT_EXAMPLES = 5
    def construct(self):
        title = Tex(r"\underline{Cuadrados perfectos}", color=Palette.BLUE)
        title.to_corner(UL)
        self.add(title)

        numbers = list(range(1, self.AMOUNT_EXAMPLES + 1))

        elements = []
        for i, n in enumerate(numbers):
            element = MathTex(f"{n}", "^2", f" = {n}\\cdot{n}", f" = {n ** 2}")
            if i == 0:
                element.move_to(np.array((-3.0, 1.0, 0.0)), aligned_edge=LEFT)
            else:
                element.next_to(elements[-1], DOWN)
                element.align_to(elements[-1], LEFT)
            elements.append(element)



        groups = []
        for i in range(4):
            group_elements = [e[i] for e in elements]
            if i == 0:
                vdots = MathTex("\\vdots")
                vdots.next_to(elements[-1][i], DOWN)
                group_elements.append(vdots)

            group = VGroup(*group_elements)
            self.play(Write(group, run_time=3))
            groups.append(group)

        self.wait()


        for i, e in enumerate(elements):
            if i != 4:
                self.remove(e)
        self.remove(vdots)
        element_25 = elements[-1]
        element_25.move_to(ORIGIN)
        self.wait()





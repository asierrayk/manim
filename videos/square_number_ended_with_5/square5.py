from manim import *

from el_placer_de_pensar.el_placer_de_pensar import Palette


class Square5(Scene):
    AMOUNT_EXAMPLES = 5
    def construct(self):
        title = Tex(r"\underline{Cuadrados perfectos}", color=Palette.BLUE)
        title.to_corner(UL)
        self.add(title)

        numbers = list(range(1, self.AMOUNT_EXAMPLES + 1))

        elements_stages = ["number", "number_square", "product", "square"]
        # equals to
        elements = []
        for i, n in enumerate(numbers):
            element = dict(
                index=i,
                number=MathTex(f"{n}"),
                number_square=MathTex(f"{n}^2"),
                product=MathTex(f"{n}^2 = {n}\\cdot{n}"),
                square=MathTex(f"{n}^2 = {n}\\cdot{n} = {n ** 2}")
            )
            for stage in elements_stages:
                if i == 0:
                    element[stage].move_to(np.array((-3.0, 1.0, 0.0)), aligned_edge=LEFT)
                else:
                    element[stage].next_to(elements[-1][stage], DOWN)
            elements.append(element)



        groups = []
        for i, stage in enumerate(elements_stages):
            vdots = MathTex("\\vdots")
            vdots.next_to(elements[-1][stage], DOWN)
            group = VGroup(*[e[stage] for e in elements], vdots)
            if i == 0:
                self.play(Write(group, run_time=4))
            else:
                self.play(ReplacementTransform(groups[-1], group))
            groups.append(group)

        self.wait()





from manim import *

class practice(Scene):
    def construct(self):
        T=MathTex(r"e^{ i\frac{\pi}{2} } 2^3 \sum \pi")
        U=Text("and it was delicious")
        T.scale(2)
        T.set_color(BLUE_B)
        U.set_color(YELLOW_B)
        self.play(Write(T),run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(T,U))
        self.wait(1)
        self.play(FadeOutAndShift(U))

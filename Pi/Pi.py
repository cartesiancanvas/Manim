from manim import*
import math
import os

class Pi(Scene):
    def construct(self):
        mobject= RegularPolygon(4).scale(2)
        self.play(Create(mobject))
        pi_4=4*math.sin(math.pi/4)
        U=Text(str(round(pi_4,3)))
        P=Text("Pi =")
        U.shift(3*DOWN,RIGHT)
        P.shift(LEFT,3*DOWN)
        self.play(Write(P))
        self.play(Write(U))
        for i in range(4,30,2):
            pi=i*math.sin(math.pi/i)
            T=Text(str(round(pi,3)))
            T.shift(3*DOWN,RIGHT)
            self.play(Transform(mobject,RegularPolygon(i).scale(2)))
            self.play(Transform(U,T))
                      
if __name__ == "__main__":
    print(os.getcwd())
    # print(f"manim {__file__} -p")
    os.system(f"manim {__file__} -p")
           

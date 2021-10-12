from manim import*
import numpy as np
import math
from itertools import cycle

class Parametric_1(GraphScene):
   
     def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-10,
            x_max=10,
            y_min=-10,
            Y_max=10,
            num_graph_anchor_points=100,
            graph_origin=ORIGIN,
            axes_color=BLUE,
            x_labeled_nums=range(-10, 12, 2),
            **kwargs
        )
        self.function_color = RED
     def construct(self):
         t=Text("Hi there").scale(1)
         u=Text("We can use Manim to Create different Graphs from their parametric equations").scale(0.5)
         l=Text("One of the most beautiful and elegant curve is the Butterfly Curve").scale(0.5)
         m=Text("discovered by Temple H. Fay of University of Southern Mississippi in 1989").scale(0.5)
         svg=SVGMobject("butterfly-with-wings-perspective-from-top-view.svg").scale(2.5)
         h=Text("Thank You")
         u.set_color=(GREEN)
         t.set_color(GOLD)
         l.set_color=(RED)
         m.set_color=(YELLOW)
         t.shift(UP*2)
         h.shift(UP*2,RIGHT*2)
         self.play(Write(t))
         self.wait(1)
         self.play(ReplacementTransform(t,u))
         self.wait(0.5)
         self.play(ReplacementTransform(u,l))
         self.wait(0.5)
         self.play(ReplacementTransform(l,m))
         self.wait(0.5)
         self.play(Uncreate(m),run_time=1)
         self.wait(0.5)
         colors =cycle([YELLOW,GREEN,PURPLE,PINK,GRAY,TEAL])
         for i in range(len(svg)):
             color = next(colors)
             svg[i].set_color(color)
             svg[i].set_stroke(color,2)
         self.play(DrawBorderThenFill(svg,rate_func=linear),run_time=5)
         self.play(FadeOut(svg))
         self.wait(1)
         self.setup_axes(animate=True)
         dot=Dot(radius=0.07,color=PURPLE)
         Colors=[YELLOW_E,RED_E,PURPLE_E,PINK]
         butterfly = ParametricFunction(self.butter,t_min=0,t_max=24*math.pi)
         butterfly.set_color(Colors)
         dot.add_updater(lambda mob:mob.move_to(butterfly.get_end()))
         self.add(dot)
         self.play(Create(butterfly),run_time=35,rate_func=smooth)
         self.wait(1)
         self.play(Uncreate(butterfly))
         self.wait(0.5)
         self.play(FadeOut(dot))
         self.play(Write(h))
         self.wait(1)
         self.play(Uncreate(h))          
         self.wait(1)
         
         
     def butter(self,t):                #Parametric equation of the butterfly curve.
        return [

            np.sin(t)*(math.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t%12)**5),
            np.cos(t)*(math.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t%12)**5),
            0
            
        ]

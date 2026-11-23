from manim import *

config.background_color = "#F7F9FC"


class IntroCard(Scene):
    def construct(self):
        box = RoundedRectangle(width=10.5, height=3.8, corner_radius=0.25, color="#0A5CC4", fill_color="#EFF6FF", fill_opacity=1)
        title = Text("10 秒样片 · 原子能力合龙", font="Noto Sans CJK SC", font_size=44, color="#122640").shift(UP * 0.55)
        sub = Text("20 行 Python 替代 AE 关键帧 · 1080p@25fps", font="Noto Sans CJK SC", font_size=26, color="#334155").shift(DOWN * 0.45)
        ring = SurroundingRectangle(title, color="#DC2626", buff=0.14, corner_radius=0.12, stroke_width=4)
        self.play(FadeIn(box), Write(title), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.2), Create(ring), run_time=0.8)
        self.wait(1.2)

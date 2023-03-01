from manim import *


class Main(Scene):
    def blink(self, obj):
        temp = obj.copy().set_color(RED)
        self.play(FadeIn(temp, run_time=0.3))
        self.play(FadeOut(temp))

    def credit(self):
        visualisation_text = Text("Visualisation by : Vignesh Babu JS(22f1001225)")
        mentor_text = Text("Mentored by : Karthik Thiagarajan").next_to(visualisation_text, DOWN)
        self.play(Write(visualisation_text))
        self.play(Write(mentor_text))

    def construct(self):
        # Union,Intersection and Difference
        title_text = MarkupText("<b><u>SET OPERATIONS</u></b>").to_edge(UP).scale(0.75)
        sub_title_text = MarkupText("<b><u>Intersection,Union and Difference </u></b>").next_to(title_text, DOWN).scale(0.55)

        set_A = Circle(radius=1.65, color=RED_E, fill_opacity=0.75, stroke_width=3, stroke_color=WHITE).move_to(LEFT * 2)

        set_B = Circle(radius=1.65, color=BLUE, fill_opacity=0.75, stroke_width=3, stroke_color=WHITE).move_to(RIGHT + LEFT * 1.7)

        text_set_A = MathTex("A").move_to(2.75 * LEFT + UP)
        text_set_B = MathTex("B").move_to(2.15 * RIGHT + UP + 2 * LEFT)

        sets_group = Group(set_A, set_B, text_set_A, text_set_B)

        i = Intersection(set_A, set_B, fill_color=RED_B, fill_opacity=0.75)
        u = Union(set_A, set_B, fill_color=YELLOW, fill_opacity=0.75)
        dif = Difference(set_A, set_B, fill_color=GREEN, fill_opacity=0.75)

        i_text = Group(MathTex(r"A \cap B", font_size=25).move_to(0.45 * UP), Text("Intersection", font_size=25)).move_to(RIGHT * 5 + UP * 2.5)
        u_text = Group(MathTex(r"A \cup B", font_size=25).move_to(0.45 * UP), Text("Union", font_size=25)).move_to(RIGHT * 5)
        dif_text = Group(MathTex(r"A \setminus B  \ or \ A-B ", font_size=25).move_to(0.45 * UP), Text("Difference", font_size=25)).move_to(
            RIGHT * 5 + DOWN * 2.5)

        self.play(Create(title_text, run_time=3))
        self.wait(0.5)
        self.play(Create(sub_title_text, run_time=3))
        self.wait(0.5)
        self.play(title_text.animate.to_corner(LEFT))
        self.wait(0.25)
        self.play(sub_title_text.animate.to_corner(LEFT))
        self.wait(0.5)

        self.play(Create(set_A, rate_func=linear), Create(set_B), Create(text_set_A), Create(text_set_B))
        self.wait(0.5)

        self.play(FadeIn(i))
        self.play(i.animate.scale(0.6).move_to(RIGHT * 3 + UP * 2.5))
        self.wait()

        self.play(FadeIn(u))
        self.play(u.animate.scale(0.45).move_to(RIGHT * 3))
        self.wait()

        self.play(FadeIn(dif))
        self.play(dif.animate.scale(0.5).move_to(RIGHT * 3 + DOWN * 2.5))
        self.wait(0.5)

        self.play(sets_group.animate.move_to(LEFT * 4))
        self.wait(0.5)

        self.play(FadeIn(i_text))
        self.wait(0.25)
        self.play(FadeIn(u_text))
        self.wait(0.25)
        self.play(FadeIn(dif_text))

        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self
                  .mobjects])

        # Subsets,Supersets and Complements
        sub_title_text = MarkupText("<b><u> Subsets, Supersets and Complements </u></b>").to_edge(UP).to_edge(LEFT).scale(0.75)

        Uni_set = Rectangle(height=4, width=6).move_to(3 * LEFT)
        Uni_text = MathTex("U").move_to(Uni_set.get_center()).move_to(LEFT + 1.5 * UP + 0.2 * RIGHT)
        set_A = Circle(radius=1.5, stroke_color=WHITE, stroke_width=3, fill_color=RED, fill_opacity=0.75).move_to(Uni_set.get_center())
        set_A_text = MathTex("A").move_to(2.2 * LEFT + UP)

        self.play(Create(sub_title_text))
        self.play(sub_title_text.animate.to_edge(LEFT))

        self.play(Create(Uni_set))
        self.play(Create(Uni_text))
        self.wait()
        self.play(Create(set_A))
        self.play(Create(set_A_text))
        self.wait()

        self.play(ShowPassingFlash(set_A.copy().set_color(BLUE), run_time=1, time_width=0.5))
        self.play(ShowPassingFlash(Uni_set.copy().set_color(BLUE), run_time=1, time_width=0.5))
        self.wait()

        text_1 = Text("Here in this diagram,", font_size=25).next_to(Uni_set, 2.4 * RIGHT + 0.4 * UP)
        A_sub_U_text = MathTex("A \subset U \ or \ U \supset A", font_size=28).next_to(text_1, 0.3 * DOWN)

        self.play(Create(text_1))
        self.play(Create(A_sub_U_text, run_time=3))
        self.wait(0.5)

        A_complement = Exclusion(Uni_set, set_A, fill_opacity=0.75, fill_color=YELLOW)

        self.play(FadeIn(A_complement))
        self.wait(0.1)
        self.play(A_complement.animate.scale(0.5).next_to(A_sub_U_text, 2 * DOWN))
        self.wait(0.3)
        self.play(FadeIn(MathTex(r"-\ \ \ A^{'}\ or\ A^{c}", font_size=30).next_to(A_complement, RIGHT)))
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self
                  .mobjects])

        # DeMorgan's Theorem-I
        sub_title_text = MarkupText("<b><u> De Morgan's Theorem </u></b>").to_edge(UP).to_edge(LEFT).scale(0.75)
        Uni_set = Rectangle(height=4, width=5.8).move_to(0.3 * UP)
        Uni_text = MathTex("U").move_to(Uni_set.get_center()).move_to(1.5 * UP + 2.5 * RIGHT)
        set_A = Circle(radius=1.3, stroke_color=WHITE, stroke_width=3, fill_color=RED, fill_opacity=0.75).move_to(Uni_set.get_center()).move_to(LEFT)
        set_B = Circle(radius=1.3, stroke_color=WHITE, stroke_width=3, fill_color=BLUE, fill_opacity=0.75).move_to(Uni_set.get_center()).move_to(
            0.2 * RIGHT)
        set_A_text = MathTex("A").move_to(UP + 1.5 * LEFT)
        set_B_text = MathTex("B").move_to(0.9 * UP + 0.75 * RIGHT)

        RECT_GRP = Group(Uni_set, Uni_text, set_A, set_B, set_B_text, set_A_text)
        Uni_set, Uni_text, set_A, set_B, set_B_text, set_A_text = RECT_GRP

        self.play(Create(sub_title_text))
        self.play(sub_title_text.animate.to_edge(LEFT))

        self.play(Create(Uni_set))
        self.play(Create(Uni_text))
        self.play(Create(set_A))
        self.play(Create(set_A_text))
        self.play(Create(set_B))
        self.play(Create(set_B_text))
        self.wait(0.5)

        theorem_stat_1 = MathTex(r"(A \cap B)^{'}=A^{'} \cup B^{'}").next_to(Uni_set, DOWN)
        self.play(Create(theorem_stat_1))
        self.wait()
        self.play(RECT_GRP.animate.to_corner(LEFT))
        self.play(theorem_stat_1.animate.next_to(sub_title_text))

        A_int_B_text = MathTex(r"A \cap B \ =").next_to(theorem_stat_1, 1.5 * DOWN).shift(0.1 * RIGHT)
        self.play(FadeIn(A_int_B_text))
        A_int_B = Intersection(set_A, set_B, fill_color=PURE_RED, fill_opacity=0.75)
        self.play(FadeIn(A_int_B))
        self.play(A_int_B.animate.scale(0.4).next_to(A_int_B_text))
        A_int_B_text_2 = MathTex(r"(A \cap B)^{'}=").move_to(A_int_B_text.get_center())
        A_int_B_comp = Exclusion(Uni_set, Intersection(set_A, set_B), fill_color=RED, fill_opacity=0.75).next_to(A_int_B_text_2).shift(LEFT)
        self.play(FadeTransform(A_int_B_text, A_int_B_text_2))
        self.play(FadeTransform(A_int_B, A_int_B_comp.scale(0.3)))

        A_comp_text = MathTex("A^{'}= \ ").next_to(A_int_B_text_2, 3 * DOWN).shift(DOWN)
        A_comp = Exclusion(Uni_set, set_A, fill_color=YELLOW, fill_opacity=0.7)

        self.play(Create(A_comp_text))
        self.play(FadeIn(A_comp))
        self.play(A_comp.animate.scale(0.3).next_to(A_comp_text).shift(0.5 * RIGHT))

        B_comp = Exclusion(Uni_set, set_B, fill_color=GREEN_A, fill_opacity=0.75)
        B_comp_text = MathTex("B^{'}= \ ").next_to(A_comp_text, DOWN).shift(DOWN)

        self.play(Create(B_comp_text))
        self.play(FadeIn(B_comp))
        self.play(B_comp.animate.scale(0.3).next_to(B_comp_text).shift(0.5 * RIGHT))

        A_comp_union_B_comp_text = MathTex(r"A^{'} \cup B{'}=").move_to(A_comp_text.get_center())
        A_comp_union_B_comp = Union(Exclusion(Uni_set, set_A),
                                    Exclusion(Uni_set, set_B), fill_color=RED, fill_opacity=0.76).next_to(A_comp_union_B_comp_text).scale(
            0.3).next_to(A_comp_union_B_comp_text)

        self.play(B_comp_text.animate.move_to(A_comp_text.get_center()))
        self.play(FadeOut(B_comp_text))
        self.play(FadeTransform(A_comp_text, A_comp_union_B_comp_text))

        self.play(B_comp.animate.move_to(A_comp.get_center()))
        self.play(FadeOut(B_comp))
        self.play(FadeTransform(A_comp, A_comp_union_B_comp))

        self.wait(3)
        self.play(FadeOut(theorem_stat_1, A_int_B_text_2, A_int_B_comp, A_comp_union_B_comp_text, A_comp_union_B_comp))

        # De Morgan's Theorem-II
        theorem_stat_1 = MathTex(r"(A \cup B)^{'}=A^{'} \cap B^{'}").next_to(Uni_set, DOWN)
        self.play(Create(theorem_stat_1))
        self.play(RECT_GRP.animate.to_corner(LEFT))
        self.play(theorem_stat_1.animate.next_to(sub_title_text))

        A_int_B_text = MathTex(r"A \cup B \ =").next_to(theorem_stat_1, 1.5 * DOWN).shift(0.1 * RIGHT)
        self.play(FadeIn(A_int_B_text))
        A_int_B = Union(set_A, set_B, fill_color=PURE_RED, fill_opacity=0.75)
        self.play(FadeIn(A_int_B))
        self.play(A_int_B.animate.scale(0.4).next_to(A_int_B_text))
        A_int_B_text_2 = MathTex(r"(A \cup B)^{'}\ =").move_to(A_int_B_text.get_center())
        A_int_B_comp = Exclusion(Uni_set, Union(set_A, set_B), fill_color=RED, fill_opacity=0.75).next_to(A_int_B_text_2).shift(LEFT)
        self.play(FadeTransform(A_int_B_text, A_int_B_text_2))
        self.play(FadeTransform(A_int_B, A_int_B_comp.scale(0.3)))

        A_comp_text = MathTex("A^{'}= \ ").next_to(A_int_B_text_2, 3 * DOWN).shift(DOWN)
        A_comp = Exclusion(Uni_set, set_A, fill_color=YELLOW, fill_opacity=0.7)

        self.play(Create(A_comp_text))
        self.play(FadeIn(A_comp))
        self.play(A_comp.animate.scale(0.3).next_to(A_comp_text).shift(0.5 * RIGHT))

        B_comp = Exclusion(Uni_set, set_B, fill_color=GREEN_A, fill_opacity=0.75)
        B_comp_text = MathTex("B^{'}= \ ").next_to(A_comp_text, DOWN).shift(DOWN)

        self.play(Create(B_comp_text))
        self.play(FadeIn(B_comp))
        self.play(B_comp.animate.scale(0.3).next_to(B_comp_text).shift(0.5 * RIGHT))

        A_comp_union_B_comp_text = MathTex(r"A^{'} \cap B{'}=").move_to(A_comp_text.get_center())
        A_comp_union_B_comp = Intersection(Exclusion(Uni_set, set_A),
                                           Exclusion(Uni_set, set_B), fill_color=RED, fill_opacity=0.76).next_to(A_comp_union_B_comp_text).scale(
            0.3).next_to(A_comp_union_B_comp_text)

        self.play(B_comp_text.animate.move_to(A_comp_text.get_center()))
        self.play(FadeOut(B_comp_text))
        self.play(FadeTransform(A_comp_text, A_comp_union_B_comp_text))

        self.play(B_comp.animate.move_to(A_comp.get_center()))
        self.play(FadeOut(B_comp))
        self.play(FadeTransform(A_comp, A_comp_union_B_comp))

        self.wait()
        self.play(FadeOut(theorem_stat_1, A_int_B_text_2, A_int_B_comp, A_comp_union_B_comp_text, A_comp_union_B_comp))
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self
                  .mobjects])

        # Principle of Inclusion and Exclusion-I
        title_text = MathTex(r" \underline{Calculating \ \ n(A \cup B) \ and \ n(A \cup B \cup C)}").to_edge(UP)
        self.play(FadeIn(title_text))
        self.wait()
        self.play(title_text.animate.to_edge(LEFT))

        set_A = Circle(radius=2, fill_color=RED, fill_opacity=0.8, stroke_color=WHITE).shift(LEFT)
        set_A_text = MathTex("A").move_to(set_A.get_center()).shift(UP + 0.5 * LEFT)

        set_B = Circle(radius=2, fill_color=BLUE, fill_opacity=0.8, stroke_color=WHITE).next_to(set_A_text, RIGHT).shift(RIGHT + DOWN)
        set_B_text = MathTex("B").move_to(set_B.get_center()).shift(UP + 0.5 * RIGHT)

        set_grp = Group(set_A, set_A_text, set_B, set_B_text)
        set_A, set_A_text, set_B, set_B_text = set_grp

        self.play(FadeIn(set_A, set_B, set_B_text, set_A_text))
        self.play(set_grp.animate.scale(0.8).shift(0.5 * UP))

        LHS = MathTex(r"n(A \cup B)=").next_to(set_A, DOWN).shift(1.3 * LEFT)
        self.play(Create(LHS))

        temp = set_A.copy().set_color(PURE_RED)
        self.play(FadeIn(temp, run_time=0.3))
        self.play(FadeOut(temp))

        n_A = MathTex(r"n(A)").next_to(LHS)
        self.play(Create(n_A))

        temp = set_B.copy().set_color(PURE_RED)
        self.play(FadeIn(temp, run_time=0.3))
        self.play(FadeOut(temp))

        n_B = MathTex(r"+ \ n(B)").next_to(n_A)
        self.play(Create(n_B))

        n_C = MathTex(r"+ \ n(C)")
        indicator = Arrow(start=RIGHT, end=Intersection(set_A, set_B).get_center(), buff=5, color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                          stroke_width=2)
        indicator_text = Text("THI REGION HAS BEEN \n COUNTED TWICE...\n!!!!!!!!!!", fill_color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                              weight=ULTRABOLD
                              ).scale(0.3).next_to(indicator)

        self.play(Create(indicator))
        self.play(FadeIn(indicator_text))
        self.blink(Intersection(set_A, set_B, fill_color=PURE_RED, fill_opacity=0.75))

        minus_sign = MathTex("-").scale(0.5).next_to(n_B)
        temp = minus_sign.copy().set_color(RED)

        self.play(FadeIn(temp, run_time=0.3))
        self.play(FadeIn(minus_sign))
        self.play(FadeOut(temp))

        n_a_int_b = MathTex(r"n(A \cap B)").next_to(minus_sign)
        eqn_grp = Group(LHS, n_A, n_B, n_a_int_b, minus_sign)
        self.play(Create(n_a_int_b))
        self.play(FadeOut(indicator, indicator_text))
        self.play(FadeOut(eqn_grp))
        self.wait(3)

        set_C = Circle(radius=2, fill_color=GREEN, fill_opacity=0.8, stroke_color=WHITE).next_to(Intersection(set_A, set_B), 0.1 * DOWN).scale(
            0.8).shift(UP)
        self.play(FadeIn(set_C))

        C_text = MathTex("C").next_to(Intersection(set_A, set_B, set_C), DOWN).shift(1.5 * DOWN).scale(0.8)
        self.play(FadeIn(C_text))

        new_grp = Group(set_A, set_B, set_C, set_B_text, set_A_text, C_text)
        set_A, set_B, set_C, set_B_text, set_A_text, C_text = new_grp

        self.play(new_grp.animate.scale(0.8).next_to(title_text, DOWN))

        LHS = MathTex(r"n(A \cup B \cup C)=").scale(0.5).next_to(set_C, 1.3 * DL)
        self.play(Create(LHS))
        self.wait()

        self.blink(set_A)
        self.play(Create(n_A.scale(0.5).next_to(LHS)))

        self.blink(set_B)
        self.play(Create(n_B.scale(0.5).next_to(n_A)))

        self.blink(set_C)
        self.play(Create(n_C.scale(0.5).next_to(n_B)))

        indicator = Arrow(start=RIGHT, end=Intersection(set_A, set_B).get_center(), buff=5, color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                          stroke_width=2)
        indicator_text = Text("THI REGION HAS BEEN \n COUNTED TWICE...\n!!!!!!!!!!", fill_color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                              weight=ULTRABOLD
                              ).scale(0.3).next_to(indicator)

        self.play(Create(indicator))
        self.play(FadeIn(indicator_text))
        self.blink(Intersection(set_A, set_B, fill_opacity=0.75, fill_color=PURE_RED))

        self.play(Create(minus_sign.next_to(n_C)))
        self.blink(minus_sign)
        self.play(Create(n_a_int_b.scale(0.5).next_to(minus_sign)))
        self.play(FadeOut(indicator, indicator_text))

        indicator = Arrow(start=RIGHT, end=Intersection(set_B, set_C).get_center(), buff=5, color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                          stroke_width=2)
        indicator_text = Text("THI REGION HAS BEEN \n COUNTED TWICE...\n!!!!!!!!!!", fill_color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                              weight=ULTRABOLD
                              ).scale(0.3).next_to(indicator)
        n_b_int_c = MathTex(r"n(B \cap C)").scale(0.5)
        n_a_int_c = MathTex(r"n(A \cap C)").scale(0.5)

        self.play(Create(indicator))
        self.play(FadeIn(indicator_text))
        self.blink(Intersection(set_B, set_C, fill_color=PURE_RED, fill_opacity=1))

        temp_minus = minus_sign.copy()
        self.play(Create(temp_minus.next_to(n_a_int_b)))
        self.blink(temp_minus)
        self.play(Create(n_b_int_c.next_to(temp_minus)))
        self.play(FadeOut(indicator, indicator_text))

        indicator = Arrow(start=RIGHT, end=Intersection(set_A, set_C).get_center(), buff=5, color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                          stroke_width=2)
        indicator_text = Text("THI REGION HAS BEEN \n COUNTED TWICE...\n!!!!!!!!!!", fill_color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                              weight=ULTRABOLD
                              ).scale(0.3).next_to(indicator)

        self.play(Create(indicator))
        self.play(FadeIn(indicator_text))
        self.blink(Intersection(set_A, set_C, fill_color=PURE_RED, fill_opacity=1))

        temp_minus = minus_sign.copy()
        self.play(Create(temp_minus.next_to(n_b_int_c)))
        self.blink(temp_minus)
        self.play(Create(n_a_int_c.next_to(temp_minus)))
        self.play(FadeOut(indicator, indicator_text))

        n_a_int_b_int_c = MathTex(r"n(A \cap B \cap C)").scale(0.5)
        indicator = Arrow(start=RIGHT, end=Intersection(set_A, set_B, set_C).get_center(), buff=5, color=PURE_RED, fill_opacity=1, stroke_color=BLACK,
                          stroke_width=2)
        indicator_text = Text("THI REGION HAS BEEN COMPLETELY \n EXCLUDED DUE TO THE PREVIOUS SUBTRACTIONS", fill_color=PURE_RED, fill_opacity=1,
                              stroke_color=BLACK,
                              weight=ULTRABOLD
                              ).scale(0.3).next_to(indicator)
        self.play(Create(indicator))
        self.play(FadeIn(indicator_text))
        self.blink(Intersection(set_A, set_B, set_C, fill_color=PURE_RED, fill_opacity=1))

        temp_minus = MathTex("+").scale(0.5)
        self.play(Create(temp_minus.next_to(n_a_int_c)))
        self.blink(temp_minus)
        self.play(Create(n_a_int_b_int_c.next_to(temp_minus)))
        self.play(FadeOut(indicator, indicator_text))
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self
                  .mobjects])

        # Credits

        self.credit()

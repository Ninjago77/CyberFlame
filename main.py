import random
import flet as ft
from dataclasses import dataclass
from enum import Enum,auto

class SkillName(Enum):
    common = "common__GROUP"
    diff_of_square = "diff_of_square__GROUP"
    square_of_sum = "square_of_sum__GROUP"
    square_of_diff = "square_of_diff__GROUP"
    x_square_trinomial = "x_square_trinomial__GROUP"
    ax_square_trinomial_a_not_1 = "ax_square_trinomial_a_not_1__GROUP"
    sum_of_cube = "sum_of_cube__GROUP"
    diff_of_cube = "diff_of_cube__GROUP"
    fully_factored = "fully_factored__GROUP"

Skill_Formulas = {
    SkillName.common: ("?(...)",ft.colors.CYAN_500),
    SkillName.diff_of_square: ("a²-b² = (a+b)(a-b)",ft.colors.YELLOW),
    SkillName.square_of_sum: (" a²+2ab+b² = (a+b)²",ft.colors.YELLOW),
    SkillName.square_of_diff: ("a²-2ab+b² = (a-b)² ",ft.colors.YELLOW),
    SkillName.x_square_trinomial: ("x²+bx+c",ft.colors.TEAL_ACCENT_400),
    SkillName.ax_square_trinomial_a_not_1: ("ax²+bx+c, a≠1",ft.colors.TEAL_ACCENT_400),
    SkillName.sum_of_cube: ("a³+b³ = (a+b)(a²-ab+b²)",ft.colors.ORANGE),
    SkillName.diff_of_cube: ("a³-b³ = (a-b)(a²+ab+b²)",ft.colors.ORANGE),
}

@dataclass
class Question():
    q_text: str
    q_list: list[str]
    skill_list: list[SkillName]

    def is_solvable(self) -> bool:
        # return len(self.skill_list) >= 2
        return self.skill_list[0] != SkillName.fully_factored

    def solve(self):
        if not self.is_solvable():
            raise Exception("too early error")
        return Question(
            q_text = self.q_list.pop(0),
            skill_list = self.skill_list[1:],
            q_list = self.q_list, # first item was removed in q_text declaration by .pop(0)
        )

the_questions = [
    Question(
        q_text="7k²+126k+119",
        q_list=[
            "(7)(k²+18k+17)",
            "(7)(k+17)(k+1)"
        ],
        skill_list=[
            SkillName.common,
            SkillName.x_square_trinomial,
            SkillName.fully_factored,
        ],

    ),
    Question(
        q_text="3a²b²+9ab+15b³",
        q_list=[
            "(3b)(5b²+a²b+3a)",
        ],
        skill_list=[
            SkillName.common,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="3a²b²+9ab+15b³",
        q_list=[
            "(3b)(5b²+a²b+3a)",
        ],
        skill_list=[
            SkillName.common,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="x²-9",
        q_list=[
            "(x+3)(x-3)",
        ],
        skill_list=[
            SkillName.diff_of_square,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="g²-g-20",
        q_list=[
            "(g+4)(g-5)",
        ],
        skill_list=[
            SkillName.x_square_trinomial,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="2c²-7c+6",
        q_list=[
            "(2c-3)(c-2)",
        ],
        skill_list=[
            SkillName.ax_square_trinomial_a_not_1,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="2ax²+8ax+x+4",
        q_list=[
            "2ax(x+4)+1(x+4)",
            "(2ax+1)(x+4)",
        ],
        skill_list=[
            SkillName.common,
            SkillName.common,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="2x²-8y²",
        q_list=[
            "(2)(x²-4y²)",
            "(2)(x-2)(x+2)",
        ],
        skill_list=[
            SkillName.common,
            SkillName.diff_of_square,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="3x²y²+6xy+9",
        q_list=[
            "(3)(x²y²+2xy+3)",
        ],
        skill_list=[
            SkillName.common,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="9y²-12y+4",
        q_list=[
            "(3y-2)²",
        ],
        skill_list=[
            SkillName.square_of_diff,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="x²-18x+81",
        q_list=[
            "(x-9)²",
        ],
        skill_list=[
            SkillName.square_of_diff,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="36x²+84x+49",
        q_list=[
            "(6x+7)²",
        ],
        skill_list=[
            SkillName.square_of_sum,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="25a²+60a+36",
        q_list=[
            "(5a+6)²",
        ],
        skill_list=[
            SkillName.square_of_sum,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="16-w⁴",
        q_list=[
            "(4+w²)(4-w²)",
            "(4+w²)(2+w)(2-w)",
        ],
        skill_list=[
            SkillName.diff_of_square,
            SkillName.diff_of_square,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="121x²+286xy+169y²",
        q_list=[
            "(11x+13y)²",
        ],
        skill_list=[
            SkillName.square_of_sum,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="(x-3)²+x-5",
        q_list=[
            "x²-5x+4",
            "(x-4)(x-1)",
        ],
        skill_list=[
            SkillName.square_of_diff,
            SkillName.x_square_trinomial,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="(y+3z)²-(y+z)²",
        q_list=[
            "(2y+4z)(2z)",
            "(y+2z)(4z)",
        ],
        skill_list=[
            SkillName.diff_of_square,
            SkillName.common,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="a⁴-13a²+36",
        q_list=[
            "(a²-4)(a²-9)",
            "(a+2)(a-2)(a+3)(a-3)",
        ],
        skill_list=[
            SkillName.x_square_trinomial,
            SkillName.diff_of_square,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="648a+1029a⁴",
        q_list=[
            "(3a)(216+343a³)",
            "(3a)(6+7a)(36-42a+49a²)",
        ],
        skill_list=[
            SkillName.common,
            SkillName.sum_of_cube,
            SkillName.fully_factored,
        ],
    ),
    Question(
        q_text="125x³-216y³",
        q_list=[
            "(5x-6y)(25x²+30xy+36)",
        ],
        skill_list=[
            SkillName.diff_of_cube,
            SkillName.fully_factored,
        ],
    ),
]
random.shuffle(the_questions)

def drag_will_accept(e):
    if e.control.group != SkillName.fully_factored:
        e.control.content.border = ft.border.all(
            5, Skill_Formulas[e.control.group][1] if e.data == "true" else ft.colors.RED
        )
        e.control.update()

def drag_leave(e):
    e.control.content.border = ft.border.all(
        5,e.control.content.bgcolor,
    )
    e.control.update()

def main(page: ft.Page):
    global Skill_Index,Display_Skill,SkillControls,mobile,PARENT_OF_DRAGTARGETS
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
        #     track_color={
        #         ft.ControlState.HOVERED: ft.colors.AMBER,
        #         ft.ControlState.DEFAULT: ft.colors.TRANSPARENT,
        #     },
        #     track_visibility=True,
        #     track_border_color=ft.colors.BLUE,
        #     thumb_visibility=True,
        #     thumb_color={
        #         ft.ControlState.HOVERED: ft.colors.RED,
        #         ft.ControlState.DEFAULT: ft.colors.GREY_300,
        #     },
        #     thickness=30,
        #     radius=15,
        #     main_axis_margin=5,
        #     cross_axis_margin=10,
        #     # interactive=False,
        )
    )
    page.theme.scrollbar_theme.cross_axis_margin = -50

    def resize(e):
        def close_dia(e):
            page.dialog.open = False
            page.update()
        page.dialog = ft.AlertDialog(
            title=ft.Text("Hello there! You just resized me!\nReload Me Please! >v<\n Or I might look wierd..."),
            actions=[ft.FloatingActionButton(
                text="I don't care",
                icon=ft.icons.CLOSE_ROUNDED,
                on_click=close_dia,
            )],
            modal=True,
        )
        page.dialog.open = True
        page.update()
        # page.launch_url(
        #     page.url,
        #     web_popup_window=False,
        #     web_window_name=ft.UrlTarget.SELF,
        # )
    page.on_resize = resize
    mobile = page.width < page.height
    if mobile:
        Nav_Control = ft.NavigationDrawer
        Nav_Control_Dest = ft.NavigationDrawerDestination
    else:
        Nav_Control = ft.NavigationBar
        Nav_Control_Dest = ft.NavigationDestination
    
    CUSTOM_THEMESTYLE_SMALLTEXT = ft.TextThemeStyle.BODY_SMALL if mobile else ft.TextThemeStyle.BODY_MEDIUM 
    CUSTOM_THEMESTYLE_LARGETEXT = ft.TextThemeStyle.DISPLAY_SMALL
    CUSTOM_THEMESTYLE_MEDUIMTEXT = ft.TextThemeStyle.TITLE_MEDIUM

    page.title = "PolyFactor!"
    Skill_Index = 0
    view_scale = 1.0
    if page.width <= 350:
        view_scale = page.width/400
    WRAP_WIDTH = page.width-20
    WRAP_WIDTH_v2 = page.width*(15/16)*(1/2)
    WRAP_HEIGHT = page.height*(3/4)
    Display_Skill = ft.Container(scale=view_scale,margin=ft.margin.only(left=1,right=1)) # TODO: fix bottom padding
    def build_dragtarget(q:Question):
        def drag_accept(e:ft.DragTargetAcceptEvent):
            if q.is_solvable():
                q2 = q.solve()
                p = PARENT_OF_DRAGTARGETS
                t2 = build_dragtarget(q2)
                p.controls[p.controls.index(e.control)] = t2
                p.update()
            # page.update()

        targ = ft.DragTarget(
            content=ft.Container(
                content=ft.Text(q.q_text,theme_style=ft.TextThemeStyle.LABEL_LARGE,color=ft.colors.BLACK if len(q.q_list) != 0 else ft.colors.WHITE),
                padding=ft.padding.only(left=10,right=10,bottom=7,top=7),
                bgcolor=ft.colors.GREY_400 if len(q.q_list) != 0 else ft.colors.GREEN_700,
                border=ft.border.all(
                    5, ft.colors.GREY_400 if len(q.q_list) != 0 else ft.colors.GREEN_700,
                ),
                border_radius=5,
            ),
            group=q.skill_list[0],
            on_will_accept=drag_will_accept,
            on_accept=drag_accept,
            on_leave=drag_leave,
        )
        return targ
    DRAGTARGETS = [build_dragtarget(q) for q in the_questions]
    def block_normal(d):
        d.color = ft.colors.BLACK
        d.theme_style = ft.TextThemeStyle.LABEL_MEDIUM
        return ft.Container(
            content=d,
            padding=ft.padding.only(left=10,right=10,bottom=7,top=7),
            bgcolor=ft.colors.GREY_400,
            border_radius=3,
        
    )
    def block_answer(d):
        d.color = ft.colors.WHITE
        d.theme_style = ft.TextThemeStyle.LABEL_MEDIUM
        return ft.Container(
            content=d,
            padding=ft.padding.only(left=10,right=10,bottom=7,top=7),
            bgcolor=ft.colors.GREEN_700,
            border_radius=3,
    )
    
    SkillControls = [
        # ft.Column(controls= [# Reverse
        #     ft.Text("Reverse Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
        #     ft.TextField(label="Input",multiline=True),
        #     ft.FloatingActionButton(text="Submit",on_click=lambda _:None ,width=300),
        #     ft.TextField(label="Output",read_only=True,multiline=True),
        # ]),
        # ft.Column(controls= [# Atbash
        #     ft.Text("Atbash Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
        #     ft.TextField(label="Input",multiline=True),
        #     ft.FloatingActionButton(text="Submit",on_click=lambda _:None ,width=300),
        #     ft.TextField(label="Output",read_only=True,multiline=True),
        # ]),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Common Factoring
                ft.Text("Common Factoring",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Factoring: writing a polynomial\nas a product of its factors",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("HCF/GCF: the greatest/highest number\n that can divide into each no. in a set",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Common Factoring: factoring a polynomial\n  by writing it as HCF x (Polynomial/HCF)",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Common Factoring?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see a common coefficient, common\nvariable or common factor in the coefficients\nin all the terms, you can factor it out!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Common Factoring?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need to use common\nfactoring, find the HCF, let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("15x²y - 33y³ + 12yz, HCF -> 3y")),
                ft.Text("Then take out the HCF, & divide each term by the HCF",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("(3y)[(15x²y/3y) + (-33y³/3y) + (12yz/3y)]")),
                ft.Text("Simplify & there's your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_answer(ft.Text("(3y)(5x² + -11y² + 4z)")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Difference of Squares
                ft.Text("Difference of Squares",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Binomial: a polynomial with 2 terms",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Difference of Squares: a binomial in the\nform a²-b²; it can be factored as (a+b)(a-b)",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Difference of Squares?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see 2 squares of any kind separated\nby a minus sign, you can factor it this way!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Difference of Squares?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need to use difference\nof squares, find the square roots, let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("49x² - 121y², roots -> √(49x²) = 7x, √(121y²) = 11y")),
                ft.Text("Then assign those values to the variables in the\nformula: a²-b² = (a + b)(a - b) to get your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_answer(ft.Text("a = 7x, b = 11y, (7x + 11y)(7x - 11y)")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Whole Square of Sum
                ft.Text("Square of Sum",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Trinomial: a polynomial with 3 terms",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Whole Square of Sum: a squared binomial\nsum in the form (a + b)²; it is the factored\nform of the trinomial a² + 2ab + b²",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Whole Square of Sum?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see 2 squares & a postive middle term that is\nthe product of both roots & 2, you can factor it this way!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Whole Square of Sum?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need to use whole square\nof sum, find the square roots & check if the middle\nterm matches the format (2*a*b), let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("144x² + 120xy + 25y²")),
                block_normal(ft.Text("roots -> √(144x²) = 12x, √(25y²) = 5y")),
                block_normal(ft.Text("120xy = 2 * 12x * 5y ✓")),
                ft.Text("Then assign those values to the variables in the\nformula: a² + 2ab + b² = (a + b)² to get your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_answer(ft.Text("a = 12x, b = 5y, (12x + 5y)²")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Whole Square of Difference
                ft.Text("Square of Difference",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Whole Square of Difference: a squared binomial\ndifference in the form (a - b)²; it is the factored\n          form of the trinomial a² - 2ab + b²",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Whole Square of Difference?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see 2 squares & a negative middle term that is\nthe product of both roots & 2, you can factor it this way!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Whole Square of Difference?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need to use whole square\nof difference, find the square roots & check if the middle\nterm matches the format (-2*a*b), let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("121x² - 198xy + 81y²")),
                block_normal(ft.Text("roots -> √(121x²) = 11x, √(81y²) = 9y")),
                block_normal(ft.Text("-198xy = -2 * 11x * 9y ✓")),
                ft.Text("Then assign those values to the variables in the\nformula: a² - 2ab + b² = (a - b)² to get your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_answer(ft.Text("a = 11x, b = 9y, (11x - 9y)²")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Trinomial x²+bx+c
                ft.Text("Factoring Trinomial",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("x² + bx + c",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Trinomial x²+bx+c : a trinomial where b = e+f, c = e*f",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Trinomial x²+bx+c?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see a square of a variable, a number & a\nterm thats the (sum of the factors of that number)\ntimes the variable, you can factor it this way!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Trinomial x²+bx+c?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need\nto use trinomial x²+bx+c, find e & f values in\nb = e+f, c = e*f, let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("x² + 7x + 10, e = 5, f = 2")),
                block_normal(ft.Text("b = e+f; 7 = 5+2, c = e*f, 10 = 5*2 ✓")),
                ft.Text("Then split the middle term b as e+f, common\nfactor twice & there's your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("x² + 5x + 2x + 10, x(x + 5) + 2(x + 5)")),
                block_answer(ft.Text("(x + 5)(x + 2)")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Trinomial ax²+bx+c, a≠1
                ft.Text("Factoring Trinomial",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("ax² + bx + c",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("where a ≠ 1",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Trinomial ax²+bx+c, a≠1 : a trinomial\nwhere b = e+f, a*c = e*f",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Trinomial ax²+bx+c, a≠1?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see a square of a variable with a coefficient,\na number & a term thats the (sum of the factors\nof the product of the number & coefficient)\ntimes the variable, you can factor it this way!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Trinomial ax²+bx+c, a≠1?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need to use\ntrinomial ax²+bx+c, a≠1, find e & f values\nin b = e+f, a*c = e*f, let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("2x² + 7x + 3, e = 6, f = 1")),
                block_normal(ft.Text("b = e+f; 7 = 6+1, a*c = e*f, 3*2 = 6*1 ✓")),
                ft.Text("Then split the middle term b as e+f, common\nfactor twice & there's your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("2x² + 6x + 1x + 3, 2x(x + 3) + 1(x + 3)")),
                block_answer(ft.Text("(2x + 1)(x + 3)")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Sum of Cubes
                ft.Text("Sum of Cubes",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Sum of Cubes: a binomial in the form a³+b³;\nit can be factored as (a + b)(a² - ab + b²)",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Sum of Cubes?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see 2 cubes of any kind separated\nby a plus sign, you can factor it this way!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Sum of Cubes?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need to use sum\nof cubes, find the cube roots, let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("27x³ + 64y³, cube-")),
                block_normal(ft.Text("roots -> ³√(27x³) = 3x, ³√(64y³) = 4y")),
                ft.Text("Then assign those values to the variables in the\nformula: a³+b³ = (a + b)(a² - ab + b²) to get your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_answer(ft.Text("a = 3x, b = 4y, (3x + 4y)(9x² - 12xy + 16y²)")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Difference of Cubes
                ft.Text("Difference of Cubes",theme_style=CUSTOM_THEMESTYLE_LARGETEXT),
                ft.Text("Difference of Cubes: a binomial in the form\na³-b³; it can be factored as (a - b)(a² + ab + b²)",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("Do I need to use Difference of Cubes?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("If you see 2 cubes of any kind separated\nby a minus sign, you can factor it this way!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                ft.Text("How do I use Difference of Cubes?",theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
                ft.Text("Once you've identified that you need to use difference\nof cubes, find the cube roots, let's use an example:-",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_normal(ft.Text("8x³ - 125y³, cube-")),
                block_normal(ft.Text("roots -> ³√(8x³) = 2x, ³√(125y³) = 5y")),
                ft.Text("Then assign those values to the variables in the\nformula: a³-b³ = (a - b)(a² + ab + b²) to get your answer!",theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
                block_answer(ft.Text("a = 2x, b = 5y, (2x - 5y)(4x² + 10xy + 25y²)")),
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            # TODO: above line really important
        ),
        ft.Card(width=page.width-40,
                height=(page.height*(7/8))-40,
                content=ft.Container(content=(ft.Column(
            controls=[
                ft.Row(
                    controls=[ft.Draggable(
                        group=s,
                        content=ft.Container(
                            content=ft.Text(Skill_Formulas[s][0],theme_style=ft.TextThemeStyle.LABEL_LARGE,color=ft.colors.BLACK),
                            padding=ft.padding.only(left=10,right=10,bottom=7,top=7),
                            bgcolor=Skill_Formulas[s][1],
                            border_radius=5,
                        )
                    ) for s in SkillName if s != SkillName.fully_factored],
                    wrap=True,
                    width=WRAP_WIDTH,
                ),
                ft.Container( # divider
                    width=page.width*(3/4),
                    height=5,
                    border_radius=5,
                    bgcolor=ft.colors.ON_SECONDARY_CONTAINER,
                ),
                ft.Row(
                    controls=DRAGTARGETS,
                    wrap=True,
                    width=WRAP_WIDTH_v2,
                    # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ) if mobile else ft.Row(
            controls=[
                # ft.Container( # divider
                #     height=page.height*(3/4),
                #     width=2,
                #     border_radius=2,
                #     bgcolor=ft.colors.ON_SECONDARY_CONTAINER,
                # ),
                ft.Column(
                    controls=[ft.Draggable(
                        group=s,
                        content=ft.Container(
                            content=ft.Text(Skill_Formulas[s][0],theme_style=ft.TextThemeStyle.LABEL_LARGE,color=ft.colors.BLACK),
                            padding=ft.padding.only(left=10,right=10,bottom=7,top=7),
                            bgcolor=Skill_Formulas[s][1],
                            border_radius=5,
                        )
                    ) for s in SkillName if s != SkillName.fully_factored],
                    wrap=True,
                    height=WRAP_WIDTH,
                ),
                ft.Container( # divider
                    height=page.height*(3/4),
                    width=2,
                    border_radius=2,
                    bgcolor=ft.colors.ON_SECONDARY_CONTAINER,
                ),
                ft.Column(
                    controls=DRAGTARGETS,
                    wrap=True,
                    height=WRAP_HEIGHT-20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )),padding=ft.padding.all(20)),margin=ft.margin.symmetric(horizontal=20,vertical=20)),
        ft.Column(controls= [# About
            ft.Text("About The App",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.Text("This Project was made by Shanvanth Arunmozhi to teach the concept of factoring Polynomials. Useful for learning factoring techniques in the course Foundations & Pre-Calculus 10. Credits: Loading Animation & Favicon by Freepik.",width=300,theme_style=ft.TextThemeStyle.BODY_LARGE),
        ]),

    ]
    
    PARENT_OF_DRAGTARGETS = SkillControls[-2].content.content.controls[-1]
    if mobile:
        SkillControls[-2].content.content.controls[-1].scroll = ft.ScrollMode.AUTO
    
    def nav_rail_switch(e):
        global Skill_Index,Display_Skill,mobile
        Skill_Index = e.control.selected_index
        # page.controls[0].alignment = ft.MainAxisAlignment.START if (Skill_Index == 8 and not mobile) else ft.MainAxisAlignment.CENTER
        if mobile:
            page.drawer.open = False
        Display_Skill_update()
    def Display_Skill_update():
        global Skill_Index,Display_Skill
        Display_Skill.content = SkillControls[Skill_Index]
        page.update()
    Display_Skill_update()
    page.appbar = ft.AppBar(
        title=ft.Text("PolyFactor!" if mobile else "PolyFactor! How to Factor Polynomials...",color=ft.colors.ON_PRIMARY),
        bgcolor=ft.colors.PRIMARY,
    )
    Nav_Control_Final = Nav_Control(
        on_change= nav_rail_switch,
    )
    Nav_Control_List = [
        Nav_Control_Dest(
            icon_content=ft.Text("?(...)",theme_style=ft.TextThemeStyle.BODY_MEDIUM),
            selected_icon_content=ft.Text("?(...)",theme_style=ft.TextThemeStyle.BODY_MEDIUM,weight=ft.FontWeight.BOLD),
            label="Common Factoring",
        ),
        Nav_Control_Dest(
            icon_content=ft.Text("a²-b²",theme_style=ft.TextThemeStyle.BODY_MEDIUM),
            selected_icon_content=ft.Text("a²-b²",theme_style=ft.TextThemeStyle.BODY_MEDIUM,weight=ft.FontWeight.BOLD),
            label="Difference of Squares",
        ),
        Nav_Control_Dest(
            icon_content=ft.Text("(a+b)²",theme_style=ft.TextThemeStyle.BODY_MEDIUM),
            selected_icon_content=ft.Text("(a+b)²",theme_style=ft.TextThemeStyle.BODY_MEDIUM,weight=ft.FontWeight.BOLD),
            label="Square of Sum", # Whole
        ),
        Nav_Control_Dest(
            icon_content=ft.Text("(a-b)²",theme_style=ft.TextThemeStyle.BODY_MEDIUM),
            selected_icon_content=ft.Text("(a-b)²",theme_style=ft.TextThemeStyle.BODY_MEDIUM,weight=ft.FontWeight.BOLD),
            label="Square of Difference", # Whole
        ),
        Nav_Control_Dest(
            icon_content=ft.Text("x²...",theme_style=ft.TextThemeStyle.BODY_SMALL),
            selected_icon_content=ft.Text("x²...",theme_style=ft.TextThemeStyle.BODY_SMALL,weight=ft.FontWeight.BOLD),
            label="Factoring x²+bx+c",
        ),
        Nav_Control_Dest(
            icon_content=ft.Text("ax²...",theme_style=ft.TextThemeStyle.BODY_SMALL),
            selected_icon_content=ft.Text("ax²...",theme_style=ft.TextThemeStyle.BODY_SMALL,weight=ft.FontWeight.BOLD),
            label="Factoring ax²+bx+c, a ≠ 1",
        ),
        Nav_Control_Dest(
            icon_content=ft.Text("a³+b³",theme_style=ft.TextThemeStyle.BODY_SMALL),
            selected_icon_content=ft.Text("a³+b³",theme_style=ft.TextThemeStyle.BODY_SMALL,weight=ft.FontWeight.BOLD),
            label="Sum of Cubes",
        ),
        Nav_Control_Dest(
            icon_content=ft.Text("a³-b³",theme_style=ft.TextThemeStyle.BODY_SMALL),
            selected_icon_content=ft.Text("a³-b³",theme_style=ft.TextThemeStyle.BODY_SMALL,weight=ft.FontWeight.BOLD),
            label="Difference of Cubes",
        ),
        Nav_Control_Dest(
            icon=ft.icons.GRID_VIEW,
            selected_icon=ft.icons.GRID_VIEW_ROUNDED,
            label="Factor Playground",
        ),
        Nav_Control_Dest(
            icon=ft.icons.INFO_OUTLINE_ROUNDED,
            selected_icon=ft.icons.INFO_ROUNDED,
            label="About",
        ),
    ]
    if mobile: Nav_Control_Final.controls = Nav_Control_List
    else:
        Nav_Control_List.pop(-2)
        Nav_Control_Final.destinations = Nav_Control_List
    if mobile:
        def menu_open(e):
            page.drawer.open = True
            page.drawer.update()
        page.appbar.leading = ft.IconButton(
            icon=ft.icons.MENU_ROUNDED,
            icon_color=ft.colors.ON_PRIMARY,
            on_click=menu_open,
        )
        page.drawer = Nav_Control_Final
        page.add(
            ft.Row([
                    Display_Skill,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )
        )
    else:
        page.appbar.center_title = True
        page.navigation_bar = Nav_Control_Final
        playground = SkillControls.pop(-2)
        page.add(
            ft.Row([
                    ft.Container(
                        content=Display_Skill,
                        width=page.width*(31/32)*(1/2),
                        alignment=ft.alignment.top_center,
                    ),
                    ft.Container(
                        content=playground,
                        width=page.width*(31/32)*(1/2),
                        alignment=ft.alignment.top_center,
                    ),
                ],
                # alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )
        )

ft.app(target=main,web_renderer=ft.WebRenderer.HTML,view=ft.AppView.WEB_BROWSER)
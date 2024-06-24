import random
import flet as ft

def main(page: ft.Page):
    global Principle_Index,Display_Principle,PrincipleControls,mobile
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

    page.title = "CyberFlame!"
    Principle_Index = 0
    view_scale = 1.0
    if page.width <= 350:
        view_scale = page.width/400
    WRAP_WIDTH = page.width-20
    WRAP_WIDTH_v2 = page.width*(15/16)*(1/2)
    WRAP_HEIGHT = page.height*(3/4)
    Display_Principle = ft.Container(scale=view_scale,margin=ft.margin.only(left=1,right=1)) # TODO: fix bottom padding

    PrincipleControls = [
        
        ft.Column(controls= [# About
            ft.Text("About The App",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.Text("This Project was made by Shanvanth Arunmozhi to teach CyberSecurity Principles.",width=300,theme_style=ft.TextThemeStyle.BODY_LARGE),
        ]),

    ]
    
    def nav_rail_switch(e):
        global Principle_Index,Display_Principle,mobile
        Principle_Index = e.control.selected_index
        if mobile:
            page.drawer.open = False
        Display_Principle_update()
    def Display_Principle_update():
        global Principle_Index,Display_Principle
        Display_Principle.content = PrincipleControls[Principle_Index]
        page.update()
    Display_Principle_update()
    page.appbar = ft.AppBar(
        title=ft.Text("CyberFlame" if mobile else "CyberFlame | Learn CyberSecurity Principles!",color=ft.colors.ON_PRIMARY),
        bgcolor=ft.colors.PRIMARY,
    )
    Nav_Control_Final = Nav_Control(
        on_change= nav_rail_switch,
    )
    Nav_Control_List = [
        # Nav_Control_Dest(
        #     icon_content=ft.Text("a³-b³",theme_style=ft.TextThemeStyle.BODY_SMALL),
        #     selected_icon_content=ft.Text("a³-b³",theme_style=ft.TextThemeStyle.BODY_SMALL,weight=ft.FontWeight.BOLD),
        #     label="Difference of Cubes",
        # ),
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
                    Display_Principle,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )
        )
    else:
        page.appbar.center_title = True
        page.navigation_bar = Nav_Control_Final
        page.add(
            ft.Row([
                    Display_Principle,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )
        )
ft.app(target=main,web_renderer=ft.WebRenderer.HTML,view=ft.AppView.WEB_BROWSER)
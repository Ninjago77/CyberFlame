import random
import string
import flet as ft

def main(page: ft.Page):
    global Principle_Index,Display_Principle,PrincipleControls,mobile
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.ORANGE,
            on_primary=ft.colors.BLACK,
            primary_container=ft.colors.AMBER_200,
            on_primary_container=ft.colors.AMBER_900,
            background=ft.colors.GREY_200,
            on_background=ft.colors.ON_PRIMARY,
        ),
    )
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.DEEP_PURPLE,
            on_primary=ft.colors.WHITE,
            primary_container=ft.colors.PURPLE_900,
            on_primary_container=ft.colors.PURPLE_200,
            background=ft.colors.GREY_800,
            on_background=ft.colors.ON_PRIMARY,
        ),

    )
    def close_dia(e):
        page.close(dlg)
    dlg = ft.AlertDialog(
        title=ft.Text("Hello there! You just resized me!\nReload Me Please! >v<\n Or I might look wierd..."),
        actions=[ft.FloatingActionButton(
            text="I don't care",
            icon=ft.icons.CLOSE_ROUNDED,
            on_click=close_dia,
        )],
        modal=True,
    )

    def resize(e):
        # page.open(dlg)
        # page.update()
        try:
            page.launch_url(
                f"https{page.url[2:]}",
                web_popup_window=False,
                web_window_name=ft.UrlTarget.SELF,
            )
        except AttributeError as e:
            page.open(dlg)
            page.update()
    page.on_resized = resize
    mobile = page.width < page.height
    if mobile:
        Nav_Control = ft.NavigationDrawer
        Nav_Control_Dest = ft.NavigationDrawerDestination
    else:
        Nav_Control = ft.NavigationBar
        Nav_Control_Dest = ft.NavigationBarDestination
    
    CUSTOM_THEMESTYLE_SMALLTEXT = ft.TextThemeStyle.BODY_SMALL if mobile else ft.TextThemeStyle.BODY_MEDIUM 
    CUSTOM_THEMESTYLE_LARGETEXT = ft.TextThemeStyle.DISPLAY_SMALL
    CUSTOM_THEMESTYLE_MEDUIMTEXT = ft.TextThemeStyle.TITLE_MEDIUM

    page.title = "CyberFlame!"
    Principle_Index = 0
    view_scale = 1.0
    if page.width <= 350:
        view_scale = page.width/400
    Display_Principle = ft.Container(scale=view_scale,margin=ft.margin.all(1)) # TODO: fix bottom padding
    def in_str(s1,s2):
        for i in s1:
            if i in s2:
                return True
        return False


    def strength_test(e):
        password = e.control.parent.controls[-3].value
        box = e.control.parent.controls[-1]
        box.value = ""
        if not in_str(string.ascii_lowercase, password):
            box.value += "✘ Your password should include lowercase characters\n"
        if not in_str(string.ascii_uppercase, password):
            box.value += "✘ Your password should include uppeascii_uppercase characters\n"
        if not in_str(string.digits, password):
            box.value += "✘ Your password should include numbers\n"
        if not in_str(string.punctuation, password):
            box.value += "✘ Your password should include symbols characters\n"
        if in_str(string.whitespace, password):
            box.value += "✘ Your password should not include whitespace\n"
        if len(password) <= 15:
            box.value += "✘ Your password should be atleast 16 characters long\n"
        
        if box.value == "":
            box.color = ft.colors.GREEN
            box.value = "✔ You password is safe"
        else:
            box.color = ft.colors.RED
        e.control.parent.update()

    
    PrincipleControls = [
        ft.Column(scroll=ft.ScrollMode.AUTO,controls= [# Password Managers
            ft.Text("Password Managers",width=300,theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.Text("Passwords must be kept safe, this doesn't mean you can just write it on a sticky note. You need a password manager to safeguard your passwords & remember them for you. Here are some:-",width=300,theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
            ft.Row(
                wrap=True,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                width=300,
                controls=[
                    ft.Container(
                        content=ft.Column(controls=[
                            ft.Image(src=i[1],fit=ft.ImageFit.SCALE_DOWN),
                            ft.Text(i[0],theme_style=CUSTOM_THEMESTYLE_SMALLTEXT,text_align=ft.TextAlign.CENTER),
                        ]),
                        width=100,
                        height=150,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.PRIMARY_CONTAINER,
                        border=ft.border.all(1, ft.colors.ON_PRIMARY_CONTAINER),
                        border_radius=ft.border_radius.all(5),
                    )
                    for i in [
                        ("1Password","https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/1Password_icon.png/900px-1Password_icon.png"),
                        ("bitwarden","https://static-00.iconduck.com/assets.00/bitwarden-v2-icon-512x512-cstnj11p.png"),
                        ("Dashlane","https://cdn.icon-icons.com/icons2/2407/PNG/512/dashlane_icon_146197.png"),
                        ("Keeper","https://govcloud.keepersecurity.us/vault/images/keeper_icons/icon_rounded_256.png"),
                        ("NordPass","https://www.techspot.com/images2/downloads/topdownload/2021/02/2021-02-18-ts3_thumbs-371-p_256.webp"),
                        ("LastPass","https://static-00.iconduck.com/assets.00/lastpass-icon-256x256-5io6p8tz.png"),
                    ]
                ],
            ),
        ]),
        ft.Column(controls= [# Password Strength Tester
            ft.Text("Password Strength Tester",width=300,theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.Text("A password needs to be secure enough to prevent someone guessing or brute forcing it.",width=300,theme_style=CUSTOM_THEMESTYLE_SMALLTEXT),
            ft.TextField(label="Try out a password!",multiline=True,password=True,can_reveal_password=True,on_change=strength_test,on_submit=strength_test),
            ft.FloatingActionButton(text="Submit",on_click=strength_test,width=300),
            ft.Text("",width=300,theme_style=CUSTOM_THEMESTYLE_SMALLTEXT)
        ]),
        ft.Column(controls= [# About
            ft.Text("About The App",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.Text("This Project was made by Shanvanth Arunmozhi to teach CyberSecurity Principles.",width=300,theme_style=CUSTOM_THEMESTYLE_MEDUIMTEXT),
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
            icon=ft.icons.LIST,
            selected_icon=ft.icons.VIEW_LIST,
            label="Password Managers",
        ),
        Nav_Control_Dest(
            icon=ft.icons.LOCK_OPEN,
            selected_icon=ft.icons.LOCK,
            label="Password Strength",
        ),
        Nav_Control_Dest(
            icon=ft.icons.INFO_OUTLINE_ROUNDED,
            selected_icon=ft.icons.INFO_ROUNDED,
            label="About",
        ),
    ]
    if mobile: Nav_Control_Final.controls = Nav_Control_List
    else: Nav_Control_Final.destinations = Nav_Control_List
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
    else:
        page.appbar.center_title = True
        page.navigation_bar = Nav_Control_Final
    page.add(
        ft.Row([
                ft.Card(
                    content=ft.Container(
                        content=Display_Principle,
                        padding=ft.padding.all(20),
                    ),
                    margin=ft.margin.all(10),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        )
    )
ft.app(target=main,web_renderer=ft.WebRenderer.HTML,view=ft.AppView.WEB_BROWSER)
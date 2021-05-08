prompt = """
###
Input: A green button that says Hello World
Output:
MDRaisedButton:
    text: "Hello World"
    md_bg_color: cfh(colors["Green"]['700'])
###
Input: Big Red Label with text I am a label
Output:
MDLabel:
    text: "I am a Label"
    halign: "center"
    theme_text_color: "Custom"
    bold: True
    text_color: cfh(colors["Red"]['800'])
    font_style:"H2"
###
Input: Small gray Label with text please read terms and conditions carefully
Output:
MDLabel:
    text: "Please read terms and conditions carefully"
    halign: "center"
    theme_text_color: "Custom"
    bold: False
    text_color: cfh(colors["Gray"]['800'])
    font_style:"H6"
###
Input: Medium size Label saying This is a nice Label
Output:
MDLabel:
    text: "This is a nice Label"
    halign: "center"
    theme_text_color: "Custom"
    bold: True
    text_color: cfh(colors["Gray"]['800'])
    font_style:"H4"
###
Input: A medium size icon button with icon language python
Output:
MDIconButton:
    icon: "language-python"
    id: language_python_icon_btn
    theme_text_color: "Custom"
    text_color: cfh(colors["Gray"]['800'])
    user_font_size: sp(50)
###
Input: A big red icon button with arrow left icon
Output:
MDIconButton:
    icon: "arrow-left"
    id: arrow_left_icon_btn
    theme_text_color: "Custom"
    text_color: cfh(colors["Red"]['700'])
    user_font_size: sp(74)
###
Input: A screen with a Toolbar with title Activities
Output:
MDScreen:
    md_bg_color: cfh(colors["Gray"]['100'])
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Activities"
            elevation: 10
        Widget:
###
Input: A green screen with a teal Toolbar that says I am a Toolbar
Output:
MDScreen:
    md_bg_color: cfh(colors["Green"]['100'])
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "I am a Toolbar"
            elevation: 10
            md_bg_color: cfh(colors["Teal"]['500'])
        Widget:
###
Input: Screen with a red Toolbar with title red toolbar
Output:
MDScreen:
    md_bg_color: cfh(colors["Gray"]['100'])
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Red Toolbar"
            elevation: 10
            md_bg_color: cfh(colors["Red"]['500'])
        Widget:
###
"""

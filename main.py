def on_button_pressed_a():
    for index in range(2):
        basic.clear_screen()
        basic.show_icon(IconNames.SQUARE)
    basic.show_string("Hello!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_icon(IconNames.TARGET)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
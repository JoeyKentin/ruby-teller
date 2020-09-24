Teller = 0

def on_button_pressed_a():
    global Teller
    Teller = Teller + 1
    if Teller == 5:
        basic.show_icon(IconNames.HEART)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    else:
        basic.show_number(Teller)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Teller
    Teller = Teller - 1
    basic.show_number(Teller)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)

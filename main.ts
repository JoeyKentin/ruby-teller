let Teller = 0
let y = 0
let x = 0
let z = 0
input.onButtonPressed(Button.A, function () {
    Teller = Teller + 1
    y = 10
    x = Teller
    z = x % y
    if (z == 0) {
        basic.showIcon(IconNames.Heart)
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
    } else {
        basic.showNumber(Teller)
    }
})
input.onButtonPressed(Button.B, function () {
    Teller = Teller - 1
    basic.showNumber(Teller)
})
basic.forever(function () {
	
})

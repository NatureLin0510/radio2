radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showNumber(1)
    } else {
        basic.showString("K")
    }
})
radio.setGroup(100)

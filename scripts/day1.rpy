label khdDay1:
    $ new_chapter(2, u"КХДшное лето. День 1")

    window hide
    show screen nextDay("День первый", "screen tvar") with Dissolve(0.5)
    play sound khdAmbList["crash"]                          #экран начала дня
    $ renpy.pause(2)
    hide screen nextDay with Dissolve(0.5)
    window show

    "day1"
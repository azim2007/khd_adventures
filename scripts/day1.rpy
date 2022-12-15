label khdDay1:
    $ new_chapter(2, u"КХДшное лето. День 1")

    $ day_time()
    $ persistent.sprite_time = "day"                        #смена оформления на летнее дневное
    
    window hide
    show screen nextDay("День первый", "screen tvar") with Dissolve(0.5)
    play sound khdAmbList["crash"]                          #экран начала дня
    $ renpy.pause(2)
    hide screen nextDay with Dissolve(0.5)
    window show

    scene bg int_bus                                        #в автобусе
    show blinking
    play music music_list["no_tresspassing"] loop           #тревога музыка
    bgd "ля, че так жарко"
    "Богдан ощутил себя евреем в 39ом"
    bgd "ААААААА{w} я женщина... ААААААА"
    bgd "лан, шучу"
    th "так всм а где я"
    th "кожанные сидушки, {w}яркий свет, {w}все выглядит рисованно, как в БЛ"
    th "ааааа, ну все понятно"
    th "я на стачке шахтеров в кузбассе в 1961"
    th "АААААААА {w}я в 1961... {w}так телефон есть, наушники есть... {w}фууух, не заскучаю..."
    th "аааааа, а зарядка?"

    play sound khdMusicList["metal_noise"]                  #звук перебирания          
    $ renpy.pause(2.0)
    "в рюкзаке Богдан нашел все: {w}тетрадки, ручки, другую ерунду, {w}жесткий диск, {w}интел кор ай 7, 
    {w}электрогитару, {w}дизельный корабельный двигатель, {w}и файнали..."
    

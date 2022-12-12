label dayAtHome:
    scene bg intro_xx                                       #салон автобуса
    show unblink
    $ renpy.pause(1) 
    play music music_list["trapped_in_dreams"]              #музыка для мечтаний
    th "бляяя...{w} вот это я охуенно подрочил..."
    play music music_list["doomed_to_be_defeated"]          #тревога
    th "СТОП... {w}ПОЧЕМУ Я В АВТОБУСЕ????"

    show blink
    $ renpy.pause(1) 
    scene toilet_room
    show unblink                                            #моргание
    $ renpy.pause(1) 

    play music khdMusicList["pofig"]
    th "о, {w}так-то лучше"
    th "че то по моему мнению галлюны это немного ненормально {w}а, блин,{w} я забыл, что я сам по себе немного ненормальный"
    th "а вообще {w}ПОХУЙ НАХУЙ!"
    th "как эту ебаную музыку в голове выключить?"
    th "..."
    th "ладно."
    th "так, блин, {w} а на что я дрочил?"
    th "ах точно! {w}на Икарус из Бесконечного Лета..."

    scene bg ext_bus                                        #Воспоминание про икарус
    show prologue_dream
    with Dissolve(0.5)
    th "Икарус... {w}Икарус... {w}Икарус..."
    hide prologue_dream
    scene toilet_room                                        #Возвращение из воспоминаний обратно в ванную
    with Dissolve(0.5)
    "я чуть не кончил во второй раз"

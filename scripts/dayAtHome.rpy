label dayAtHome:
    $ new_chapter(1, u"КХДшное лето. Начало")

    show screen nextDay("День дома", "screen trol") with Dissolve(0.5)
    play sound khdAmbList["sranie"]                         #экран начала дня
    $ renpy.pause(2)
    hide screen nextDay with Dissolve(0.5)

    scene bg intro_xx                                       #салон автобуса
    show unblink
    $ renpy.pause(1) 
    play music music_list["trapped_in_dreams"]              #музыка для мечтаний
    th "бляяя...{w} вот это я охуенно подрочил..."
    play music music_list["doomed_to_be_defeated"]          #тревога
    th "СТОП... {w}ПОЧЕМУ Я В АВТОБУСЕ????"

    show blink
    $ renpy.pause(1) 
    scene bg toilet_room
    show unblink                                            #моргание
    $ renpy.pause(1) 

    play music khdMusicList["pofig"] loop volume 0.3        #музыка пофиг
    th "о, {w}так-то лучше"
    th "че то по моему мнению галлюны это немного ненормально {w}а, блин,
    {w} я забыл, что я сам по себе немного ненормальный"
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
    scene bg toilet_room                                    #Возвращение из воспоминаний обратно в ванную
    with Dissolve(0.5)
    "я чуть не кончил во второй раз"

    play sound khdAmbList["unitaz"]                         #звук смыва
    "..."
    "Богдан смыл за собой все свои выделения и направился на кухню, 
    чтоб позавтракать как настоящий чемпион {w}по количеству дрочек в день"
    scene bg kitchen_room with Dissolve(0.5)                #переход в кухню
    th "хмм... {w}чтоб себе приготовить?"
    th "пожарю яйца"
    play ambience khdAmbList["friing"] loop

    window hide
    $ set_mode_nvl()                                        #nvl mode
    nvl show Dissolve(0.3)
    "Пока жарятся яйца, немного расскажем вам о главном герое"
    "Наверное, вы уже поняли, что он немного не нормальный, {w}и в дальнейшем найдете 
    этим мыслям хорошее подтверждение"
    "ГГ, ясное дело, был взят с ИРЛ человека, но ИРЛ он не настолько необычен {w}в общем, 
    все, что он делает в моде - ЛИШЬ СЦЕНИЧЕСКИЙ ОБРАЗ, ИРЛ бы он такого не сделал"
    "кстати, ГГ зовут Богдан {w}вот и познакомились"
    "Что такое КХД из названия мода?"
    "Клуб"
    "Хронических"
    "Девственников"
    "В общем, в этом клубе состоят 3 человека: {w}Богдан, Макар и Автор этого мода"
    "Суть клуба в полном игнорировании тней(селедок) и полной отдаче какому-нибудь делу 
    {w} (искусству, созданию чего-либо)"
    "(на деле это просто \"Инцълобат всъя Русь\")"
    "в общем-то все, приятного прочтения!"
    nvl hide Dissolve(0.3)
    $ set_mode_adv()                                        #adv mode
    window show

    "о, яйца пожарились!"
    stop ambience
    th "бля, {w}я их в скорлупе пожарил..."
    th "ну и ладно {w}съем со скорлупой"

    play ambience khdAmbList["egg_eating"]                  #поедание яйца
    "Богдан был вне себя от наслаждения яйцом в скорлупе"
    th "ммм... {w}оно пожарилось наславу, {w}все полезные микро и макро элементы, 
    а также цианистый калий, содержащиеся в скорлупе заиграли новыми красками"
    "после поедания яйца Богдан решил выпить чифир, {w}заваренный им еще со вчерашнего дня"

    stop ambience
    scene cg chifir with Dissolve(0.3)
    th "мммм... {w}как же аппетитно он выглядит..."
    play ambience khdAmbList["drinking"]                    #звук чифира
    bgd "оаоаоаоаоаао {w}оаоаоаоаоаоао{w} ммммм как же это вкусно"
    stop ambience
    "Богдан выпил поллитра чифира залпом, не думая о том, что у него язва желудка 4 степени. 
    {w}Во всяком случае, ему было настолько похуй, что он даже не почувствовал адской боли от 
    разрыва кишки"
    th "ну поели - можно и в вангеров поиграть"

    scene bg semen_room with Dissolve(0.5)                  #комната Богдана
    $ renpy.pause(1)
    play music khdMusicList["vangers"] volume 1             #музыка из вангеров
    scene cg playing_vangers with Dissolve(0.5)             #Богдан играет в Вангеров
    bgd "аааа {w}АААА {w}СЪЕБИ НАХУЙ ЕБАНЫЙ РАФА! {w}...{w} ааааа, как же заебали эти кочки"
    bgd "ыыыыыыы, {w}БЛЯТЬ Я ПРОВАЛИЛСЯ СУКА, ОТСЮДА НЕ ВЫБРАТЬСЯ {w}НУ НАХУЙ, Я НЕНАВИЖУ ЭТУ ЖИЗНЬ"
    stop music
    play sound khdAmbList["crash"]                          #звук падения компа
    scene bg semen_room with Dissolve(0.5)                  #комната Богдана
    bgd "ой {w}кажется я психанул, сделал офицерский выход на столе, насрал себе на лицо, 
    и выбросил компьютер с 7 этажа..."
    bgd "случайно..."
    bgd "ну ладно... {w}мама новый купит"

    th "так, во сколько там у нас уроки сегодня начинаются... {w}а, точно, в 8:30"
    th "а время сейчас 9:00... {w}ну норм, как раз успеваю"

    play sound khdAmbList["closing_door"]                   #звук двери
    scene bg khd_podezd with Dissolve(0.5)                  #подъезд
    "выйдя в подъезд, Богдан встретил нарика"
    "поначалу он хотел на него нассать, но потом передумал"
    "ведь сегодня он ссыт на нарика, а завтра для него пойдет дождь, {w}и не простой, а золотой!"
    play sound khdAmbList["podezd_door"]                    #звук домофона
    scene bg winter_outside with Dissolve(0.5)              #зимняя улица
    play sound khdAmbList["boots_on_snow"] loop             #звук ботинок на снегу

    "Богдан любит ходить по улице, слушая приятную, успокаивающую музыку"
    "Именно поэтому, сегодня он решил послушать Skipknot"
    stop sound
    play music khdMusicList["slipknot_sic"] loop volume 1   #slipknot sic музыка
    "..."
    scene bg tram_station with Dissolve(0.5)                #трамвайная остановка
    th "сегодня мне снился странный сон..."

    scene cg school65                                       #воспоминания про 65
    show prologue_dream
    with Dissolve(0.5)
    th "сначала мне приснилось, что меня выгнали после 8 класса, и я пошел в 65 школу"
    th "где мне пришлось дружить с таджиком"
    th "крутой чел был"
    scene cg sharaga
    show prologue_dream                                     #воспоминания про шарагу
    with Dissolve(0.5)
    th "а потом мне пришлось идти в шарагу, где ко мне пристал чел со странным голосом, он уже был не крутой"
    th "ужасный сон {w}как же хорошо, что я пошел в 10 класс и остался со своим другом Макаром"
    scene cg makar_cup
    show prologue_dream                                     #воспоминания про Макара
    with Dissolve(0.5)
    th "да, вот Макар - реально топ кент {w}сколько всего мы с ним пережили, начиная с 8 класса"
    hide prologue_dream

    scene cg ext_tram with Dissolve(0.5)
    play sound khdAmbList["tram_sound"]                     #приезжает трамвай
    "из рассуждений Богдана вывел звук приближающегося трамвая"
    scene cg int_tram with Dissolve(0.5)                    #внутри трамвая
    th "о место свободное, сяду"
    "на самом деле на то место хотела сесть бабка,{w} но Богдан ее опередил, и ему было похуй, 
    что она ему там говорит, так как он слушал музыку"

    show blinking
    th "кажется чифир имел сегодня снотворный эффект"
    show blinking
    th "не спать... {w}не спать... {w}не спать... {w}"
    show blinking                                           #Богдан засыпает
    th "не спа... *звуки спания*"
    show blink
    $ renpy.pause(1)
    stop music
    jump khdDay1
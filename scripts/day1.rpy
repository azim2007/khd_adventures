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

    play sound khdAmbList["metal_noise"]                  #звук перебирания          
    $ renpy.pause(2.0)
    "в рюкзаке Богдан нашел все: {w}тетрадки, ручки, другую ерунду, {w}жесткий диск, {w}интел кор ай 7, 
    {w}электрогитару, {w}дизельный корабельный двигатель, {w}и файнали..."
    stop sound
    scene cg svar_apparat with Dissolve(0.5)                #сварочный аппарат
    "он нашел зарядку для телефона"

    scene bg int_bus with Dissolve(0.5)                     #снова в автобусе
    th "топчик, {w}ну все, можно идти трудиться в шахту кузбасса на благо партии"
    play ambience ambience_camp_entrance_day loop           #звуки перед воротами
    scene bg ext_camp_entrance_day with Dissolve(0.5)       #ворота
    "Богдан вышел из автобуса и понял, что не не на кузбассе 1961го"
    th "co-be-hok{w} что бы это могло значить?{w} хмммм, а может тут на русском написано?"
    th "совенок... Я ЧЕ В БЕСКОНЕЧНОЕ ЛЕТО ПОПАЛ?????"
    play music khdMusicList["i_w_t_p_gachi"]                #музыка Ульяны гачи ремикс
    show bg ext_camp_entrance_day:
        linear 0.2 ypos 0.9
        linear 0.2 ypos 1.0                                 #прыжки
        repeat

    th "Урааа{w} я в бесконечном лете"
    "От радости Богдан запрыгал, забыв, что в его рюкзаке лежат жесткий диск, интел кор, электруха и двигатель"
    show bg ext_camp_entrance_day                           #ворота
    th "так стоп, {w}а Икарус то здесь еще?"
    scene bg ext_bus with Dissolve(0.5)                     #автобус
    th "Икарусик, мой Икарус"
    show blink
    $ renpy.pause(1)
    play music khdMusicList["semyaiz"]                      #семяизвержение Стрыкало
    show black                                              #закрытые глаза
    "Богдан всем телом прижался к икарусу"
    "Нежность и тепло разлились по его телу,{w} он готов был расствориться в Икарусе, остаться навсегда с ним, 
    слиться с ним воединое"
    "Его прекрасные формы так и ласкали кожу Богдана, {w}а приятная вибрация мотора возбуждала его"
    "а его окна...."
    sl "эммм...{w} извиняюсь?"
    th "да блять, кто там пришел"
    bgd "не мешай! {w}не видишь? я занят!"
    sl "И чем же ты занят, интересно мне знать?"
    bgd "Я питаюсь энергией денег, {w}ой, всмысле Икаруса"
    sl "ты тупой что-ли?"
    bgd "ЧЕ СКАЗАЛ?"

    scene bg ext_camp_entrance_day                          #вход в совенок
    show sl angry pioneer at center                         #Славя злая
    with Dissolve(0.5)
    play music music_list["pile"]                           #музыка наказание

    "Когда Богдан понял, что это была Славя, он проглотил язык, {w}буквально {w}и начал задыхаться, но не подал виду, так 
    как знал, что Славя точно обеспокоится и категорически этого не хотел"
    sl "Ну и че застыл? {w}женщину в первый раз увидел?"
    bgd "Да."
    "это была чистая правда"
    sl "а как так?"
    bgd "аче не норм для 12 лет?"
    sl "нет, только для 11 норм"
    bgd "лол, я в шкафу прячусь"

    stop music
    show sl smile pioneer at center                         #Славя улыбается
    sl "хахаха {w}а ты смешной"
    show sl normal pioneer at center                        #Славя нормальная
    sl "блин, я не представилась..."
    bgd "стой, можешь не представляться, я сам имя угадаю"
    show sl surprise pioneer at center                      #Славя удивлена
    sl "чеее, всмысле, а как?"
    bgd "ща увидишь"
    play music khdMusicList["chunga"]                       #смешная гачи чунга чанга
    "Богдан начал жоско танцевать чунга-чангу"
    show sl laugh pioneer at center                         #Славя смеется
    "Славю это сильно рассмешило, {w}она уже каталась по земле в конвульсиях"
    "к сожалению, Богдан вовремя остановился"
    stop music
    sl "нннну и..... ахахахахахаахахах..... {w}так как меня зовут"
    bgd "чутье подсказывает мне, ты Славяной будешь"
    show sl surprise pioneer at center                      #Славя удивлена
    sl "чтоооооо? {w}как ты угадал?"
    bgd "хз, на предиктычах"
    sl "ок пон"
    show sl normal pioneer at center                        #Славя нормальная
    sl "ты это, {w}тебе к вожатой ща надо"
    bgd "к Олечке?"
    sl "какой Олечке?"
    bgd "ну вожатой"
    sl "нееее, вожатую не так зовут, {w}блин у нее имя такое... {w} странное... {w}что-то на До..."
    th "опа, а это еще че за пиво и приколы? Какая еще До..."
    sl "ну короче это, тебе к дому треугольному"
    bgd "ага"
    hide sl normal pioneer with Dissolve(0.5)               #Славя ушла

    "Славя скрылась за воротами, а Богдан все еще обдумывал, что это за До"
    th "хммм... {w}Домашний пивзавод? {w}Ну во всяком случае мечтать не вредно"

    scene bg ext_clubs_day with Dissolve(0.5)               #Клубы
    play ambience ambience_camp_center_day loop
    "В раздумьях Богдан зашел в лагерь и подошел к зданию клубов"
    th "оооо, логово пидора...{w} ой простите кхдшников"
    th "то есть таких как я"
    th "ну надо навеное зайти к ним, поздороваться что-ли"

    play sound sfx_open_door_clubs_2                        #звук двери
    play ambience ambience_clubs_inside_day loop            #звук внутри клубов
    scene bg int_clubs_male_day                             #внутри клубов
    show mkr norm far at cright                             #Макар
    with Dissolve(0.5)
    th "это что Макар????"
    bgd "МАКАР ЭТО ТЫЫЫ?"
    show mkr sad far at cright                              #Макар грустный (испуганный)
    mkr "ААААА, кто здесь.... {w}а, ты новенький, ну ты почти угадал,{w} меня зовут Икар"
    show mkr norm far at cright                             #Макар
    th "почти как Икарус"
    "Богдан опять размечтался об Икарусе"
    bgd "ок, меня Богдан"
    bgd "аче ты тут делаешь то? Всмысле что за клуб, есть ли тут еще кто?"
    mkr "это игродельная студия, ну то есть мы тут игры под zx spectrum делаем и на кассеты записываем"
    th "чет припоминаю у бати были такие кассеты с пакманом, змейкой и тетрисом"
    bgd "а кто мы?"
    mkr "ну тут еще есть один чел, {w}его Тоха Доха зовут"
    mkr "но он ща в музклуб пошел, {w}кассеты у них пиздить, ато свои у нас закончились"
    mkr "тут такое дело, мы игру затеяли, там по сюжету чел просыпается в логове у зеленой гусеницы с 8 глазами, 
    {w}она называется элиподом,{w} а потом надо развозить флегму и нимбос, участвовать в элирекции и т д, и открывать новые
    миры, {w}а в конце игры происходит разлом четвертой стены и игрок в шоке"
    th "хахах, они че вангеров делают?)"
    mkr "игра, кстати, Вангеры называется"
    mkr "но как погляжу, ты слишком глуп внимать мне, что с тебя взять, несчастная личинка элипода, что зря жирел и породил
    тебя - урода"
    bgd "ага да, миры у вас там наверное называются фострал, глоркс, икспло, да?"
    show mkr smile far at cright                            #Макар улыбается
    mkr "а ты откуда знаешь? {w}ну хотя ладно, кстати, хочешь в наши игры поиграть?"
    
    play music khdMusicList["cool_mus"]                     #крутая музыка)
    bgd "а какие есть?"
    mkr "есть дота 2, недавно сделали, {w}на трубе играть умеешь?"
    bgd "нет, а что?"
    mkr "да, там просто управление такое, {w}тоже в рот надо брать"
    bgd "ну ниче, ща научусь)"
    show mkr smile far at goLeft                            #Макар уходит в кладовку
    play sound khdAmbList["metal_noise"]                    #звуки поиска 
    "Икар ушел в кладовку искать кассету с дотой 2"
    th "хммм, а тут так то норм челы, судя по всему обитают"
    stop sound 
    scene cg makar_dota with Dissolve(0.5)                  #Макар играет в доту
    mkr "ну ка погоди... {w}о, катка нашлась, я на кунке играть буду, ща покажу"
    mkr "во, чекай, вот это ходить, {w}вот так стрелять, {w}во ульта"
    mkr "ну, все давай садись на киберспорт-табуретку..."
    hide cg makar_dota
    stop music
    window hide
    $ renpy.movie_cutscene(khdVidList["dota"])              #видео с дотой
    window show

    scene bg int_clubs_male_day                             #в клубах
    show mkr smile far at cright                            #Макар улыбается
    with Dissolve(0.5)
    mkr "ну, как тебе?)"
    "на самом деле судьба компа кибернетиков чуть не повторила судьбу компа Богдана"
    bgd "ну, игра хорошая, только сложная, реакцию надо иметь, {w}короче мне не понравилось"
    show mkr sad far at cright                              #Макар грустный
    mkr "блиин, вот никто в нее играть не может"
    th "ну ниче, Икар, погоди, лет через 30 это станет мЕйНсТрИмОм"
    play sound sfx_open_door_clubs                          #открытие двери (Тоха)
    show mkr norm far at cright                             #Макар нормальный
    mkr "о, Тоха пришел"

    "в комнату зашел кудрявый чел, чем-то похожий на Электроника, но в отличии от него этот чел был темноволосым"



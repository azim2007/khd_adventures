#************************************** ПОСЛЕ УЖИНА ИДЕМ СМОТРЕТЬ ФИЛЬМ С КИБЕРНЕТИКАМИ (ЕСЛИ ВСТУПИЛИ В КЛУБ) *******

label titanEvening1DayKhd:
    show bg ext_dining_hall_away_sunset with Dissolve(0.5)  #столовая снаружи
    play music music_list["silhouette_in_sunset"]           #спокойная музыка под вечер
    "кибернетики опять говорили на эльфийском о чем-то своем кибернетическом, {w}Богдан их не слушал, ибо не понимал 
    ни одного слова"
    th "как с химией: {w}вроде на русском говорят, а ничего не понятно!"
    "в общем в таком обществе очень легко погрузиться в свои мысли, что наш Богдан и сделал"
    show bg ext_square_sunset with Dissolve(0.5)            #площадь
    bgd "здарова, Генда"
    show bg ext_houses_sunset with Dissolve(0.5)            #дорога с домиками
    "быстро пройдя площадь, наши мушкетеры направлялись прямо к клубу, {w}обстановочка для Богдана была по кайфу: дневная
    жарища уже прошла, и солнце постепенно клонилось к горизонту, распространяя запах полезных витаминов"
    th "интересно, здесь солнце тоже на западе садится?"
    "опять озвучиваем рандомные мысли."
    show bg ext_clubs_sunset with Dissolve(0.5)             #рядом с клубами
    "вот из-за угла показался рай компов и паяльников, и ребята подошли к нему"
    
    show bg int_clubs_male_sunset with Dissolve(0.5)        #в клубе
    play sound sfx_open_door_clubs                          #открытие двери
    play ambience ambience_clubs_inside_day                 #эмбиенс в клубах
    ant "так, Икар, ты помнишь где кассета?"
    mkr "хз, ну ты наверн ее в кладовку положил, куда ж еще?"
    show ant norm sunset at goLeft                          #Тоха уходит в кладовку
    play sound khdAmbList["metal_noise"]                    #звук поиска
    "пока Тоха искал кассету, Богдан стал рассматривать их клуб"
    th "интересно, какая у них ось на компе?... {w}зачем им паяльник кстати?... {w}а вечером тут все же атмосферненько"
    bgd "слушай, Икар, а зачем вам паяльник?"
    show mkr smile sunset at left                           #Макар улыбается
    mkr "а, это если Ульяна в клуб зайдет, ей глаза выколоть этим паяльником, хехехе"
    th "что за клуб садистов-то такой?"
    bgd "и много раз уже выкалывали?"
    mkr "уже четыре глаза выкололи, у нее регенерация на сотку вкачана, так что ей норм"
    th "да бля, {w}че не так с этим лагерем"
    show mkr norm sunset at left                            #Икар нормальный
    "пока Богдан в очередной раз недоумевал, Тоха уже нашел кассету и вернулся из кладовки в хорошем расположениии духа"
    
    stop sound
    show ant smile sunset at right with Dissolve(0.5)       #Тоха улыбается
    mkr "ну че, нашел?"
    ant "не то, что искал, но это лучше"
    "Антон протянул товарищам кассету с цветастым вкладышем"
    scene cg vhs_voron with Dissolve(0.5)                   #воронины кассета
    th "нихуя, тут есть этот шедевр!"
    "если кто не понял что это, то это воронины - величайший сериал, олицетворение нулевых, {w}для Богдана - это 
    глоток беззаботного прошлого, а для местных - картина светлого будущего"
    scene bg int_clubs_male_sunset                          #в клубе
    show mkr norm sunset at left
    show ant norm sunset at right                           #кибернетики нормальные
    with Dissolve(0.5)
    "но, пожалуй, отвлечемся от философских рассуждений и наконец посмотрим это произведение искусства"
    "Тоха взял кассету и вставил ее в проигрыватель"
    "ща рил будет серия ворониных, видик большой, мб зависнет, не пугайтесь"
    $ renpy.movie_cutscene(khdVidList["voroniny"])          #воронины
    
    "да, это жоско"
    show mkr smile sunset at left                           #Икар улыбается
    mkr "а хороший фильм, как раз под нашу тематику"
    show ant smile sunset at right                          #Антон улыбается
    ant "рял, я чет даже не заметил"
    th "эхххх, светлые нулевые... {w}навсегда утраченная эпоха, {w}хотя, тут она еще не наступила даже"
    play music music_list["get_to_know_me_better"]          #веселенькая музыка
    "какое-то время кибернетики обсуждали фильм, и то, как лучше реализовать детектор лжи, {w}Богдан же в это время 
    любовался закатом"
    "вдруг Богдан услышал свое имя, среди нескончаемых терминов в разговоре своих собутыльников"
    ant "Богдан, а кстати, ты завтра с кем на субботник идешь?"
    if evs2Day["cleaning"] == "mz":
        bgd "с Женей"
        show ant sad sunset at right
        show mkr sad sunset at left                         #кибернетики грустные
        ant "c-c-c кем?"
        "от услышанного имени Тоха и Икар скривились, на их лицах застыл тихий ужас"
        bgd "с Женей"
        mkr "а не съест?"
        bgd "а вот об этом я как-то не подумал, ну надеюсь нет"
        mkr "ну ты давай там осторожней, не шути с ней, ато я пытался ей показать серию рисунков своих \"еврейская 
        эпитафия\", а она на меня накричала и даже рисунки не посмотрела"
        bgd "да, наверное тебе тяжело как художнику от такого"
        show mkr norm sunset at left                        #Макар нормальный
        mkr "хоть кто-то меня понимает"
    else:
        bgd "какой еще субботник?"
        ant "ну, там все убираются, кто площадь подметает, кто цветы сажает, а мы в клубе убираем ну и еще там по мелочи 
        эксплуатируют нас как грузчиков"
        mkr "ну не преувеличивай, заставили его один раз сахар потаскать, грузчиком он стал"
        ant "короче, с нами будешь убираться завтра?"
        menu subbotnik_club:
            "да.":
                show ant smile sunset at right              #Антон улыбается
                $ evs2Day["cleaning"] = "titan"             #субботник с кибернетиками
                ant "о, ну здорово, тогда завтра после обеда приходи, будешь помогать"
            "нет.":
                $ evs2Day["cleaning"] = "sl"                #субботник со Славей
                show ant sad sunset at right                #Антон грустный
                ant "блин, ну ладно"
                mkr "че, Тох, не будет помощников сахар таскать?"
                ant "а ты?"
                mkr "ну яяя... {w}хотя да, ладно"
            
    "посидев еще с минутку и поболтав с кибернетиками, Богдан все же встал и решил покинуть обитель кхд"
    bgd "че то мы засиделись, пора мне, пока ребят"
    ant "давай, удачи"
    mkr "пока, заходи еще"
    scene bg ext_clubs_sunset with Dissolve(0.5)            #рядом с клубами
    play ambience ambience_camp_center_evening              #эмбиенс на улице
    th "хммм, ну до ночи еще время есть, пойду на площадь что-ли"
    show bg ext_houses_sunset with Dissolve(0.5)            #дорога с домиками
    "Богдан неторопясь шел по дороге, думая над только что просмотренным сериалом, {w}ведь в нем безусловно очень 
    много смысловой нагрузки, как и между строк данного мода"
    show bg ext_houses_night with Dissolve(5.0)             #дорога с домиками ночью
    th "жалко так то Леню из Ворониных, {w}не легко наверное быть жирным уебаном"
    "Богдан так долго шел, что не заметил, как начало темнеть"
    play ambience ambience_camp_center_night loop           #эмбиенс на улице ночью
    "запах ночи, всеобщего расслабления животных, природы, растений, людей, наполнил воздух, сделав его свежим и 
    прохладным"
    th "интересно, что ща на площади происходит"
    show bg ext_square_night with Dissolve(0.5)             #центр площади
    "а на площади все как всегда, {w}Лена, мирно читающая книжку, полнейшая тишина и ночной покой, и лишь изредка 
    пробегающие мимо пионеры"
    "Богдан уселся на одну из скамеек, растопырил руки и поднял глаза к звездам"
    show cg stars_sky with Dissolve(0.5)                    #звездное небо
    "ну тут типо должны быть философские мысли, как в других модах"
    th "вчера я мог только мечтать об отправлении в БЛ, а теперь я здесь"
    th "как же все-таки иногда все просто получается: {w}не прикладываешь никаких усилий и оказываешься в раю на Земле, 
    {w}а иногда пилишь рэп-альбомы БДСеМ, и их никто не слушает"
    "(послушайте BDSeM)"
    th "не знаю, зачем Семен из каноничного БЛ хотел выбраться отсюда, но я бы остался здесь навсегда"
    scene bg ext_square_night with Dissolve(0.5)             #площадь
    th "ладно, время позднее, даже Лена уже ушла, пора и мне спать пойти"
    "Богдан встал со скамейки и направился к домику Доры"

    show bg ext_houses_night with Dissolve(0.5)             #дорога с домиками
    th "а завтра субботник... {w}не охота"
    "конечно, ну а кому охота трудиться за бесплатно, {w}даже в раю на Земле"
    show bg ext_house_of_mt_night with Dissolve(0.5)        #домик Доры
    "свет рядом с домиком еще горел, значит Дора еще не спала, {w}ну конечно, время то еще детское"

    show bg int_house_of_mt_night with Dissolve(0.5)        #в домике Доры
    play sound sfx_open_door_1                              #звук двери
    show dor norm night with Dissolve(0.5)                  #Дора нормальная
    play ambience ambience_int_cabin_night loop             #хвук в домике
    dor "о, вернулся, {w}что делал весь вечер?"
    bgd "фильмец с кибернетиками смотрел"
    dor "ого, ты подружился с ними"
    bgd "в клуб вступил"
    dor "ммм, не ожидала"
    bgd "а что так?"
    dor "да не знаю, они прост какие-то замкнутые, сами по себе, а ты тоже не сильно хорошо на контакт с людьми 
    идешь"
    th "ну, что правда, то правда"
    bgd "ну так вот именно, от одиночества люди притягиваются друг к другу, таков мир"
    dor "что ж, наверное ты прав"
    "разговаривая с Дорой, Богдан уже прошел на свою койку и лег, {w}Дора также лежала на кровати и читала какую-то 
    книжку"
    th "запишу себе в ачивки сон с Дорой в одном помещении"
    "по прошествии нескольких минут Дора закрыла книгу, встала и погасила свет"
    show bg int_house_of_mt_night2 with Dissolve(0.5)       #в домике Доры без света
    hide dor norm night with Dissolve(0.5)                  #Дора прячется
    dor "спокойной ночи, Богдан"
    bgd "спокойной ночи"
    "дав полежать Богдану еще с минуту, сон все же его одолел, и глаза Богдана постепенно начали слипаться"
    show blinking                                           #моргание
    "вскоре Богдан уснул"
    show blink                                              #глаза закрываются
    return

#************************************** ПОСЛЕ УЖИНА ИДЕМ МЕНЯТЬ ЛАМПОЧКУ С ДОРОЙ (ЕСЛИ НЕ ВСТУПИЛИ В КЛУБ) *******

label dorEvening1DayKhd:
    show bg ext_dining_hall_near_sunset with Dissolve(0.5)  #столовая рядом
    play ambience ambience_camp_center_evening loop         #эмбиенс вечером на улице
    play music music_list["lightness"]                      #музыка под вечер
    "Богдан с Дорой вышли из столовой и направились к своему домику"
    show bg ext_dining_hall_away_sunset with Dissolve(0.5)  #столовая снаружи
    "солнце постепенно садилось, освещая кроны деревьев золотыми лучами, что создовало несколько романтичную атмосферу, 
    учитывая, что Богдан шел с Дорой, для него это был неплохой такой турбо буст"
    show bg ext_square_sunset with Dissolve(0.5)            #площадь
    bgd "здарова, Генда"
    show dor norm sunset                                    #Дора нормальная
    dor "что что?"
    "Богдан вслух поздоровался с Гендой, забыв, что здесь такое поведение считается мягко говоря экзотическим"
    th "да бляяя, опять"
    bgd "я это, с памятником поздоровался"
    show dor smile sunset                                   #Дора улыбается
    dor "хаха, смешной ты"
    th "ну спасибо, хоть не сумашедший"
    
    show bg ext_houses_sunset with Dissolve(0.5)            #дорога с домиками
    "Дора с Богданом прошли площадь и по дороге направлялись к дому"
    show dor norm sunset                                    #Дора нормальная
    dor "ну че Богдан, {w}как тебе первый день в нашем лагере?"
    bgd "да знаете, классно, я вообще не думал, что когда-нибудь окажусь в таком месте"
    dor "в каком таком?"
    bgd "ну, в хорошем смысле, {w}тут и воздух чистый, и пляж есть, и клубы всякие, {w}одним словом - все, что нужно для 
    счастья"
    show dor smile sunset                                   #Дора улыбается
    dor "о, ну здорово, рада слышать, что тебе здесь понравилось"
    
    show bg ext_house_of_mt_sunset with Dissolve(0.5)       #Домик Доры
    "за разговором Богдан и не заметил, как они подошли к домику"
    show bg int_house_of_mt_sunset with Dissolve(0.5)       #в домике
    play sound sfx_open_door_1                              #звук двери
    play ambience ambience_int_cabin_evening loop           #звук в домике
    show dor norm sunset                                    #Дора нормальная
    dor "вот она, эта лампа, выкрути, пж, и поставь эту"
    "Дора протянула Богдану новую лампу накаливания"
    th "хммм, а тут есть знак качества?"
    "покрутив лампу, Богдан таки увидел заветный пятиугольник и надпись ГОСТ"
    th "не обманули!"
    dor "ты что, лампу впервые видишь?"
    bgd "ааа, {w}ой, задумался прост"
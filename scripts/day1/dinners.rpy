#*************************** УЖИН С ЖЕНЕЙ (ЕСЛИ ВСТУПИЛ В БИБЛИОТЕКУ) *************************************************

label mzDinner1DayKhd:
    hide mz normal glasses pioneer with Dissolve(0.5)           #Женя уходит за стол
    "в это время Женя уже взяла удон с говядиной и красное вино и уселась за стол, {w}ну а хули, она ж винишка, значит
    и питание соответствующее"
    "Богдан оглядел столовую, {w}как он и ожидал, из-за того, что он проспал людей в столовке уже было не много, {w}
    помимо него с Женей были разве что кибернетики и Алиса"
    th "как и ожидалось, ну, хотя, так даже лучше, никто не шумит"
    "родители всегда учили Богдана искать плюсы во всех мелочах"
    show mz angry glasses pioneer far with Dissolve(0.5)        #Женя злая
    "подойдя к столу, Богдан заметил, что Женя была чем-то раздражена"
    show mz angry glasses pioneer close                         #Женя злая близко
    bgd "хей, че за злая мина?"
    mz "всм, блять, хули ты так долго стоял после того, как чифир взял?"
    bgd "текст читал."
    show mz shy glasses pioneer close                           #Женя удивлена
    mz "какой еще текст?"
    bgd "хуй его знает, по ходу событий Автор озвучивает мои мысли и обстановку вокруг, приходится читать"
    "(типо разлом 4 стены)"
    mz "нихуя, я также хочу"
    bgd "лучше не надо, это выключить нельзя"
    th "оххх, бля, какая же Женя сочная, хочу вставить ей.... {w}блять, Автор, нахуя эти то мысли озвучивать?"
    show mz normal glasses pioneer close                        #Женя нормальная
    mz "ммм.... ладно"

    if evCibClubJoin:
        show mz smile glasses pioneer close                     #Женя улыбается
        mz "кстати, а ты мне не рассказывал, читал ли ты Возвращение 1980"
        th "нихуя, че еще за возвращение? {w}не уж то за 4 года я что-то упустил?"
        bgd "нет, вроде, не читал"
        show mz shy glasses pioneer close                       #Женя смущена
        mz "может, тогда это... {w}если ты не занят... {w}го что ли посидим, почитаем, {w}вместе"
        th "ага, \"почитаем\")"
        "Женя говорила пиздец смущенно, как будто у этой солевой было такое чувство как смущение, даже Богдан охуел"
        bgd "ну, вообще не свободен я сейчас, обещал с кибернетиками фильм смотреть"
        show mz angry glasses pioneer close                     #Женя злая
        "смущение как рукой смело"
        mz "то есть всмысле с кибернетиками... {w}ты водишься с этими..."
        "Женя была покультурней той же самой Алисы, поэтому решила воздержаться от нелестных реплик в адрес светил 
        советского игропрома"
        show mz bukal glasses pioneer close                     #Женя презирает
        mz "хотя... {w}вполне ожидаемо от тебя, я как только тебя встретила, сразу подумала, что ты заинтересуешься 
        их кружком, {w}не смею осуждать, у каждого свой жизненный путь"
        th "даааа, именно поэтому она это говорит с презрением"
        show mz normal glasses pioneer close                    #Женя нормальная
        "..."
        "посидев еще немного в неловкой тишине, Женя все же решила ее нарушить очередным типичным разговором 
        для винишко-тян и винишко-куна"
        show mz smile glasses pioneer close                     #Женя улыбается
        mz "ой, знаешь, Богдан, в ашане вино самое лучшее... ываромивро вора иыволап и фвокрыаи а ывфоари "
        "короче, бля, я заебался диалоги с Женей прописывать, {w}так что просто представьте разговор на серьезных щах
        о вине из ашана на 5 минут"
        "..."
        bgd "короче, это, Жень, мне пора"
        mz "ну ладно, давай, прятного просмотра"
        "Женя помахала рукой и улыбнулась"
        bgd "пока"
        hide mz smile glasses pioneer close with Dissolve(0.5)  #Женя прячется
        "Богдан унес стакан в мойку и отправился на выход"
        
        play ambience ambience_camp_center_evening              #эмбиенс на улице
        play sound sfx_close_door_1                             #закрытие двери
        scene bg ext_dining_hall_near_sunset with Dissolve(0.5) #рядом со столовой
        show ant norm sunset at right 
        show mkr norm sunset at left                                   #Тоха и Икар нормальные
        with Dissolve(0.5)
        "только Богдан вспоминал кибернетиков и сегодняшнее кино на троих, как на улице он увидел своих собутыльников 
        по фильму"
        bgd "йоу, ну че, идем фильм смотреть?"
        ant "ооо, ты вышел, здорово, теперь идем"
    else:
        "вдалеке показался силуэт Доры"
        show dor norm far sunset at right with Dissolve(0.5)    #Дора нормальная
        th "да бля, еще и Дора, вы хотите, чтоб я от спермотоксикоза сдох?"
        "Дора тем временем подошла ближе"
        show dor norm sunset at right                           #Дора ближе
        dor "йоу йоу йоу, Богдан, что делаешь после ужина?"
        show mz bukal glasses pioneer close                     #Женя с презрением
        "Женя как будто бы хотела что-то возразить, но Богдан ее опередил, находясь под действием спермотоксикоза"
        bgd "вроде ничего"
        show dor smile sunset at right                          #Дора улыбается
        show mz normal glasses pioneer close                    #Женя нормальная
        dor "здорово, здорово, {w}тогда это, тут такое дело, помощь в общем нужна, лампочка у нас в домике перегорела, 
        поменять надо, а я не достаю, поможешь?"
        "Богдан уже представил, как он помогает Доре, а она ему потом... {w}в прочем, не будем озвучивать все мысли
        Богдана"
        dor "але, че застыл"
        bgd "а, да, {w}конечно помогу"
        dor "вот и славно, тогда давай доедай, или допивай... {w}ой, фуууу, что это у тебя в чашке"
        "посмотрев на чифир, Дора наморщилась, после чего недоумевающе уставилась на Богдана, {w}но ей простительно, 
        это же Дора"
        bgd "это чифир"
        "Богдан никак не мог устать каждому встречному хвастаться своими экстравагантными вкусами, тем более - Доре, 
        поэтому эти слова он произнес с пребольшой гордостью, словно он самолично этот чифир синтезировал"
        dor "а, ну пей, пей, я тогда тут подожду"
        "все это время Женя молча сидела, уткнувшись в свою тарелку, {w}видимо Доре здесь никто перечить не смеет, {w}
        ну, все правильно: она ведь богиня"
        "следующие 5 минут Женя с отсутствующим видом доедала пюре, а Богдан мечтательно допивал чифир, представляя 
        как он сейчас поможет Доре и получит +100 сошиал кредит от нее"
        "вскоре Богдан допил чифир и вышел из-за стола"
        dor "о, допил, классно, тогда пойдем быстрее"
        "Женя медленно проводила Богдана подавленым взглядом, на ее лице можно было прочитать угнетение альфа-самкой 
        всея совенок, {w}но нашему герою уже было похуй на это, ведь он шел менять лампу с самой богиней 
        кьют-рока, с Дорой"
        hide mz normal glasses pioneer close with Dissolve(0.5) #Женя прячется
        "Богдан отнес чашку в мойку и направился с Дорой на выход"
    
    return

#*************************** УЖИН С АЛИСОЙ (ЕСЛИ ВСТУПИЛ В МУЗКЛУБ) **************************************************

label dvDinner1DayKhd:
    hide dv normal pioneer2 with Dissolve(0.5)                  #Алиса уходит за стол
    "в это время Алиса уже взяла пюрешку с котлеткой и заняла место"
    "Богдан оглядел столовую, {w}из-за того, что они убирались в музклубе на ужин они опоздали, столовая была почти 
    пустая, {w} за исключением кибернетиков и Жени"
    th "ну и сквад..."
    "частично описав параллель Б из его лицея, Богдан отправился за стол"
    show dv angry pioneer2 far with Dissolve(0.5)               #Алиса злая
    "Как Богдан заметил, Алиса была чем-то раздражена"
    show dv angry pioneer2 close                                #Алиса злая близко
    bgd "хей, че за злая мина?"
    dv "всм, блять, хули ты так долго стоял после того, как чифир взял?"
    bgd "текст читал."
    show dv surprise pioneer2 close                             #Алиса удивлена
    dv "какой еще текст?"
    bgd "хуй его знает, по ходу событий Автор озвучивает мои мысли и обстановку вокруг, приходится читать"
    "(типо разлом 4 стены)"
    dv "нихуя, я также хочу"
    bgd "лучше не надо, это выключить нельзя"
    th "оххх, бля, какая же Алиса сочная, хочу вставить ей.... {w}блять, Автор, нахуя эти то мысли озвучивать?"
    show dv normal pioneer2 close                               #Алиса нормальная
    dv "ммм.... ладно"
    
    if evCibClubJoin:
        show dv shy pioneer2 close                              #Алиса смущается
        dv "слууушай, Богдан, {w} а ты.... {w}сейчас куда планируешь?"
        "Алиса говорила пиздец смущенно, настолько, что даже Богдан, который за счет своего зрения не попал на СВО понял 
        это, {w}а, бля зрение на слух не влияет, ну и похуй, читаем дальше"
        th "это че, она смущается так типо?"
        bgd "ну вообще, с кибернетиками фильм смотреть собирался"
        show dv angry pioneer2 close                            #Алиса злая
        dv "ты че, с этими педиками водишься, и особенно с Тохой?"
        "смущение как рукой смело"
        play music music_list["that_s_our_madhouse"]            #энергичная музыка
        bgd "ну да, так я же в клуб вступил"
        show dv rage pioneer2 close                             #Алиса пиздец злая
        dv "ты еще и в клуб вступил, фыоваприлцгукнрсмышгувк рпыдушгк рцугшлцгшлукпр ыувлг, ну ты и пидрила конечно, 
        рывао рыпв ва орывалоры пава оа ваолр, ты норм ваще"
        "Алису просто распирало от злости"
        "в следующее мгновение в Богдана полетело недоеденное пюре"
        play sound sfx_water_sink_stream                        #типо Богдана бьет пюре

        show blinking
        "открыв глаза Богдан увидел, что Алиса все еще была зла, хотела что-то ему сказать, но была не в состоянии"
        show dv guilty pioneer2 close                           #Алиса виновная
        stop music fadeout 1.0
        "вскоре Алиса успокоилась и, судя по всему, чувствовала себя неловко из-за этого поступка"
        th "молчание мне не по душе"
        bgd "все еще обижаешься?"
        dv "да знаешь, не особо уже, прости что я тебя это, ну, {w}пюрешкой обмазала"
        bgd "нет уж, теперь отсосешь мне"
        show dv shy pioneer2 close                              #Алиса смущается
        dv "ну, я вообще-то не пробовала еще..."
        th "нихуя се блять, я ж пошутил"
        bgd "не, Алис, давай лучше в очко"
        dv "давай..."
        bgd "только это, у меня карт нет, у тебя не найдется колоды?"
        show dv surprise pioneer2 close                         #Алиса удивлена
        dv "каких еще карт..."
        show dv angry pioneer2 close                            #Алиса злая
        "ааааа, так ты в этом смысле, слушай, не надо злить пж"
        bgd "ладно, больше не буду"
        show dv normal pioneer2 close                           #Алиса нормальная
        "к этому времени Богдан уже допил чифир и вышел из-за стола"
        dv "давай, Богдан, что ли, хорошо фильм тебе посмотреть"
        bgd "тебе тоже удачи, пока"
        dv "пока"
        hide dv normal pioneer2 close with Dissolve(0.5)        #Алиса прячется
        "Богдан унес стакан в мойку и отправился на выход"

        play ambience ambience_camp_center_evening              #эмбиенс на улице
        play sound sfx_close_door_1                             #закрытие двери
        scene bg ext_dining_hall_near_sunset with Dissolve(0.5) #рядом со столовой
        show ant norm sunset at right 
        show mkr norm sunset at left                                   #Тоха и Икар нормальные
        with Dissolve(0.5)
        "только Богдан вспоминал кибернетиков и сегодняшнее кино на троих, как на улице он увидел своих собутыльников 
        по фильму"
        bgd "йоу, ну че, идем фильм смотреть?"
        ant "ооо, ты вышел, здорово, теперь идем"
    else:
        "в это время в далеке показалась Дора"
        show dor norm far sunset at right with Dissolve(0.5)    #Дора нормальная
        th "о, нихуя, к нам идет, {w}прям на меня смотрит"
        "если бы это была Олечка, Богдан бы не был так рад, но тут - сама Дора, ради нее он был готов хоть 100 мешков с 
        сахаром перетаскать"
        show dor norm sunset at right                           #Дора нормальная
        $ renpy.pause(1)
        show dor sad sunset at right                            #Дора грустная
        dor "ээээ, Алиса, ты че нефар? нормально рубашка одевай"
        show dv sad pioneer close                               #Алиса грустная с норм рубашкой
        dv "ну Дораааа..."
        dor "не Доркай мне тут!"
        th "сразу видно, кто тут альфа, {w}это я!"
        show dor norm sunset at right                           #дора нормальная
        dor "йоу, йоу, Богдан, че делаешь после ужина?"
        bgd "да хз, ниче не делаю"
        show dv surprise pioneer close                          #Алиса удивлена
        "Алиса удивилась и точно хотела что-то сказать, но Дора ее опередила, а как вы поняли перечить Доре даже сама 
        Алисочка не смеет, что еще раз доказывает, что Дора - богиня"
        "извините"
        show dv sad pioneer close                               #Алиса грустная
        "Алису явно угнетало присутствие Доры"
        dor "здорово, в общем, там в домике нашем лампочка перегорела, а я крч не достаю до туда, поможешь в общем?"
        bgd "ну, да, хуу... {w}ой то есть, {w}конечно помогу!"
        show dor smile sunset at right                          #Дора улыбается
        dor "о, классно, тогда доедай... {w}или допивай, {w}ужас, что это у тебя в чашке?"
        "Дора посмотрела сначала в чашку, а потом вопросительно на Богдана"
        bgd "чифир."
        dor "а, ок"
        "Богдан задумчиво попивал чифир, предвкушая то, как он будет менять лампочку для Доры, {w}Алиса же решила уткнуться 
        носом в тарелку, чтобы больше не видеть Дору"
        "наконец, допив чифир Богдан встал из-за стола"
        dor "о, допил, тогда пошли в домик"
        "Алиса проводила Богдана взглядом, полным отчаяния и горя, но Богдану было похуй, так как он сейчас пойдет менять 
        лампочку с самой богиней кьют рока - Дорой"
        hide dv sad pioneer close                               #Алиса прячется

        "Богдан унес стакан в мойку и вместе с Дорой отправился на выход"

    return

#*************************** УЖИН С КИБЕРНЕТИКАМИ (ЕСЛИ ВСТУПИЛ В КИБЕРКЛУБ) ****************************************

label titanDinner1DayKhd:
    play music music_list["dance_of_fireflies"]                 #музыка вечер на подумать
    "после попадания чашки с чифиром Богдану в руки, он решил оглядеть столовую на наличие в ней живых существ"
    th "хмм... ну, Женя сидит в углу, ее я кажется обидел, вряд ли с ней получится сесть"
    "в одиночку есть Богдан категорически не желал, так как в людных местах, по его мнению, лучше есть в небольшой 
    компании людей, так спокойней"
    "помимо Жени в столовой так же были кибернетики, ведущие спор о чем-то своем кибернетическом и Алиса, скучающе 
    ковыряющая пюрешку"
    th "ну, Алиса чет не в настроении, сяду с кибернетиками"
    th "тем более, мне после ужина с ними идти фильмец смотреть"

    show ant norm sunset at right with Dissolve(0.5)            #Тоха
    show mkr norm sunset at left with Dissolve(0.5)             #Икар
    bgd "йоу, мужики, не занято?"
    show ant smile sunset at right                              #Тоха улыбается
    ant "а, нет кшн, присаживайся"
    show ant smile close sunset at right                        #Тоха
    show mkr norm close sunset at left                          #Икар 
    "Богдан сел за кибернетический стол"
    show ant norm close sunset at right                         #Тоха нормальный
    mkr "опять чифир?"
    bgd "именно"
    mkr "феноменально, не думал, что человек может развить себе способность питаться только от чифира"
    bgd "как оказалось - может"
    ant "кстати, Богдан, где ты был после обеда, {w}я видел, что ты куда-то шел, а вот куда - не понял"
    bgd "так я это, на пляже был"
    ant "аааа, а я то думал на склад старый пошел, откуда мы... {w}ой ну то есть..."
    show mkr smile close sunset at left                         #Икар улыбается
    mkr "то есть не мы, а Ульяна, и не на склад, а так, по крышам прыгала"
    "Икар подмигнул Богдану и переглянулся с Тохой"
    th "ладно, не буду даже спрашивать у близнеца моего Макара, чем они там таким в старом складе занимались, {w}ну, 
    в смысле, какие детали там искали"
    ant "ну че, Богдан, киношка в силе?"
    bgd "ага"
    show ant smile close sunset at right                    #Тоха улыбается
    "Тоха сразу повеселел, видно общения с людьми кроме Икара ему явно не хватало"
    show us grin pioneer far at right with Dissolve(0.5)    #Ульяна ухмылка
    show ant smile close sunset at right                    #Тоха улыбается
    "вдруг вдалеке показалась Ульяна, {w}по ее глазам было видно, что она что-то замышляет, и шла она в направлении 
    нашей кхд братии"
    play music music_list["i_want_to_play"]                 #музыка Ульяны
    show us grin pioneer at right                           #Ульяна ближе
    us "слушай, Антон, как дела у тебя?"
    show ant sad close at right                             #Антон грустный
    ant "как обычно"
    "видимо с этим человеком Тохе общаться явно не хотелось"
    show us surp3 pioneer at right                          #Ульяна удивлена
    us "что же ты так грубо... {w}ой, это что, Алиса в купальнике?"
    "после этих слов Тоха с каменным выражением лица скрутил Ульяну и с криком suction сломал ей обе руки"
    play sound sfx_bones_breaking                           #Звук костей
    show us fear pioneer at right                           #Ульяна напугана
    us "ААААААААААААААААА ФЫВА РФВЫАФВ ФЩУУКАШР ФЫВДОАРУ ФДК АУ"
    "Ульяна скривилась от боли, будто ей сломали обе руки, {w}хотя лол, ей и так сломали обе руки"
    show us fear pioneer at goLeft                          #Ульяна убегает
    show ant smile close at right                           #Тоха улыбается
    ant "ахахахахахахаах, ну что за нуб?"
    mkr "красава, наебал лоха"
    th "пиздец, в 8 классе мне такое даже не снилось"
    bgd "а она не пожалуется?"
    ant "да не, по дороге от боли сдохнет, потом очнется с амнезией"
    bgd "а, ну тогда ладно, главное - анонимность"
    "этими словами Богдан частично описал свою любовь к анонимным имиджбордам и ананирующим имидживым бородам"
    show ant norm close at right                            #Тоха нормальный
    show mkr norm close at left                             #Икар нормальный
    "оставшуюся часть ужина наши пионеры провели более ли менее спокойно: {w}кибернетики, посмеиваясь, доедали пюрешку, 
    а Богдан допивал напиток богов"
    mkr "ну че как, допил?"
    "Икар уже встал из-за стола и вместе с Тохой собирался уносить тарелки"
    bgd "ну да, допил"
    "Богдан вместе с кибернетиками отнес чашки и тарелки в мойку и направился к выходу"

    play ambience ambience_camp_center_evening              #эмбиенс на улице
    play sound sfx_close_door_1                             #закрытие двери
    scene bg ext_dining_hall_near_sunset with Dissolve(0.5) #рядом со столовой
    show ant norm sunset at right 
    show mkr norm sunset at left                                   #Тоха и Икар нормальные
    with Dissolve(0.5)
    th "ну все, ща пойдем крутить вхс кассеты"

    return
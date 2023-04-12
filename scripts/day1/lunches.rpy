#*************************************** ОБЕД С КИБЕРНЕТИКАМИ ****************************************

label khdBoyLunch:
    "(кхд партия гордится тобой!)"
    show mkr norm at cright
    show ant norm at cleft                                  #Тоха и Икар 
    with Dissolve(0.5)
    "кибернетики о чем-то очень бурно разговаривали"
    ant "я тебе говорю, как ты собрался mvc на ассемблере реализовывать?"
    mkr "легчайше: для начала на ассемблере напишем какой-нибудь ооп язык типо джавы, а потом на нем лабать будем..."
    bgd "извините, а у вас не занято?"
    ant "нет конечно, садись"
    show mkr norm close at cright
    show ant smile close at cleft                           #Тоха и Икар близко

    play music music_list["just_think"]                     #музыка подумать
    show blink
    $ renpy.pause(1)
    scene black
    "кибернетики напомнили Богдану о времени, когда он с другом пытался сделать игрорю в стиле фаллаута 1"
    th "дааа, хорошее было время"
    "Богдан полностью ушел в свои мысли, и разговоры кибернетиков лишь изредка доносились до его сознания"
    th "тогда я не боялся мечтать, думал, что все еще впереди, и будущее казалось светлым и радостным"
    th "теперь же я целыми днями просиживаю дома, я стал хикканом, который почти не выходит из дома, и лишь изредка я
    выхожу в школу, чтоб меня оттуда не выперли"
    th "где же я свернул не туда?"
    mkr "эй, Богдан, все хорошо"
    scene bg int_dining_hall_people_day
    show mkr sad close at cright
    show ant sad close at cleft
    show unblink
    $ renpy.pause(1)
    stop music

    bgd "дада, я просто задумался"
    show mkr norm close at cright
    show ant norm close at cleft                            #норм кибернетики
    mkr "ну ладно, ато ты просто сидишь, глаза закрыл и не двигаешься"
    bgd "ну, со мной бывает такое"
    "Повисло молчание, {w}Богдан начал пялиться в свою чашку с чифиром, раздумывая из каких выделительных жидкостей осла
    сделан этот чудесный напиток"
    ant "эй, а где твой обед?"
    bgd "вот он"
    "Богдан показал Тохе чифир"
    ant "а что ты есть будешь?"
    bgd "этот чифир, {w}он содержит все необходимые соли для работы моего организма"
    "(шутка) когда все люди на 70 процентов состоят из воды, Богдан на 90 процентов состоит из чифира"
    bgd "они всасываются прямо в кровь, а потом расходуются по мере необходимости"
    ant "круто, а можно мне попробовать?"
    mkr "и мне"
    bgd "ну попробуйте"
    play music music_list["that_s_our_madhouse"]            #энергичная музыка

    "ничего не подозревая, Богдан протянул чашку кибернетикам"
    show mkr sad close at cright
    show ant sad close at cleft                             #грустные кибернетики
    $ renpy.pause(0.5)
    "отпив по глотку, кибернетики сильно изменились в лицах: Тоха скривился, как будто ему Алиса снова кишки вырвала,
    а Икар аж черно-белым стал"
    show mkr sad close at goLeft
    show ant sad close at goLeft                            #кибернетики убегают
    th "хех, петушки неопытные, {w}вот постоянно надо молодняк учить чифир пить"
    stop music
    "посамоутверждавшись за счет кибернетиков, Богдан стал скучающе рассматривать людей"

    "вдалеке он увидел Дору"
    show dor norm far at right                              #норм Дора далеко
    with Dissolve(0.5)
    "Дора тоже заметила Богдана"
    "Он рукою помахал, она помахала в ответ, {w}он пошел к ней навстречу, {w}это было так глу... {w}ой, не та пластинка"
    hide dor norm far with Dissolve(0.5)
    "в это время вернулись кибенетики"
    show mkr sad close at cright
    show ant sad close at cleft                             #грустные кибернетики
    with Dissolve(0.5)
    ant "ну и напитки у тебя!"
    mkr "да уж"
    bgd "эх вы, ниче не понимаете"
    ant "сам-то эту дрянь выпьешь?"
    play sound khdAmbList["drinking"]                       #звук питья

    "Богдан с каменным лицом, залпом выпил чифир, наслаждаясь каждой ноткой его вкуса и смакуя каждую его капельку"
    stop sound
    "чифир вылился через дырявый желудок прямо во внутреннюю среду, сразу же всосался в кровь, {w}которая, по правде
    сказать, состояла на 99 процентов из чифира и на 1 процент из нефти, {w}и сразу же разбежался по организму, 
    усваиваться в разные органы"
    bgd "ммммм, вкуснотища"
    show ant smile close at cleft                           #Антон улыбается
    ant "а, это, кстати, {w}как насчет вступления в клуб?"

    menu kiberClubJoin:                                     #вступление в клуб кибернетики
        "Вступить в клуб"
        "Даааа!! (я тру кхд)":
            $ evCibClubJoin = True                          #вступление в клуб кибернетики
            $ rootTitan += 1                                #увеличение переменной рута титана кхд
            play music khdMusicList["opening_gachi"]        #музыка опенинг гачи
            show mkr smile close at cright                  #Икар улыбается
            ant "кайф"
            mkr "поздравляю со вступлением! {w}надо будет отпраздновать!"
            bgd "а как?"
            mkr "нууу... {w}у нас в кладовке видик есть, можно посмотреть что-нибудь, может у тебя есть кассеты?"
            th "ну да, каждый день с собой ношу"
            bgd "нет, у меня их нет"
            mkr "ну ничего, зато у нас есть... {w}ты смотрел Курьера?"
            th "ну так то да, и не раз"
            bgd "нет, а что за фильм?"
            mkr "сам хз, недавно купил, еще не смотрел"
            ant "ну насколько я знаю, там просто про чела какого-то"
            "весьма исчерпывающее описание"
            mkr "ну, давай тогда сегодня после ужина"
            bgd "да, давайте"
            hide mkr smile close
            hide ant smile close                            #кибернетики прячутся
            with Dissolve(0.5)
        "Неееет (я тупой даун)":
            show ant sad close at cleft                     #Антон грустный
            play music music_list["i_dont_blame_you"]       #грустная музыка
            ant "блиииин, почему?"
            mkr "даа, почему?"
            bgd "ну, а чем я могу вам помочь? {w}пива принести?"
            mkr "ну было бы славно"
            ant "хотя да, пользы от тебя наверное было бы мало, {w}но тем не менее рабочие руки нам бы не помешали"
            bgd "вот именно что РАБочие"
            ant "ну ладно, не хочешь как хочешь, удачи, че"
            mkr "ну да, ты заходи к нам если что, не стесняйся"
            hide mkr sad close
            hide ant sad close                              #кибернетики прячутся
            with Dissolve(0.5)

    stop music
    "Богдан встал изо стола, отнес бокал изпод чифира и уже было направился к выходу, как вдруг ему навстречу показалась
    чем-то обозленная Мику"
    play music music_list["you_lost_me"]                    #музыка злая
    show mi angry pioneer far with Dissolve(0.5)            #Мику злая далеко
    mi "Богдан!!!!!"
    show mi angry pioneer                                   #Мику злая ближе
    mi "ты совсем охуел... чин чан чин чаи пиуааа пиуааа взвзвзвзвзвзв фофовыроарваорарфокаро я ж тебе говорила пиирвсивра
    втмир чин чин чин, и почему ты с нами не сел?"
    bgd "че?"
    show mi rage pioneer                                    #Мику пиздец злая 
    mi "ты меня вообще слушаешь?"
    th "охуеть, блять"
    bgd "а ты не можешь помедленнее?"
    mi "а ой"
    show mi smile pioneer                                   #Мику улыбается
    play music music_list["timid_girl"]                     #Добрая музыка
    mi "прости, забываю, что ты затупо... ой {w}что я слишком быстро говорю"
    th "нихуя чсв"
    bgd "я прощаю тебя"
    mi "ой как милаааа.... кхм кхм"
    show mi shy pioneer                                     #Мику смущенная
    mi "ой, слушай, я зачем пришла то.... {w}как ты смотришь на вступление в клуб?"

    menu musicClubJoin:
        "Вступить в музклуб"
        "Даааааа":
            $ evMusClubJoin = True                          #вступление в муз клуб
            $ rootDv += 1                                   #рут Алисы
            show mi happy pioneer                           #Мику счастлива
            mi "здорово, здорово, ура ура, Богдан вступил в клуб, ура ура"
            th "ну как ребенок, ей слово скажи и радости полные штаны"
            mi "давай тогда пиуааа пиуааа пипипипипи рынь рынь рынь пиапиапиаиаиапфломиывлаарвга сейчас ипрваипвриа 
            шфгывипаови фываорим порепетируем"
            mi "все понял?"
            bgd "ниче не понял"
            show mi upset pioneer                           #Мику расстроена
            mi "ну вот, опять меня Богдан не понимает"
            bgd "ну не плачь только, лучше по человечески скажи"
            show mi smile pioneer                           #Мику улыбается
            mi "так {w}сейчас {w}мы {w}пойдем {w}репетировать"
            mi "ты с нами?"

            if evCibClubJoin:                               #если вступил в киберклуб
                th "ну вроде кибернетики меня после ужина звали..."

            th "хотя Дора может меня заставить обходной подписывать, {w}ну и похуй на него"
            bgd "да, давай"
            show mi happy pioneer                           #Мику счастлива
            mi "урааааа ураааа, здорово здорово, Богдан идет с нами репетировать"
            bgd "погоди, а с кем \"с нами\"?"
            show mi serious pioneer                         #Мику серьезная
            mi "ну в клубе еще Тоха состоит {w}и Алиса {w}но только они перед обедом, скажем так, поссорились, поэтому не
            знаю придет ли Тоха"
            th "хех, это она про то, как он ее за жопу лапнул, а она ему кишки вырвала?)"
            bgd "а если не секрет, что там произошло?"
            show mi laugh pioneer                           #Мику смеется
            mi "ахахахахахаха, там такая смешная ситуация вышла... {w}он ее за жопу лапнул, а она ему кишки вырвала, {w}
            кровищи было.... ахахахахаха"
            bgd "согл, смешно пиздец"
            th "хотя, если верить сюжету, у нее ж мать из Жепена, кто знает, может всратые фетиши передаются по наследству"

        "Неееееет":
            show mi upset pioneer                           #Мику печальная
            mi "блин, печально, а нам как раз людей не хватает, Алиска с Тохой перессорились, а у меня спид"
            bgd "что у тебя?"
            mi "а да так, {w}в больницу ходила, сказали, что спид, сама хз что это"
            th "блин ок"
            bgd "ну ты это сильно не расстраивайся, будет и на твоей улице праздник"
            show mi dontlike pioneer                        #Мику донтлайк
            mi "не люблю праздники, дискотека хочу"
            bgd "ну будет дискотека"
            show mi smile pioneer                           #Мику улыбается
            mi "правда правда, честно честно?"
            bgd "да, обещаю"
            mi "урааа урааа, у меня будет дискотека"

    mi "ну мне в общем это, {w}пора, там аппаратуру выставлять, подготавливать всякие гитары там, комбики и прочую
    бесполезную хуйню"
    if evMusClubJoin:
        mi "ты тоже приходи, поможешь что ли"
    
    mi "ну все, я побежала"
    show mi smile pioneer at goRight                        #Мику уходит
    bgd "лан, пока"
    "Богдан также направился к выходу из столовой"
    return

#********************************************* ОБЕД С ДЕВОЧКАМИ *****************************************************

label khdGirlLunch:
    show us normal pioneer far at left
    show dv normal pioneer2 far
    show mi normal pioneer far at right                     #девочки далеко
    with Dissolve(0.5)
    play music music_list["take_me_beautifully"]            #спокойная музыка
    "за столом сидели две рыжие и Мику"
    show mi smile pioneer far at right                      #Мику улыбается
    mi "ой, Богдан, иди сюда, хехей хехей"
    "Мику начала размахивать руками, будто она в толпе"
    th "вот интересно, это она искренне так ко мне относится, {w}или может усыпляет мою бдительность, чтоб потом вырубить
    и продать на органы?"
    th "хотя, в любом случае, {w}состояние моих органов оставляет желать лучшего"
    show us surp2 pioneer at left
    show dv normal pioneer2
    show mi smile pioneer at right                          #Девочки ближе

    us "ой Богдан, а что это у тебя такое в чашке?"
    menu chifirDrink:                                       #что сказать Ульяне про напиток
        ""
        "чифир":
            $ evs1Day["dvFall"] = True                      #Алиса упала (когда побежит за Ульяной)
            bgd "ну, это чифир, {w}судя по всему, оч крепкий, видишь как нефть"
            show us upset pioneer at left                   #Ульяна расстроена
            us "эхххх... жаль, {w}я думала это что-то вкусненькое"
            show dv grin pioneer2                           #Алиса ухмыляется
            dv "Ульяна, Ульяна, тебе бы только за чужой счет полакомиться"
            th "ага, кто бы говорил"
            show us angry pioneer at left                   #Ульяна злая
            us "а вот и не правда, {w}я просто за Богдана беспокоюсь, чтоб он всякое говно не пил"
            th "ТЫ ЧЕ, СУКА, ОХУЕЛА ТАК НАПИТОК БОГОВ НАЗЫВАТЬ"
            "Богдан еле сдержался от того, чтобы сказать это вслух"
            th "а хотя.... {w}ну ладно, прощу девочку в первый раз, неопытная сельдь все таки еще"
            dv "ой, какие мы благородные..."

            play music music_list["pile"]                   #жоская музыка
            play sound sfx_face_slap                        #Пощечина
            "вдруг Ульяна неожиданно дала Алисе пощечину"
            show mi scared pioneer at right                 #Мику напуганная
            show dv rage pioneer2                           #Алиса злая
            dv "ТЫ ЧЕ СОВСЕМ ОХУЕЛА???"
            play sound sfx_body_bump                        #падение
            show us angry at goLeft                         #Ульяна убегает
            hide dv rage pioneer2 with Dissolve(0.3)        #Алиса падает                   
            "Алиса тоже попыталась дать Ульяне пощечину, но та вовремя отодвинулась и начала убегать, {w}в резульятате 
            чего Алиса гулко упала на пол"
            show dv rage pioneer2 
            show dv rage pioneer2 at goLeft                 #Алиса убегает
            "но она быстро аклималась и побежала за своей обидчицей"
            "Мику в это время испуганно смотрела на своих подруг"
            stop music fadeout 1.0
            show mi sad pioneer at right                    #Мику грустная
            mi "ты уж их прости, вечно они ссорятся"
            bgd "та ниче, привыкну"
            th "а Алиса, судя по звуку, сильно упала"
            show mi normal pioneer at right                 #Мику нормальная

            mi "слушай, Богдан, а расскажи анекдот"
            bgd "хмммм, ну давай расскажу"

            window hide
            $ set_mode_nvl()                                #nvl мод для анекдота
            nvl show Dissolve(0.3)

            "кхе кхе {w}ну в общем, слушай"
            "значит собрались как-то Хой, Цой и Летов на рыбалку"
            "взяли снасти, водку, рюмки и хлеб"
            "приехали на рыбалку, значит, и Хой предлагает: {w}\"А давайте, кто сколько себе рюмок водки в стихах скажет,
            тот столько и выпьет\""
            "ну, Цой и Летов согласились"
            "Хой решил начать: \"Рыбка плавает в пруду, выпью рюмочку одну\""
            "и опрокинул в себя стопку"
            "следующим был Цой: \"Рыбка плавает на дне, выпью рюмочки я две\""
            "и опрокинул в себя две стопки"
            "а Летов как натужился, {w}пыжится весь, {w}покраснел как помидор, {w}и вдруг заорал: \"ААААА БЛЯЯЯЯТЬ 
            НАХУУУУЙ!!!!!!!!\""
            "взял две бутылки и в лес убежал"

            nvl hide Dissolve(0.3)
            $ set_mode_adv()                                #adv мод, анекдот кончился
            window show

            show mi laugh pioneer at right                  #Мику смеется
            mi "ахахахахахаха {w}какой у тебя смешной анекдот.... ахахахахахах"
            th "хех, ну хоть кому-то он смешным кажется"
            mi "только я одного не поняла, {w}кто такой Хой?"
            th "оййййй"
            bgd "а, это.... {w}так, один музыкант есть, {w}неизвестный"

            show dv sad pioneer2 far at left                #грустная Алиса далеко
            "в это время в поле зрения Богдана оказалась Алиса, {w}уже без Ульяны и сильно огорченная"
            show dv sad pioneer2 at left                    #грусная Алиса
            show mi smile pioneer at right                  #Мику улыбается
            play music music_list["smooth_machine"]         #спокойная музыка
            mi "ооооо, Алиса, ты как?"
            dv "да вроде нормально"
            "тем не менее на ее локте красовался не плохой такой синяк"
            th "даа, не повезло ей"
            bgd "догнала Ульяну?"
            dv "ага, кшн, только пятки посверкали, и она из виду скрылась, {w}все-таки по части бега она - самый настоящий
            знаток хренов"
            "пройдя кучу модов, Богдан понимал, что это чистая правда"
            show dv normal pioneer2 at left                 #Алиса нормальная

        "горячий шоколад)":
            th "о, ща прикольнемся"
            play music khdMusicList["i_w_t_p_gachi"]        #веселая гачи музыка
            bgd "горячий шоколад"
            show dv surprise pioneer2
            show mi surprise pioneer at right               #Мику и Алиса удивлены
            th "кажется клюнули"
            show us grin pioneer at left                    #Ульяна ухмыляется

            us "слуууушай Богдан, {w}а там на входе Дора в купальнике"
            th "ничесе у тебя способы, {w}но ладно, подыграем"
            "Богдан, состроив удивленную гримасу, повернулся в сторону входа, {w}а Ульяна, как от нее и ожидалось в это
            время схватила стакан с чифиром и сделала мощный такой глоток"
            play sound khdAmbList["drinking"]               #Звук питья
            $ renpy.pause(1)
            show us fear pioneer at left                    #Ульяна в ахуе от чифира
            "на лице Ульяны сменились тысячи эмоций от страха и ужаса до выражения лица мертвеца"
            show mi surprise pioneer at right
            show dv surprise pioneer2                       #Алиса и Мику удивлены
            "Алиса и Мику же вообще не понимали, что происходит с их подругой из-за \"Горячего шоколада\""
            us "фуууу, что это за гадость.... *плевки*"
            "Ульяна начала выплевывать чифир на пол"
            show us fear pioneer at goLeft                  #Ульяна убегает

            show mi laugh pioneer at right
            show dv laugh pioneer2                          #Алиса и Мику смеются
            "поняв, что от вкуса чифира ей так просто не избавиться, Ульяна побежала мыть рот с мылом"
            th "справедливость торжествует!"
            "Алиса и Мику уже смекнули, что происходит и гоготали во весь голос над происходящим"
            stop music fadeout 1.0

            show dv grin pioneer2                           #Алиса ухмыляется
            dv "а это ты здорово придумал, я даже сначала и не поняла, молодец!"
            dv "только вот, что это за напиток такой волшебный?"
            "Богдана распирало от гордости"
            bgd "зеленый чифирь"
            play music music_list["smooth_machine"]         #спокойная музыка
            show mi surprise pioneer at right               #Мику удивлена
            mi "ой, Богдан, а чифир - это что такое?"
            bgd "напиток богов"
            show mi shy pioneer at right                    #Мику смущена
            mi "а из чего он делается?"
            bgd "ну, берется большая доза заварки чайной и заваривается в небольшом объеме воды где-то 2-3 дня"
            show mi happy pioneer at right                  #Мику счастлива
            mi "ой, здорово, здорово, я люблю чай, вот у нас в жепене... чин чин чин вот, так что я обязательно попробую"
            show mi smile pioneer at right                  #Мику улыбается
            th "дааа, наивности хоть отбавляй"
            dv "слууушай, Богдан, а ты сам то этот чифир выпьешь?"
            bgd "нет, блин, я его взял просто чтобы любоваться"
            show dv angry pioneer2                          #Алиса злая
            dv "мог бы спокойно сказать, нет, ему надо поострить"
            bgd "говоришь как моя мама"
            play sound khdAmbList["drinking"]               #звук питья

            "Богдан с каменным лицом, залпом выпил чифир, наслаждаясь каждой ноткой его вкуса и смакуя каждую его капельку"
            stop sound
            show dv surprise pioneer2                       #Алиса удивлена
            "чифир вылился через дырявый желудок прямо во внутреннюю среду, сразу же всосался в кровь, {w}которая, по правде
            сказать, состояла на 99 процентов из чифира и на 1 процент из нефти, {w}и сразу же разбежался по организму, 
            усваиваться в разные органы"
            bgd "ммммм, вкуснотища"
            "Богдан ехидно уставился на удивленную Алису"
            dv "ничесе, не ожидала такого"
            show dv normal pioneer2                         #Алиса нормальная
    
    "дальше наши пионеры какое-то время обедали молча: {w}Богдан медленно попивал чифир, а Мику и Алиса поедали
    пюрешку с котлетой"
    "вдруг Мику хлопнула по столу, и выпалила"
    play sound sfx_salt_impact                              #удар по столу
    show mi shy pioneer at right                            #Мику смущенная
    mi "блин, Богдан, я тут с этим твоим чифиром чуть о главном не забыла, {w}ты в музклуб вступишь?"
    th "кто о чем, а вшивый о бане"
    menu musClubJoin2:
        ""
        "Даааааа!":
            $ rootDv += 1                                   #рут Алисы +
            $ evMusClubJoin = True                          #вступление в клуб
            play music music_list["timid_girl"]             #музыка Мику
            show mi smile pioneer at right                  #Мику улыбается
            show dv smile pioneer2 at left                  #Алиса улыбается
            mi "урааа, уроааа, здорово, здорово, Богдан вступил в музклуб..."
            dv "поздравляю со вступлением"
            "радости полные штаны"
            mi "значит так, сейчас после обеда у нас будет репетиция, ты должан прийти, понял?"
            bgd "понял"
            mi "ну вот и здорово, жду не дождусь"

        "Нет.":
            show mi sad pioneer at right                    #Мику расстроена
            show dv sad pioneer2 at left                    #Алиса расстроена
            mi "ну вот, теперь музклуб точно закроют, Алиса с Тохой перессорились.."
            show dv rage pioneer2 at left                   #Алиса пиздец злая
            dv "видеть не хочу этого грязного уебка"
            show mi dontlike pioneer at right               #Мику с отвращением
            mi "Алиса, успокойся"
            show dv angry pioneer2 at left
            $ renpy.pause(1)                                #Алиса постепенно успокаивается
            show dv normal pioneer2 at left
            "краски на лице Алисы постепенно приняли естесственный цвет"
            th "дааа, обиделась, так обиделась"
            show mi normal pioneer at right                 #Мику нормальная
            mi "ну ты это, если что заходи не стесняйся"
    
    show mi normal pioneer at right
    show dv normal pioneer2 at left                         #девочки нормальные    
    th "блин, вот интересно, за какие такие заслуги судьба решила отправить меня в этот рай на Земле?"
    th "хотя почему на Земле? {w}Может быть это даже не наша вселенная"
    play sound sfx_door_squeak_light                        #скрип
    "доев обед и выпив компот, Мику встала из-за стола"
    mi "в общем, я пойду, мне там это, {w}пора, там аппаратуру выставлять, подготавливать всякие гитары там, комбики и 
    прочую бесполезную хуйню"
    dv "давай, до встречи"
    bgd "пока"

    hide mi normal pioneer with Dissolve(0.5)               #Мику уходит
    "два лазурных хвоста промелькали, а потом скрылись из виду за дверями столовой"
    "прошло еще минуты 2 и Алиса тоже доела свой обед и встала"
    dv "короче это, пока"
    if evMusClubJoin:
        dv "встретимся на репетиции"
        bgd "до встречи"
    else:
        bgd "пока"

    hide dv normal pioneer2 with Dissolve(0.5)              #Алиса уходит
    th "ну эта... мне ща тоже наверн идти надо, а то одному тут не кайф сидеть"
    "Богдан отнес чашку в мойку и отправился к выходу"

    return

#******************************* РЕПЕТИЦИЯ В МУЗКЛУБЕ 1 ДЕНЬ ******************************************

label musClubAfterLunch1DayKhd:
    th "что ж, пойду на репетицию"
    scene bg ext_houses_day with Dissolve(0.5)              #дорога с домиками
    "солнышко, как казалось Богдану, приятно светило, {w}на деле же оно палило с ебучей силой, достаточной для сравнения
    со взрывом в Хиросиме и Нагасаки"
    th "хммм, интересно, а Мику была в Хиросиме или Нагасаки?"
    "гениальные мысли преследовали его, но он был быстрее"
    scene bg ext_square_day with Dissolve(0.5)              #площадь
    th "здарова, Генда"
    "из-за отсутствия общения ирл у Богдана развилась привычка про себя разговаривать со всем, {w}таким образом он желал
    своему компу сладких снов, когда переводил его в спящий режим, говорил спасибо книге, когда читал ее, и тут решил
    поздороваться с Гендой, {w}хорошо, что про себя"
    "Лены в этот раз на площади не было"
    scene bg ext_musclub_day with Dissolve(0.5)             #дорога к музклубу
    "размышляя обо всем, Богдан не заметил, как подошел к музклубу"
    th "интересно, Тоха пришел?)"
    play sound sfx_open_door_1                              #открытие двери
    scene bg int_musclub_day                                #внутри музклуба
    show dv normal pioneer2 at right                        #Алиса нормальная 
    with Dissolve(0.5)
    play music music_list["so_good_to_be_careless"]         #музыка под муз клуб
    play ambience ambience_music_club_day                   #эмбиенс в музклубе

    "зайдя в музклуб, Богдан увидел Алису, возящуюся с гитарой, {w}судя по всему ее гитара не строила и она пыталась это
    исправить"
    dv "... ах ты Урал падла такая, не строишь, сука, падла, сука, падла, колки твои ебливые, падла, {w}сукападла"
    th "это она про меня?"
    bgd "эй, тебе помочь, может?"
    "Алиса явно не ожидала, что кто-то ее окликнет, поэтому она вздрогнула и чуть не выронила свой урал"
    show dv shocked pioneer2 at right                       #Алиса в шоке
    $ renpy.pause(1)
    show dv smile pioneer2 at right                         #Алиса улыбается
    dv "охуохуохуоавыфлор, {w}блин, ты че так пугаешь то, {w}я тут это, гитару настроить пытаюсь, хз че за ерунда, 
    не строит и все тут"
    bgd "ну ка, дай посмотреть"
    show dv grin pioneer2 at right                          #Алиса ухмыляется
    dv "ну да, эксперт нашелся, значит я не смогла, а ты сможешь?"
    bgd "ну да, ты ж женщина"
    "(просто шутка, девочки не обижайтесь, вы оч хорошие!!! (лично бы вас трахнул))"
    show dv angry pioneer2 at right                         #Алиса злая
    $ renpy.pause(1)
    show dv sad pioneer2 at right                           #Алиса грустная
    "по лицу Алисы было видно, что такой подкол ее задел, но все же она сдержалась и просто дала гитару Богдану"
    scene cg broken_guitar with Dissolve(0.5)               #Сломанная гитара

    bgd "тааак, посмотрим, {w}ну, в принципе дефолтное состояние для гитары урал... {w}ща, {w}ее надо просто взбодрить"
    scene bg int_musclub_day                                #в муз клубе
    show dv shocked pioneer2 at right                       #Алиса в шоке
    with Dissolve(0.5)
    play sound khdAmbList["crash"]                          #звук падения
    play music khdMusicList["scarygym"]                     #веселая музыка)
    "после этих слов Богдан разъебашил гитару об пол, сломал пол и гитару и выкинул гитару в окно нахуй, на глазах 
    у шокированной и испуганной Алисы"
    show dv rage pioneer2 at right                          #Алиса злая
    "как только Алиса поняла что происходит, краски на ее лице стали сгущаться, при том не от смущеная, а от злости, 
    искренней злости"
    dv "ты че наделал, мудак, это была моя единственная гитара, на которую я на заводе кокса полгода работала"
    show dv rage pioneer2 close at right                    #Алиса злая близко
    "Алиса бегом начала приближаться к Богдану, {w}явно не из хороших побуждений"
    "Богдан побежал от Алисы в обратном направлении, чтобы не отхватить пиздюлей, {w}но в конце концов он обо что-то 
    запнулся и они оба свалились на пол друг на друга"
    hide dv rage pioneer2 close with Dissolve(0.2)          #Алисы нет
    show bg int_musclub_day with vpunch                     #встряска
    play sound sfx_body_bump                                #звук падения
    $ renpy.pause(0.4)
    show blink
    $ renpy.pause(1)
    show black
    "Богдан ощутил два притных объекта на своей спине"
    th "вот это я здорово гитару починил"
    "но счастье Богдана продолжалось недолго: Алиса очухалась и начала бить Богдана со спины"
    "к счастью, до тех пор, пока Алиса не забила Богдана насмерть в клуб кто-то вошел"
    play sound sfx_open_door_1                              #звук открытия двери
    mi "КОНИЧИВА... {w}ой, а что тут происходит?"
    "по голосу Богдан узнал Мику"
    dv "да, Мику, конь ничего, вот только этот мудак только что раздолбал и выкинул мой любимый уральчик в окно"
    mi "ч-{w}ч-{w}что? {w}А я тут под окном нашла этот фендер мустанг 1969 года, и на нем подпись: Алиса Двачевская"
    "Алиса замерла на секунду и слезла с Богдана"

    show cg dv_and_mustang                                  #Алиса и мустанг
    show unblink
    stop music fadeout 1.0                                  #музыка стоп
    "открыв глаза, Богдан увидел картину маслом: Алиса гладит свою гитару и радуется как ребенок тому, что теперь у нее
    есть новенький мустанг, какого нет даже у самого Чимина из \"Кино\""
    dv "мустангчик, мой мустангчик..."
    "чуть очухавшись от восторга и порыва спермотоксикоза к мустангу, Алиса поспешила проявить себя с хорошей стороны"
    scene bg int_musclub_day                                #в музклубе
    show dv shy pioneer2 at right                           #Алиса смущена
    show mi surprise pioneer at left                        #Мику удивлена
    with Dissolve(0.5)

    dv "Богдан, ты это, {w}прости что я тебя это, {w}ну ножом хуйнула короче, нехорошо вышло... {w}А вот за мустанг
    спасибо тебе большое!"
    show dv shy pioneer2 close at right                     #Алиса близко
    "после этих слов Алиса подошла и крепко обняла Богдана, {w}по-дружески"
    th "а она меня рил что ли ножом порезала?"
    "Богдан почувствовал, что из его правой бочины, а именно из печени, сочится что-то теплое"
    th "до свадьбы заживет"

    play music music_list["went_fishing_caught_a_girl"]     #дружеская музыка
    show mi smile pioneer at left                           #Мику улыбается
    show dv smile pioneer at right                          #Алиса улыбается
    "Алиса отстранилась, и в клубе повисла дружеская атмосфера"
    mi "ой, а кстати, Богдан еще нам не показал, как он на гитарах играть умеет, ну или не на гитарах, не знаю, на чем он 
    еще играть умеет, Богдан, ты ведь покажешь?"
    th "покажу, заткнись только"
    bgd "ну да, ато че я как лох"
    stop music fadeout 1.0
    "Богдан взял первую попавшуюся гитару и начал представление"
    play music khdMusicList["jesus_tod"]                    #джизус тод бурзум
    "он решил сыграть песню jesus tod у группы burzum"
    show dv shocked pioneer2 at right                       #Алиса в ахуе
    show mi shocked pioneer at left                         #Мику в ахуе
    "по лицам Мику и Алисы было видно, что они знатно прихуели от игры Богдана"
    th "интересно, они вообще знают что это за жанр?"
    "тыкните, чтобы продолжить"
    stop music fadeout 1.0

    "Богдан закончил играть и вопросительно посмотрел на девочек"
    play music music_list["went_fishing_caught_a_girl"]     #снова дружеская музыка
    bgd "ну, как вам?"
    dv "а{w}ху{w}еть {w}ты где так играть научился?"
    bgd "та я это, {w}в вангеров играл, там такое же управление просто"
    show dv grin pioneer2 at right                          #Алиса ухмыляется
    dv "а, ну ладно, а то я подумала, что ты из этих, из сатанистов"
    "Алиса была почти права"
    "Мику до сих пор находилась в состоянии культурного шока от увиденного, {w}наконец она очухалась и тут понеслось..."
    show mi smile pioneer at left                           #Мику улыбается
    mi "ой, Богдан, ничего себе, как ты умеешь, а говорил, что плохо играешь... фыволарывлормиукшщк дфшокраицугркимволр
    ыловарпилцгкур, вот это да, до сих пор поверить не могу, а меня... фывдлаорываор ыувкорикапикыв, но мне такое... 
    фыловаро ывиаор, в общем давайте играть что-нибудь поспокойнее"
    bgd "че она сказала?"
    dv "другое че то сыграть хочет"
    bgd "ну давайте другое, хули, {w}я как раз знаю одну песню, мне ее друг показал..."
    "Богдан начал показывать песню Новый Гад у группы Капилляры, ЭТО ГРУППА АВТОРА МОДА"
    
    "Алиса, Мику и Богдан долго репетировали, аж вечер настал, и в итоге смогли сыграть эту песню, {w}Мику на басу, Алиса 
    на барабанах, а Богдан на гитаре и еще петь решил"
    
    $ persistent.sprite_time = "sunset"                     #оформление спрайтов сансет
    $ sunset_time()

    play music khdMusicList["new_year"]                     #новый гад
    "дослушайте, пж"
    show bg int_musclub_sunset with Dissolve(5)             #в музклубе
    stop music fadeout 1.0
    mi "здорово сыграли"
    show mi scared pioneer at left                          #Мику напуганна
    mi "ой, блин, совсем забыла, я ж сегодня в столовке дежурная, я должна там чашки ложки подготовить, в общем вы можете
    без меня тут прибраться? Короче я побежала"
    show dv angry pioneer2 at right                         #Алиса злая
    show mi scared pioneer at goLeft                        #Мику убегает
    dv "эй, ты че..."
    "Алиса пыталась остановить Мику, но ее попытки оказались тщетны"
    show dv sad pioneer2                                    #Алиса грустная
    play music music_list["silhouette_in_sunset"]           #спокойная вечерняя музыка
    dv "вот, блин, убежала, все как есть оставила, тут эти кабеля долбанные, {w}ну а ты то что стоишь, давай прибираться
    теперь будем"
    "сама Алиса тоже пошла прибирать кабеля, {w} Богдан решил прибрать гитары"
    hide dv sad pioneer2 at goRight                         #Алиса уходит
    "убирая третью гитару на стойку в углу, Богдан улышал, что в кладовке, куда Алиса убирала кабеля, послышалось падение"
    play sound sfx_body_bump                                #звук падения
    dv "ауууч"
    "оказывается, упала Алиса"
    bgd "все хорошо?"
    if not evs1Day["dvFall"]:
        dv "да, со мной все нормально, со стула упала прост"
        "в это время Алиса уже вышла из кладовки"
        show dv normal pioneer2 with Dissolve(0.5)          #Алиса нормальная
        "нигде действительно не было видно ни ссадин, ни синяков"
        dv "ну че на ужин пойдем?"
        bgd "ну, да, пойдем"
    else:
        dv "блин, на локоть упала, как в столовке, теперь сильнее болит"
        show dv sad pioneer2 with Dissolve(0.5)             #Алиса грустная
        "выйдя, у Алисы был грустный вид, судя по всему локоть ныл"
        bgd "сильно больно?"
        dv "да, ноет"
        menu regretAlice:
            ""
            "пожалеть Алису":
                $ rootDv += 1                               #рут Алисы +
                "Богдан решил подойти к Алисе и пожалеть ее"
                show dv sad pioneer2 close                  #Алиса грустная близко
                bgd "у кошечки боли, у собачки боли, а у Алисы ен боли"
                show dv shy pioneer2 close                  #Алиса смущена
                dv "спасибо, уже лучше, {w}ты не думал медиком стать?)"
                bgd "я уже медик, ну как, в пту учусь"
                "на самом деле Богдан учился на архитектора"
                dv "ладно, медик, нам на ужин пора"
                bgd "ну, пошли на ужин"
            "промолчать":
                "Богдан решил промолчать, так как жаление Алисы могло принести неизвестные последствия"
                "..."
                dv "на ужин идем?"
                bgd "пойдем"

    play sound sfx_open_door_1                              #открытие двери
    show bg ext_musclub_sunset with Dissolve(0.5)           #снаружи музклуба
    show dv normal pioneer2                                 #Алиса нормальная
    with Dissolve(0.5)
    play ambience ambience_camp_center_evening loop         #эмбиенс в лагере
    play music music_list["lightness"]                      #музыка под вечер
    "Богдан шел вместе с Алисой и наслаждался свежим воздухом"
    show bg ext_clubs_sunset with Dissolve(0.5)             #клубы
    th "интересно, а кибернетики на ужине"
    "проходя мимо клубов Богдан заметил, что Алиса как-то косо посмотрела туда, {w}наверное из-за Тохи"
    show bg ext_square_sunset with Dissolve(0.5)            #площадь
    "всю дорогу наши пионеры шли молча"
    bgd "здарова, Генда"
    dv "что?"
    th "бля, я вслух сказал"
    bgd "та, я это, {w}с памятником поздоровался"
    if rootDv > 1:
        show dv laugh pioneer2                                  #Алиса смеется
        dv "хах, ну ты рил смешной"
        th "ладно хоть сумашедшим не посчитала"
    else:
        dv "ммм... ок"
        th "бля, кажись я чмоня"
    
    show dv normal pioneer2                                     #Алиса нормальная
    show bg ext_dining_hall_away_sunset with Dissolve(0.5)      #путь к столовке
    $ renpy.pause(1)
    show bg ext_dining_hall_near_sunset with Dissolve(0.5)      #столовая ближе
    bgd "ты че кста на ужин будешь?"
    dv "да хз, че дадут, {w}самое главное - чтоб пизды не дали"
    th "у меня так вся жизнь..."

    return

#******************************* ИДЕМ НА ПЛЯЖ 1 ДЕНЬ (ЕСЛИ НЕ ЗАПИСАЛИСЬ В МУЗ) ***********************

label beachAfterLunch1DayKhd:
    th "ну делать мне, пожалуй, нечего, {w}после зимы у себя дома, я бы не отказался от водных процедур на воздухе"
    th "на пляж, короче, хочу"
    scene bg ext_houses_day with Dissolve(0.5)              #дорога с домиками
    "солнышко, как казалось Богдану, приятно светило, {w}на деле же оно палило с ебучей силой, достаточной для сравнения
    со взрывом в Хиросиме и Нагасаки"
    th "хммм, интересно, а Мику была в Хиросиме или Нагасаки?"
    "гениальные мысли преследовали его, но он был быстрее"
    play ambience ambience_lake_shore_day loop              #звук на пляже
    scene bg ext_beach_day with Dissolve(0.5)               #пляж
    "вскроре наш прилежный пионер, ударник сосистического труда, Богдан, пришел на уже изученный им в различных модах 
    пляж"
    th "дааа, не жизнь, а сказка, {w}хотя лол, это и есть сказка"
    "наш пионер уже решил было поплавать, как вдруг вспомнил, что у него нет плавок"
    th "блин, плавок то нет, {w}ну ладно, поплаваю в трусах, быстро высохнут, лето в конце концов"
    play sound sfx_blanket_off_stand                        #звук всплоха ткани (типо одежда)
    "Богдан одним взмахом снял с себя одежду и остался лишь в одних крутых трусах"
    scene cg panties with Dissolve(0.5)                     #крутые трусы
    "(ставь лайк этому моду, если тоже хочешь себе такие)"
    show bg ext_beach_day at khdRun                         #снова пляж
        
    "после чего он сильно разбежался и плюхнулся в воду"
    play sound sfx_water_emerge                             #плюх в воду
    scene cg under_water with Dissolve(0.5)                 #под водой (обложка невермайнд)
    "Богдан ходил в бассейн и умел очень хорошо плавать"
    play sound sfx_swimming loop                            #звук плавания
    "Богдан плыл от берега и обратно к берегу, вода казалась ему очень приятной и теплой, как парное молоко"
    th "в последний раз вот так вот в речке я плавал... {w}хммм... {w}пожалуй лет в 8, с отцом на рыбалке"
    "проплавав минут 30, Богдан выдохся, астма давала о себе знать, {w}он поплыл к берегу и вышел на сушу"
    stop sound
    scene bg ext_beach_day with Dissolve(0.5)               #пляж 
    "после такого активного плавания Богдан устал и решил вздремнуть"
    "найдя хорошую тень от дерева, Богдан надел свою пионерскую форму и лег под дерево"
    show blinking                                           #моргание

    "его глаза закрывались, {w}он не сопротивлялся сладостным объятиям Морфея"
    show blink                                              #закрывание глаз
    $ renpy.pause(1)
    show black
    stop music
    "Богдану снился очень странный сон, отвечающий на все вопросы, связанные с совенком, и его пребыванием здесь"
    window hide
    show prologue_dream
    $ renpy.movie_cutscene(khdVidList["dr_barec"])          #сон со стасом барецким
    hide prologue_dream
    window show

    $ sunset_time()
    $ persistent.sprite_time = "sunset"                     #смена оформления на сансет

    hide black
    scene bg ext_beach_sunset
    show unblink                                            #вечерний пляж
    th "ахайо... {w}ой, конбавва, {w}так, сколько я спал?"
    play music music_list["your_bright_side"]               #музыка под знакомство с Женей
    "задиванонив себя, как анимешника, Богдан заметил вдали чей-то силуэт"
    th "как жаль, что я не взял очки"
    show mz normal glasses pioneer at right                 #Женя
    "тем временем силуэт приближался, и Богдан узнал в этом силуэте {w}Женю"
    th "она че, выходит из своей сычевальни?"

    show mz bukal glasses pioneer at right                  #Женя с презрением
    mz "эй ты, {w}че тут разлегся, ужин скоро"
    bgd "а ты почему не там?"
    mz "не твое дело"
    bgd "а че так грубо, меня Богдан, кстати зовут"
    mz "очень приятна, Евгения"
    "произнося слова, Женя нарочно проговаривала их очень четко, артикулируя каждую букву, давая понять уровень иронии, 
    с которой она говорит, {w}после чего она с отвращением посмотрела на протянутую ей руку Богданом и неестественно 
    пожала ее"
    th "вот так вот значит, {w}может удасться с ней сдружится, показав, что я \"свой\"?"
    bgd "слууушай, {w}Женя, ты ведь в библиотеке заведуешь?"
    mz "ну да, {w}не знаю, откуда ты это узнал, но я думаю тебе на это плевать"
    th "ну ниче, ща ты увидишь весь мой читательский стаж за 4 года, которые я был тру хиккой"
    bgd "что ж, возможно, {w}как тебе кстати Ужасы Малышка?"

    show mz normal glasses pioneer at right                 #Женя
    mz "вижу, ты немного отличаешься от остальной массы, {w}но это - база"
    th "база значит..."
    "Богдан шел с Женей по направлению к столовой, обсуждая все менее и менее популярные, но тем не менее псевдошедевры
    отечественной литературы, которые могли быть популярны у местных винишек типа Жени"

    play ambience ambience_forest_evening loop              #эмбиенс в лесу
    show bg ext_path_sunset with Dissolve(0.5)              #дорога в лесу
    show mz smile glasses pioneer at right                  #Женя улыбается
    bgd "...слушай, ну не знаю как тебе, но лично мне показалось, что автор Звездных Драчунов и Жуковска, после своего 
    первого произведения вырос, как автор, но также вторая глава Жуковска мне показалась намного лучше первой"
    mz "ну, отчасти так, конечно, но не показались ли тебе Звездные Драчуны несколько самобытными, именно потому, что это 
    было \"пробное\" произведение, не обремененное жанровыми рамками и прочими коммерческими приблудами?"
    bgd "ну, как по мне в Звездных Драчунах автор спалился, что он еще неопытный малек..."

    play ambience ambience_camp_center_evening loop         #эмбиенс в лагере
    show bg ext_houses_sunset with Dissolve(0.5)            #дорога с домиками
    "так, обсуждая книжки они постепенно подходили к столовой"
    show bg ext_dining_hall_away_sunset with Dissolve(0.5)  #столовая
    show mz shy glasses pioneer at right                    #Женя смущенная
    mz "что ж ты раньше молчал, шалун, что ты так просвящен?"
    show bg ext_dining_hall_near_sunset with Dissolve(0.5)  #столовая рядом
    th "действительно"
    mz "как ты смотришь на вступление в библиотеку?"
    
    menu libraryJoin:                                       #вступление в библиотеку
        ""
        "Вступлююю!!!":
            $ rootMz += 1                                   #Рут Жени +
            $ evLibClubJoin = True                          #вступление в библиотеку
            $ evs2Day["cleaning"] = "mz"                    #проведение суботника во 2 день вместе с Женей в библиотеке
            bgd "ну го"
            show mz smile glasses pioneer at right          #Женя улыбается
            mz "кайфарики, Богдан вступил в библиотеку"
            mz "слушай, ты ведь знаешь, что завтра день уборки?"
            bgd "какой еще уборки?"
            mz "нууу, все пионеры будут разделены на стайки, убирающие территорию в разных местах, так вот {w}
            может, поможешь мне тогда в библиотеке?"
            th "хмм... {w}пожалуй, переставлять книжки, вытирать пыль и двигать шкафы будет куда лучше чем подметать
            площадь с какой-нибудь Славей"
            bgd "ну да, почему бы нет"
            show mz shy glasses pioneer at right            #Женя смущается
            mz "здорово, я как раз не могу в соляну там шкафы с кучей книг двигать"
            bgd "ну, теперь сможешь"
            show mz normal glasses pioneer at right         #Женя нормальная
            mz "что-то мы с тобой разговорились, сейчас обед закончится, пошли есть быстрее"
        "неееееет" if evCibClubJoin:
            show mz angry glasses pioneer at right          #Женя злая
            $ renpy.pause(0.5)
            show mz bukal glasses pioneer at right          #Женя презрение
            mz "что ж, очень жаль"
            "Женя пыталась сказать это максимально безучастно, как будто ей все равно, но все же на ее лице проскальзнула
            нотка злости, а в голосе слышалась фальш"
            show mz normal glasses pioneer far at right     #Женя дальше
            "пройдя уже несколько метров к столовой она все же развернулась"
            mz "ну ты заходи, если что, не стесняйся, у меня кстати новые книжки скоро будут"
            bgd "хорошо, зайду"
            hide mz normal glasses pioneer far with Dissolve(0.5)#Женя зашла в столовую
            "после этого Женя окончательно скрылась из виду в дверях столовой"

            th "видно зря я не вступил, расстроилась ведь"
            "постояв еще немного Богдан все же решил зайти в столовку за очередной порцией чифира"
    
    return
        
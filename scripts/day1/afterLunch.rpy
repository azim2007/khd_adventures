#******************************* РЕПЕТИЦИЯ В МУЗКЛУБЕ 1 ДЕНЬ ******************************************

label musClubAfterLunch1Day:
    "репа"

#******************************* ИДЕМ НА ПЛЯЖ 1 ДЕНЬ (ЕСЛИ НЕ ЗАПИСАЛИСЬ В МУЗ) ***********************

label beachAfterLunch1Day:
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

    show ext_beach_sunset
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
        
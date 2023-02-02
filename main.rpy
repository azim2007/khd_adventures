init:
    $ mods ["dayAtHome"] = u"КХДЪшное лето"
    #переменные для сохранений
    $ rootTitan = 0
    $ rootDv = 0
    $ rootMz = 0
    $ evCibClubJoin = False
    $ evMusClubJoin = False
    $ evLibClubJoin = False
    $ evs1Day = {                   #события, происходящие в 1 день в совенке
        "dvFall": False
    }

    $ evs2Day = {
        "cleaning" : "none",
    }

    #имена папок
    $ khdRoot     = "khd_adventures/"
    $ khdBg       = khdRoot + "bg/"
    $ khdScreens  = khdRoot + "screens/"
    $ khdSprites  = khdRoot + "sprites/"

    #дополнительные герои
    $ bgd = Character("Богдан", color="#89ce00", what_color="#FFDD7D")
    $ mkr = Character("Икар", color="#FFF226", what_color="#FFDD7D")
    $ ant = Character("Тоха", color="#ffff00", what_color="#FFDD7D")
    $ dor = Character("Дора", color="#f95252", what_color="#FFDD7D")
    $ ogu = Character("Огузок", color="#1619c2", what_color="#FFDD7D")

    #словарь цветов, в зависимости от времени
    $ timeColorDict = {
        "day" :         im.matrix.tint(1, 1, 1),
        "sunset" :      im.matrix.tint(0.94, 0.82, 1.0),
        "night" :       im.matrix.tint(0.63, 0.78, 0.82),
    }

    #картинки для перехода между днями
    image screen trol           = (khdScreens + "bogdan_trolley.jpg")
    image screen tvar           = (khdScreens + "bogdan_tvar.jpg")
    image screen huev           = (khdScreens + "huevyy.jpg")

    #дополнительные бэкграунды
    image bg toilet_room        = (khdBg + "toilet.jpg")
    image bg kitchen_room       = (khdBg + "kitchen.jpg")
    image bg khd_podezd         = (khdBg + "podezd.jpg")
    image bg winter_outside     = (khdBg + "winter_outside.jpg")
    image bg tram_station       = (khdBg + "tram_station.jpg")
    image bg int_musclub_sunset = (khdBg + "int_musclub_sunset.jpg")
    image bg int_musclub_night_nolight = (khdBg + "int_musclub_night_nolight.jpg")
    image bg int_musclub_night_light = (khdBg + "int_musclub_night_light.jpg")
    image bg ext_musclub_sunset = (khdBg + "ext_musclub_sunset.jpg")
    image bg ext_musclub_night  = (khdBg + "ext_musclub_night.jpg")

    #дополнительные cg
    image cg chifir             = (khdBg + "chifir.jpg")
    image cg playing_vangers    = (khdBg + "playing_vangers.png")
    image cg school65           = (khdBg + "bogdan_in_65.jpg")
    image cg sharaga            = (khdBg + "sharaga.jpg")
    image cg makar_cup          = (khdBg + "makar_memories.jpg")
    image cg ext_tram           = (khdBg + "tram_outside.jpg")
    image cg int_tram           = (khdBg + "tram_inside.jpg")
    image cg svar_apparat       = (khdBg + "svar_apparat.jpg")
    image cg makar_dota         = (khdBg + "makar_dota.jpg")
    image cg dv_us_from_roof    = (khdBg + "dv_us_from_roof.png")
    image cg malyshok_mares     = (khdBg + "malyshok_mares.jpg")
    image cg in_mirror          = (khdBg + "inmirror.jpg")
    image cg oguzok_kitch       = (khdBg + "oguzok.jpg")
    image cg panties            = (khdBg + "panties.jpg")
    image cg under_water        = (khdBg + "under_water.jpg")
    image cg broken_guitar      = (khdBg + "broken_guitar.jpg")
    image cg dv_and_mustang     = (khdBg + "alice_and_mustang.jpg")
    image cg vhs_voron          = (khdBg + "vhs_voroniny.jpg")
    image cg stars_sky          = (khdBg + "stars_sky.jpg")
    image cg change_lamp        = (khdBg + "change_lamp.jpg")

    #экран для перехода между днями
    screen nextDay(dayName, screenName):
        tag nextDayScreen
        modal True
        add screenName
        text dayName size 250 outlines[ (5, "#000000", 0, 0) ]:
            align(0.5, 0.5)

    #спрайт "уходит" с экрана вправо
    transform goRight:
        linear 0.3 xpos 1.3

    #спрайт "уходит" с экрана влево
    transform goLeft:
        linear 0.3 xpos -0.3

    #эффект бега
    transform khdRun:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)            
        ease 0.20 pos (-25,25)
        repeat

init python:
    #названия папок
    khdRoot     = "khd_adventures/"
    khdBg       = khdRoot + "bg/"
    khdMusic    = khdRoot + "music/"
    khdAmbience = khdRoot + "ambience/"
    khdSprites  = khdRoot + "sprites/"
    khdVideos   = khdRoot + "video/"

    #дополнительная музыка
    khdMusicList = {
        "pofig"         : khdMusic + "carbo8_polubomu.mp3",
        "vangers"       : khdMusic + "fostral_theme.mp3",
        "slipknot_sic"  : khdMusic + "slipknot_sic.mp3",
        "i_w_t_p_gachi" : khdMusic + "i_want_to_play_gachi.mp3",
        "semyaiz"       : khdMusic + "semyaizverzh.mp3",
        "chunga"        : khdMusic + "ass_chunga.mp3",
        "cool_mus"      : khdMusic + "ass_cool_mus.mp3",
        "opening_gachi" : khdMusic + "ass_opening_theme.mp3",
        "scarygym"      : khdMusic + "ass_scary_gym.mp3",
        "jesus_tod"     : khdMusic + "jesus_tod.mp3",
        "new_year"      : khdMusic + "new_year.mp3",
    }

    #дополнительные эмбиенсы
    khdAmbList = {
        "unitaz"        : khdAmbience + "unitaz_sound.mp3",
        "sranie"        : khdAmbience + "srat.mp3",
        "friing"        : khdAmbience + "friing.mp3",
        "egg_eating"    : khdAmbience + "egg_eating.mp3",
        "drinking"      : khdAmbience + "drinking.mp3",
        "crash"         : khdAmbience + "crash_sound.mp3",
        "closing_door"  : khdAmbience + "closing_door.mp3",
        "podezd_door"   : khdAmbience + "domofon_sound.mp3",
        "boots_on_snow" : khdAmbience + "boots_on_snow.mp3",
        "tram_sound"    : khdAmbience + "tram_sound.mp3",
        "metal_noise"   : khdAmbience + "metal_noise.mp3",
    }

    #видео
    khdVidList = {
        "dota"          : khdVideos + "dota.avi", 
        "dr_barec"      : khdVideos + "dream_bareckiy.avi",
        "voroniny"      : khdVideos + "voroniny.avi",
    }

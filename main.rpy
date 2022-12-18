init:
    $ mods ["dayAtHome"] = u"КХДЪшное лето"

    $ khdRoot     = "khd_adventures/"
    $ khdBg       = khdRoot + "bg/"
    $ khdScreens  = khdRoot + "screens/"
    $ khdSprites  = khdRoot + "sprites/"

    #дополнительные герои
    $ bgd = Character("Богдан", color="#89ce00", what_color="#FFDD7D")
    $ mkr = Character("Икар", color="#FFF226", what_color="#FFDD7D")

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
    }

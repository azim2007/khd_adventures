init:
    $ mods ["dayAtHome"] = u"приключения кхдъ'шника"

    $ khdRoot     = "khd_adventures/"
    $ khdBg       = khdRoot + "bg/"
    $ khdScreens  = khdRoot + "screens/"

    #картинки для перехода между днями
    image screen trol = (khdScreens + "bogdan_trolley.jpg")
    image screen tvar = (khdScreens + "bogdan_tvar.jpg")
    image screen huev = (khdScreens + "huevyy.jpg")

    #дополнительные бэкграунды
    image bg toilet_room = (khdBg + "toilet.jpg")
    image bg kitchen_room = (khdBg + "kitchen.jpg")

    #экран для перехода между днями
    screen nextDay(dayName, screenName):
        tag nextDayScreen
        modal True
        add screenName
        text dayName size 250 outlines[ (5, "#000000", 0, 0) ]:
            align(0.5, 0.5)

init python:
    #названия папок
    khdRoot     = "khd_adventures/"
    khdBg       = khdRoot + "bg/"
    khdMusic    = khdRoot + "music/"
    khdAmbience    = khdRoot + "ambience/"
    khdSprites  = khdRoot + "sprites/"

    #дополнительная музыка
    khdMusicList = {
        "pofig" : khdMusic + "carbo8_polubomu.mp3"
    }

    #дополнительные эмбиенсы
    khdAmbList = {
        "unitaz" : khdAmbience + "unitaz_sound.mp3",
        "sranie" : khdAmbience + "srat.mp3",
        "friing" : khdAmbience + "friing.mp3",
    }

init:
    $ mods ["dayAtHome"] = u"приключения кхдъ'шника"

    $ khdRoot     = "khd_adventures/"
    $ khdBg       = khdRoot + "bg/"

    #дополнительные бэкграунды
    image toilet_room = (khdBg + "toilet.jpg")

init python:
    #названия папок
    khdRoot     = "khd_adventures/"
    khdBg       = khdRoot + "bg/"
    khdMusic    = khdRoot + "music/"
    khdSprites  = khdRoot + "sprites/"

    #дополнительная музыка
    khdMusicList = {
        "pofig" : khdMusic + "carbo8_polubomu.mp3"
    }
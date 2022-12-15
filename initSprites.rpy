init 2:
    #спрайты дополнительных персонажей
    #Макар
    image mkr norm far          = im.MatrixColor(
        khdSprites + "makar/norm_far.png", timeColorDict["day"])
    image mkr norm              = im.MatrixColor(
        khdSprites + "makar/norm_normal.png", timeColorDict["day"])
    image mkr norm close        = im.MatrixColor(
        khdSprites + "makar/norm_close.png", timeColorDict["day"])

    image mkr norm far sunset   = im.MatrixColor(
        khdSprites + "makar/norm_far.png", timeColorDict["sunset"])
    image mkr norm sunset       = im.MatrixColor(
        khdSprites + "makar/norm_normal.png", timeColorDict["sunset"])
    image mkr norm close sunset = im.MatrixColor(
        khdSprites + "makar/norm_close.png", timeColorDict["sunset"])

    image mkr norm far night    = im.MatrixColor(
        khdSprites + "makar/norm_far.png", timeColorDict["night"])
    image mkr norm night        = im.MatrixColor(
        khdSprites + "makar/norm_normal.png", timeColorDict["night"])
    image mkr norm close night  = im.MatrixColor(
        khdSprites + "makar/norm_close.png", timeColorDict["night"])
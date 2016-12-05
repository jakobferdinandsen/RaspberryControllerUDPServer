class JoystickDataPacketTranslator():
    #This is the left Joypad X axis(Primarily used for turning) -128 to 128
    l3x = None

    #This is the left Joypad Y axis(Probably not needed) -128 to 128
    l3y = None

    #This is the right Joypad X axis(Probably not needed) -128 to 128
    r3x = None

    #This is the right Joypad Y axis(Probably not needed) -128 to 128
    r3y = None

    #This is the the left trigger(Primarily used for brakes) 0-256
    l2 = None

    #This is the the right trigger(Primarily used as a gas pedal) 0-256
    r2 = None

    #This is R1, used for camera right
    r1 = None

    #This is L1, used for camera left
    l1 = None

    #This is Triangle, used to reset camera position
    triangle = None

    def createDataString(self, l3x, l3y, r3x, r3y, l2, r2, l1, r1, triangle):
        dataString = "l3x:%s" % l3x
        dataString += " l3y:%s" % l3y
        dataString += " r3x:%s" % r3x
        dataString += " r3y:%s" % r3y
        dataString += " l2:%s" % l2
        dataString += " r2:%s" % r2
        dataString += " l1:%s" % l1
        dataString += " r1:%s" % r1
        dataString += " triangle:%s" % triangle

        return dataString

    def interpretDataString(self, dataString):
        for dat in dataString.split():
            if dat.startswith("l3x"):
                self.l3x = float(dat.split(":")[1])
            if dat.startswith("l3y"):
                self.l3y = float(dat.split(":")[1])
            if dat.startswith("r3x"):
                self.r3x = float(dat.split(":")[1])
            if dat.startswith("r3y"):
                self.r3y = float(dat.split(":")[1])
            if dat.startswith("l2"):
                self.l2 = float(dat.split(":")[1])
            if dat.startswith("r2"):
                self.r2 = float(dat.split(":")[1])
            if dat.startswith("l1"):
                self.l1 = float(dat.split(":")[1])
            if dat.startswith("r1"):
                self.r1 = float(dat.split(":")[1])
            if dat.startswith("triangle"):
                self.triangle = float(dat.split(":")[1])

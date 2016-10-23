class JoystickDataPacketTranslator():

    l3x = None
    l3y = None
    r3x = None
    r3y = None
    l2 = None
    r2 = None



    def createDataString(self, l3x, l3y, r3x, r3y, l2, r2):
        dataString = "l3x:%s" % l3x
        dataString += " l3y:%s" % l3y
        dataString += " r3x:%s" % r3x
        dataString += " r3y:%s" % r3y
        dataString += " l2:%s" % l2
        dataString += " r2:%s" % r2

        return dataString

    def interpretDataString(self, dataString):
        for dat in dataString.split():
            print dat
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

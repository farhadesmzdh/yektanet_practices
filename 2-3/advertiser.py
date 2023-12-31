import base_model


class Advertiser(base_model.BaseModel):
    __advertisers = set()

    @staticmethod
    def help():
        return ("ID:    unique identification for each advertiser"
                "\nname:    name of the advertiser")

    @staticmethod
    def getTotalClicks():
        total_clicks = 0
        for advertiser in Advertiser.__advertisers:
            total_clicks += advertiser.getClicks()
        return total_clicks

    def __init__(self, id, name):
        super().__init__()
        self.__id = id
        self.__name = name
        Advertiser.__advertisers.add(self)

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def describeMe(self):
        return ("ID:    " + str(self.__id) +
                "\nAdvertiser:  " + self.__name +
                "\nClicks:  " + str(self.getClicks()) +
                "\nViews:   " + str(self.getViews()))

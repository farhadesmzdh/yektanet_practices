import advertiser
import base_model


class Ad(base_model.BaseModel):
    @staticmethod
    def help():
        return ("ID:    unique identification for each advertiser"
                "\ntitle:   title of the advertiser"
                "\ncimgUrl:   url of ad's image"
                "\nvlink:   redirection url"
                "\nadvertiser:   advertiser of ad")

    def __init__(self, id, title, img_url, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__img_url = img_url
        self.__link = link
        self.advertiser = advertiser

    def getTitle(self):
        return self.__title

    def getImgUrl(self):
        return self.__img_url

    def getLink(self):
        return self.__link

    def setTitle(self, title: str):
        self.__title = title

    def setImgUrl(self, img_url: str):
        self.__img_url = img_url

    def setLink(self, link: str):
        self.__link = link

    def setAdvertiser(self, adv: advertiser.Advertiser):
        self.advertiser = adv

    def describeMe(self):
        return ("ID:    " + str(self.getId()) +
                "\nTitle:  " + self.__title +
                "\nImgUrl:  " + self.getImgUrl() +
                "\nLink:  " + self.__link +
                "\nClicks:  " + str(self.getClicks()) +
                "\nViews:   " + str(self.getViews()))

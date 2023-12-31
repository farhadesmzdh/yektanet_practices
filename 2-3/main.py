from ad import Ad
from advertiser import Advertiser


advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")

ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img-url12", "link2", advertiser2)

print(ad2.describeMe() + "\n")
print(advertiser1.describeMe() + "\n")

ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad2.incViews()

ad1.incClicks()
ad1.incClicks()
ad2.incClicks()

print(advertiser2.getName() + "\n")
advertiser2.setName("new name")
print(advertiser2.getName() + "\n")

print(str(ad1.getClicks()) + "\n")
print(str(advertiser2.getClicks()) + "\n")

print(str(Advertiser.getTotalClicks()) + "\n")
print(Advertiser.help() + "\n")



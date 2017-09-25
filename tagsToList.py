mTags = raw_input()
#mTags = "#flowers #flower #TagsForLikes #petal #petals #nature #beautiful #love #pretty #plants #blossom #sopretty #spring #summer #flowerstagram #flowersofinstagram #flowerstyles_gf #flowerslovers #flowerporn #botanical #floral #florals #insta_pick_blossom #flowermagic #instablooms #bloom #blooms #botanical #floweroftheday"
x = mTags.split("#")
finalList = []
for i in x:
	finalList.append(i.strip())
print finalList
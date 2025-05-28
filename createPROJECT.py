
#Init

#Function
fruits = ["Apple","Apricot","Avocado","Banana","Bilberry","Blackberry","Blackcurrant","Blueberry","Boysenberry","Currant","Cherry","Cherimoya","Chico","Cloudberry","Coconut","Cranberry","Cucumber","Damson","Date","Dragonfruit","Durian","Elderberry","Feijoa","Fig","Goji","Gooseberry","Grape","Raisin","Grapefruit","Guava","Honeyberry","Huckleberry","Jabuticaba","Jackfruit","Jambul","Jujube","Juniper","Kiwano","Kiwifruit","Kumquat","Lemon","Lime","Loquat","Longan","Lychee","Mango","Mangosteen","Marionberry","Melon","Cantaloupe","Honeydew","Watermelon","Mulberry","Nectarine","Olive","Orange","Clementine","Mandarine","Tangerine","Papaya","Passionfruit","Peach","Pear","Persimmon","Physalis","Plantain","Plum","Prune","Pineapple","Plumcot","Pomegranate","Pomelo","mangosteen","Raspberry","Salmonberry","Rambutan","Redcurrant","Salal","Salak","Satsuma","Soursop","Quitoense","Strawberry","Tamarillo","Tamarind","Ugli","Yuzu"]
grams = [182,35,200,118,0.5,5,0.6,0.5,7,0.3,8,250,150,0.5,1500,0.4,300,40,24,600,900,1,100,50,0.2,5,5,0.6,230,250,0.5,0.5,10,1000,10,20,0.4,200,100,35,100,67,40,10,20,200,200,5,800,800,800,5000,4,150,3,130,150,100] filteredList = []

def weightFilter(size):
    if size == "tiny":
        for i in range(len(grams)):
            if grams[i] < 10:
                filteredList.append(fruits[i])
        print(filteredList)

    if size == "small":
        for i in range(len(grams)):
            if grams[i] > 10 and grams[i] < 100:
                filteredList.append(fruits[i])
        print(filteredList)

    if size == "medium":
        for i in range(len(grams)):
            if grams[i] > 100 and grams[i] < 750:
                filteredList.append(fruits[i])
        print(filteredList)

    if size == "large":
        for i in range(len(grams)):
            if grams[i] > 750 and grams[i] < 2000:
                filteredList.append(fruits[i])
        print(filteredList)

    if size == "enormous":
        for i in range(len(grams)):
            if grams[i] > 2000:
                filteredList.append(fruits[i])
        print(filteredList)


#List of 15 Unique fruits. Image source: EverInTransit 2025. Accessed via https://everintransit.com/exotic-fruits/ CC BY-NC 2.0.
#List of 40 Exotic Fruits. Image source: LiveEatLearn 2024. Accessed via https://www.liveeatlearn.com/exotic-fruits/ CC BY-NC 2.0.
#List of 40 Exotic Fruits. Image source: GoodGoodGood 2025. Accessed via https://www.goodgoodgood.co/articles/list-of-fruits CC BY-NC 2.0.
#List of 43 Fruits with weights. Image source: HowLongToCook 2021. Accessed via https://howlongtocook.org/tips/largest-fruits-vegetables CC BY-NC 2.0.

#Main
weightFilter(input(("Pick a size: Tiny, Small, Medium, Large, Enormous")).lower())

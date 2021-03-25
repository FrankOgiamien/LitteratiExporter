import csv

#     Shoptowel brand is KimberlyClark    paper/latex composition
#     Clean up strap -> strapping
print "Customizing Litterati tags for csv export."

PlasticCount = 0

outfile = open("C:\\Projects\\Litterati\\LitteratiOut.csv", "w")
outfile.write("LitterID, Date, Year, Latitude, Longitude, Object, Material, Brand \n")

with open("C:\\Projects\\Litterati\\Litterati-Partners_03252021.csv") as csvfile:
    litter = csv.reader(csvfile)
    litter.next()
    for row in litter:
        LitterID = row[0]
        ChallengeID = row[1]
        DateID = row[6]
        YearID = row[6][-4:]
        Tag = row[2]

        # clean up some inconsistent tags
        Tag = Tag.replace("baggie", "ziplock")
        Tag = Tag.replace("baloon", "balloon")
        Tag = Tag.replace("bandaid", "bandage")
        Tag = Tag.replace("beer", "can")
        Tag = Tag.replace("beercan", "can")
        Tag = Tag.replace("beercap", "beerbottlecap")
        Tag = Tag.replace("beercase", "beercarton")
        Tag = Tag.replace("blizzard", "blizzardcup")
        Tag = Tag.replace("bottlecapseal", "bottleseal")
        Tag = Tag.replace("candybar", "candywrapper")
        Tag = Tag.replace("candypackage", "candybag")
        Tag = Tag.replace("candypackaging", "candybag")
        Tag = Tag.replace("cigarettebutts", "cigarettebutt")
        Tag = Tag.replace("cigarette lighter", "lighter")
        Tag = Tag.replace("cigarettelighter", "lighter")
        Tag = Tag.replace("cigarette,", "cigarettebutt,")
        Tag = Tag.replace("coffeelid", "coffeecuplid")
        Tag = Tag.replace("condoms", "condom")
        Tag = Tag.replace("coolant", "coolantcontainer")
        Tag = Tag.replace("drinkcup", "softdrink")
        Tag = Tag.replace("drugspoon", "cooker")
        Tag = Tag.replace("drugwrapper", "drugpacket")
        Tag = Tag.replace("icecreamwrapper", "candywrapper")
        Tag = Tag.replace("ketchuppacket", "condiment")
        Tag = Tag.replace("mask", "facemask")
        Tag = Tag.replace("medecine", "prescriptionbottle")
        Tag = Tag.replace("medication", "prescriptionbottle")
        Tag = Tag.replace("medicationbottle", "medicinebottle")
        Tag = Tag.replace("motoroil", "motoroilcontainer")
        Tag = Tag.replace("plasticdrinkseal", "bottleseal")
        Tag = Tag.replace("pillbottlelitter", "prescriptionbottle")
        Tag = Tag.replace("pillbottle", "prescriptionbottle")
        Tag = Tag.replace("prescriptiondrugs", "prescriptionbottle")
        Tag = Tag.replace("pillsstrip", "pillstrip")
        Tag = Tag.replace("plasticcandybag", "candybag")
        Tag = Tag.replace("scratchers", "scratcher")
        Tag = Tag.replace("syringewrapper", "syringepackaging")
        Tag = Tag.replace("saline", "sterilewater")
        Tag = Tag.replace("shoprag", "shoptowel")       
        Tag = Tag.replace("sanicup", "stericup")
        Tag = Tag.replace("cooker, metal", "cooker, tin")
        Tag = Tag.replace("candywrapper, ohenry", "candywrapper, plastic, ohhenry")
        Tag = Tag.replace("coffeecup, timhortons", "coffeecup, paper, timhortons")

        # check if tag only identified as plastic
        if len(Tag) == 7 and Tag[0:7] == "plastic":
            Tag = "piece, plastic"

        # check if Object tag is missing for records starting with plastic or cardboard
        if Tag[0:8] == "plastic," or Tag[0:9] == "cardboard" or Tag[0:9] == "styrofoam":
            Tag = "piece, " + Tag

        # count plastic items
        if ", plastic" in Tag or ",plastic" in Tag or ", styrofoam" in Tag or ", celluloseacetate" in Tag or ", polystyrene" in Tag:
            PlasticCount += 1
##        else:
##            print Tag + "      not counted as Plastic"
        
        # fix cookers missing brand - stericup
        if Tag == "cooker, tin":
            Tag = "cooker, tin, stericup"
        
        # split the Tags and Coords string into two lists
        Tags = Tag.split(",")
        Coords = row[3].split("/")
        
        Vintage = row[5]

        # uncomment the if statement if you want to filter on a particular type of object
##        if Tags[0] == "syringe":
##        print LitterID + ",   " + Coords[0] + ",   " + Coords[1] + ",   " + Tags[0]
##        print Tag + "     " + "Counted as Plastic"
        outfile.write(LitterID + ", " + DateID + ", " + YearID + ", " + Coords[0] + ", " + Coords[1] + ", " + Tag + "\n")
    outfile.close()

print "Count of Plastic items: " + str(PlasticCount)



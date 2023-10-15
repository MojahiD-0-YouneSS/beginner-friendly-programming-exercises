wiki_Mb = int(input("Enter how many Mbps you consumed on wikipedia : "))
meme_Mb = int(input("Enter how many Mbps you consumed on meme : "))
def opare_meme_wiki(meme_Mb, wiki_Mb):
    if wiki_Mb < meme_Mb:
        return " '\"WOW MANY MEMES\" , \"SUCH LOL\""
    else:
        pass

def Mbps_consumtion(wiki_Mb, meme_Mb):
    total_wiki_consumption = wiki_Mb * 0.10
    total_meme_consumption = meme_Mb * 0.05
    total_overall_consumtion = total_wiki_consumption + total_meme_consumption
    if total_overall_consumtion >= 100:
        print("Too much consumption")
    else:
        pass
    return round(total_overall_consumtion, 2)

print(Mbps_consumtion(wiki_Mb, meme_Mb))
print(opare_meme_wiki(meme_Mb, wiki_Mb))















""""Reads X(wikipedia Mb consupmtion) and Y(watching meme Mb consumption)
* Calculates the total consumption
* If total consumption greater than 100$ print proper message
* If watching meme consumption  is greater than reading wikipedia articles print proper messages"""
import requests
from bs4 import BeautifulSoup

#def getTeamAbv(name):
#    match name:
#        case "Ducks":
#            return "ANA"
#        case "Coyotes":
#            return "ARI"
#        case "Bruins":
#            return "BOS"
#        case "Sabres":
#            return "BUF"
#        case "Flames":
#            return "CGY"
#        case "Hurricanes":
#            return "CAR"
#        case "Blackhawks":
#            return "CHI"
#        case "Avalanche":
#            return "COL"
#        case "Blue Jackets":
#            return "CBJ"
#        case "Stars":
#            return "DAL"
#        case "Red Wings":
#            return "DET"
#        case "Oilers":
#            return "EDM"
#        case "Panthers":
#            return "FLA"
#        case "Kings":
#            return "LAK"
#        case "Wild":
#            return "MIN"
#        case "Canadiens":
#            return "MTL"
#        case "Predators":
#            return "NSH"
#        case "Devils":
#           return "NJD"
#        case "Islanders":
#            return "NYI"
#        case "Rangers":
#            return "NYR"
#        case "Senators":
#            return "OTT"
#        case "Flyers":
#            return "PHI"
#        case "Penguins":
#            return "PIT"
#        case "Sharks":
#            return "SJS"
#        case "Blues":
#            return "STL"
#        case "Kraken":
#            return "SEA"
#        case "Lightning":
#            return "TBL"
#        case "Maple Leafs":
#            return "TOR"
#        case "Canucks":
#            return "VAN"
#        case "Golden Knights":
#            return "VGK"
#        case "Capitals":
#            return "WSH"
#        case "Jets":
#            return "WPG"
#        case _:
#            print("Team not recognized, exiting...")
#            exit()

teamarr = ["ANA", "ARI", "BOS", "BUF", "CGY", "CAR", "CHI", "COL", "CBJ", "DAL", "DET", "EDM", "FLA", "LAK", "MIN", "MTL", "NSH", "NJD", "NYI", "NYR", "OTT", "PHI", "PIT", "SJS", "STL", "SEA", "TBL", "TOR", "VAN", "VGK", "WSH", "WPG"]
teamabv = input("Please input the abbreviation of the team you would like to find an NHL trade deadline acquisition for: (For example, Capitals = WSH, Sabres = BUF, etc.)\n") 

if(not(teamabv in teamarr)):
    print("Error: Invalid team abbreviation")
    exit()

URL = "https://www.hockey-reference.com/teams/" + teamabv + "/"
page = requests.get(URL)

bsoup = BeautifulSoup(page.text, 'html.parser')

print(bsoup.prettify())

for player in bsoup.find_all('td'):
    if(not(player.get('csk')) == ("None")):
        print(player.get('csk'))
    

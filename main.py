import requests
import json
url = "https://overlordmaruyama.fandom.com/"

# Print match or list of matches if specified
def processResponse():
    response = doSearchQuery()
    matches = parseUrl(json.loads(response.text)["query"]["search"])
    try:
        print("The first match was", matches[0]["url"])
        if (str(input("Do you want a list of all matches? [y/n] ")) == "y"):
            print("A full list of all matches:")
            for match in matches: print(match["url"])
            input("Press ENTER to continue...")
        else: pass
    except:
        print("No result found.")
        input("Press ENTER to continue...")

# API request
def doSearchQuery():
    text = str(input("Search: "))
    params = {
            "action" : "query",
            "list": "search",
            "srsearch" : text,
            "utf8": True,
            "format": "json"
            }
    response = requests.get(url + "api.php", params)
    return response

# Add page-"url" attribute to every match
def parseUrl(matches):
    matchesContainingUrls = []
    for match in matches:
        match["url"] = url + match["title"].replace(" ", "_")
        matchesContainingUrls.append(match)
    return matchesContainingUrls


processResponse()
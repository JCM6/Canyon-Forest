from dataclasses import dataclass
from Models.MoxfieldModels import *

import requests
import json

import pprint
import logging
import sys

# This file will contain the classes and methods used to interract with a moxfield deck collection that is more robus than their usual tools and services.

# POST Authorize the Agent
# Example Call:
# fetch("https://api2.moxfield.com/v2/account/token", {
#   "headers": {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
#     "authorization": "Bearer undefined",
#     "content-type": "application/json",
#     "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site"
#   },
#   "referrer": "https://www.moxfield.com/",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": "{\"userName\":\"Fredstack\",\"password\":\"persepolisRISE2022!\",\"token\":\"03AEkXODD_REsWy-7hC7wHwmD7-h3BnIzIFcIV8m7tRFH1FZ9_yKtD522TRgiEHxa2GiERutbFGNbvpGYMsy0c2jaXOi73YZKwD5TCvgqUI3Q6EFoWxDzQRK3xJ5MOorS5wNz0JzwwNXJfGgtxSJM1sKAJviytQPCYdnayv03RWGrjLOIORXbIzBwYut43P_OWs3pAMJS5qg6P75B8M0iU3EF4yGNXqtLZhCAYNWsRYgLiw_yrJsAQZNjDeG3gGuJyHObW_q2TA5wvTc5sVWaaheu-HRe-_zJ1-ZOF0_u8wamFC0-s5TBvBPmlmt5fiUHUENGejqNMt3e1QZAdmGOXtlbyIJ3Kouc6zgXGIUWE76siVLshg_UfVxAURczmEUw2a5Pi49tqoeC_Oy0vlzQeEaN8YhrSXPo_TLZg_sSO4nWVKlTuZuzJf12Tc0bCO3uyoOCz8TLvuHRKu88SSbb8ypMOAPmhh8p9zF43PwVDT-nkYAthV-h3VjEZqfYZKzD6lIyUX5WaMuPm4yyj_HCZwoqBxEqADfmDntwHk-iMMQvCCwTpS8UsCMxnJ_8dmzx-YZclyNvgkpxuPy0wHy8fm-Uy195Yoe45VeB2hyUhYM-L0bRxvgVYhxZKNuRV0hEQx6Eqghe1DcpfX18S_2qIQXGGVuWg-xaZy_7SqPZr9tojW5FJNGhNPC15YJl6FyPLokvuG_fdEVkpwVusATzQoMO_58Z7ZTQKuOxcxvNiYBu3oYdwkSzGGNOwTRYbh6qsxsrpG2wn-cycSA2YCcjrH7ragHO1W5_nOmJWlR5O8M_6FQm4-H79mSB5JEPIxmmr1tu16C9ooR1Gj20K0PqIedQvcRbs7xlql0CdwbhI-qlrS3gw6wsls80mKoVk61nyxbOc2Zh7aYAgihAWE4O3Yyoyr0GODWbPIuxfiwVnXF9kItBV_XrAozzs7GFAKaN9ny7369sqjxvEePoKwBed5-dTs0ICcnj8BL4ZL4HzdhaDQ6P657gUHKG8D4DDoTVicqRtXtqtk3hy301jx4lhbnRSkzBci578zU81Af_UIgUp081M3Zyaq3ZDmOV1pAi5vntJllTlNlB_BhEC6xn2cAbuDtgpoSGxm1gRsJ2eDIBDLt6HK8lbLMo8ZxOVGopgKhhP54e4F_7xVTo-lBtvspF16wPG0OW5ar704cGGuv9u7TJ1s7dsfYFe874TISGHwG6ZEsSx9DyAroWUAYobwaIi1LkVg3rcrd_XFlDGRzQ7ypiG3liFOUM\"}",
#   "method": "POST",
#   "mode": "cors",
#   "credentials": "include"
# });
# Example Failure Response: 400
# {"":["Invalid username or password."]}
# Example Success Response: 200
# {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJGcmVkc3RhY2siLCJqdGkiOiJkMTM1NGQzOC0zNjI0LTRjZDctOTk1MC04OTgzYzJiMTUwNDciLCJodHRwOi8vd3d3Lm1veGZpZWxkLmNvbS93cy8yMDE2LzA4L2lkZW50aXR5L2NsYWltcy9Vc2VySWQiOiIxMDMwNyIsImh0dHA6Ly93d3cubW94ZmllbGQuY29tL3dzLzIwMTYvMDgvaWRlbnRpdHkvY2xhaW1zL0VtYWlsQ29uZmlybWVkIjoiVHJ1ZSIsImV4cCI6MTY2Nzg1OTQ4MSwiaXNzIjoiaHR0cHM6Ly9tb3hmaWVsZC1hcGkuYXp1cmV3ZWJzaXRlcy5uZXQvIiwiYXVkIjoidXNyIn0.RU71EKaV-6MclRpxBiVk4gXeShaGUEQqwEk6rBYKQec","refresh_token":"cb8f89b8-ecfe-4681-97df-0511798fc36c","token_type":"Bearer","user_name":"Fredstack","email_address":"jcmoody6@protonmail.com","is_email_confirmed":true,"unread_notification_count":0,"expiration":"2022-11-07T22:18:01Z","expires_in_minutes":15,"permissions":[],"preferences":{"deckSortColumn":"name","deckSortDirection":"ascending","affiliate":"cardkingdom","hasConfirmedChoices":"true","lastUsedFormat":"highlanderCanadian","isFirstMoxleComplete":"true","selectedSleeveKey":"Black","isCollectionTrackerEnabled":"true"},"view_settings":{"groupBy":"type","sortBy":"name","useMana":false,"usePrice":false,"useSet":false,"columns":"three","isHighlightBarEnabled":false,"isDarkModeEnabled":true,"playStyle":"paperDollars","viewMode":"table","personalDeckListMode":"list","viewAsAuthorIntends":true,"splitPrimerWidth":25,"primerTheme":"default","foilMode":"animated","showLegalOnly":true,"ignoreAuthorOverrides":false,"allowMultiplePrintings":false},"feed_access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRVAyYWwifQ.4bKk8I_LF0YvoBbTjVCZPg4uK9N6hQzdCGlgjRVbnIg","user_id":"EP2al"}


def AuthorizeAgent():
    auth = Authorization
    return auth

# GET Decks

# GET Folders

# POST Create Folder

# POST Move Deck to New Folder By Id

# POST Move Decks to New Folder By Id

if __name__ =="__main__":
    
    logName = f"{__file__}.txt"
    
    # Clear old test log

    logging.basicConfig(filename=logName, level=logging.DEBUG)
    
    print(AuthorizeAgent())
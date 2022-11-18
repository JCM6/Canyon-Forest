from dataclasses import dataclass, field

import pprint
import logging
import sys

# Represents a user's authorization
@dataclass(frozen=True)
class Authorization:

    userId: str
    accessToken: str
    refreshToken: str
    tokenType: str
    userName: str
    emailAddress: str
    expiration: str
    expiresInMins: str
    viewSettings: dict
    feedAccessToken: str




# Represents a deck
@dataclass
class UserDeck:
    id:str
    name: str
    format: str
    visibility: str
    publicUrl: str
    publicId: str
    folder: dict
    pass

#Represents a collection of decks
@dataclass
class UserDecks:
    pass

# Represents user folders
@dataclass
class UserFolders:
    id: str
    name: str
    pass


if __name__ =="__main__":

    logName = f"{__file__}.txt"
    
    # Clear old test log

    logging.basicConfig(filename=logName, level=logging.DEBUG)
    
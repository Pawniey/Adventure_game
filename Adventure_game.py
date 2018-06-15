
#The map consists of 5 locations and option to exit the game
#Every location has description and exits
#Location's exits differ(Your exits are limited depending on the location)
#           Location          Description           Direction : To where
game_map = {"Road": ["You are in the middle of the road", {'W': "Hill",
                                                           'N': "Forest",
                                                           'E': "Building",
                                                           'S': "Valley",
                                                           'X': "Exit game"}],

            "Hill": ["The top of the hill , you can see everything", {'N': "Forest",
                                                                      'E': "Road",
                                                                      'X': "Exit game"}],

            "Building": ["You are inside the building , hiding", {'W': "Road",
                                                                  'X': "Exit game"}],

            "Valley": ["The valley is mysterious place", {'W': "Hill",
                                                          'N': "Road",
                                                          'X': "Exit game"}],

            "Forest": ["You can hear strange voices", {'W': "Hill",
                                                       'S': "Road",
                                                       'X': "Exit game"}]}

end_game = False
#Initializes location
current_location = "Road"
print("Welcome to game of forest")
while end_game is False:
    #Informs user about his current location and the exits available
    print("""
    Place description: {}
    Available Exits: {}""".format(game_map.get(current_location)[0], game_map.get(current_location)[1]))

    change_location = input("Which way you want to go? ").upper()

    if change_location == "X":#Exits game if user entered "E"
        print("Thank you for playing , come again later!")
        break
    while game_map.get(current_location)[1].get(change_location) is None:#Make sure location is available
        print("You cant go that way")
        change_location = input("Which way you want to go? ").upper()
    current_location = game_map.get(current_location)[1].get(change_location)



    #For debugging
    # for location in game_map.keys():
    #     print("""
    #     Location: {}
    #     Description: {}
    #     Available Exits: {} """.format(location, game_map.get(location)[0], game_map.get(location)[1]))

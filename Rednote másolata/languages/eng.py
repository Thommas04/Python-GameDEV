
# English language pack

def set_language():
    main_menu = {'Play' : 'Play',
                 'Settings' : 'Settings',
                 'Quit' : 'Quit',
                 'Save' : 'Save',

                 'LoadInfo' : '- Load your created game!',
                 'NewGameInfo' : '- Make a new game!',
                 'QuitInfo':'- Exit to desktop',
                 'SaveInfo' : 'Save your game',
                 'GAMETITLE': 'PLAY',
                 'QUITTITLE' : 'QUIT',
                 'Back': 'Back [Esc]',
                 'NewGame': 'New game',
                 'LoadGame': 'Load game',
                 'QuitGame': 'Quit game',
                 'SaveGame': 'Save game',
                 'LOADTITLE': 'LOAD GAME',
                 'NEWGAMETITLE' : 'NEW GAME',
                 'NAME' : 'Your name : ',
                 'ON' : 'On',
                 'OFF' : 'Off',
                 'STARTGAME' : 'Start Game',
                 'ALLOWCHEATS': 'Allow cheats :',
                 'TUTORIAL': 'Tutorial :',
                 'SAVENAME' : 'Save name : ',

                 'Player': 'Player :',
                 'Season': 'Season :',
                 'Wealth': 'Wealth :',
                 'Created': 'Created :',
                 'Playtime': 'Play time :',
                 'Cheats': 'Cheats :',
                 'Mission': 'Mission :',

                 'Spring': 'Spring',
                 'Summer': 'Summer',
                 'Fall': 'Fall',
                 'Winter': 'Winter',

                 'Enabled': 'Enabled',
                 'Disabled': 'Disabled',

                 }

    pause_menu = {'Resume': 'Resume',
                  'Map': 'Map',
                  'Story': 'Story',
                  'Help': 'Help',
                  'Settings': 'Settings',
                  'Quit': 'Quit Game'
                  }

    death_screen = {'Continue' : 'Continue'}

    wave_system = {'Wave' : 'Wave',
                   'Enemy' : 'Enemy',
                   }

    markers = {'STORE': 'Store',
               'SHOP': 'Shop',
               'BUY': 'Buy',
               'SELL': 'Sell',
            }



    list_of_pack = [main_menu, pause_menu, death_screen, wave_system, markers]
    return list_of_pack

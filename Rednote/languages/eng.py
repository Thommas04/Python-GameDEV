
# English language pack

def set_language():
    main_menu = {'Play' : 'Play',
                 'Settings' : 'Settings',
                 'Quit' : 'Quit',

                 'LoadInfo' : '- Load your created game!',
                 'NewGameInfo' : '- Make a new game!',
                 'QuitInfo':'- Exit to desktop',
                 'GAMETITLE': 'PLAY',
                 'QUITTITLE' : 'QUIT',
                 'Back': 'Back [Esc]',
                 'NewGame': 'New game',
                 'LoadGame': 'Load game',
                 'QuitGame': 'Quit game',
                 'LOADTITLE': 'LOAD GAME',

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

    list_of_pack = [main_menu, pause_menu, death_screen]
    return list_of_pack

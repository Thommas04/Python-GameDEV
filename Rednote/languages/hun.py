
# Hungarian language pack

def set_language():
    main_menu = {'Play' : 'Játék',
                 'Settings' : 'Beállítások',
                 'Quit' : 'Kilépés',

                 'LoadInfo' : '- Töltsd be a már létrehozott játékodat!',
                 'NewGameInfo' : '- Hozz létre egy új játékot!',
                 'QuitInfo':'- Kilépés az asztalra',
                 'GAMETITLE': 'JÁTÉK',
                 'QUITTITLE' : 'KILÉPÉS',
                 'Back': 'Vissza [Esc]',
                 'NewGame': 'Új játék',
                 'LoadGame': 'Betöltés',
                 'QuitGame': 'Kilépés',
                 'LOADTITLE': 'JÁTÉK BETÖLTÉSE',

                 'Player': 'Játékos :',
                 'Season': 'Évszak :',
                 'Wealth': 'Vagyon :',
                 'Created': 'Létrehozás :',
                 'Playtime': 'Játékidő :',
                 'Cheats': 'Csalások :',
                 'Mission': 'Feladat :',

                 'Spring': 'Tavasz',
                 'Summer': 'Nyár',
                 'Fall': 'Ősz',
                 'Winter': 'Tél',

                 'Enabled': 'Engedélyezve',
                 'Disabled': 'Letiltva',

                 }

    pause_menu = {'Resume' : 'Vissza',
                  'Map' : 'Térkép',
                  'Story' : 'Történet',
                  'Help' : 'Segítség',
                  'Settings' : 'Beállítások',
                  'Quit' : 'Kilépés'
                 }

    death_screen = {'Continue': 'Folytatás'}

    list_of_pack = [main_menu, pause_menu, death_screen]
    return list_of_pack

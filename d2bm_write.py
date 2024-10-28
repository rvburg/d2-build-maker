# main function
def main():
    welcome()
    directory()


# main welcome func 
def welcome():
    print('Welcome to the Destiny 2 Build Maker')
    print('v.0.01')
    print('Built by rvburg')
    print()
    print('-------------------------------------------')


# main directory func
def directory():
    print('D2 Build Maker Main Menu')
    print()
    print('Please Select from the Following Options:')
    print()
    print(
        'Type g to Select: Guided Build Creation', 
        'Type e to Select: Edit A Saved Build', 
        'Type x to Select: Export Build to .csv File', 
        sep='\n')
    print()
    choice = directory_choice()
    if choice == 'g':
        build_create()
    else:
        build_create()


# main directory menu selection func
def directory_choice():
    while True:
        main_menu_pc_selection = input('Your Selection: ').strip().lower()
        if main_menu_pc_selection == 'g': 
            print('Selection Confirmed: Guided Build Creation')
            return ('g')
        else:
            print()
            print('Selection Unconfirmed: Please retype your selection.')


# user build creation func
def build_create():
    print('-------------------------------------------')
    print()
    pc_build_name = input('Build Name: ')
    print()
    pc_class_type = get_pc_class_type()
    pc_subclass_type, pc_subclass_damage_type = get_pc_subclass_type(pc_class_type)
    pc_ablty_super, pc_subclass_damage_type = get_pc_ablty_super(pc_class_type, pc_subclass_type, pc_subclass_damage_type)
    pc_ablty_classablty = get_pc_ablty_classablty(pc_class_type, pc_subclass_type)
    pc_ablty_moveablty = get_pc_ablty_moveablty(pc_class_type, pc_subclass_type)
    pc_ablty_meleeablty = get_pc_ablty_meleeablty(pc_class_type, pc_subclass_type)
    pc_ablty_grenadeablty = get_pc_ablty_grenadeablty(pc_class_type, pc_subclass_type)
    print('-------------------------------------------')
    print()
    print('Build Name:', pc_build_name)
    print()
    print('Class:', pc_class_type)
    print('Subclass:', pc_subclass_type)
    print('Super:', pc_ablty_super)
    print('Dmg Type:', pc_subclass_damage_type)
    print('Class:', pc_ablty_classablty)
    print('Movement:', pc_ablty_moveablty)
    print('Melee:', pc_ablty_meleeablty) 
    print('Grenade:', pc_ablty_grenadeablty)
    print()
    # print('Aspect 1:', pc_aspect_0)
    # print('Aspect 2:', pc_aspect_1)
    print()
    print('-------------------------------------------')


# user picks between titan, hunter, or warlock
def get_pc_class_type():
    print('-------------------------------------------')
    print()
    # prompts the user
    print('Which guardian class would you like to play?')
    print()
    # prints the available options from dict
    for pc_class_type in pc_class_types:
        print('Type', pc_class_type['var'], 'to Select:', pc_class_type['name'])
    while True:
        print()
        # takes input from user
        player_character = input('Your Selection: ').strip().lower()
        # matches user input to class type dict and returns class type name 
        for pc_class_type in pc_class_types:
            if player_character == pc_class_type['var']:
                print(pc_class_type['name'], 'confirmed')
                return (pc_class_type['name'])


# get player character subclass type and damage type
def get_pc_subclass_type(pc_class_type):
    print('-------------------------------------------')
    print()
    # prompts the user
    print(f'As a {pc_class_type}, what subclass would you like to play?')
    print()
    # prints the available options from dict
    for pc_subclass_type in pc_subclass_types:
        if pc_class_type == pc_subclass_type['class type']:
            print('Type', pc_subclass_type['damage type var'], 'to Select:', pc_subclass_type['damage type'], pc_subclass_type['name'])
    while True:
        print()
        # takes input from user
        subclass_type = input('Your Selection: ').strip().lower()
        # matches user input to subclass type dict and returns subclass type name and damage type
        for pc_subclass_type in pc_subclass_types:    
            if (pc_class_type == pc_subclass_type['class type']) and (subclass_type == pc_subclass_type['damage type var']):
                print(pc_subclass_type['damage type'], pc_subclass_type['name'], f'{pc_class_type} confirmed')
                return (pc_subclass_type['name'], pc_subclass_type['damage type'])


# get player character super ability
def get_pc_ablty_super(pc_class_type, pc_subclass_type, pc_subclass_damage_type):
    print('-------------------------------------------') 
    print()
    # prompts the user for input
    print(f'As a {pc_subclass_type} {pc_class_type} with the {pc_subclass_damage_type} subclass equipped, your super ability options are:')
    print()
    # prints the available options from dict
    for ablty_super in ablty_supers:    
        if (pc_class_type == ablty_super['class type']):
            for _ in list(ablty_super['subclass']):                
                if _ == pc_subclass_type:
                    print('Type', ablty_super['abbrev'], 'to Select:', ablty_super['name'])
    while True:
        print()
        # takes input from user
        pc_ablty_super = input('Your Selection: ').strip().lower()
        # matches user input to super dict and returns super ablity name and damage type
        for ablty_super in ablty_supers:
            if (pc_class_type == ablty_super['class type']) and (pc_ablty_super == ablty_super['abbrev']):
                print(ablty_super['name'], 'confirmed')
                return (ablty_super['name'], ablty_super['dmg type'])


# get player character class ability
def get_pc_ablty_classablty(pc_class_type, pc_subclass_type):
    print('-------------------------------------------')
    print()
    # prompts the user for input
    print(f'As a {pc_subclass_type} {pc_class_type}, your class ability options are:')
    print()
    # prints the available options from dict
    for ablty_classablty in ablty_classabltys:
        if pc_class_type == ablty_classablty['class type']:
            for _ in list(ablty_classablty['subclass']):                
                if _ == pc_subclass_type:
                    print('Type', ablty_classablty['abbrev'], 'to Select:', ablty_classablty['name'])
    while True:
        print()
        # takes input from user
        pc_ablty_classablty = input('Your Selection: ').strip().lower()
        # matches user input to super dict and returns super ablity name and damage type
        for ablty_classablty in ablty_classabltys:
            if (pc_class_type == ablty_classablty['class type']) and (pc_ablty_classablty == ablty_classablty['abbrev']):
                print(ablty_classablty['name'], 'confirmed')
                return (ablty_classablty['name'])


# get player character movement ability
def get_pc_ablty_moveablty(pc_class_type, pc_subclass_type):
    print('-------------------------------------------')
    print()
    # prompts the user for input
    print(f'As a {pc_subclass_type} {pc_class_type}, your movement ability options are:')
    print()
    # prints the available options from dict
    for ablty_moveablty in ablty_moveabltys:
        if pc_class_type == ablty_moveablty['class type']:
            for _ in list(ablty_moveablty['subclass']):                
                if _ == pc_subclass_type:
                    print('Type', ablty_moveablty['abbrev'], 'to Select:', ablty_moveablty['name'])
    while True:
        print()
        # takes input from user
        pc_ablty_moveablty = input('Your Selection: ').strip().lower()
        # matches user input to super dict and returns super ablity name and damage type
        for ablty_moveablty in ablty_moveabltys:
            if (pc_class_type == ablty_moveablty['class type']) and (pc_ablty_moveablty == ablty_moveablty['abbrev']):
                print(ablty_moveablty['name'], 'confirmed')
                return (ablty_moveablty['name'])


# get player character melee ability
def get_pc_ablty_meleeablty(pc_class_type, pc_subclass_type):
    print('-------------------------------------------')
    print()
    # prompts the user for input
    print(f'As a {pc_subclass_type} {pc_class_type}, your melee ability options are:')
    print()
    # prints the available options from dict
    for ablty_meleeablty in ablty_meleeabltys:
        if pc_class_type == ablty_meleeablty['class type']:
            for _ in list(ablty_meleeablty['subclass']):                
                if _ == pc_subclass_type:
                    print('Type', ablty_meleeablty['id'], 'to Select:', ablty_meleeablty['name'])
    while True:
        print()
        # takes input from user
        pc_ablty_meleeablty = input('Your Selection: ').strip().lower()
        # matches user input to super dict and returns super ablity name and damage type
        for ablty_meleeablty in ablty_meleeabltys:
            if (pc_class_type == ablty_meleeablty['class type']) and (pc_ablty_meleeablty == ablty_meleeablty['id']):
                print(ablty_meleeablty['name'], 'confirmed')
                return (ablty_meleeablty['name'])


# get player character grenade ability
def get_pc_ablty_grenadeablty(pc_class_type, pc_subclass_type):
    print('-------------------------------------------')
    print()
    # prompts the user for input
    print(f'As a {pc_subclass_type} {pc_class_type}, your grenade ability options are:')
    print()
    # prints the available options from dict
    for ablty_grenadeablty in ablty_grenadeabltys:
        for _ in list(ablty_grenadeablty['class type']):
            if _ == pc_class_type:
                for _ in list(ablty_grenadeablty['subclass']):                
                    if _ == pc_subclass_type:
                        print('Type', ablty_grenadeablty['id'], 'to Select:', ablty_grenadeablty['name'])
    while True:
        print()
        # takes input from user
        pc_ablty_grenadeablty = input('Your Selection: ').strip().lower()
        # matches user input to super dict and returns super ablity name and damage type
        for ablty_grenadeablty in ablty_grenadeabltys:
            for _ in list(ablty_grenadeablty['class type']):
                if _ == pc_class_type:
                    if pc_ablty_grenadeablty == ablty_grenadeablty['id']:
                        print(ablty_grenadeablty['name'], 'confirmed')
                        return (ablty_grenadeablty['name'])


# get player character aspect options
def get_pc_aspects(pc_class_type, pc_subclass_type):
    print('-------------------------------------------')
    print()
    # prompts the user for input
    print(f'As a {pc_subclass_type} {pc_class_type}, your aspect options are:')
    print()
    # prints the available options from dict
    for pc_aspect in pc_aspects:
        if pc_class_type == pc_aspect['cl']:
            for _ in list(pc_aspect['subcl']):
                if _ == pc_subclass_type:
                    print('Type', pc_aspect['id'], 'to Select:', pc_aspect['name'])


# player character class types dict
pc_class_types = [
    {'name': 'titan', 'var': 't'},    
    {'name': 'hunter', 'var': 'h'},
    {'name': 'warlock', 'var': 'w'},
]


# player character subclass types dict
pc_subclass_types = [
    {'name': 'striker', 'class type': 'titan', 'damage type': 'arc', 'damage type var': 'arc'},
    {'name': 'sunbreaker', 'class type': 'titan', 'damage type': 'solar', 'damage type var': 'sol'},
    {'name': 'sentinel', 'class type': 'titan', 'damage type': 'void', 'damage type var': 'voi'},
    {'name': 'behemoth', 'class type': 'titan', 'damage type': 'stasis', 'damage type var': 'sta'},
    {'name': 'berserker', 'class type': 'titan', 'damage type': 'strand', 'damage type var': 'str'},
    {'name': 'prismatic', 'class type': 'titan', 'damage type': 'prismatic', 'damage type var': 'pri'},
    {'name': 'arcstrider', 'class type': 'hunter', 'damage type': 'arc', 'damage type var': 'arc'},
    {'name': 'gunslinger', 'class type': 'hunter', 'damage type': 'solar', 'damage type var': 'sol'},
    {'name': 'nightstalker', 'class type': 'hunter', 'damage type': 'void', 'damage type var': 'voi'},
    {'name': 'revenant', 'class type': 'hunter', 'damage type': 'stasis', 'damage type var': 'sta'},
    {'name': 'threadrunner', 'class type': 'hunter', 'damage type': 'strand', 'damage type var': 'str'},
    {'name': 'prismatic', 'class type': 'hunter', 'damage type': 'prismatic', 'damage type var': 'pri'},
    {'name': 'stormcaller', 'class type': 'warlock', 'damage type': 'arc', 'damage type var': 'arc'},
    {'name': 'dawnblade', 'class type': 'warlock', 'damage type': 'solar', 'damage type var': 'sol'},
    {'name': 'voidwalker', 'class type': 'warlock', 'damage type': 'void', 'damage type var': 'voi'},
    {'name': 'shadebinder', 'class type': 'warlock', 'damage type': 'stasis', 'damage type var': 'sta'},
    {'name': 'broodweaver', 'class type': 'warlock', 'damage type': 'strand', 'damage type var': 'str'},
    {'name': 'prismatic', 'class type': 'warlock', 'damage type': 'prismatic', 'damage type var': 'pri'},
]


# damage types dict
damage_types = [
    {'name': 'kinetic', 'alignment': None, 'elemental pickup': None, 'verbs': None},
    {'name': 'arc', 'alignment': 'light', 'elemental pickup': 'ionic trace', 'verbs': ['jolt', 'blind', 'amplified']},
    {'name': 'solar', 'alignment': 'light', 'elemental pickup': 'firesprite', 'verbs': ['cure', 'restoration', 'scorch', 'ignition']},
    {'name': 'void', 'alignment': 'light', 'elemental pickup': 'void breach', 'verbs': ['suppression', 'volatile', 'weaken', 'void overshield']},
    {'name': 'stasis', 'alignment': 'dark', 'elemental pickup': 'stasis shard', 'verbs': ['shatter', 'freeze', 'slow', 'frost armor']},
    {'name': 'strand', 'alignment': 'dark', 'elemental pickup': 'tangle', 'verbs': ['woven mail', 'suspend', 'unravel']},
]


# super ability dict
ablty_supers = [
    {'name': 'fists of havoc', 'dmg type': 'arc', 'class type': 'titan', 'subclass': ['striker'], 'abbrev': 'foh'},
    {'name': 'thundercrash', 'dmg type': 'arc', 'class type': 'titan', 'subclass': ['striker', 'prismatic'], 'abbrev': 'tcr'},
    {'name': 'hammer of sol', 'dmg type': 'solar', 'class type': 'titan', 'subclass': ['sunbreaker', 'prismatic'], 'abbrev': 'hos'},
    {'name': 'burning maul', 'dmg type': 'solar', 'class type': 'titan', 'subclass': ['sunbreaker'], 'abbrev': 'bma'},
    {'name': 'ward of dawn', 'dmg type': 'void', 'class type': 'titan', 'subclass': ['sentinel'], 'abbrev': 'wod'},
    {'name': 'sentinel shield', 'dmg type': 'void', 'class type': 'titan', 'subclass': ['sentinel'], 'abbrev': 'sen'},
    {'name': 'twilight arsenal', 'dmg type': 'void', 'class type': 'titan', 'subclass': ['sentinel', 'prismatic'], 'abbrev': 'twr'},
    {'name': 'glacial quake', 'dmg type': 'stasis', 'class type': 'titan', 'subclass': ['behemoth', 'prismatic'], 'abbrev': 'glq'},
    {'name': 'bladefury', 'dmg type': 'strand', 'class type': 'titan', 'subclass': ['berserker', 'prismatic'], 'abbrev': 'blf'},
    {'name': 'arc staff', 'dmg type': 'arc', 'class type': 'hunter', 'subclass': ['arcstrider'], 'abbrev': 'ast'},
    {'name': 'gathering storm', 'dmg type': 'arc', 'class type': 'hunter', 'subclass': ['arcstrider'], 'abbrev': 'gst'},
    {'name': 'storms edge', 'dmg type': 'arc', 'class type': 'hunter', 'subclass': ['arcstrider', 'prismatic'], 'abbrev': 'ste'},
    {'name': 'golden gun: deadshot', 'dmg type': 'solar', 'class type': 'hunter', 'subclass': ['gunslinger'], 'abbrev': 'ggd'},
    {'name': 'golden gun: marksman', 'dmg type': 'solar', 'class type': 'hunter', 'subclass': ['gunslinger', 'prismatic'], 'abbrev': 'ggm'},
    {'name': 'blade barrage', 'dmg type': 'solar', 'class type': 'hunter', 'subclass': ['gunslinger'], 'abbrev': 'blb'},
    {'name': 'shadowshot: deadfall', 'dmg type': 'void', 'class type': 'hunter', 'subclass': ['nightstalker', 'prismatic'], 'abbrev': 'sdf'},
    {'name': 'shadowshot: moebius quiver', 'dmg type': 'void', 'class type': 'hunter', 'subclass': ['nightstalker'], 'abbrev': 'smq'},
    {'name': 'spectral blades', 'dmg type': 'void', 'class type': 'hunter', 'subclass': ['nightstalker'], 'abbrev': 'spb'},
    {'name': 'silence and squall', 'dmg type': 'stasis', 'class type': 'hunter', 'subclass': ['revenant', 'prismatic'], 'abbrev': 'sas'},
    {'name': 'silkstrike', 'dmg type': 'strand', 'class type': 'hunter', 'subclass': ['threadrunner', 'prismatic'], 'abbrev': 'sil'},
    {'name': 'stormtrance', 'dmg type': 'arc', 'class type': 'warlock', 'subclass': ['stormcaller', 'prismatic'], 'abbrev': 'stt'},
    {'name': 'chaos reach', 'dmg type': 'arc', 'class type': 'warlock', 'subclass': ['stormcaller'], 'abbrev': 'chr'},
    {'name': 'daybreak', 'dmg type': 'solar', 'class type': 'warlock', 'subclass': ['dawnblade'], 'abbrev': 'day'},
    {'name': 'well of radiance', 'dmg type': 'solar', 'class type': 'warlock', 'subclass': ['dawnblade'], 'abbrev': 'wel'},
    {'name': 'song of flame', 'dmg type': 'solar', 'class type': 'warlock', 'subclass': ['dawnblade', 'prismatic'], 'abbrev': 'sof'},
    {'name': 'nova warp', 'dmg type': 'void', 'class type': 'warlock', 'subclass': ['voidwalker'], 'abbrev': 'now'},
    {'name': 'nova bomb: vortex', 'dmg type': 'void', 'class type': 'warlock', 'subclass': ['voidwalker'], 'abbrev': 'vor'},
    {'name': 'nova bomb: cataclysm', 'dmg type': 'void', 'class type': 'warlock', 'subclass': ['voidwalker', 'prismatic'], 'abbrev': 'cat'},
    {'name': 'winters wrath', 'dmg type': 'stasis', 'class type': 'warlock', 'subclass': ['shadebinder', 'prismatic'], 'abbrev': 'win'},
    {'name': 'needlestorm', 'dmg type': 'strand', 'class type': 'warlock', 'subclass': ['broodweaver', 'prismatic'], 'abbrev': 'nee'},
]


# player character class ability dict
ablty_classabltys = [
    {'name': 'towering barricade', 'class type': 'titan', 'subclass': ['striker', 'sunbreaker', 'sentinel', 'behemoth', 'berserker', 'prismatic'], 'abbrev': 'tow'},
    {'name': 'rally barricade', 'class type': 'titan', 'subclass': ['striker', 'sunbreaker', 'sentinel', 'behemoth', 'berserker', 'prismatic'], 'abbrev': 'ral'},
    {'name': 'thruster', 'class type': 'titan', 'subclass': ['striker', 'prismatic'], 'abbrev': 'thr'},
    {'name': 'marksmans dodge', 'class type': 'hunter', 'subclass': ['arcstrider', 'gunslinger', 'nightstalker', 'revenant', 'threadrunner', 'prismatic'], 'abbrev': 'mar'},
    {'name': 'gamblers dodge', 'class type': 'hunter', 'subclass': ['arcstrider', 'gunslinger', 'nightstalker', 'revenant', 'threadrunner', 'prismatic'], 'abbrev': 'gam'},
    {'name': 'acrobats dodge', 'class type': 'hunter', 'subclass': ['gunslinger', 'prismatic'], 'abbrev': 'acr'},
    {'name': 'healing rift', 'class type': 'warlock', 'subclass': ['stormcaller', 'dawnblade', 'voidwalker', 'shadebinder', 'broodweaver', 'prismatic'], 'abbrev': 'hea'},
    {'name': 'empowering rift', 'class type': 'warlock', 'subclass': ['stormcaller', 'dawnblade', 'voidwalker', 'shadebinder', 'broodweaver', 'prismatic'], 'abbrev': 'emp'},
    {'name': 'phoenix dive', 'class type': 'warlock', 'subclass': ['dawnblade', 'prismatic'], 'abbrev': 'pho'},
]


# player character movement ability dict
ablty_moveabltys = [
    {'name': 'high lift', 'class type': 'titan', 'subclass': ['striker', 'sunbreaker', 'sentinel', 'behemoth', 'berserker', 'prismatic'], 'abbrev': 'hih'},
    {'name': 'strafe lift', 'class type': 'titan', 'subclass': ['striker', 'sunbreaker', 'sentinel', 'behemoth', 'berserker', 'prismatic'], 'abbrev': 'stf'},
    {'name': 'catapult lift', 'class type': 'titan', 'subclass': ['striker', 'sunbreaker', 'sentinel', 'behemoth', 'berserker', 'prismatic'], 'abbrev': 'cat'},
    {'name': 'high jump', 'class type': 'hunter', 'subclass': ['arcstrider', 'gunslinger', 'nightstalker', 'revenant', 'threadrunner', 'prismatic'], 'abbrev': 'hih'},
    {'name': 'strafe jump', 'class type': 'hunter', 'subclass': ['arcstrider', 'gunslinger', 'nightstalker', 'revenant', 'threadrunner', 'prismatic'], 'abbrev': 'stf'},
    {'name': 'triple jump', 'class type': 'hunter', 'subclass': ['arcstrider', 'gunslinger', 'nightstalker', 'revenant', 'threadrunner', 'prismatic'], 'abbrev': 'trp'},
    {'name': 'blink', 'class type': 'hunter', 'subclass': ['arcstrider', 'prismatic'], 'abbrev': 'bnk'},
    {'name': 'strafe glide', 'class type': 'warlock', 'subclass': ['stormcaller', 'dawnblade', 'voidwalker', 'shadebinder', 'broodweaver', 'prismatic'], 'abbrev': 'stf'},
    {'name': 'burst glide', 'class type': 'warlock', 'subclass': ['stormcaller', 'dawnblade', 'voidwalker', 'shadebinder', 'broodweaver', 'prismatic'], 'abbrev': 'bur'},
    {'name': 'balanced glide', 'class type': 'warlock', 'subclass': ['stormcaller', 'dawnblade', 'voidwalker', 'shadebinder', 'broodweaver', 'prismatic'], 'abbrev': 'bal'},
    {'name': 'blink', 'class type': 'warlock', 'subclass': ['voidwalker', 'prismatic'], 'abbrev': 'bnk'},
]


# player character melee ability dict
ablty_meleeabltys = [
    {'id': 'sei', 'name': 'seismic strike', 'class type': 'titan', 'subclass': ['striker'], 'dmg type': 'arc'},
    {'id': 'bal', 'name': 'ballistic slam', 'class type': 'titan', 'subclass': ['striker'], 'dmg type': 'arc'},
    {'id': 'thu', 'name': 'thunderclap', 'class type': 'titan', 'subclass': ['striker', 'prismatic'], 'dmg type': 'arc'},
    {'id': 'ham', 'name': 'hammer strike', 'class type': 'titan', 'subclass': ['sunbreaker', 'prismatic'], 'dmg type': 'solar'},
    {'id': 'thr', 'name': 'throwing hammer', 'class type': 'titan', 'subclass': ['sunbreaker'], 'dmg type': 'solar'},
    {'id': 'bsh', 'name': 'shield bash', 'class type': 'titan', 'subclass': ['sentinel'], 'dmg type': 'void'},
    {'id': 'sth', 'name': 'shield throw', 'class type': 'titan', 'subclass': ['sentinel', 'prismatic'], 'dmg type': 'void'},
    {'id': 'shv', 'name': 'shiver strike', 'class type': 'titan', 'subclass': ['behemoth', 'prismatic'], 'dmg type': 'stasis'},
    {'id': 'frn', 'name': 'frenzied blade', 'class type': 'titan', 'subclass': ['berserker', 'prismatic'], 'dmg type': 'strand'},
    {'id': 'com', 'name': 'combination blow', 'class type': 'hunter', 'subclass': ['arcstrider', 'prismatic'], 'dmg type': 'arc'},
    {'id': 'dis', 'name': 'disorienting blow', 'class type': 'hunter', 'subclass': ['arcstrider'], 'dmg type': 'arc'},
    {'id': 'lit', 'name': 'lightweight knife', 'class type': 'hunter', 'subclass': ['gunslinger'], 'dmg type': 'solar'},
    {'id': 'wei', 'name': 'weighted throwing knife', 'class type': 'hunter', 'subclass': ['gunslinger'], 'dmg type': 'solar'},
    {'id': 'trk', 'name': 'knife trick', 'class type': 'hunter', 'subclass': ['gunslinger', 'prismatic'], 'dmg type': 'solar'},
    {'id': 'prx', 'name': 'proximity explosive knife', 'class type': 'hunter', 'subclass': ['gunslinger'], 'dmg type': 'solar'},
    {'id': 'snr', 'name': 'snare bomb', 'class type': 'hunter', 'subclass': ['nightstalker', 'prismatic'], 'dmg type': 'void'},
    {'id': 'wth', 'name': 'withering blade', 'class type': 'hunter', 'subclass': ['revenant', 'prismatic'], 'dmg type': 'stasis'},
    {'id': 'the', 'name': 'threaded spike', 'class type': 'hunter', 'subclass': ['threadrunner', 'prismatic'], 'dmg type': 'strand'},
    {'id': 'bal', 'name': 'ball lightning', 'class type': 'warlock', 'subclass': ['stormcaller'], 'dmg type': 'arc'},
    {'id': 'chn', 'name': 'chain lightning', 'class type': 'warlock', 'subclass': ['stormcaller', 'prismatic'], 'dmg type': 'arc'},
    {'id': 'cel', 'name': 'celestial fire', 'class type': 'warlock', 'subclass': ['dawnblade'], 'dmg type': 'solar'},
    {'id': 'inc', 'name': 'incinerator snap', 'class type': 'warlock', 'subclass': ['dawnblade', 'prismatic'], 'dmg type': 'solar'},
    {'id': 'pok', 'name': 'pocket singularity', 'class type': 'warlock', 'subclass': ['voidwalker', 'prismatic'], 'dmg type': 'void'},
    {'id': 'pen', 'name': 'penumbral blast', 'class type': 'warlock', 'subclass': ['shadebinder', 'prismatic'], 'dmg type': 'stasis'},
    {'id': 'arc', 'name': 'arcane needle', 'class type': 'warlock', 'subclass': ['broodweaver', 'prismatic'], 'dmg type': 'strand'},
]


# player character grenade ability dict
ablty_grenadeabltys = [
    {'id': 'lit', 'name': 'lightning grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['striker', 'arcstrider', 'stormcaller'], 'dmg type': 'arc'},
    {'id': 'str', 'name': 'storm grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['striker', 'arcstrider', 'stormcaller'], 'dmg type': 'arc'},
    {'id': 'fla', 'name': 'flashbang grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['striker', 'arcstrider', 'stormcaller'], 'dmg type': 'arc'},
    {'id': 'pul', 'name': 'pulse grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['striker', 'arcstrider', 'stormcaller'], 'dmg type': 'arc'},
    {'id': 'skp', 'name': 'skip grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['striker', 'arcstrider', 'stormcaller'], 'dmg type': 'arc'},
    {'id': 'flx', 'name': 'flux grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['striker', 'arcstrider', 'stormcaller'], 'dmg type': 'arc'},
    {'id': 'arc', 'name': 'arcbolt grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['striker', 'arcstrider', 'stormcaller'], 'dmg type': 'arc'},
    {'id': 'trp', 'name': 'tripmine grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'thr', 'name': 'thermite grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'inc', 'name': 'incendiary grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'sol', 'name': 'solar grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'swm', 'name': 'swarm grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'fus', 'name': 'fusion grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'fir', 'name': 'firebolt grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'hea', 'name': 'healing grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmg type': 'solar'},
    {'id': 'spk', 'name': 'void spike', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sentinel', 'nightstalker', 'voidwalker'], 'dmg type': 'void'},
    {'id': 'wal', 'name': 'void wall', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sentinel', 'nightstalker', 'voidwalker'], 'dmg type': 'void'},
    {'id': 'sup', 'name': 'suppressor grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sentinel', 'nightstalker', 'voidwalker'], 'dmg type': 'void'},
    {'id': 'vor', 'name': 'vortex grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sentinel', 'nightstalker', 'voidwalker'], 'dmg type': 'void'},
    {'id': 'sca', 'name': 'scatter grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sentinel', 'nightstalker', 'voidwalker'], 'dmg type': 'void'},
    {'id': 'mag', 'name': 'magnetic grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sentinel', 'nightstalker', 'voidwalker'], 'dmg type': 'void'},
    {'id': 'axn', 'name': 'axion bolt', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['sentinel', 'nightstalker', 'voidwalker'], 'dmg type': 'void'},
    {'id': 'gla', 'name': 'glacier grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['behemoth', 'revenant', 'shadebinder'], 'dmg type': 'stasis'},
    {'id': 'dsk', 'name': 'duskfield grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['behemoth', 'revenant', 'shadebinder'], 'dmg type': 'stasis'},
    {'id': 'col', 'name': 'coldsnap grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['behemoth', 'revenant', 'shadebinder'], 'dmg type': 'stasis'},
    {'id': 'sha', 'name': 'shackle grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['berserker', 'threadrunner', 'broodweaver'], 'dmg type': 'strand'},
    {'id': 'thr', 'name': 'threadling grenade', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['berserker', 'threadrunner', 'broodweaver'], 'dmg type': 'strand'},
    {'id': 'gap', 'name': 'grapple', 'class type': ['titan', 'hunter', 'warlock'], 'subclass': ['berserker', 'threadrunner', 'broodweaver'], 'dmg type': 'strand'},
]


# player character aspects dict
pc_aspects = [
    {'id': 'gap', 'name': 'touch of thunder', 'cl': 'titan', 'subcl': ['striker'], 'dmgtyp': 'arc', 'engycap': 2},
    {'id': 'gap', 'name': 'juggernaut', 'cl': 'titan', 'subcl': ['striker'], 'dmgtyp': 'arc', 'engycap': 2},
    {'id': 'gap', 'name': 'knockout', 'cl': 'titan', 'subcl': ['striker'], 'dmgtyp': 'arc', 'engycap': 2},
    {'id': 'gap', 'name': 'roaring flames', 'cl': 'titan', 'subcl': ['sunbreaker'], 'dmgtyp': 'solar', 'engycap': 2},
    {'id': 'gap', 'name': 'sol invictus', 'cl': 'titan', 'subcl': ['sunbreaker'], 'dmgtyp': 'solar', 'engycap': 2},
    {'id': 'gap', 'name': 'consecration', 'cl': 'titan', 'subcl': ['sunbreaker'], 'dmgtyp': 'solar', 'engycap': 2},
    {'id': 'gap', 'name': 'controlled demolition', 'cl': 'titan', 'subcl': ['sentinel'], 'dmgtyp': 'void', 'engycap': 2},
    {'id': 'gap', 'name': 'bastion', 'cl': 'titan', 'subcl': ['sentinel'], 'dmgtyp': 'void', 'engycap': 2},
    {'id': 'gap', 'name': 'offensive bulwark', 'cl': 'titan', 'subcl': ['sentinel'], 'dmgtyp': 'void', 'engycap': 2},
    {'id': 'gap', 'name': 'unbreakable', 'cl': 'titan', 'subcl': ['sentinel'], 'dmgtyp': 'void', 'engycap': 2},
    {'id': 'gap', 'name': 'cryoclasm', 'cl': 'titan', 'subcl': ['behemoth'], 'dmgtyp': 'stasis', 'engycap': 2},
    {'id': 'gap', 'name': 'tectonic harvest', 'cl': 'titan', 'subcl': ['behemoth'], 'dmgtyp': 'stasis', 'engycap': 2},
    {'id': 'gap', 'name': 'howl of the storm', 'cl': 'titan', 'subcl': ['behemoth'], 'dmgtyp': 'stasis', 'engycap': 2},
    {'id': 'gap', 'name': 'diamond lance', 'cl': 'titan', 'subcl': ['behemoth'], 'dmgtyp': 'stasis', 'engycap': 3},
    {'id': 'gap', 'name': 'into the fray', 'cl': 'titan', 'subcl': ['berserker'], 'dmgtyp': 'strand', 'engycap': 2},
    {'id': 'gap', 'name': 'drengrs lash', 'cl': 'titan', 'subcl': ['berserker'], 'dmgtyp': 'strand', 'engycap': 2},
    {'id': 'gap', 'name': 'flechette storm', 'cl': 'titan', 'subcl': ['berserker'], 'dmgtyp': 'strand', 'engycap': 2},
    {'id': 'gap', 'name': 'banner of war', 'cl': 'titan', 'subcl': ['berserker'], 'dmgtyp': 'strand', 'engycap': 2},
]


# player charcter fragments dict
pc_fragments = [
    {'id':'gap', 'name': 'spark of haste', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of instinct', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of beacons', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of resistance', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': ['str'], 'eff': (10), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of momentum', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of shock', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': ['dis'], 'eff': (-10), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of ions', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of discharge', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': ['str'], 'eff': (-10), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of frequency', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of focus', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': ['res'], 'eff': (-10), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of recharge', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of magnitude', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of amplitude', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of feedback', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': ['res'], 'eff': (10), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of volts', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': ['rec'], 'eff': (10), 'engycsum': 1},
    {'id':'gap', 'name': 'spark of brilliance', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['striker', 'arcstrider', 'stormcaller'], 'dmgtyp': 'arc', 'stat': ['int'], 'eff': (10), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
    {'id':'gap', 'name': 'ember of ', 'cl': ['titan', 'hunter', 'warlock'], 'subcl': ['sunbreaker', 'gunslinger', 'dawnblade'], 'dmgtyp': 'solar', 'stat': [None], 'eff': (0), 'engycsum': 1},
]


if __name__ == "__main__":
    main()





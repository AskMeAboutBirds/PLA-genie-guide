# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:51:20 2023

Stripped down version of Lincoln-LM's PLA-Live-MAp
https://github.com/Lincoln-LM/PLA-Live-Map

All credit to them for the original code converting seeds to spreads

@author: amab
"""

import json
import nxreader
from xoroshiro import XOROSHIRO
import argparse


def generate_from_seed(seed,rolls,guaranteed_ivs):
    """Generate pokemon information from a fixed seed (FixInitSpec)"""
    rng = XOROSHIRO(seed)
    encryption_constant = rng.rand(0xFFFFFFFF)
    sidtid = rng.rand(0xFFFFFFFF)
    for _ in range(rolls):
        pid = rng.rand(0xFFFFFFFF)
        shiny = ((pid >> 16) ^ (sidtid >> 16) ^ (pid & 0xFFFF) ^ (sidtid & 0xFFFF)) < 0x10
        if shiny:
            break
        
    ivs = [-1,-1,-1,-1,-1,-1]
    for i in range(guaranteed_ivs):
        index = rng.rand(6)
        while ivs[index] != -1:
            index = rng.rand(6)
        ivs[index] = 31
    for i in range(6):
        if ivs[i] == -1:
            ivs[i] = rng.rand(32)
    ability = rng.rand(2)
    #gender = rng.rand(252) + 1
    nature = rng.rand(25)
    height = rng.rand(0x81) + rng.rand(0x80)

    weight = rng.rand(0x81) + rng.rand(0x80)

    return encryption_constant,pid,ivs,ability,0,nature,shiny, height, weight



def check_iv(iv,ivf,ivc):
    if ivc == '>=':
        return iv >= ivf
    if ivc == '>':
        return iv >= ivf
    if ivc == '=':
        return iv == ivf
    if ivc == '==':
        return iv == ivf
    if ivc == '!=':
        return iv != ivf
    if ivc == '<=':
        return iv <= ivf
    if ivc == '<':
        return iv < ivf    
                
    

def generate_from_seed_wgender(seed,rolls,guaranteed_ivs):
    """Generate pokemon information from a fixed seed (FixInitSpec)"""
    rng = XOROSHIRO(seed)
    encryption_constant = rng.rand(0xFFFFFFFF)
    sidtid = rng.rand(0xFFFFFFFF)
    for _ in range(rolls):
        pid = rng.rand(0xFFFFFFFF)
        shiny = ((pid >> 16) ^ (sidtid >> 16) ^ (pid & 0xFFFF) ^ (sidtid & 0xFFFF)) < 0x10
        if shiny:
            break
    ivs = [-1,-1,-1,-1,-1,-1]
    for i in range(guaranteed_ivs):
        index = rng.rand(6)
        while ivs[index] != -1:
            index = rng.rand(6)
        ivs[index] = 31
    for i in range(6):
        if ivs[i] == -1:
            ivs[i] = rng.rand(32)
    ability = rng.rand(2)
    gender = rng.rand(252) + 1
    nature = rng.rand(25)
    height = rng.rand(0x81) + rng.rand(0x80)

    weight = rng.rand(0x81) + rng.rand(0x80)
    return encryption_constant,pid,ivs,ability,gender,nature,shiny, height, weight



def get_size(h):
    if h == 0:
        return 'xxxs'
    if h >= 1 and h <31:
        return 'xxs'
    if h >= 31 and h < 61:
        return 'xs'
    if h >= 61 and h < 100:
        return 's'
    if h >= 100 and h < 161:
        return 'av'
    if h >= 161 and h < 195:
        return 'L'
    if h >= 195 and h < 242:
        return 'XL'
    if h >= 242 and h < 255:
        return 'xxL'
    if h == 255:
        return 'xxxL'
        


def scan_group_id(group_id = 305,
                  rolls = 1,
                  guaranteed_ivs = 3,
                  init_spawn = False,
                  filters = True,
                  nature_filter =[5,20],
                  iv_filter = [30,0,30,30,30,31],
                  search_range=200,
                  gender = False, gs = -1, iv_filter_comparison = ['>=', '>=', '>=', '>=', '>=', '>='], shiny_filter=0, reader=None, known_spawner_ids =None, spawner_to_species=None ):
    
    SPAWNER_PTR = "[[main+42a6ee0]+330]"

    if gs == -1:
        """Find the next advance that matches poke_filter for a spawner"""
        # pylint: disable=too-many-locals,too-many-arguments
        generator_seed = reader.read_pointer_int(f"{SPAWNER_PTR}"\
                                                f"+{0x70+group_id*0x440+0x20:X}",8)
    else:
        generator_seed = gs
        
    spawner_id = reader.read_pointer_int(f"{SPAWNER_PTR}"\
                                                f"+{0x70+group_id*0x440+0x20+126*8:X}",8)

    generator_seed = reader.read_pointer_int(f"{SPAWNER_PTR}"\
                                             f"+{0x70+group_id*0x440+0x20:X}",8)

        
    group_seed = (generator_seed - 0x82A2B175229D6A5B) & 0xFFFFFFFFFFFFFFFF
    main_rng = XOROSHIRO(group_seed)    
    
    if not init_spawn:
        # advance once
        main_rng.next() # spawner 0
        main_rng.next() # spawner 1
        main_rng.reseed(main_rng.next())        
    
    
    print('______________')
    print('GID:        %s'%str(group_id))
    if generator_seed == 0x0:
        print('Blank')
        return 
        # 'GID:        %s'
    print('GS:         %s'%hex(generator_seed))
    print('Group seed: %s'%hex(group_seed))
    if str(spawner_id) in known_spawner_ids:
        xx=1
        print('Spawner:    %s'% '/'.join(spawner_to_species[str(spawner_id)]))
    else:
        xx=1
        print('Spawner:    %s'%hex(spawner_id) + ' Unknown')
    nf = [x.lower() for x in nature_filter]
    
    
    
    for i in range(search_range):
        generator_seed = main_rng.next();
        main_rng.next();
        rng = XOROSHIRO(generator_seed);
        rng.next()
        
        
        if not gender:
            encryption_constant,pid,ivs,ability,gender,nature,shiny, height, weight = generate_from_seed(rng.next(),rolls,guaranteed_ivs)
        else:
            encryption_constant,pid,ivs,ability,gender,nature,shiny, height, weight = generate_from_seed_wgender(rng.next(),rolls,guaranteed_ivs)
        
        filter_true = 0
        if sum([check_iv(ivs[x],iv_filter[x],iv_filter_comparison[x]) for x in range(6)]) == 6:
            if natures[nature].lower() in nf:
                if shiny_filter != None:
                    if shiny:
                        filter_true = True
                else:
                    filter_true = True
                
        sz = get_size(height)
        
        if filter_true:
            print('*** ' + str(i) + ' ' + str(hex(encryption_constant)) +  ' ' + str(hex(pid)) +  ' ' + natures[nature] +  ' ', ivs, 'a: ' + str(ability),  ' h:' + str(height) + ' w:' + str(weight) +  ' s: ' + str(sz) + ' shiny: ' + str(shiny)  )    
        if filters == False:
            print(str(i) + ' ' + str(hex(encryption_constant)) +  ' ' + str(hex(pid)) +  ' ' + natures[nature] +  ' ', ivs, 'a: ' + str(ability),  ' h: ' + str(height) + ' w: ' + str(weight) + ' s: ' + str(sz)  + ' shiny: ' + str(shiny)      )  
        


        main_rng.reseed(main_rng.next())
        
        
def main(args):



    with open('./pla_spawner_ids.json','r') as f:
        spawner_to_species = json.load(f)
    
    
    natures = ['Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Docile', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty', 'Serious', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Bashful', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky']
    with open("config.json","r",encoding="utf-8") as config:
        IP_ADDRESS = json.load(config)["IP"]
        
    reader = nxreader.NXReader(IP_ADDRESS)
    
    legend_spawner_ids = {0x97d85b3bb18fd0ab:'Manaphy',
                         0x7c9e6d810b343908:'Phione',
                         0x162f766db48fc6d8:'Phione',
                         0xe1cbacbba2d63665:'Phione',
                         0xA468ADF5964CCE65:'Enamorus',
                         0xB8B7D33AB95F7A11:'Tornadus',
                         0x08398514506FBE25:'Thundurus',
                         0x88AF9BCFDD5FCD8F:'Landorus',
                         0x80E30B44446F80BE:'Cresselia',
                         0xCDE0EAB0B0192256:'Shaymin',
                         0x14044B0D5D36E4B6:'Darkrai',
                         0xDA1BB574FA53D58C:'Heatran',
                         0x375CE0719E93B5CF:'Mesprit',
                         0x1E4356A6DFECC4B4:'Mesprit',
                         0x33DB175E98E892F7:'Azelf',
                         0xB45F56744903DACD:'Azelf',
                         0x5A67A8230FAF4B95:'Uxie',
                         0xBB70EEA5247394B0:'Uxie'}
    
    known_spawner_ids = spawner_to_species.keys()
        
    str2list = lambda s: s.replace(' ','').split(',')[:6]
    list2int = lambda l: [int(x) for x in l]
    
    ############################################
    
    # search 
    if args.natures == '' or args.natures =='none' or args.natures == 'None':
        nature_filter = natures
    else:
        nature_filter =  [x.lower() for x in str2list(args.natures)] #['Adamant', 'Jolly']
    guaranteed_ivs = int(args.guaranteed_ivs) # 3 for every legend other than phione
    
                        #hp    atk   def  spa   spdf  speed
    iv_filter =    list2int(str2list(args.iv_filter))
    iv_filter_comparison = str2list(args.iv_comp) #>, >=, <, <=, ==, !=
    
    shiny_filter = int(args.shiny_filter)
    
    #enamorous = 398, -2
    #403 manaphy
    gender = int(args.gender)     # false for every legend BUT heatran
    group_ids = list2int(args.gids.replace(' ','').split(','))  # list of group ids to check
    filters = int(args.filter_on)        # set to false to print every frame
    search_range = int(args.search_range) # how many frames to search
    gs = -1            # manual override for generator seed
    init_spawn = int(args.init_spawn)
    rolls = int(args.rolls)
    
    while 1:
        print(' ')
        input('press button to run')
        print('_______________')
        print('Running....')
        print('_______________')
        
        for gid in group_ids:
            scan_group_id(group_id = gid,
                          iv_filter = iv_filter,
                          nature_filter = nature_filter,
                          iv_filter_comparison = iv_filter_comparison,
                          filters=filters,
                          search_range=search_range,
                          gender=gender,
                          gs = gs,
                          guaranteed_ivs = guaranteed_ivs,
                          init_spawn=init_spawn, rolls=rolls, shiny_filter=shiny_filter,
                          reader=reader,  known_spawner_ids =known_spawner_ids, spawner_to_species=spawner_to_species )
    
        
    
    
if __name__ == '__main__':
    
    
    
    natures = ['Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Docile', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty', 'Serious', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Bashful', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky']
    
    
    
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--natures", help="natures seperated by commas, ex: Modest,timid",
                        type=str, default='')
    parser.add_argument("--iv_filter", help="iv value for comparison seperated by commas, ex: 31,31,31,0,31,31", type=str, default = '0,0,0,0,0,0')
    parser.add_argument("--iv_comp", help="iv comparison logic for iv_filter seperated by commas, >=,>=,>=,>=,>=,>= for all greater than",
                        type=str, default='>=,>=,>=,>=,>=,>=')
    parser.add_argument("--guaranteed_ivs", help="how many guaranteed ivs?, default is 3",
                        type=int, default=3)
    
    parser.add_argument("--search_range", help="how many frames to search, default is 500",
                        type=int, default=500)
    parser.add_argument("--gids", help="spawner group ids to look at seperated by commas, ex: 405,406,407",
                        type=str, default=300)
    
    parser.add_argument("--gender", help="Gender? default is false, only legend with gender is heatran!",
                        type=int, default=0)
    parser.add_argument("--filter_on", help="use the designated filter? ie dont print all frames, default is True",
                        type=int, default=1)
    parser.add_argument("--init_spawn", help="initial spawn of the pokemon? default is True",
                        type=int, default=1)
    
    parser.add_argument("--rolls", help="number of shiny rolls? default is 1 for legends",
                        type=int, default=1)
    
    parser.add_argument("--shiny_filter", help="only display shinies? default is false for legends",
                        type=int, default=0)
    
    args = parser.parse_args()

    #############################################
    
    main(args)
    
    
    

        


import numpy as np
import sys
import random

class Player:
    
    def __init__(self, name):
        self.name = name
        self.symbol = ''
        self.taken_strength = 0
        self.eye = ''
        self.creeping_darkness = 0
        self.ascendant_atrophy = False
        self.metaphysical_bleed = False
    
    def __str__(self):
        return self.name

symbols = ['Seaweed Fish', 'Double Fish', 'Down Fish', 'Up Fish',
           'Infinity Snake', 'Eight Snake', 'Down Snake', 'Up Snake',
           'Left Fire', 'Right Fire', 'Left Spear', 'Right Spear',
           'Down Bird', 'Up Bird', 'Sitting Bird', 'Standing Bird']

def main():
    fireteam = [Player('p1'),
                Player('p2'),
                Player('p3'),
                Player('p4'),
                Player('p5'),
                Player('p6')]
    
    # Encounter 1
    while kalli(fireteam):
        continue
    
    # Encounter 2
    while shuro_chi(fireteam):
        continue
    
    # Encounter 3
    while morgeth(fireteam):
        continue
    
    # Encounter 4
    while vault(fireteam):
        continue

    # Encounter 5
    while riven(fireteam):
        continue
    
    # Encounter 6
    while queenswalk(fireteam):
        continue
    
def kalli(fireteam):
    print('Encounter 1: Kalli, the Corrupted')
    
    for dps_phase in range(3):
        correct_plates = sorted(np.random.choice(symbols, size=3, replace=False).tolist() * 2)
        print(f'Plate Symbols: {correct_plates}')
        
        # Assign players to plates
        print('Plate Assignments:')
        for i in range(len(correct_plates)):
            p = fireteam[i]
            p.symbol = correct_plates[i]
            print(f'\t{p}: {p.symbol}')
        
        # Identify the "safe slice" without bombs on it
        plate = ['*'] * 3
        safe = np.random.randint(3)
        plate[safe] = ' '
        print(f'\nPlate:\n{plate}')
        chosen_slice = int(input('Choose a slice to stand on: ')) - 1
        if chosen_slice != safe:
            return light_fades()
        
        # Kill taken knights to complete plates
        knights_killed = int(input('Total Taken Knights Killed: '))
        
        # DPS Phase
        print('\nDPS Phase (Repeat 3x):')
        print('Kalli conceives an ontological weapon')
        print('DPS')
        print('Kalli prepares to wield her weapon')
        if knights_killed != len(fireteam):
            return light_fades()
        print('Players hide behind stained glass doors')
        print(f'\nDPS Phase {dps_phase + 1} complete')
        input()
    
    print('Kalli has been defeated!')
    input()

def shuro_chi(fireteam):
    print('Encounter 2: Shuro Chi, the Corrupted')
    
    dps_phase = 1
    
    for floor in range(1,4):
        print(f'Floor {floor}: Shuro Chi\'s Song (4:00)')
        
        # DPS Phase
        for altar in range(2):
            print('Pick up prism weapon and form a triangle to remove shield')
            print(f'DPS Phase {dps_phase}')
            if dps_phase == 6:
                print('Shuro Chi has been defeated!')
                input()
                return 0
            else:
                dps_phase += 1
                input()
        
        # Repeat until end of 3rd floor DPS phase (6th altar)
        if dps_phase == 6:
            print('Shuro Chi has been defeated!')
            input()
            return 0
        
        # Puzzle
        print('Puzzle:')
        puzzle_players = fireteam[:4]
        add_clear = fireteam[4:]
        
        puzzle_matrix = np.array(['O'] * 9)
        missing_indices = np.sort(np.random.choice(range(len(puzzle_matrix)), size=4, replace=False))
        puzzle_matrix[missing_indices] = ' '
        puzzle_matrix = puzzle_matrix.reshape(3, 3).tolist()

        for i in range(3):
            print(puzzle_matrix[i])
        player = np.random.randint(len(puzzle_players))
        platform_index = int(input(f'You are player {player + 1}. Facing the image, which platform should you step on (1-9)? ')) - 1
        if platform_index != missing_indices[player]:
            return light_fades()
        else:
            print('Continue to the next floor...')
            input()
    
def morgeth(fireteam):
    
    def reset_strength(fireteam):
        for p in fireteam:
            p.taken_strength = 0
        
    def print_strength(fireteam, total_strength):
        print('\nCurrent Taken Strength:')
        for p in fireteam:
            print(f'{p}: {p.taken_strength} stacks')
        print(f'Total Strength: {total_strength}')
        print()
        
    print('Encounter 3: Morgeth, the Spirekeeper')
    
    # Collect a total of 10 taken strength
    reset_strength(fireteam)
    total_strength = 0
    
    # Pick up initial strength
    fireteam[np.random.randint(len(fireteam))].taken_strength += 1
    total_strength += 1
    
    # Pick up next rounds of strengths (up to 5)
    for i in random.sample(list(range(len(fireteam))), (len(fireteam))):
        if fireteam[i].taken_strength == 0:
            fireteam[i].taken_strength += 1
            print(f'{fireteam[i]} has acquired taken strength')
            total_strength += 1
        if total_strength == 3:
            break
    for i in random.sample(list(range(len(fireteam))), (len(fireteam))):
        if fireteam[i].taken_strength == 0:
            for j in range(2):
                fireteam[i].taken_strength += 1
                print(f'{fireteam[i]} has acquired taken strength')
                total_strength += 1
        if total_strength == 5:
            break
    print_strength(fireteam, total_strength)
    
    trapped = int(input('Who needs to be freed using Taken Essence (1-6)? '))
    if fireteam[trapped - 1].taken_strength != 2:
        return light_fades()
    
    free = int(input('Who can free them? (1-6)? '))
    if fireteam[free - 1].taken_strength != 0:
        return light_fades()
    
    # Free trapped player, taking their strengths
    fireteam[trapped - 1].taken_strength, fireteam[free - 1].taken_strength = fireteam[free - 1].taken_strength, fireteam[trapped - 1].taken_strength
    print(f'p{free} has freed p{trapped}, taking their stacks!')
    print_strength(fireteam, total_strength)
    input()
    
    # Pick up next round of strengths (up to 7)
    for i in random.sample(list(range(len(fireteam))), (len(fireteam))):
        if fireteam[i].taken_strength == 0:
            for j in range(2):
                fireteam[i].taken_strength += 1
                print(f'{fireteam[i]} has acquired taken strength')
                total_strength += 1
            break
    
    print_strength(fireteam, total_strength)
    
    pickup = int(input('Who can pick up more taken strength (1-6)? ')) - 1
    if fireteam[pickup].taken_strength != 1:
        return light_fades()
    
    # Pick up next round of strengths (up to 9)
    for i in random.sample(list(range(len(fireteam))), (len(fireteam))):
        if fireteam[i].taken_strength == 1:
            fireteam[i].taken_strength += 1
            print(f'{fireteam[i]} has acquired taken strength')
            total_strength += 1
        if total_strength == 9:
            break
    
    # Free the next trapped player
    for i in random.sample(list(range(len(fireteam))), (len(fireteam))):
        if fireteam[i].taken_strength == 2:
            trapped = i + 1
            break
    for i in range(len(fireteam)):
        if fireteam[i].taken_strength == 0:
            free = i + 1
            break
    fireteam[trapped - 1].taken_strength, fireteam[free - 1].taken_strength = fireteam[free - 1].taken_strength, fireteam[trapped - 1].taken_strength
    print(f'p{trapped} is trapped! p{free} has freed p{trapped}, taking their stacks!')
    print_strength(fireteam, total_strength)
    input()
    
    # Pick up the final taken strength
    fireteam[trapped - 1].taken_strength += 1
    total_strength += 1
    print(f'p{trapped} has acquired the final taken strength')
    print_strength(fireteam, total_strength)
    input()
    
    # DPS
    print('DPS Phase')
    input()
    
    print('Repeat the stackening until...')
    input()
    print('Morgeth has been defeated!')
    input()

def vault(fireteam):
    print('Encounter 4: The Vault')
    
    rooms = ['Trees', 'Rocks', 'Stairs']
    room_map = {0: 'Trees', 1: 'Rocks', 2: 'Stairs'}
    
    np.random.seed(116)
    
    for round in range(3):
        print(f'Round {round + 1}:')
        
        # Set distinct umbral symbols for each area
        room_symbols = np.full((3, 3), '', dtype='<U30')
        symbols_shuffled = symbols.copy()
        random.shuffle(symbols_shuffled)
        for i in range(room_symbols.shape[0]):
            room_symbols[i, 1] = symbols_shuffled.pop() # Assign umbral symbols

        # Ensure true randomness/no bias for order of matched rooms to buffs
        room_indices = [0, 1, 2]
        random.shuffle(room_indices)
        
        # Place matching symbols
        placement_options = [0, 2] # penumbral or antumbral
        placements = np.random.choice(placement_options, size=3, replace=True)
        
        room_symbols[room_indices[0], placements[0]] = room_symbols[room_indices[1], 1]
        room_symbols[room_indices[1], placements[1]] = room_symbols[room_indices[2], 1]
        room_symbols[room_indices[2], placements[2]] = room_symbols[room_indices[0], 1]

        for i in range(room_symbols.shape[0]):
            for j in range(room_symbols.shape[1]):
                if room_symbols[i, j] == '':
                    room_symbols[i, j] = symbols_shuffled.pop()
    
        # Determine which buffs are required for each room
        buffs_required = {}
        for i in range(len(rooms)):
            placement = placements[room_indices.index(i)]
            buffs_required[room_map[i]] = 'penumbra' if placement == 0 else 'antumbra'
            
        # Save room symbols to dictionary for ease of handling
        symbols_dict = {room_map[i]: room_symbols[i] for i in range(3)}
        
        # Validate player buff choices
        for room in rooms:
            print(f'{room}: {symbols_dict[room]}')
        for room in rooms:
            guess = input(f'{room} required buff (penumbra or antumbra)? ').strip().lower()
            if guess != buffs_required[room]:
                return light_fades()
    
    print('\nSuccessfully opened the vault!')
    input()

def riven(fireteam):
    print('Encounter 5: Riven of a Thousand Voices')
    
    def num_to_eye(i):
        cases = {
            0: 'L2',
            1: 'R3',
            2: 'L5',
            3: 'L3',
            4: 'L1',
            5: 'R2',
            6: 'R4',
            7: 'L4',
            8: 'R1',
            9: 'R5'
        }
        return cases.get(i)
    
    def eye_sequence():
        print('Riven has appeared!')
        print('Damage Riven to stagger her')
        input()
    
        eyes = '      *     *\n *  *  *   *   * \n  *       *     *'
        
        # Randomize glowing eyes
        glowing = np.random.choice(10, size=2, replace=False)
        count = 0
        eyes_list = list(eyes)
        for i, c in enumerate(eyes_list):
            if c == '*':
                if count in glowing:
                    eyes_list[i] = 'o'
                count += 1
        eyes = ''.join(eyes_list)
        
        # Determine proper callout
        proper_callouts = []
        for i in glowing:
            proper_callouts.append(num_to_eye(i))
        print(eyes)
        # Assess proper callouts
        callouts = input('Provide the proper callout for Riven\'s glowing eyes (e.g. "L2R5"): ')
        if sorted(proper_callouts) != sorted([callouts[:2].upper(), callouts[2:4].upper()]):
            return 1
    
    def cleanse_sequence():
        # Determine symbol to cleanse
        print(f'Symbol to cleanse: {np.random.choice(symbols)}')
        input()
        
    def dps_sequence():
        # DPS Phase
        print('Shoot the Taken orb in Riven\'s mouth!')
        input()
        print('Riven has shut her mandible')
        print('Shoot the correct eyes or you will wipe!')
        input()
    
    # Assign players to blue or yellow room
    blue_players = fireteam[:3]
    yellow_players = fireteam[3:]
    
    # Aim for 2 damage phases
    for phase in range(2):
        print(f'Phase {phase + 1}:')
    
        for round in range(2):
            print(f'Bottom Level Round {round + 1}:')
            
            if np.random.randint(2) == 0:
                # Riven has appeared
                if eye_sequence():
                    return light_fades()
                # Cleanse
                cleanse_sequence()
            else:
                # Cleanse
                cleanse_sequence()
                # DPS Phase
                dps_sequence()
        
        print('Take the lift to the top level...')
        input()
        
        print('Complete 3 Riven stagger sequences, assigning an eye to each player')
        glowing = np.random.choice(10, size=6, replace=False)
        for i in range(len(fireteam)):
            fireteam[i].eye = num_to_eye(glowing[i])
            print(f'{fireteam[i]}: {fireteam[i].eye}')
        print('Each player shoots their assigned eye')
        input()
        
        print('Stand on plates to cleanse creeping darkness')
        for i in range(len(fireteam)):
            fireteam[i].cleansing_darkness = 0
        print('Shoot at Riven\'s weak spots on the way down!')
        input()
    
    print('You have been teleported to the Ascendant Realm')
    for i in range(len(fireteam)):
        fireteam[i].ascendant_atropy = True
    print('Journey to the Taken Strength node to cleanse Ascendant Atrophy')
    for i in range(len(fireteam)):
        fireteam[i].ascendant_atropy = False
    input()
    
    print('You have been teleported back to Riven')
    print('FINAL STAND')
    input()
    
    for i in range(len(fireteam)):
        fireteam[i].metaphysical_bleed = True
    print('Run down Riven\'s throat to destroy the Taken Blight')
    for i in range(len(fireteam)):
        fireteam[i].metaphysical_bleed = False
    input()
    
    print('Riven has been defeated!')
    input()

def queenswalk(fireteam):
    print('Encounter 6: The Queenswalk')
    
    random.shuffle(fireteam)
    
    first = fireteam.pop()
    print(f'Riven\'s Heart chooses {first}')
    print(f'{first} has been teleported to the dream world\n')
    
    for strength_num in range(len(fireteam) - 1):
        carrier = fireteam.pop()
        print(f'Riven\'s Heart chooses {carrier}')
        print(f'Each collect a Taken Strength ({strength_num + 1} Total) to refresh Fate\'s Chosen')
        input()
        print('Riven\'s Heart beats slower...')
        input()
        print(f'{carrier} has been teleported to the dream world\n')
    
    print('Dunk Riven\'s Heart')
    print('GGs')
    
def light_fades():
    print('YOUR LIGHT FADES AWAY...')
    input()
    return 1
    
if __name__ == '__main__':
    main()

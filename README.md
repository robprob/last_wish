# last_wish

A fully interactive Python simulation of the Last Wish raid from Destiny 2, featuring all six encounters with mechanics, randomized elements, and logic-based challenges. Designed for fun, practice, or reverse-engineering raid logic.

## Example Output:
```
Encounter 1: Kalli, the Corrupted
Plate Symbols: ['Down Snake', 'Down Snake', 'Left Fire', 'Left Fire', 'Up Bird', 'Up Bird']
Plate Assignments:
        p1: Down Snake
        p2: Down Snake
        p3: Left Fire
        p4: Left Fire
        p5: Up Bird
        p6: Up Bird

Plate:
[' ', '*', '*']
Choose a slice to stand on: 1
Total Taken Knights Killed: 6

DPS Phase (Repeat 3x):
Kalli conceives an ontological weapon  
DPS
Kalli prepares to wield her weapon     
Players hide behind stained glass doors

DPS Phase 1 complete

Plate Symbols: ['Infinity Snake', 'Infinity Snake', 'Left Spear', 'Left Spear', 'Standing Bird', 'Standing Bird']
Plate Assignments:
        p1: Infinity Snake
        p2: Infinity Snake
        p3: Left Spear
        p4: Left Spear
        p5: Standing Bird
        p6: Standing Bird

Plate:
['*', ' ', '*']
Choose a slice to stand on: 2
Total Taken Knights Killed: 6

DPS Phase (Repeat 3x):
Kalli conceives an ontological weapon
DPS
Kalli prepares to wield her weapon   
Players hide behind stained glass doors

DPS Phase 2 complete

Plate Symbols: ['Eight Snake', 'Eight Snake', 'Left Spear', 'Left Spear', 'Up Snake', 'Up Snake']
Plate Assignments:
        p1: Eight Snake
        p2: Eight Snake
        p3: Left Spear
        p4: Left Spear
        p5: Up Snake
        p6: Up Snake

Plate:
[' ', '*', '*']
Choose a slice to stand on: 1
Total Taken Knights Killed: 6

DPS Phase (Repeat 3x):
Kalli conceives an ontological weapon
DPS
Kalli prepares to wield her weapon
Players hide behind stained glass doors

DPS Phase 3 complete

Kalli has been defeated!

Encounter 2: Shuro Chi, the Corrupted
Floor 1: Shuro Chi's Song (4:00)
Pick up prism weapon and form a triangle to remove shield
DPS Phase 1

Pick up prism weapon and form a triangle to remove shield
DPS Phase 2

Puzzle:
['O', 'O', ' ']
['O', ' ', 'O']
[' ', 'O', ' ']
You are player 4. Facing the image, which platform should you step on (1-9)? 9
Continue to the next floor...

Floor 2: Shuro Chi's Song (4:00)
Pick up prism weapon and form a triangle to remove shield
DPS Phase 3

Pick up prism weapon and form a triangle to remove shield
DPS Phase 4

Puzzle:
[' ', ' ', ' ']
['O', 'O', 'O']
[' ', 'O', 'O']
You are player 2. Facing the image, which platform should you step on (1-9)? 2
Continue to the next floor...

Floor 3: Shuro Chi's Song (4:00)
Pick up prism weapon and form a triangle to remove shield
DPS Phase 5

Pick up prism weapon and form a triangle to remove shield
DPS Phase 6
Shuro Chi has been defeated!

Encounter 3: Morgeth, the Spirekeeper
p1 has acquired taken strength
p6 has acquired taken strength
p3 has acquired taken strength
p3 has acquired taken strength

Current Taken Strength:
p1: 1 stacks
p2: 0 stacks
p3: 2 stacks
p4: 0 stacks
p5: 1 stacks
p6: 1 stacks
Total Strength: 5

Who needs to be freed using Taken Essence (1-6)? 3
Who can free them? (1-6)? 2
p2 has freed p3, taking their stacks!

Current Taken Strength:
p1: 1 stacks
p2: 2 stacks
p3: 0 stacks
p4: 0 stacks
p5: 1 stacks
p6: 1 stacks
Total Strength: 5


p4 has acquired taken strength
p4 has acquired taken strength

Current Taken Strength:
p1: 1 stacks
p2: 2 stacks
p3: 0 stacks
p4: 2 stacks
p5: 1 stacks
p6: 1 stacks
Total Strength: 7

Who can pick up more taken strength (1-6)? 1
p6 has acquired taken strength
p5 has acquired taken strength
p5 is trapped! p3 has freed p5, taking their stacks!

Current Taken Strength:
p1: 1 stacks
p2: 2 stacks
p3: 2 stacks
p4: 2 stacks
p5: 0 stacks
p6: 2 stacks
Total Strength: 9


p5 has acquired the final taken strength

Current Taken Strength:
p1: 1 stacks
p2: 2 stacks
p3: 2 stacks
p4: 2 stacks
p5: 1 stacks
p6: 2 stacks
Total Strength: 10


DPS Phase

Repeat the stackening until...

Morgeth has been defeated!

Encounter 4: The Vault
Round 1:
Trees: ['Left Fire' 'Up Fish' 'Down Snake']
Rocks: ['Eight Snake' 'Down Snake' 'Double Fish']
Stairs: ['Up Bird' 'Eight Snake' 'Up Fish']
Trees required buff (penumbra or antumbra)? antumbra
Rocks required buff (penumbra or antumbra)? penumbra
Stairs required buff (penumbra or antumbra)? antumbra
Round 2:
Trees: ['Seaweed Fish' 'Left Spear' 'Eight Snake']
Rocks: ['Right Fire' 'Seaweed Fish' 'Up Snake']
Stairs: ['Left Spear' 'Up Snake' 'Up Bird']
Trees required buff (penumbra or antumbra)? penumbra
Rocks required buff (penumbra or antumbra)? antumbra
Stairs required buff (penumbra or antumbra)? penumbra
Round 3:
Trees: ['Seaweed Fish' 'Infinity Snake' 'Sitting Bird']
Rocks: ['Infinity Snake' 'Down Fish' 'Up Snake']
Stairs: ['Down Fish' 'Sitting Bird' 'Down Snake']
Trees required buff (penumbra or antumbra)? antumbra
Rocks required buff (penumbra or antumbra)? penumbra
Stairs required buff (penumbra or antumbra)? penumbra

Successfully opened the vault!

Encounter 5: Riven of a Thousand Voices
Phase 1:
Bottom Level Round 1:
Symbol to cleanse: Double Fish

Shoot the Taken orb in Riven's mouth!

Riven has shut her mandible
Shoot the correct eyes or you will wipe!

Bottom Level Round 2:
Symbol to cleanse: Right Spear

Shoot the Taken orb in Riven's mouth!

Riven has shut her mandible
Shoot the correct eyes or you will wipe!

Take the lift to the top level...

Complete 3 Riven stagger sequences, assigning an eye to each player
p1: R2
p2: R4
p3: R3
p4: L1
p5: L3
p6: L2
Each player shoots their assigned eye

Stand on plates to cleanse creeping darkness
Shoot at Riven's weak spots on the way down!

Phase 2:
Bottom Level Round 1:
Symbol to cleanse: Up Bird

Shoot the Taken orb in Riven's mouth!

Riven has shut her mandible
Shoot the correct eyes or you will wipe!

Bottom Level Round 2:
Riven has appeared!
Damage Riven to stagger her

      *     *
 *  *  *   *   o
  o       *     *
Provide the proper callout for Riven's glowing eyes (e.g. "L2R5"): L4R4
Symbol to cleanse: Right Spear

Take the lift to the top level...

Complete 3 Riven stagger sequences, assigning an eye to each player
p1: L1
p2: R1
p3: L4
p4: R2
p5: L2
p6: L5
Each player shoots their assigned eye

Stand on plates to cleanse creeping darkness
Shoot at Riven's weak spots on the way down!

You have been teleported to the Ascendant Realm
Journey to the Taken Strength node to cleanse Ascendant Atrophy

You have been teleported back to Riven
FINAL STAND

Run down Riven's throat to destroy the Taken Blight

Riven has been defeated!

Encounter 6: The Queenswalk
Riven's Heart chooses p1
p1 has been teleported to the dream world

Riven's Heart chooses p4
Each collect a Taken Strength (1 Total) to refresh Fate's Chosen

Riven's Heart beats slower...

p4 has been teleported to the dream world

Riven's Heart chooses p3
Each collect a Taken Strength (2 Total) to refresh Fate's Chosen

Riven's Heart beats slower...

p3 has been teleported to the dream world

Riven's Heart chooses p2
Each collect a Taken Strength (3 Total) to refresh Fate's Chosen

Riven's Heart beats slower...

p2 has been teleported to the dream world

Riven's Heart chooses p5
Each collect a Taken Strength (4 Total) to refresh Fate's Chosen

Riven's Heart beats slower...

p5 has been teleported to the dream world

Dunk Riven's Heart
GGs
```

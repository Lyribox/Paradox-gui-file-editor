# Importing required libraries
import fileinput

# gui variables
slotNumber = 99
coordVertical = 1177
coordHorizontal = 0

# Load the current descriptor to begin editing
with fileinput.FileInput('uiod_topbar_traditions_view.gui', inplace = True, backup ='.bak') as f:
    # Iterating line by line to edit
    for line in f:
        # Finds last line of slots and adds more according to specifications
        if 'name = "ap_99"' in line:
            print(line, end='')
            # 	positionType = { name = "ap_99" position = { x = 174  y = 1177 } }

            # Add 173 lines for slots
            while slotNumber < 172:
                slotNumber += 1
                if (slotNumber%4 == 0):# change coords at every multiple of 4 slot
                    coordVertical += 49
                    coordHorizontal = 29
                
                if (slotNumber%8 == 0):# change horizontal at every multiple of 8 slot
                    coordHorizontal = 0
                print(f'\tpositionType = {{ name = "ap_{slotNumber}" position = {{ x = {coordHorizontal}  y = {coordVertical} }} }}')

                coordHorizontal += 58

        else:
            print(line, end='')


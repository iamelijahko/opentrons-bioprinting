from opentrons import robot, labware, instruments

metadata = {
    'protocolName': 'S.S. - Slime Swatch',
    'author': 'Elijah Ko <elijah.ko@network.rca.ac.uk> / <hkk18@ic.ac.uk>',
    'description': 'Bioprinting with Opentrons. The code will print the double word "SLIME".'

# Speed of motor
max_speed_per_axis = {
    'x': 40,
    'y': 40,
    'z': 125,
    'a': 125,
    'b': 50,
    'c': 50
}

robot.head_speed(combined_speed=max(max_speed_per_axis.values()), **max_speed_per_axis)

# Labware
tiprack = labware.load('opentrons_96_tiprack_300ul', slot='10')
reservoir = labware.load('usascientific_12_reservoir_22ml', slot='11')
plate = labware.load('corning_96_wellplate_360ul_flat', slot='8')

# Pipette
pipette = instruments.P50_Multi(mount='right', tip_racks=[tiprack])

# 1st print: Letter 'S'
pipette.pick_up_tip(tiprack.wells('A1'))
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [161.37, 141.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [159.37, 145.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [154.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [148.37, 145.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [148.37, 145.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [147.37, 141.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [149.37, 138.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [161.37, 134.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [162.37, 130.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [162.37, 130.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [161.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [154.37, 123.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [150.37, 125.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [147.37, 128.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [146.37, 131.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 1st print: Letter 'L'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [170.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [170.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [184.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 1st print: Letter 'I'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [190.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [190.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 1st print: Letter 'M'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [206.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [206.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [206.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [216.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [216.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [225.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [225.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [225.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 1st print: Letter 'E'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [250.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37, 147.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37, 136.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [235.37, 136.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [250.37, 136.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37, 136.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [235.37, 136.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [235.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [250.37, 126.0, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 2nd print: Letter 'S'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

dev = 3.0

CALIBRATION_CROSS_COORDS = [161.37-dev, 141.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [159.37-dev, 145.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [154.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [148.37-dev, 145.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [148.37-dev, 145.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [147.37-dev, 141.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [149.37-dev, 138.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [161.37-dev, 134.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [162.37-dev, 130.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [162.37-dev, 130.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [161.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [154.37-dev, 123.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [150.37-dev, 125.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [147.37-dev, 128.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [146.37-dev, 131.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 2nd print: Letter 'L'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [170.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [170.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [184.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 2nd print: Letter 'I'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [190.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [190.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 2nd print: Letter 'M'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [206.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [206.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [206.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [216.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [216.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [225.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [225.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [225.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

# 2nd print: Letter 'E'
pipette.aspirate(50, reservoir.cols('1'))
pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [250.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37-dev, 147.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37-dev, 136.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [235.37-dev, 136.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [250.37-dev, 136.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37-dev, 136.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [235.37-dev, 136.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [235.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.dispense(5, plate.wells('A1'))

CALIBRATION_CROSS_COORDS = [235.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

CALIBRATION_CROSS_COORDS = [250.37-dev, 126.0-dev, -2.0]
pipette.move_to((robot.deck, CALIBRATION_CROSS_COORDS))

pipette.blow_out(reservoir.cols('1'))

pipette.drop_tip(tiprack.wells('A1'))
from pyDHM import utilities
from pyDHM import phaseShifting

# Phase shifting using the SOSR approach

print("SOSR example")
# Load the holograms
inp0 = utilities.imageRead('test2.png')
inp1 = utilities.imageRead('test3.png')
inp2 = utilities.imageRead('test4.png')
inp3 = utilities.imageRead('test2.png')

# Phase shifting using the SOSR approach
output = phaseShifting.SOSR(inp0, inp1, inp2, inp3, True, 632.8e-9, 6.9e-6, 6.9e-6, 1, 4)

# Display the amplitude reconstruction
amplitude = utilities.amplitude(output, False)
utilities.imageShow(amplitude, 'SOSR - Amplitude reconstruction')

# Display the phase reconstruction
phase = utilities.phase(output)
utilities.imageShow(phase, 'SOSR - Phase reconstruction')


# Phase shifting via ps5-inline

print("ps5-inline example")
inp0 = utilities.imageRead('pic65.jpg')
inp1 = utilities.imageRead('pic66.jpg')
inp2 = utilities.imageRead('pic67.jpg')
inp3 = utilities.imageRead('pic68.jpg')
inp4 = utilities.imageRead('pic69.jpg')

# Phase shifting via ps5 ()
output = phaseShifting.PS5(inp0, inp1, inp2, inp3, inp4)
phase = utilities.phase(output)

# Display the phase reconstruction
utilities.imageShow(phase, 'ps5-inline - Phase reconstruction')


# Phase shifting via ps4-inline

print("ps4-inline example")
inp0 = utilities.imageRead('p70.jpg')
inp1 = utilities.imageRead('p71.jpg')
inp2 = utilities.imageRead('p72.jpg')
inp3 = utilities.imageRead('p73.jpg')

# Phase shifting via ps4 ()
output = phaseShifting.PS4(inp0, inp1, inp2, inp3)
phase = utilities.phase(output)

# Display the phase reconstruction
utilities.imageShow(phase, 'ps4-inline - Phase reconstruction')


# Phase shifting via ps3-inline

print("ps3-inline example")
inp0 = utilities.imageRead('p90.jpg')
inp1 = utilities.imageRead('p91.jpg')
inp2 = utilities.imageRead('p92.jpg')

# Phase shifting via ps3 ()
output = phaseShifting.PS3(inp0, inp1, inp2)
phase = utilities.phase(output)

# Display the phase reconstruction
utilities.imageShow(phase, 'ps3-inline - Phase reconstruction')


# three blind raw Holograms

print("BPS3 example")
# Load the holograms
inp0 = utilities.imageRead('p45.jpg')
inp1 = utilities.imageRead('p46.jpg')
inp2 = utilities.imageRead('p47.jpg')

# Resize inp1 to match the shape of inp0
inp1 = utilities.imageResize(inp1, inp0.shape[1], inp0.shape[0])

utilities.imageShow(inp0, 'Hologram 1')
utilities.imageShow(inp1, 'Hologram 2')
utilities.imageShow(inp2, 'Hologram 3')

# Phase shifting via BPS3 (three holograms slightly off-axis)
output = phaseShifting.BPS3(inp2, inp1, inp0, 0.532, 2.4, 2.4)

# Display the phase reconstruction
phase = utilities.phase(output)
utilities.imageShow(phase, 'BPS3 - Phase reconstruction')


# two blind raw Holograms

print("BPS2 example")
# Load the holograms
# inp0 = utilities.imageRead('data/phase-shifting samples/Neuron_1.jpg')
# inp1 = utilities.imageRead('data/phase-shifting samples/Neuron_3.jpg')
inp0 = utilities.imageRead('p14.jpg')
inp1 = utilities.imageRead('spic2.jpg')

# Resize inp1 to match the shape of inp0
inp1 = utilities.imageResize(inp1, inp0.shape[1], inp0.shape[0])

# Phase shifting via BPS2 (two holograms slightly off-axis)
output = phaseShifting.BPS2(inp1, inp0, 0.532, 2.4, 2.4)

# Display the phase reconstruction
phase = utilities.phase(output)
utilities.imageShow(phase, 'BPS2 - Phase reconstruction')

plt.show()














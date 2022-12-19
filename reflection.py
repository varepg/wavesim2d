import numpy as np
from wavesim2d import WaveSim2d


def phaseshift(x, theta_r, wavelength):
    return (2*np.pi / wavelength * np.sin(theta_r) * x) #% (2*np.pi)


def setup(L, xres, disc, theta_r, wavelength):
    sim = WaveSim2d((-10, 10), (0,20))

    x0 = -L/2
    x1 = L/2

    sources = np.linspace(x0, x1, xres)

    dx = (x1-x0) / disc
    xdisc = np.linspace(x0 + dx/2, x1 - dx/2, disc)
    phases = [phaseshift(x-x0, theta_r, wavelength) for x in xdisc]

    i = 0
    for x in sources:
        if x-x0 > (i+1)*dx:
            i+=1
        phase = phases[i]
        sim.add_source(x, 0, wavelength, phase)

    return sim
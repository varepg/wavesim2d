import numpy as np
import reflection


def main():
    wavelength = 1
    L = 2*wavelength
    xres = 10*L
    disc = int(5*L)
    theta_r = np.pi/4

    sim = reflection.setup(L, xres, disc, theta_r, wavelength)

    sim.plot()


if __name__ == "__main__":
    main()
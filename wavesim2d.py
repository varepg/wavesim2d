import numpy as np
import matplotlib.pyplot as plt


class WaveSim2d:
    def __init__(self, xlim, ylim, xres=1000, yres=1000):
        self._x = np.linspace(xlim[0], xlim[1], xres)
        self._y = np.linspace(ylim[0], ylim[1], yres)
        self._X, self._Y = np.meshgrid(self._x, self._y)
        self._sources = {}

    @staticmethod
    def _r(x, y):
        return np.sqrt(x*x + y*y)

    def add_source(self, x, y, wavelength, phase=0):
        k = 2*np.pi / wavelength
        X0 = x*np.ones(np.shape(self._X))
        Y0 = y*np.ones(np.shape(self._Y))
        r = self._r(self._X-X0, self._Y-Y0)
        self._sources[(x,y)] = np.cos(k*r+phase)
    
    def remove_source(self, x, y):
        self._sources.pop((x, y))

    def clear_sources(self):
        self._sources = {}

    def plot(self, savepath=""):
        res = np.zeros(np.shape(self._X))

        for source in self._sources.values():
            res += source

        plt.imshow(
            res,
            origin="lower",
            extent=[
                np.min(self._x),
                np.max(self._x),
                np.min(self._y),
                np.max(self._y)
                ]
            )

        if savepath:
            plt.savefig(savepath)

        plt.show()

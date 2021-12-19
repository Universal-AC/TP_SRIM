import numpy as np
from srim.output import Results
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

linestyles = lss = [
    ('solid', (0, ())),

    # ('loosely dotted', (0, (1, 10))),
    ('dotted', (0, (1, 1))),
    ('densely dotted', (0, (1, 1))),

    # ('loosely dashed', (0, (5, 10))),
    ('dashed', (0, (5, 5))),
    ('densely dashed', (0, (5, 1))),

    ('loosely dashdotted', (0, (3, 10, 1, 10))),
    ('dashdotted', (0, (3, 5, 1, 5))),
    ('densely dashdotted', (0, (3, 1, 1, 1))),

    ('dashdotdotted', (0, (3, 5, 1, 5, 1, 5))),
    ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
    ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]

plt.rcParams.update({'font.size': 14})

res_path = os.path.realpath(__file__)
print(res_path+'\srim_output')
data = Results('C:\\Users\\Mathis\\Desktop\\TP_SRIM\\Alpha in UO2\\srim_output')

def plot_ioniz(res):
    ioniz = res.ioniz
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Depth (Angstroem)')
    ax.set_ylabel(r'eV/Angstroem')
    ax.plot(ioniz.depth, ioniz.ions, label='Ionization from Ions')
    ax.plot(ioniz.depth, ioniz.recoils, label='Ionization from Recoils')
    plt.legend()
    plt.tight_layout()
    fig.savefig('ionization.pdf')
    plt.close(fig)


def plot_etorecoils(res):
    etorecoils = res.etorecoils
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Depth (Angstroem)')
    ax.set_ylabel(r'eV/Angstroem')
    ax.plot(etorecoils.depth, etorecoils.ions, label='Energy from Ions')
    #ax.plot(etorecoils.depth, etorecoils.recoils, label='Ionization from Recoils')
    plt.legend()
    plt.tight_layout()
    fig.savefig('etorecoils.pdf')
    plt.close(fig)


def plot_etorecoils(res):
    etorecoils = res.etorecoils
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Depth (Angstroem)')
    ax.set_ylabel(r'eV/Angstroem')
    ax.plot(etorecoils.depth, etorecoils.ions, label='Energy from Ions')
    #ax.plot(etorecoils.depth, etorecoils.recoils, label='Ionization from Recoils')
    plt.legend()
    plt.tight_layout()
    fig.savefig('etorecoils.pdf')
    plt.close(fig)


def plot_range(res):
    range = res.range
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Depth (Angstroem)')
    ax.set_ylabel(r'Number')
    ax.plot(range.depth, range.ions, label='Ions range')
    plt.legend()
    plt.tight_layout()
    fig.savefig('range.pdf')
    plt.close(fig)


plot_ioniz(data)
plot_etorecoils(data)
plot_range(data)

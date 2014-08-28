from __future__ import division,print_function
import os,os.path
import numpy as np
import pkg_resources

import pandas as pd

from . import isochrones as iso

DATADIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

MASTERFILE = '{}/dartmouth.h5'.format(DATADIR)

#MASTERFILE = os.path.expanduser('~/.isochrones/dartmouth/dartmouth.h5')

class Dartmouth_Isochrone(iso.Isochrone):
    def __init__(self,feh=0,bands=['U','B','V','R','I','J','H','K','g','r','i','z','Kepler','D51']):
        store = pd.HDFStore(MASTERFILE)
        df = store[iso.fehstr(feh)]

        for band in bands:
            try:
                mags[band] = df[band]
            except:
                if band == 'kep' or band == 'Kepler':
                    mags[band] = df['Kp']
                else:
                    raise
        
        iso.Isochrone.__init__(self,log10(df['age']*1e9),df['M'],df['M'],df['logL'],
                           10**df['logTeff'],df['logg'],mags)

    
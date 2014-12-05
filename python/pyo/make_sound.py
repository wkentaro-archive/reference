#-*- coding: utf-8 -*-
# make_sound.py
from pyo import *

def make_sound():
    s = Server().boot()
    s.start()
    wav = SquareTable()
    env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
    met = Metro(.125, 12).play()
    amp = TrigEnv(met, table=env, mul=.1)
    pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
    out = Osc(table=wav, freq=pit, mul=amp).out()
    s.gui(locals())


if __name__ == '__main__':
    make_sound()

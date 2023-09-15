#!/usr/bin/env python3

from pyhackrf2 import HackRF
import numpy as np

hackrf = HackRF()


def get_gps_signal():
    hackrf.center_freq = 1575420000
    hackrf.sample_rate = 2.5e6
    samples = hackrf.read_samples(int(1e6))
    print(len(samples))


def get_hackrf_devices():
    print(HackRF.enumerate())


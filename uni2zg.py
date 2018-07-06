# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input
    output = output.replace(u'\u106A', u'\u1009')
    #  nyalay

    output = output.replace(u'\u1033', u'\u102F')
    #  1chaungngin

    output = output.replace(u'\u1034', u'\u1030')
    #  2chaungngin

    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')
    #  hahtoe

    output = output.replace(u'\u103C', u'\u103D')
    #  waswe

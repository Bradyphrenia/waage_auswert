#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os


def main():
    pfad = '/Users/steffen/Desktop/'
    trans(pfad)


def trans(pfad):
    dateiliste = os.listdir(pfad)
    datensatz = dict()
    datentuple = tuple
    with open(pfad + 'data.json', 'r') as daten:
        datensatz = json.load(daten)
    with open(pfad + 'waage.sql', 'w') as wrt:
        for item in datensatz:
            datentuple = datensatz[item]
            wrt.write(
                'INSERT INTO gewichte (datum,volk,gewicht,einheit) VALUES (' + "'" + item + "'" + ',' + "'" + 'Volk 006' + "'" + "," +
                str(datentuple[7]) + "," + "'" + 'kg' + "'" + ');\n')
    return 0


if __name__ == "__main__":
    main()

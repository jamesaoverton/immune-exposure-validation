#!/usr/bin/env python3

import argparse, os, csv, re

mappings = {
    'Influenza A H1N1 2009 Monovalent Vaccine Novartis': 'Influenza A (H1N1) 2009 Monovalent Vaccine (Novartis)',
    'administration': 'administering substance in vivo',
    'transplant / transfusion': 'transplant or transfusion',
    'disease': 'occurrence of disease',
    'infectious disease': 'occurence of infectious disease',
    'allergic disease': 'occurrence of allergic disease',
    'autoimmune disease': 'occurrence of autoimmune disease',
    'cancer': 'occurrence of cancer',
    'exposure (without disease)': 'exposure to substance without evidence for disease',
    'asymptomatic infection/colonization': 'occurence of asymptomatic infection',
    'exposure with immune reactivity': 'exposure with existing immune reactivity without evidence for disease',
    'exposure with documentation': 'documented exposure without evidence for disease',
    'exposure to endemic/ubiquitous agent': 'environmental exposure to endemic/ubiquitous agent without evidence for disease',
    '2366': 'DOID:2366',
    '1316510': 'NCBITaxon:1316510',
    '12206': 'DOID:12206',
    'Dengue hemorrhagic fever': 'dengue hemorrhagic fever',
    '64320': 'NCBITaxon:64320',
    'NCBI:txid11103': 'NCBITaxon:11103',
    'NCBI:txid31708': 'NCBITaxon:31708',
    '12365': 'DOID:12365',
    '60478': 'DOID:0060478',
    'Hepatitis C Virus': 'Hepacivirus C',
    'Trivalent inactivated influenza': '2008-2009 trivalent influenza vaccine',
    'Meningococcal Polysaccharide Vaccine': 'Meningococcal Polysaccharide Vaccine, Groups A & C, Menomune A/C',
    'Tuberculosis': 'tuberculosis',
    'NA': ''
}

parser = argparse.ArgumentParser(
    description='Convert immune_exposure.txt to CSV and update')
parser.add_argument('input',
    type=str,
    help='The immune_exposure.txt file to read')
parser.add_argument('output',
    type=str,
    help='The immune_exposure.csv file to write')
args = parser.parse_args()

with open(args.output, 'w') as o:
  w = csv.writer(o, lineterminator='\n')
  with open(args.input, 'r') as i:
    rows = csv.reader(i, delimiter='\t')
    first = next(rows)
    if first[0] == 'immuneexposure':
      w.writerow(next(rows))
      w.writerow([
        "",
        "",
        "",
        "is-required; subclass-of 'exposure process';",
        "subclass-of 'exposure material'; is-required (when %4 subclass-of ('administering substance in vivo' or 'exposure to substance without evidence for disease' or 'occurrence of infectious disease' or 'occurrence of allergic disease')); is-excluded (when %4 equivalent-to 'occurrence of disease'); is-excluded (when %4 subclass-of ('occurrence of autoimmune disease' or 'occurrence of cancer' or 'no exposure' or unknown))",
        "equivalent-to %5",
        "subclass-of 'disease'; subclass-of 'has material basis in' some %5 (when %4 subclass-of not ('occurrence of autoimmune disease' or 'occurrence of cancer'));is-required (when %4 subclass-of disease); is-excluded (when %4 equivalent-to 'administering substance in vivo'); is-excluded (when %4 subclass-of (vaccination or 'transplant or transfusion' or 'exposure to substance without evidence for disease' or 'no exposure' or unknown))",
        "equivalent-to %7",
        "subclass-of 'disease stage'; is-required (when %4 subclass-of disease); is-excluded (when %4 subclass-of not disease)"
      ])
    else:
      w.writerow(first)
      w.writerow([
        "",
        "",
        "equivalent-to %5",
        "", # "equivalent-to %5",
        "subclass-of 'disease'; subclass-of 'has material basis in' some %10 (when %11 subclass-of not ('occurrence of autoimmune disease' or 'occurrence of cancer'));is-required (when %11 subclass-of disease); is-excluded (when %11 equivalent-to 'administering substance in vivo'); is-excluded (when %11 subclass-of (vaccination or 'transplant or transfusion' or 'exposure to substance without evidence for disease' or 'no exposure' or unknown))",
        "subclass-of 'disease stage'; is-required (when %11 subclass-of disease); is-excluded (when %11 subclass-of not disease)",
        "",
        "equivalent-to %10",
        "", # "equivalent-to %10",
        "subclass-of 'exposure material'; is-required (when %11 subclass-of ('administering substance in vivo' or 'exposure to substance without evidence for disease' or 'occurrence of infectious disease' or 'occurrence of allergic disease')); is-excluded (when %11 equivalent-to 'occurrence of disease'); is-excluded (when %11 subclass-of ('occurrence of autoimmune disease' or 'occurrence of cancer' or 'no exposure' or unknown))",
        "is-required; subclass-of 'exposure process';",
        "",
        ""
      ])
    for row in rows:
      values = []
      for cell in row:
        cell = re.sub(' ; .*', '', cell)
        if cell in mappings:
          values.append(mappings[cell])
        else:
          values.append(cell.replace('_',':'))
      w.writerow(values)

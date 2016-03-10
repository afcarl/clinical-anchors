import string
from warnings import warn
from collections import defaultdict
import sys

def insert_decimal(code):
  prefix = ''
  if code[0] == 'E':
    prefix = 'E'
  code = code.strip('E') 
  front = code[:3]
  back = code[3:]
  if len(back) == 0:
    return prefix+front
  else:
    return prefix+front+'.'+back
  
mapper = {}
mapper['icd9'] = defaultdict(lambda: '?')

try:
  code_file = file('CMS32_DESC_LONG_DX.txt')
  for l in code_file:
    l = l.strip()
    code, name = string.split(l, maxsplit=1)
    code = insert_decimal(code)
    mapper['icd9'][code]=name
except:
  warn('could not load icd9 code reference')

mapper['gsn'] = defaultdict(lambda: '?')
try:
  gsn_file = file('RXNCONSO.RRF')
  for l in gsn_file:
    l = l.split('|')
    src=l[11]
    if src != 'NDDF':
      continue

    rxcui = l[0]
    gsn = l[13]
    name = l[14]
    mapper['gsn'][gsn] = name
except:
  warn('could not load RXNORM reference')

for l in file(sys.argv[1]):
  if '--' in l:
    print l.strip()
    continue
  source, code = l.strip().split('|')
  if 'mdcomments' in source or 'triage' in source:
    disp = '|'.join([source, code])
    print disp
    continue

  elif 'med' in source:
    print '|'.join([source, code, mapper['gsn'][code]])

  elif 'icd9' in source:
    print '|'.join([source, code, mapper['icd9'][code]])


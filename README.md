Anchor Specifications
=====================

This repository holds the lists of anchors used the paper:

_Electronic Medical Record Phenotyping using the Anchor & Learn Framework_

by Halpern, Horng, Choi, Sontag 2015

For each condition there is a file that contains a list of anchors in the format:

`source|identifier`

possible sources are:
* ICD9 billing codes (icd9)
* medication history (med history)
* dispensed medications (med dispensed)
* MD comments (mdcomments)
* Triage assessment (triage)



Human readable names
--------------------

To translate the identifiers to human readable names, we suggest that users download the following reference files:

* CMS32\_DESC\_LONG\_DX.txt -- download [here](https://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/Downloads/ICD-9-CM-v32-master-descriptions.zip)
* RXNCONSO.RRF -- available as part of the RXNORM package. More info [here](https://www.nlm.nih.gov/research/umls/rxnorm/). [Download page](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html). Requires a license which can be requested [here](https://uts.nlm.nih.gov//license.html).

The medication identifiers are GSN codes from First Databank (source name NDDF in RxNorm), which are only availble in the full releases of RxNorm.

The python script display.py uses the above reference files to add human readable names to every anchor. 

Usage: `python display.py condition_file`

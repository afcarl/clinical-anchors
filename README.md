Anchor Specifications
=====================

This repository holds the lists of anchors used the paper:

Electronic Medical Record Phenotyping using the Anchor & Learn Framework

Halpern, Horng, Choi, Sontag 2015

For each condition there is a file that contains a list of anchors in the format:

source|identifier

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
* RXNCONSO.RRF -- available as part of the RXNORM package. More info [here](https://www.nlm.nih.gov/research/umls/rxnorm/)

import mutation,mutationDao,mutationUnit,cancerTypeUnit
import json
from datetime import date

from bravado.client import SwaggerClient
cbioportal = SwaggerClient.from_url('https://www.cbioportal.org/api/api-docs',
                                    config={"validate_requests":False,"validate_responses":False})
print(cbioportal)

for a in dir(cbioportal):
    cbioportal.__setattr__(a.replace(' ', '_').lower(), cbioportal.__getattr__(a))

dir(cbioportal)

with open("study_list.json", encoding="utf-8") as s:
    study_lists = json.load(s)

for study_list in study_lists:
    cancer_type = cancerTypeUnit.get_cancer(cbioportal,study_list)
    mutation_list = mutationUnit.get_mutation_list(cbioportal,study_list + "_mutations",study_list + "_all")

    for a in mutation_list:
        if a:
            hugo_symbol = a.gene.hugoGeneSymbol
            protein_change = a.proteinChange
            mutation_type = a.mutationType
            refseq_mrna_id = a.refseqMrnaId
            tumor_alt_count = a.tumorAltCount
            tumor_ref_count = a.tumorRefCount
            study_id = study_list
            sample_id = a.sampleId
            create_time = date.today()
            update_time = date.today()
            status = 1
            par = (cancer_type,hugo_symbol,protein_change,mutation_type,refseq_mrna_id,tumor_alt_count,tumor_ref_count,study_id,sample_id,create_time,update_time,status)
            if mutationDao.do_sql_insert(par):
                print("insert false in " + study_list + " where mutation is " + a.gene.hugoGeneSymbol + "," + a.proteinChange + "," + a.mutationType)

    print("Successfully insert data in study_list:" + study_list)
    print(mutationDao.do_sql_count("mutations"))

mutationDao.close_sql_connection()


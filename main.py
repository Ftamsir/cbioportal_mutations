import mutationDao,mutationUnit,cancerTypeUnit
import json
from datetime import date
import time

from bravado.client import SwaggerClient
cbioportal = SwaggerClient.from_url('https://www.cbioportal.org/api/api-docs',
                                    config={"validate_requests":False,"validate_responses":False})
print(cbioportal)

for a in dir(cbioportal):
    cbioportal.__setattr__(a.replace(' ', '_').lower(), cbioportal.__getattr__(a))

dir(cbioportal)

with open("study_list.json", encoding="utf-8") as s:
    study_lists = json.load(s)

start = time.time()
page = 1
# pars = []
cancer_time = 0
try:
    # for study_list in study_lists:

    # mutation_list = mutationUnit.get_mutation_list(cbioportal,study_list + "_mutations",study_list + "_all")

    mutation_list = mutationUnit.get_mutation_list_by_page(cbioportal, "ccle_broad_2019_mutations", "ccle_broad_2019_all", page, 5500)

    for a in mutation_list:
        if a:
            hugo_symbol = a.gene.hugoGeneSymbol
            protein_change = a.proteinChange
            mutation_type = a.mutationType
            refseq_mrna_id = a.refseqMrnaId
            tumor_alt_count = a.tumorAltCount
            tumor_ref_count = a.tumorRefCount
            # study_id = study_list
            study_id = "ccle_broad_2019"
            sample_id = a.sampleId
            create_time = date.today()
            update_time = date.today()
            status = 1

            cancer_start = time.time()
            cancer_type = cancerTypeUnit.get_cancer_type(cbioportal,"ccle_broad_2019",sample_id)
            cancer_end = time.time()
            cancer_time += cancer_end - cancer_start

            par = (cancer_type,hugo_symbol,protein_change,mutation_type,refseq_mrna_id,tumor_alt_count,tumor_ref_count,study_id,sample_id,create_time,update_time,status)
            # pars.append(par)
            if mutationDao.do_sql_insert(par):
                print("insert false in " + "ccle_broad_2019" + " where mutation is " + a.gene.hugoGeneSymbol + "," + a.proteinChange + "," + a.mutationType)

    print(str(len(int(cancer_time))))
    # print("Successfully insert data in study_list: " + study_list + " by page " + str(page))
    print("Successfully insert data in study_list: " + "ccle_broad_2019" + " by page " + str(page))
    print(mutationDao.do_sql_count("mutations"))
    end = time.time()
    used_time = str((end - start)/60)
    print(used_time)

except Exception as e:
    print(e)
    print("Failed in insert data now_id: " + str(mutationDao.do_sql_count("mutations")))

finally:
    mutationDao.close_sql_connection()



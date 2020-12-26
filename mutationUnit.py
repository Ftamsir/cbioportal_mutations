def get_mutation_list(s,molecular_profile_id,sample_list_id):
    mutations = s.mutations.getMutationsInMolecularProfileBySampleListIdUsingGET(
        direction="DESC",
        molecularProfileId=molecular_profile_id, # {study_id}_mutations gives default mutations profile for study
        sampleListId=sample_list_id, # {study_id}_all includes all samples
        projection="DETAILED",#include gene info
    ).result()

    return mutations

def get_mutation(s):
    mutation = dir(s)
    return mutation
mutation = dict.fromkeys(
    ["id","hugo_symbol","protein_change","refseq_mrna_id","tumor_alt_count","tumor_ref_count","study_id","sample_id","create_time","update_time","status"],
    ["","","","","","","","","","",""])

def set_mutation(hugo_symbol, protein_change, mutation_type, refseq_mrna_id, tumor_alt_count, tumor_ref_count, study_id, sample_id, create_time, update_time, status):
    mutation['hugo_symbol'] = hugo_symbol
    mutation['protein_change'] = protein_change
    mutation['mutation_type'] = mutation_type
    mutation['refseq_mrna_id'] = refseq_mrna_id
    mutation['tumor_alt_count'] = tumor_alt_count
    mutation['tumor_ref_count'] = tumor_ref_count
    mutation['study_id'] = study_id
    mutation['sample_id'] = sample_id
    mutation['create_time'] = create_time
    mutation['update_time'] = update_time
    mutation['status'] = status

    return mutation
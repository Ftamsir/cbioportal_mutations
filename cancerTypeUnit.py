def get_cancer_type(s,study_id,sample_id):
    cancer_type = s.Clinical_Data.getAllClinicalDataOfSampleInStudyUsingGET(
        attributeId = 'CANCER_TYPE_DETAILED',
        sampleId = sample_id,
        studyId = study_id,
    ).result()[0].value

    return cancer_type
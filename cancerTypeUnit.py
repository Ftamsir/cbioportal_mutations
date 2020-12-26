def get_cancer(s,study_id):
    cancer = s.Studies.getStudyUsingGET(
        studyId = study_id
    ).result().cancerType.name

    return cancer
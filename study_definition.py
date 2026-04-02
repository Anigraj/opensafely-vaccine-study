from cohortextractor import StudyDefinition, patients

study = StudyDefinition(
    population=patients.satisfying("age >= 18"),

    age=patients.age_as_of("2020-01-01"),

    vaccinated=patients.with_tpp_vaccination_record(
        returning="binary_flag"
    ),

    covid_positive=patients.with_these_clinical_events(
        ["COVID_CODE"],
        returning="binary_flag"
    )
)

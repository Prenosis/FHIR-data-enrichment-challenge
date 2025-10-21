# FHIR Data Enrichment Challenge

## Dataset
You are provided with a FHIR dataset containing [Observations](https://build.fhir.org/observation.html) and [MedicationAdministrations](https://build.fhir.org/medicationadministration.html) for nine synthetic patient encounters. `example.py` demonstrates how to access the data store. 

## Task
Your task is to calculate SOFA (Sequential Organ Failure Assessment) scores for each patient over the course of a hospital encounter.  

The SOFA score quantifies the severity of organ dysfunction based on lab and vital measurements and other patient characteristics, evaluating six organ systems:  
- Cardiovascular  
- Central Nervous System (CNS)  
- Respiratory  
- Kidney  
- Liver  
- Coagulation  

The overall SOFA score is the sum of the individual scores for these six components.

Many different methods exist for calculating SOFA scores. For this project, you should use the scoring criteria from **The Third International Consensus Definition of Sepsis** [Table T1](https://pmc.ncbi.nlm.nih.gov/articles/PMC4968574/table/T1/), along with a few extra rules:

- **Measurement Validity:** Laboratory and vital sign measurements are valid for up to 6 hours after their effective time.  
- **Data Completeness:** A SOFA score can only be calculated if data for all six organ system components are available.  
- **Default FiO₂:** If not specified, assume an inspired oxygen concentration (FiO₂) of 21%, the oxygen content of room air.  
- **PaO₂ Substitution:** If PaO₂ data is unavailable, use the **SpO₂/FiO₂ ratio** instead of the PaO₂/FiO₂ ratio with these cutoffs:  
  - Score 0: >302  
  - Score 1: <302  
  - Score 2: <221  
  - Score 3: <142 (with respiratory support)  
  - Score 4: <67 (with respiratory support)

Your submission should contain a `main.py` or `main.R` file that, when executed, generates `submission.csv` in the main working directory with three columns: `patient_id`, `sofa_score_datetime`, `sofa_score`. The submission file should contain a row for all valid SOFA scores for all 9 patients.

All code should be written in Python or R. Your submission should include dependency management, as needed, for reproducibility.

## Assessment Criteria
Submissions will be evaluated based on the following:

**Data Processing Framework**: FHIR data is designed to be highly expressive, which can make it difficult to use for data analysis. Your framework should transform the raw FHIR data in a way that makes it practical to use for SOFA score calculation, and for data analysis broadly.

**Accuracy**: The calculated SOFA scores should be correct and consistent with the scoring system.

**Code Quality**: Your code should be clean, readable, and maintainable.


## Submission
1. Push your solution to a private GitHub repo.
2. Add `leeschmalz` to the repository.
3. Include the link to your private GitHub repo in the associated screening question when you apply to the [active job posting]([https://www.todo.com](https://prenosis.com/careers/#job-2305120)).

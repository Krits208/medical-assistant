import pandas as pd
import numpy as np

# Define sample data
doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Brown", "Dr. Jones"]
specialties = ["Cardiology", "Dermatology", "Neurology", "Orthopedics", "Pediatrics"]
diseases = [
    "Psoriasis", "Asthma", "Diabetes", "Arthritis", "Hypertension",
    "Eczema", "Bronchitis", "Osteoporosis", "Migraine", "Obesity",
    "Anemia", "Cancer", "Gout", "Alzheimer's", "Parkinson's",
    "Influenza", "Allergies", "Depression", "Anxiety", "Stroke",
    "Chronic kidney disease", "Heart disease", "Pneumonia", "Tuberculosis",
    "Hepatitis", "HIV/AIDS", "Osteoarthritis", "Rheumatoid arthritis", "Fibromyalgia",
    "Multiple sclerosis", "COPD", "Endometriosis", "Glaucoma", "Cataracts",
    "Macular degeneration", "Diabetic retinopathy", "Gingivitis", "Periodontitis", "Celiac disease",
    "Crohn's disease", "Ulcerative colitis", "Diverticulitis", "Gastritis", "GERD",
    "Peptic ulcer disease", "Pancreatitis", "Gallstones", "Hemorrhoids", "Hepatitis B",
    "Hepatitis C", "Herpes", "Shingles", "Lupus", "Scleroderma",
    "Epilepsy", "Migraine", "Trigeminal neuralgia", "Tourette syndrome", "Autism spectrum disorder",
    "ADHD", "Bipolar disorder", "Schizophrenia", "PTSD", "OCD",
    "Eating disorders", "Sleep disorders", "Restless leg syndrome", "Narcolepsy", "Insomnia",
    "Sleep apnea", "Tinnitus", "Vertigo", "Meniere's disease", "Chronic fatigue syndrome",
    "Fibromyalgia", "Hypothyroidism", "Hyperthyroidism", "Diabetic neuropathy", "Peripheral neuropathy",
    "ALS", "Muscular dystrophy", "Cystic fibrosis", "Huntington's disease", "Myasthenia gravis",
    "Sickle cell disease", "Thalassemia", "Leukemia", "Lymphoma", "Melanoma",
    "Breast cancer", "Prostate cancer", "Colon cancer", "Lung cancer", "Pancreatic cancer"
]

# Generate random doctor's names, specialties, and diseases
data = {
    "Doctor's Name": np.random.choice(doctors, size=200),
    "Specialty": np.random.choice(specialties, size=200),
    "Disease": np.random.choice(diseases, size=200)
}

# Create a dataframe
df = pd.DataFrame(data)

# Save dataframe to CSV
df.to_csv('doctor_dataset.csv', index=False)

print("Dataset saved as 'doctor_dataset.csv'")

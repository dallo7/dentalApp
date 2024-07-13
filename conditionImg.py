listofDisease = ['Tooth Decay (Cavities)', 'Gingivitis (Early Gum Disease)',
                 'Periodontitis (Advanced Gum Disease)', 'Enamel Erosion',
                 'Dentin Hypersensitivity', 'Oral Thrush', 'Canker Sores',
                 'Cold Sores (Fever Blisters)', 'Impacted Tooth',
                 'Wisdom Tooth Pain', 'Bruxism (Teeth Grinding)',
                 'Temporomandibular Joint Disorder (TMJ)', 'Xerostomia (Dry Mouth)',
                 'Angular Cheilitis (Cracked Corners of Mouth)', 'Leukoplakia',
                 'Geographic Tongue', 'Burning Mouth Syndrome', 'Pericoronitis',
                 'Gingival Hyperplasia', 'Category',
                 'Gum Disease (Periodontal Disease)', 'Oral Cancer',
                 'Developmental Abnormalities', 'Fungal Infections',
                 'Dental Condition', 'Tooth Erosion', 'Attrition', 'Abfraction',
                 'Cracked Tooth Syndrome', 'Chipped or Broken Tooth',
                 'Dental Abscess', 'Missing Teeth', 'Misaligned Teeth',
                 'Excessive Tooth Spacing', 'Overbite', 'Underbite', 'Open Bite',
                 'Crossbite']

dictofDisease = {'Tooth Decay (Cavities)': 'img/tooth decay cavity.jpeg',
                 'Gingivitis (Early Gum Disease)': 'img/Gingivitis (Early Gum Disease).jpeg',
                 'Periodontitis (Advanced Gum Disease)': 'img/Periodontitis (Advanced Gum Disease).jpeg',
                 'Enamel Erosion': 'img/Enamel Erosion.jpeg',
                 'Dentin Hypersensitivity': 'img/Dentin Hypersensitivity.jpeg', 'Oral Thrush': 'img/Oral Thrush.jpeg',
                 'Canker Sores': 'img/Canker Sores.jpeg',
                 'Cold Sores (Fever Blisters)': 'img/Cold Sores (Fever Blisters).jpeg',
                 'Impacted Tooth': 'img/Impacted Tooth.jpeg',
                 'Wisdom Tooth Pain': 'img/Wisdom Tooth Pain.jpeg',
                 'Bruxism (Teeth Grinding)': 'img/Bruxism (Teeth Grinding).jpeg',
                 'Temporomandibular Joint Disorder (TMJ)': 'img/Temporomandibular Joint Disorder (TMJ).jpeg',
                 'Xerostomia (Dry Mouth)': 'img/Xerostomia (Dry Mouth).jpeg',
                 'Angular Cheilitis (Cracked Corners of Mouth)': 'img/Angular Cheilitis (Cracked Corners of Mouth).jpeg',
                 'Leukoplakia': 'img/Leukoplakia.jpeg',
                 'Geographic Tongue': 'img/Geographic Tongue.jpeg',
                 'Burning Mouth Syndrome': 'img/Burning Mouth Syndrome.jpeg', 'Pericoronitis': 'img/Pericoronitis.jpeg',
                 'Gingival Hyperplasia': 'img/Gingival Hyperplasia.jpeg',
                 'Gum Disease (Periodontal Disease)': 'img/Gum Disease (Periodontal Disease).jpeg',
                 'Oral Cancer': 'img/Oral Cancer.jpeg',
                 'Developmental Abnormalities': 'img/Developmental Abnormalities.jpeg',
                 'Fungal Infections': 'img/Fungal Infections.jpeg',
                 'Dental Condition': 'img/Dental Condition.jpeg', 'Tooth Erosion': 'img/Tooth Erosion.jpeg',
                 'Attrition': 'img/Attrition.jpeg', 'Abfraction': 'img/Abfraction.jpeg',
                 'Cracked Tooth Syndrome': 'img/Cracked Tooth Syndrome.jpeg',
                 'Chipped or Broken Tooth': 'img/Chipped or Broken Tooth.jpeg',
                 'Dental Abscess': 'img/Dental Abscess.jpeg', 'Missing Teeth': 'img/Missing Teeth.jpeg',
                 'Misaligned Teeth': 'img/Misaligned Teeth.jpeg',
                 'Excessive Tooth Spacing': 'img/Excessive Tooth Spacing.jpeg', 'Overbite': 'img/Overbite.jpeg',
                 'Underbite': 'img/Underbite.jpeg', 'Open Bite': 'img/Open Bite.jpeg',
                 'Crossbite': 'img/Crossbite.jpeg'}

toothdamage = [
    "Pain, sensitivity, discoloration, visible holes",
    "Sensitivity, smooth or pitted tooth surface",
    "Sharp pain in response to hot, cold, or sweet stimuli",
    "Toothache, sensitivity, visible holes, staining",
    "Damage to tooth enamel and dentin",
    "Loss of tooth enamel due to acid wear",
    "Tooth wear due to grinding or clenching",
    "Tooth wear at the gumline",
    "Sharp pain when biting or chewing",
    "Pain, sensitivity, jagged edge"
]

gumIssues = [
    "Red, inflamed gums, bleeding gums",
    "Receding gums, loose teeth, bad breath",
    "Swollen, red, or tender gums, bleeding gums",
    "Gingivitis symptoms + loose teeth, receding gums, pus",
    "Inflammation of gums and supporting bone",
    "Inflammation of gum tissue around erupting wisdom tooth",
    "Overgrowth of gum tissue"
]

oralInfectionsAbnormalities = [
    "White patches on tongue or inner cheeks",
    "Painful ulcers on soft tissues",
    "Fluid-filled blisters near lips, burning, tingling",
    "White patches inside mouth, may be precancerous",
    "Smooth, red patches on tongue with raised white borders",
    "Burning sensation in mouth, no visible cause",
    "Fungal growth in the mouth (thrush)",  # Added "thrush" for clarity
    "Abnormal cell growth in the mouth"
]

toothEruptionAlignment = [
    "Unerupted or partially erupted tooth, pain, swelling",
    "Tooth fails to erupt normally (impacted tooth)",
    "Gaps in teeth (diastema)",
    "Crooked or crowded teeth (malocclusion)",
    "Large gaps between teeth (diastema)",
    "Upper front teeth significantly overlap lower teeth (overbite)",
    "Lower front teeth protrude in front of upper teeth (underbite)",
    "Vertical space between upper and lower front teeth when biting (open bite)",
    "Upper teeth bite inside lower teeth on one or both sides (crossbite)",
]

jawIssuesTeethGrinding = [
    "Teeth wear, jaw pain, headaches",
    "Jaw pain, clicking or popping sounds, difficulty chewing",
    "Unconscious grinding or clenching of teeth (bruxism)",
    "Pain in jaw joint, headaches, and difficulty chewing",
]
mouthSoresDifficultySwallowing = [
    "Dryness, difficulty speaking or swallowing",
    "Cracks at corners of mouth (angular cheilitis), burning, bleeding",
    "Mouth sore that won’t heal (chronic canker sore) , lump in mouth/neck, white/red patches on gums/tongue, difficulty swallowing",
]
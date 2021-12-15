# COVID19FakeNewsClassifier
Classify the COVID19 Fake news from the LIAR-PLUS dataset (https://github.com/Tariq60/LIAR-PLUS) using the ADABoost

# Train.py 
Takes the dataset as the tsv file in the Database folder. Use the CountVectorizer to count amount of words relating to each class. Drop some unnecessary features ("justification", "speaker", "context" and count of each classes for a person) that has a low chi-square. Train using the ADABoost.

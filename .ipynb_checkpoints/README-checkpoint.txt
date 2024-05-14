There are many notebooks where different preprocessing steps were tried out and the data was inspected. These are irrelevant. All relevant, cleaned code is in the folder'final version'

All notebooks have markdown where the steps and the rationale behind each step is explained.

The seeds that were used are in the folder final_version/seeds.

SCRAPING: 
    run 'final_version/scripts/minetmerge.py'
        Requires a .txt file with the channels to scrape; it

    This was done for the first two seeds 
    3rd seed: ‘final_version/notebooks/Datenänderung.ipynb’ to determine how many more channels to scrape on the basis of the first two iterations
    then run the script again with the third seed

TEXT ANALYSIS
    Preprocessing:
        'final_version/notebooks/BERTopic_separatemodels.ipynb'
            Here I tried out which preprocessing steps to take

        ‘final_version/notebooks/Preprocessing20March.ipynb’
            Actual preprocessing that was used for the model that was adopted; here the path to the scripts for text cleaning in the scripts folder may need to be adjusted since this was initially executed with SSP Datalab.


NETWORK ANALYSIS
    'final_version/notebooks/networkanal_8april.ipynb'
        For testing how the network functions and how best to visualise it
    ‘final_version/notebooks/network_guillaume.ipynb’ 
        For the actual network graphics visualised in the findings


TOPIC MODEL
    'final_version/notebooks/BERT one large model.ipynb
        Creation of BERTopic model and identification of the relevant topics for furtheranalysis; aggregation of topics

    'final_version/notebooks/topic_graphs.ipynb'
        Analysis of topics; topics through network, regex

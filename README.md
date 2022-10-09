# Generic Real Estate Consulting Project
Groups should generate their own suitable `README.md`.
#### Document description and project instruction is in the [summary_notebook.ipynb](./notebook/summary_note_book.ipynb).


### Project Background
Improving living standards has boosted people's requirements for a living environment. For many people, selecting an cost-effective property has become a complicated problem. Companies and individuals who want to invest in real estate may also hesitate because of uncertainty about the direction of the properties' prices and the return on Investment (ROI). 


### Code Structure
For scipts dir
  
    dataset_dowload.py                                  downloads all dataset used in project.
    convert_xls_to_csv.py                               convert all XLS file to CSV file.
    scrape.py                                           scrape the properties' link.
    scrape2.py                                          scrape the properties' information.
    GLM.Rmd                                             GLM R markdown script
 
For notebooks dir
    
    analysis.ipynb                                      preview datasets
    distance_to_CBD.ipynb                               find property distance to CBD
    distance_to_school.ipynb                            find property distance to cloest school
    distance_to_train_station.ipynb                     find property distance to cloest train station
    GLM.pdf                                             GLM R markdown output
    hospital_and_school_count.ipynb                     preview hospital and school datasets
    income.ipynb                                        find suburb income
    population_for_suburb.ipynb                         find suburb population
    population_forcast.ipynb                            find suburb population projection in next 3 years
    predict_model.ipynb                                 the predict model for suburb average rental price
    preprocess_crime.ipynb                              preprocess crime dataset
    preprocess_property_1.ipynb                         preprocess property dataset stage 1
    preprocess_property_2.ipynb                         preprocess property dataset stage 2
    preprocess_suburb.ipynb                             preprocess suburb data
    random_forest_for_feature_importance.ipynb          random forest regression model for feature importance
    random_forest_for_prediction.ipynb                  random forest regression model for property rental price prediction
    rating_features.ipynb                               rate suburbs and find most affordable and liveable suburb
    summary_notebook.ipynb                              summary notebook for this project, demonstrate the overall approach and project instructions.
    visualization.ipynb                                 some visualization used in summary notebook and presentation.
    

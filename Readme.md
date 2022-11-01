# A Dynamic Risk Assessment System

This project deploys an API that serves a risk assessment ML model that will help a company to predict and monitor their attrition risks 


## Project Steps Overview

### Data ingestion. 

Automatically check wheither new data is available for model training. Compile all training data and save it a given storage location. Defne metrics for ingestion process

### Training, scoring, and deploying. 
This step comprises three scripts. One script is for training an ML model, another is for generating scoring metrics for the model, and the third is for deploying the trained model.

### Diagnostics. 
In this step, a script is written that performs diagnostic tests related to your model as well as your data
### Reporting. 
In this step, scripts create reports related to your ML model, its performance, and related diagnostics.An API is setup using app.py so that  ML diagnostics and results can be easily accessed 

### Process Automation. 

A script and cron job is created that will automatically run all previous steps at regular intervals.
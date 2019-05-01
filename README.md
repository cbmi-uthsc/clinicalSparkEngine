# clinicalSparkEngine
Apache spark streaming analytic engine for predicting patient deterioration using physiological data

Engine consists of two parts
- Prediction model generator and evaluator (module `model`)
- Spark engine itself (module `engine`)

### Model
At this early stage real deterioration data is not provided, 
but there are many physiological realtime datasets on the web, so for
a proof-of-concept I selected [The University of Queensland Vital Signs Dataset](https://outbox.eait.uq.edu.au/uqdliu3/uqvitalsignsdataset/index.html).  

I chose 6 features (heart rate, blood ox. saturation, blood pressure etc.). The task is to predict end-tidal sevoflurane 
concentration that patient will have next second.
 
Dataset processing, model training and exporting is done in Jupyter Notebook (`model/notebooks/predict-etSEV.ipynb`). 
For this task I used linear regression with Tensorflow. Achieved accuracy is >99.99%, so linear methods are more than sufficient for this problem.

### Engine
For sake of brevity, engine operates on data received through socket and prints predictions to stdout.

## Usage
- launch a server
```bash
nc -l 9999
```
- launch the engine
```bash
./run_clinical_engine.sh
``` 
- feed some data (to netcat)
```bash
0.73469388 1.0 0.80851064 0.77011494 0.45238095 0.5952381 0.24137931 0.37037037
```

## TODO
- add separate script for training and exporting model
- add real datasource and datasink (e.g. Kafka topic and RDBMS)
- serve exported model with Tensorflow Serving
- wrap engine and TF Serving in Docker images and add a deploy script
- fault tolerance
- tests
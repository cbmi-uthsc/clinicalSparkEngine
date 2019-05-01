from pyspark import SparkContext
from pyspark.streaming import StreamingContext

import model


class Engine:
    def __init__(self, model_dir):
        self.model_dir = model_dir

    def run(self):
        # spark context
        sc = SparkContext(appName="deteriorationPredictor")
        ssc = StreamingContext(sc, 1)

        # socket server
        lines = ssc.socketTextStream('localhost', 9999)

        # split incoming line and feed to the predictor
        pred = lines. \
            map(lambda line: [float(n) for n in line.split(' ')]). \
            map(lambda sample: model.ModelLoader.get(self.model_dir).predict(sample))

        # print the prediction
        pred.pprint()

        ssc.start()
        ssc.awaitTermination()

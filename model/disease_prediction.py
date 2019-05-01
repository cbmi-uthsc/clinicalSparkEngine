import tensorflow as tf
from tensorflow.contrib import predictor as prd

COLUMNS = ['HR', 'SpO2', 'etCO2', 'NBPMean', 'etSEV', 'inSEV', 'inO2', 'RR']

x = [0.73469388, 1., 0.80851064, 0.77011494, 0.45238095, 0.5952381, 0.24137931, 0.37037037]
y = 0.45238095238095233
input_x = {col: [x] for col, x in zip(COLUMNS, x)}


class ClinicalPredictor:
    def __init__(self, pred_fn):
        self.static_pred_fn = pred_fn

    @staticmethod
    def convert_to_example(sample):
        feature = {}
        for col, value in zip(COLUMNS, sample):
            feature[col] = tf.train.Feature(float_list=tf.train.FloatList(value=[value]))
        example = tf.train.Example(
            features=tf.train.Features(
                feature=feature
            )
        )
        return example.SerializeToString()

    def predict(self, sample: list):
        return self.static_pred_fn({'inputs': [self.convert_to_example(sample)]})['outputs'][0]


class ModelLoader:
    predictor = None

    @staticmethod
    def get(export_dir='model/export/1554673286'):
        if not ModelLoader.predictor:
            ModelLoader.predictor = ClinicalPredictor(prd.from_saved_model(export_dir=export_dir))
        return ModelLoader.predictor

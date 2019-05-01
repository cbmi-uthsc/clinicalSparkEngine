import argparse

parser = argparse.ArgumentParser("clinicalSparkEngine",
                                 description="Apache spark streaming analytic engine for predicting patient "
                                             "deterioration using physiological data")

parser.add_argument("model", nargs='?', default='model/export/1554673286',
                    help="Directory where predictor is saved")

args = parser.parse_args()

# import guts after argument parsing to make it more responsive (tf imports too long)
import engine

eng = engine.Engine(args.model)
eng.run()

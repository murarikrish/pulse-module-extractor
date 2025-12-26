import json
import argparse
from module_extractor.pipeline import ModuleExtractionPipeline

parser = argparse.ArgumentParser()
parser.add_argument("--urls", nargs="+", required=True)
args = parser.parse_args()

pipeline = ModuleExtractionPipeline()
result = pipeline.run(args.urls)

print(json.dumps(result, indent=2))


# Motivation

The purpose of this project is to test the capabilities of openai image generation in anticipation for another project to come further down the road.

# Environment Variables

There is a single environment variable needed to run `image_generation_update.py`. This is solely the `OPENAI_API_KEY` from your openai API project. The variable is automatically detected by the openai client, so it doesn't need to directly passed as an argument as long as environemnt variables are loaded into the workspace before instantiating `client = OpenAI()`.

# Executing Project

To run the image generation script you need have [Pixi](https://pixi.sh/latest/installation/) installed on your system and run `pixi install` in the top level directory. Then you can simply run `pixi run python .\scripts\image_generation_update.py` on windows or `pixi run python ./scripts/image_generation_update.py` on mac.
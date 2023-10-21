#
# Program that grabs models that generate text
# and uses it to generate shopping links

import google.generativeai as palm

# Get the list of models
for m in palm.list_models():
    print(f"name: {m.name}")
    print(f"description: {m.description}")
    print(f"generation methods:{m.supported_generation_methods}\n")

models = [m for m in palm.list_models()
          if 'generateText'
          in m.supported_generation_methods]

# Grab the first one that can has the generateText method
model_bison = models[0]

# print(model_bison)

# Define the generate_text method
from google.api_core import retry
@retry.Retry()
def generate_text(prompt,
                  model=model_bison,
                  temperature=0.0):
    return palm.generate_text(prompt=prompt,
                              model=model,
                              temperature=temperature)

# Example prompt that generates shopping links
prompt = "List the best GPU laptops on Amazon.com and include the urls"
completion = generate_text(prompt)
print(completion.result)

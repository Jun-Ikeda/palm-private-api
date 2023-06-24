import pprint
import google.generativeai as palm

palm.configure(api_key='AIzaSyCiW4RWz9wQaazXK0N9BUtXAM43wOvjIqY')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

prompt = """
Today is Friday, June 23rd, 2023.
What day is it next Wednesday?
"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)
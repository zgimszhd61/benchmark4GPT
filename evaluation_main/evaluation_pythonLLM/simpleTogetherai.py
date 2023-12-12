import together
together.api_key = ""
output = together.Complete.create(
  prompt = "<human>: What are Isaac Asimov's Three Laws of Robotics?\n<bot>:", 
  model = "mistralai/Mixtral-8x7B-Instruct-v0.1", 
  max_tokens = 256,
  temperature = 0.8,
  top_k = 60,
  top_p = 0.6,
  repetition_penalty = 1.1,
  stop = ['<human>', '\n\n']
)

# print generated text
print(output['output']['choices'][0]['text'])

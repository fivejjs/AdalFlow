import adalflow as adal

llama_llm = adal.Generator(
   model_client=adal.OllamaClient(), model_kwargs={"model": "qwen3-vl:235b-cloud"}
)
response = llama_llm(prompt_kwargs={"input_str": "What is LLM?"})
print(response.data)
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Model name
model_name = "ml6team/keyphrase-generation-keybart-inspec"

# Save the model and tokenizer locally
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save model and tokenizer to a local directory
model.save_pretrained("./keywordsGeneration-model")
tokenizer.save_pretrained("./keywordsGeneration-tokenizer")

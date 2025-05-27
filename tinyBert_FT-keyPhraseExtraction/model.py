from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("nirusanan/tinyBert-keyword")
model = AutoModelForTokenClassification.from_pretrained("nirusanan/tinyBert-keyword")

# Save model and tokenizer to a local directory
model.save_pretrained("./keywordsGeneration-model")
tokenizer.save_pretrained("./keywordsGeneration-tokenizer")

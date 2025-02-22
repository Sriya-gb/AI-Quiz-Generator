
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

#  Force use of SentencePiece instead of Tiktoken
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

#  Save locally
model.save_pretrained("mcq_model")
tokenizer.save_pretrained("mcq_model")

print("Model and tokenizer saved successfully!")

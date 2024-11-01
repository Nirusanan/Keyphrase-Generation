from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from typing import List
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class TextInput(BaseModel):
    text: str


class KeyphraseGenerationPipeline:
    def __init__(self, model: str, tokenizer: str, keyphrase_sep_token=";"):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        self.keyphrase_sep_token = keyphrase_sep_token

    def generate_keyphrases(self, text: str) -> List[str]:
        inputs = self.tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        outputs = self.model.generate(**inputs)
        decoded = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        keyphrases = [phrase.strip() for phrase in decoded[0].split(self.keyphrase_sep_token) if phrase.strip()]
        return keyphrases


pipeline = KeyphraseGenerationPipeline(
    model="./keywordsGeneration-model",
    tokenizer="./keywordsGeneration-tokenizer"
)

# Add CORS Middleware to allow access from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers, like Content-Type
)


@app.post("/generate-keyphrases/")
async def generate_keyphrases(input_text: TextInput):
    keyphrases = pipeline.generate_keyphrases(input_text.text)
    return {"keyphrases": keyphrases}


if __name__ == "__main__":
    # Start the server with Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
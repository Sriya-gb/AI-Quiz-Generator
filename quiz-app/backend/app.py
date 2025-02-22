from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

# ✅ Load model from local directory instead of downloading
MODEL_PATH = "./mcq_model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

class MCQRequest(BaseModel):
    text: str
    num_questions: int = 5

@app.post("/generate-mcq/")
async def generate_mcq(request: MCQRequest):
    prompt = f"""
    Generate {request.num_questions} multiple-choice questions from the given passage.

    Passage: {request.text}

    Each question should have **one correct answer** and **three incorrect but plausible distractors**.

    Format each question as follows:
    Q: [Question]
    A) [Incorrect Option]
    B) [Incorrect Option]
    C) [Correct Option]
    D) [Incorrect Option]
    Correct Answer: C
    """

    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=512, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract and process questions
    mcqs = generated_text.split("\n")
    final_mcqs = []

    for mcq in mcqs:
        if mcq.startswith("Q:"):
            question = mcq
            options = []
        elif mcq.startswith(("A)", "B)", "C)", "D)")):
            options.append(mcq)
        elif mcq.startswith("Correct Answer"):
            correct_option = mcq.split(":")[-1].strip()

            # Ensure all options are unique (replacing duplicates if needed)
            unique_options = list(set(options))
            if len(unique_options) < 4:
                unique_options += ["(Incorrect Placeholder)"] * (4 - len(unique_options))

            final_mcqs.append(f"{question}\n" + "\n".join(unique_options) + f"\nCorrect Answer: {correct_option}")

    return {"mcqs": "\n\n".join(final_mcqs)}



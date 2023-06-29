import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, set_seed
from transformers import GPT2LMHeadModel, GPT2Tokenizer

#output_path = r"C:\Users\ilknur\Desktop\GPT-2\model"
output_path = r"..\GPT-2\model"  # The directory where the trained model was saved
tokenizer = GPT2Tokenizer.from_pretrained(output_path)
model = GPT2LMHeadModel.from_pretrained(output_path)

class Request(BaseModel):
    prompt: str
    max_tokens_to_generate: int
    
class Response(BaseModel):
    prompt: str
    max_tokens_to_generate: int
    generated_text: str

# declaring FastAPI instance
app = FastAPI()

@app.get("/")
async def status():
    return {"api_status": "OK"}


 
@app.post('/generate', response_model=Response)
async def generate(request: Request) -> Response:
    
    input_ids = tokenizer.encode(request.prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=request.max_tokens_to_generate, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_text2 = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return Response(
        prompt = request.prompt,
        max_tokens_to_generate = request.max_tokens_to_generate,
        generated_text = generated_text2
        )
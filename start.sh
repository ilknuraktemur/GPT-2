# get trained model from drive link
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=142O0NY0nmXnvgkHuCUxluygRfrE330VC' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=142O0NY0nmXnvgkHuCUxluygRfrE330VC" -O model.zip && rm -rf /tmp/cookies.txt
#unzip model file to model folder
unzip model.zip -d model
#To run the FastAPI web server
uvicorn FastAPI:app --reload

#To generate text according to the prompt we write and max tokens value we give
curl -X 'POST' \
  'http://127.0.0.1:8000/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "such a beautiful day",
  "max_tokens_to_generate": 50
}'
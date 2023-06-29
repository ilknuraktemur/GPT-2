## Text Generation GPT-2
### Project Description
The goal of this project is to fine-tune the GPT-2 model on the works of Shakespeare and deploy this fine tuned model on Linux using Fast API. 
### Steps

- pre-trained GPT-2 model was fine tuned with input from Shakespeare works. You can access this input from the data folder in the repo.
- Then this trained model was saved in Google Drive for later use.
- In the next step, a python application was created for this model using the FastAPI framework. You can access it from the FastAPI.py file.
- Then a bash script was created to run this application on the Linux. This script is the file named start.sh in the repo.
- After installing the required dependencies specified in the requirement.txt file, the trained model in the drive is accessed using wget, after downloading the model, there are the required commands to run the FastAPI web server in start.sh script.
- After all steps you can generate text according to the prompt you want using the curl tool.(these commands are also in start.sh )

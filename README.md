## Text Generation GPT-2
Project Description:
The goal of this project is to fine-tune the GPT-2 model on the works of Shakespeare and deploy this fine tuned model on Linux using Fast API. 

- When creating this repo, a pre-trained GPT-2 model was first fine tuned with input from Shakespeare works. You can access this input from the data folder.
- This trained model was then saved in Google Drive for later use.
- In the next step, a python application was created for this model using the FastAPI framework. FastAPI to this application code. You can access it from the py file.
- Then a bash script was created to run this application in the Linux environment. This script is the file named start.sh in the repo.
- After installing the required dependencies specified in the requirement.txt file, the trained model in the drive is reached with the help of wget, then there are the required commands to run the FastAPI web server. 
- After all steps you can generate text according to the prompt you want using the curl tool.(these commands are in start.sh )

AI Image Generation Program
This repository contains code for an AI image generation program built in Python. Follow the instructions below to run the program either in Google Colab or locally on your machine.

Running in Google Colab
Open the Google Colab notebook: Link
Change the runtime to use a T4 GPU:
Click on Runtime in the menu.
Select Change runtime type.
Choose GPU and select T4 from the dropdown.
Simply run the code cells in the notebook to generate images.
Running Locally
To run the program locally, follow these steps:

Install Python: Make sure you have Python installed on your machine. You can download it from python.org.

Install CUDA (if you have an NVIDIA GPU):

Follow the instructions on the NVIDIA CUDA Toolkit page to install CUDA.
Create and Activate a Virtual Environment:

python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
Install Requirements:

Clone this repository and navigate to the directory:
git clone <repository-url>
cd <repository-directory>
Install the required packages:
pip install -r requirements.txt
Install PyTorch:

Install PyTorch by following the instructions on the PyTorch website. Make sure to select the appropriate options for your system.
Create a Hugging Face Account:

Go to Hugging Face and create an account.
Get a Hugging Face Access Token:

After logging in, go to your account settings and generate an access token.
Run Hugging Face CLI:

huggingface-cli login
Paste your access token when prompted.
Request Access to High End Models

Some mode;s require you accept their license agreements. If you plan to use the newest stable diffusion model you must accept the license here.
Choose the Script to Run:

You can choose to run either 2-1.py or 3-5.py:
2-1.py: Suitable for most systems.
3-5.py: Requires a high-end GPU and takes nearly 50 times longer to run.
Conclusion
Follow these steps to successfully set up and run the AI image generation program. If you encounter any issues, please refer to the documentation or open an issue in the repository.
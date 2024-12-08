# AI Image Generation Program

This repository contains code for an AI image generation program built in Python. Follow the instructions below to run the program either in Google Colab or locally on your machine.

## Running in Google Colab

1. Open the Google Colab notebook: [Link](https://colab.research.google.com/drive/123ZtMp35m_5ITFdkdJ1aDeakxZHwbf_2?usp=sharing)
2. Change the runtime to use a T4 GPU:
   - Click on `Runtime` in the menu.
   - Select `Change runtime type`.
   - Choose `GPU` and select `T4` from the dropdown.
3. Simply run the code cells in the notebook to generate images.

## Running Locally

To run the program locally, follow these steps:

1. **Install Python**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install CUDA** (if you have an NVIDIA GPU):
   - Follow the instructions on the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) page to install CUDA.

3. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```
   
4. **Install Requirements**:
   - Clone this repository and navigate to the directory:
     ```bash
     git clone <repository-url>
     cd <repository-directory>
     ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```
5. **Install PyTorch**:
   - Install PyTorch by following the instructions on the [PyTorch website](https://pytorch.org/get-started/locally/). Make sure to select the appropriate options for your system.

6. **Create a Hugging Face Account**:
   - Go to [Hugging Face](https://huggingface.co/) and create an account.

7. **Get a Hugging Face Access Token**:
   - After logging in, go to your account settings and generate an access token.

8. **Run Hugging Face CLI**:
   ```bash
   huggingface-cli login
   ```
   - Paste your access token when prompted.

9. **Request Access to High End Models**
   - Some mode;s require you accept their license agreements. If you plan to use the newest stable diffusion model you must accept the license [here](https://huggingface.co/stabilityai/stable-diffusion-3.5-large).

10. **Choose the Script to Run**:
   - You can choose to run either `2-1.py` or `3-5.py`:
     - `2-1.py`: Suitable for most systems.
     - `3-5.py`: Requires a high-end GPU and takes nearly 50 times longer to run.

## Conclusion

Follow these steps to successfully set up and run the AI image generation program. If you encounter any issues, please refer to the documentation or open an issue in the repository.

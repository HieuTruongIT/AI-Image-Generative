import torch
from diffusers import  StableDiffusion3Pipeline

large_model = "stabilityai/stable-diffusion-3.5-large"

pipe = StableDiffusion3Pipeline.from_pretrained(large_model, torch_dtype=torch.bfloat16)
pipe.enable_attention_slicing()
pipe = pipe.to("cuda")

prompt = "a programmer touching grass"

results = pipe(
    prompt,
    num_inference_steps=20,
    guidance_scale=3.5,
    height=512,
    width=512
)

images = results.images

# Save or display the images
for i, img in enumerate(images):
    img.save(f"image_{i}.png")  # Save each image
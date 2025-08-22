from openai import OpenAI
import base64
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = """

1. Analyze the Image: Examine the original image to understand its composition, color palette, and key elements.
2. Study Studio Ghibli Style: Familiarize yourself with the distinctive features of Studio Ghibli's art style, including: - Soft, vibrant color palettes - Detailed backgrounds with a focus on nature - Expressive character designs with large, emotive eyes - Use of light and shadow to create depth
3. Sketch the Transformation: Create a preliminary sketch that incorporates the Ghibli style elements into the original image.
4. Apply Color and Texture: Use soft, vibrant colors typical of Studio Ghibli films. Pay attention to textures that mimic traditional animation techniques.
5. Refine Details: Add intricate details to the background and characters, ensuring they align with the Ghibli aesthetic.
6. Final Adjustments: Make any necessary adjustments to lighting, contrast, and saturation to achieve a cohesive look.

"""


def encode_image(file_path):
    with open(file_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode("utf-8")
    return base64_image


base64_image1 = encode_image("inputs/kitty.jpeg")

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image1}",
                },
            ],
        }
    ],
    tools=[{"type": "image_generation", "size": "1024x1024"}],
)

image_generation_calls = [
    output for output in response.output if output.type == "image_generation_call"
]

image_data = [output.result for output in image_generation_calls]

if image_data:
    image_base64 = image_data[0]
    with open("outputs/kitty.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
else:
    print(response.output.content)


# try:
#     img = Image.open("inputs/kitty.jpeg").convert("RGBA")
#     img.save("inputs/kitty.png")
#     print("Image successfully converted to PNG.")
# except FileNotFoundError:
#     print("Error: The input image file was not found.")
#     exit()

from google import genai
from config import *
from templates import PROMPT_TEMPLATE

client = genai.Client(api_key=API_KEY)


def generate_copy(
        product_name,
        description,
        platform,
        tone,
        temperature,
        top_p):

    prompt = PROMPT_TEMPLATE.format(
        product_name=product_name,
        description=description,
        platform=platform,
        tone=tone
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "temperature": temperature,
            "top_p": top_p
        }
    )

    generated_text = response.text

    with open("output.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "="*50 + "\n")
        file.write(generated_text)
        file.write("\n")

    return generated_text
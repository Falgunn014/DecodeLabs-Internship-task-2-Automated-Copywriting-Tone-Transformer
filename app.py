from copywriter import generate_copy

print("=" * 60)
print("AI Copywriter & Tone Transformer")
print("=" * 60)

product_name = input("Product Name: ")

description = input("Product Description: ")

platform = input(
    "Platform (LinkedIn/Instagram/Email): "
)

tone = input(
    "Tone (Professional/Casual/Friendly/Luxury): "
)

temperature = float(
    input(
        "Temperature (0.0 - 1.0): "
    )
)

top_p = float(
    input(
        "Top P (0.0 - 1.0): "
    )
)

print("\nGenerating Copy...\n")

result = generate_copy(
    product_name,
    description,
    platform,
    tone,
    temperature,
    top_p
)

print(result)
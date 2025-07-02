from config import app_config
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

def __image2text(image, word_count, creativity):
    """Generates a short description of the image"""
    try:
        # Load the BLIP model and processor from Hugging Face Hub
        model_name = "Sof22/image-caption-large-copy"
        processor = BlipProcessor.from_pretrained(model_name)
        model = BlipForConditionalGeneration.from_pretrained(model_name)

        # Preprocess inputs
        image = Image.open(io.BytesIO(image)).convert("RGB") 
        inputs = processor(images=image, return_tensors="pt")

        # Generate the output
        outputs = model.generate(
            pixel_values=inputs["pixel_values"],  # Pass pixel_values directly
            max_length=word_count+50,  # Adjust for longer responses
            temperature=creativity,
            top_k=100,
            top_p=0.95,
            num_beams=5, # Use beam search for better quality
            do_sample=True
        )

        # Decode and print the result
        result = processor.decode(outputs[0], skip_special_tokens=True)
        return result #response
        
    except Exception as e:
        print(e)


def generate_story(image_file, word_count, creativity):
    """Generates a story given an image"""
    # read image as bytes arrayS
    with open(image_file, "rb") as f:
        input_image = f.read()
    # generate caption for image
    image_desc = __image2text(image=input_image, word_count=word_count, creativity=creativity,)
    story = image_desc

    return story
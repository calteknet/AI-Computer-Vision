
# Art to Tale 🎨📖

**Transform artwork into short, AI-generated stories.**  
Art to Tale is a Gradio-based web application that turns uploaded images into creative narratives using a fine-tuned image captioning model.

> **Inspired by:** [pic-to-story by sssingh](https://github.com/sssingh/pic-to-story/tree/main)

---

## Features

- Upload any image to inspire a story  
- Adjustable story length (30–200 words)  
- Creativity index to shape tone and language  
- Dark mode support  
- Built with Hugging Face’s BLIP model and Gradio interface  

---

## Requirements

- Python 3.8+
- `transformers`
- `gradio`
- `Pillow`
- `Pytorch`
- `torchvision`
- `huggingface_hub`

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Model

Art to Tale uses the **BLIP (Bootstrapped Language Image Pretraining)** model architecture for generating descriptive captions and stories from images.

The current model used:
- **Model:** [`Sof22/image-caption-large-copy`](https://huggingface.co/Sof22/image-caption-large-copy)
- **Based on:** `Salesforce/blip-image-captioning-large`
- **Hosted on:** Hugging Face Model Hub

This model takes an image input and generates a descriptive, human-like caption using a vision-language transformer.  
Output quality is influenced by the **word count** and **creativity index** settings in the app.

---

## Configuration

Settings are defined in `config.py` using a `dataclass`:

```python
@dataclass
class AppConfig:
    title = "Art to Tale"
    theme = "freddyaboulton/dracula_revamped"
    css = "style.css"
```

---

## Running the App

Launch the app locally:

```bash
python app.py
```

This will start a Gradio server and open the interface in your browser.

---

## How It Works

1. The user uploads an image.
2. A Hugging Face BLIP model generates a caption or story.
3. Word count and creativity are adjustable via sliders.
4. The result is displayed in a text field.

---

## Project Structure

```
.
├── app.py                # Gradio app logic
├── model.py              # Image caption generation
├── config.py             # Application settings
├── style.css             # Custom CSS (optional)
├── requirements.txt      # Project dependencies
└── data/
    └── example images 
```

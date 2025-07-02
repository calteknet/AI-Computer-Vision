import gradio as gr
import model
from config import app_config

def clear():
    return None, 50, 0.7, None, None


def create_interface():
    js_enable_darkmode = """() => 
    {
        document.querySelector('body').classList.add('dark');
    }"""
    js_toggle_darkmode = """() => 
    {
        if (document.querySelectorAll('.dark').length) {
            document.querySelector('body').classList.remove('dark');
        } else {
            document.querySelector('body').classList.add('dark');
        }
    }"""

    with gr.Blocks(
        title=app_config.title, theme=app_config.theme, css=app_config.css
    ) as app:
        # Enable darkmode
        app.load(fn=None, inputs=None, outputs=None, _js=js_enable_darkmode)
        with gr.Row():
            darkmode_checkbox = gr.Checkbox(
                label="Dark Mode", value=True, interactive=True
            )
            # Toggle darkmode on/off when checkbox is checked/unchecked
            darkmode_checkbox.change(
                None, None, None, _js=js_toggle_darkmode, api_name=False
            )
        # Title and description
        with gr.Row():
            with gr.Column():
                gr.Markdown(
                    """
                    # Art to Tale 🎨📖  
                    **Turn your images into imaginative stories.**  
                    <br>  
                    Upload an inspiring image, choose your preferred `Story Length`, and adjust the `Creativity Index` to shape the tone and flavor of the narrative. Then click **Generate Story** and let the model craft your tale.  
                    <br>  
                    _Please note: the story may take a few seconds to generate. If the result doesn’t seem right at first, give it a moment and try again as the model might still be initializing._  
                    """
                )          
        # Image upload and story generation
        with gr.Row():
            with gr.Column():
                image = gr.Image(
                    type="filepath",
                )
                with gr.Row():
                    with gr.Column():
                        # Word Count Slider
                        word_count = gr.Slider(
                            label="Story Length (words):",
                            minimum=30,
                            maximum=200,
                            value=50,
                            step=10,
                        )
                        creativity = gr.Slider(
                            label="Creativity Index:",
                            minimum=0.3,
                            maximum=1.0,
                            value=0.7,
                            step=0.1,
                        )
                with gr.Row():
                    submit_button = gr.Button(
                        value="Generate Story", elem_classes="orange-button"
                    )
                    clear_button = gr.ClearButton(elem_classes="gray-button")
            with gr.Column():
                story = gr.Textbox(
                    label="Story:",
                    placeholder="Generated story will appear here.",
                    lines=21,
                )
    
        submit_button.click(
            fn=model.generate_story,
            inputs=[image, word_count, creativity],
            outputs=[story],
        )
        clear_button.click(
            fn=clear, inputs=[], outputs=[image, word_count, creativity, story]
        )
        image.clear(fn=clear, inputs=[], outputs=[image, word_count, creativity, story])

    return app


if __name__ == "__main__":
    # Initialize the database
    app = create_interface()
    app.launch(share=True)

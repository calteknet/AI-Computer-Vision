from dataclasses import dataclass

@dataclass
class AppConfig:
    
    title = "Art to Tale Generator"
    theme = "freddyaboulton/dracula_revamped"
    css = "style.css"
# Initialize the database connection
app_config = AppConfig()

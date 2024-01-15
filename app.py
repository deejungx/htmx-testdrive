from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/", response_class=HTMLResponse)
async def get_quote():
    html_content = """
    <blockquote>
        <p>
            "The only way to do great work is to love what you do." - Steve Jobs
        </p>
    </blockquote>
    """
    return html_content

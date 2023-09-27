from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Mount the "static" directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def get_index():
    # Define the path to your HTML file
    html_path = Path("static/index.html")
    
    # Return the HTML file as a response
    return FileResponse(html_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

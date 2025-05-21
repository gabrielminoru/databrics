from pathlib import Path
from rest.app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app)

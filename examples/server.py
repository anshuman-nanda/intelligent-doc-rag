"""
Example FastAPI server demonstrating RAGflow usage.

This is a demo server that shows how to use RAGflow in a web service context.
To run this server:
    python examples/server.py
    or
    uvicorn examples.server:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RAGflow Demo Server",
    description="Demo server for RAGflow document Q&A system",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to RAGflow Demo Server",
        "docs": "/docs",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


# TODO: Add RAGflow-specific endpoints here
# @app.post("/documents/add")
# async def add_documents(files: List[UploadFile]):
#     """Add documents to the knowledge base."""
#     pass
#
# @app.post("/query")
# async def query_documents(query: str):
#     """Query the document knowledge base."""
#     pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

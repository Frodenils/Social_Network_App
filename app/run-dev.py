import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "main:main",
        host="localhost",
        port=8000,
        reload=True
    )

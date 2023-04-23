from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

keys_db = {
        "3ae3d477038a787541e305acb004cddb5066a2ef": "alice@example.com",
        "4321zhztiv69ur8t6jco4004cd04cdxbx0x4cdad": "bob@example.com"
}

@app.get("/privaterssdemo/")
async def read_feed(key: str):
    if key not in keys_db:
        raise HTTPException(status_code=401, detail="Invalid key provided")
    return FileResponse("./feed.xml")


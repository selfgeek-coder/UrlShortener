from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    target_url: HttpUrl

class URLResponse(BaseModel):
    success: bool
    slug: str
    short_url: str
    target_url: str

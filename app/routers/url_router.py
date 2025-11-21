from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from ..db import get_db
from ..schemas.url_schema import URLCreate, URLResponse
from ..services.url_service import URLService

router = APIRouter()


@router.post("/shorten", response_model=URLResponse)
def create_short_url(payload: URLCreate, request: Request, db: Session = Depends(get_db)):
    created = URLService.create_short_url(db, str(payload.target_url))

    base_url = str(request.base_url).rstrip("/")

    return {
        "success": True,
        "slug": created.slug,
        "short_url": f"{base_url}/{created.slug}",
        "target_url": created.target_url,
    }


@router.get("/{slug}")
def redirect(slug: str, db: Session = Depends(get_db)):
    url = URLService.resolve_slug(db, slug)

    if not url:
        raise HTTPException(status_code=404,
                            detail="slug not found")

    return RedirectResponse(url.target_url)

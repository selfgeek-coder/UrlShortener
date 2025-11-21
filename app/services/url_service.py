from sqlalchemy.orm import Session

from .utils import generate_slug
from ..repositories.url_repo import URLRepository

class URLService:
    @staticmethod
    def create_short_url(db: Session, target_url: str):
        slug = generate_slug()

        # если slug уже есть
        while URLRepository.get_by_slug(db, slug):
            slug = generate_slug()

        return URLRepository.create(db, slug, target_url)

    @staticmethod
    def resolve_slug(db: Session, slug: str):
        return URLRepository.get_by_slug(db, slug)

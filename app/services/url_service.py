import string
from secrets import choice
from sqlalchemy.orm import Session

from app.repositories.url_repo import URLRepository

alphabet = string.ascii_letters + string.digits

def generate_slug(length: int = 6) -> str:
    return "".join(choice(alphabet) for _ in range(length))


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

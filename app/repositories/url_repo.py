from sqlalchemy.orm import Session

from app.models.url_model import URL

class URLRepository:
    @staticmethod
    def create(db: Session, slug: str, target_url: str) -> URL:
        url = URL(slug=slug, target_url=target_url)

        db.add(url)
        db.commit()
        db.refresh(url)
        
        return url

    @staticmethod
    def get_by_slug(db: Session, slug: str) -> URL | None:
        return db.query(URL).filter(URL.slug == slug).first()

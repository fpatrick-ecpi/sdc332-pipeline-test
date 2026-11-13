"""The /health route: status 200 with the text ok."""
from flask import Blueprint

bp = Blueprint("health", __name__)


@bp.get("/health")
def health():
    return "ok", 200

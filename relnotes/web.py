"""Flask web pages: / lists the notes, /health answers ok."""
from flask import Flask

from relnotes.health import bp as health_bp
from relnotes.notes import read_notes
from relnotes.settings import load_settings


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    settings = load_settings()

    @app.get("/")
    def index():
        lines = [f"mode={settings.get('APP_MODE')} label={settings.get('SETTINGS_LABEL', '-')}"]
        for version, notes in read_notes():
            lines.append(version + ": " + "; ".join(notes))
        return "\n".join(lines) + "\n", 200, {"Content-Type": "text/plain"}

    return app


if __name__ == "__main__":
    port = int(load_settings().get("PORT", "8000"))
    create_app().run(host="0.0.0.0", port=port)

import os, shutil
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.template.loader import render_to_string

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()


def clear_build_dir():
  print(f"Removing existing {settings.BUILD_DIR} dir, if any...")
  shutil.rmtree(settings.BUILD_DIR, ignore_errors=True)

  print(f"Copying contents of static/ into {settings.BUILD_DIR}...")
  shutil.copytree(settings.STATIC_DIR, settings.BUILD_DIR)


def get_render_context(**kwargs):
  return {**settings.CONTEXT, "articles": articles, "home_url": "/", **kwargs}


class Article:
  def __init__(self, article_key):
    self.key = article_key

  @property
  def file_name(self):
    return f"{self.key}.html"

  @property
  def file_path(self):
    return self.file_name

  @property
  def template_path(self):
    return f"articles/{self.file_name}"

  @property
  def url(self):
    return f"/{self.file_name}"

  @property
  def subject(self):
    return render_to_string(self.template_path, get_render_context(render_subject=True))

  @property
  def content(self):
    return render_to_string(self.template_path, get_render_context(article=self))


article_keys = [html[:-5] for html in os.listdir("templates/articles") if html.endswith(".html")]
article_keys = sorted(article_keys, reverse=True)

articles = [Article(article_key) for article_key in article_keys]


def render_to_file(template_path, context, file_path):
  print(f"Rendering {template_path} to {file_path}...")
  rendered = render_to_string(template_path, context)
  full_file_path = os.path.join(settings.BUILD_DIR, file_path)
  fout = open(full_file_path, "w")
  fout.write(rendered)
  fout.close()


def main():
  print("Let's build.")
  clear_build_dir()

  render_to_file("index.html", get_render_context(), "index.html")

  for index, article in enumerate(articles):
    prev_article = None if index == 0 else articles[index - 1]
    next_article = None if index == len(articles) - 1 else articles[index + 1]
    render_context = get_render_context(article=article,
                                        next_article=next_article,
                                        prev_article=prev_article)
    render_to_file("site-article.html", render_context, article.file_path)

  print("Done")


if __name__ == "__main__":
  main()

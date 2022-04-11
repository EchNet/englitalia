from django.core.management.base import BaseCommand, CommandError

from utils.mails import send_html_mail


class Command(BaseCommand):
  help = "Send an email"

  def add_arguments(self, parser):
    parser.add_argument("template", nargs="?", type=str)
    parser.add_argument("--to", nargs=1, type=str)
    parser.add_argument("--subject", nargs="?", type=str)

  def handle(self, *args, **options):
    to_email = options["to"]
    subject = options["subject"]
    template = options["template"] or "email/intro.html"
    send_html_mail(template, context={}, subject=subject, to=to_email)

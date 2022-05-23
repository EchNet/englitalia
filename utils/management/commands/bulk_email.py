from django.core.management.base import BaseCommand, CommandError

from utils.mails import send_html_mail

TEST_MAILING_LIST = [
    "ech@ech.net",
]

REVIEW_MAILING_LIST = [
    "annarosa1.brunelli@gmail.com",
    "m.danielapoli@gmail.com",
]

MAILING_LIST = [
    "ech@ech.net",
    "annarosa1.brunelli@gmail.com",
    "valeriosapienza@gmail.com",
    "lidiabonata@hotmail.com",
    "merhpoo@me.com",
    "m.danielapoli@gmail.com",
    "laurabiolcati@gmail.com",
    "massimomalavasi1972@gmail.com",
    "Gabry_9it@yahoo.it",
    "konitzlee@yahoo.it",
    "barbarabignami@yahoo.com",
    "corinne.ech@gmail.com",
    "francescosai@hotmail.it",
    "fdelconte80@gmail.com",
    "t.poli1984@gmail.com",
    "stefania_colonna@hotmail.com",
    "eli.poli@libero.it",
    "valentemarialuise@gmail.com",
    "elena.furi1999@gmail.com",
    "cosimodc@gmail.com",
    "federica.fontana.ba@gmail.com",
    "pandfcox@gmail.com",
]


class Command(BaseCommand):
  help = "Send a bulk email"

  def add_arguments(self, parser):
    parser.add_argument("template", nargs=1, type=str)
    parser.add_argument("--subject", nargs=1, type=str)
    parser.add_argument("--real", action="store_true")
    parser.add_argument("--review", action="store_true")

  def handle(self, *args, **options):
    subject = options["subject"]
    template = options["template"]
    real = options["real"]
    review = options["review"]
    mailing_list = (REVIEW_MAILING_LIST
                    if review else MAILING_LIST if real else TEST_MAILING_LIST)
    for to_email in mailing_list:
      print(f'sending to {to_email}...')
      send_html_mail(template, context={}, subject=subject, to=to_email)

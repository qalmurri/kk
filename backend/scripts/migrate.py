from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Purpose, Institute, Orderer, Scripts, Size, CoverColor, ScriptsOrderer, ScriptsStatusCode, ScriptsStatus, ISBN

@receiver(post_migrate)
def create_default_table(sender, **kwargs):
    if sender.name != "scripts":
        return

    User = get_user_model()
    default_users = [
        {"username": "qodri", "password": "pakisaji"},
        {"username": "sarah", "password": "pakisaji"},
        {"username": "menik", "password": "pakisaji"},
    ]
    for u in default_users:
        if not User.objects.filter(username=u["username"]).exists():
            User.objects.create_user(
                username=u["username"],
                password=u["password"]
            )

    code = [
        "status 1",
        "status 2",
        "status 3",
        "status 4"
    ]
    for item in code:
        ScriptsStatusCode.objects.get_or_create(
            code=item
        )

    purpose = [
        {"code": 1, "sum": 1, "label": 1},
        {"code": 2, "sum": 2, "label": 1}
    ]
    for item in purpose:
        Purpose.objects.get_or_create(
            code_id=item["code"],
            sum=item["sum"],
            label=item["label"]
        )

    institute = [
        "Fakultas Teknik",
        "Fakultas Pertanian",
        "Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA)",
        "Fakultas Ilmu Budaya (kebudayaan, sastra, humaniora)",
        "Fakultas Ekonomi dan Bisnis",
        "Fakultas Hukum",
        "Fakultas Kedokteran",
        "Fakultas Seni Rupa dan Desain",
        "Fakultas Ilmu Sosial dan Ilmu Politik",
        "Fakultas Keolahragaan",
        "Fakultas Psikologi",
        "Fakultas Teknologi Informasi dan Sains Data",
        "Sekolah Vokasi",
        "Sekolah Pascasarjana",
    ]
    for item in institute:
        Institute.objects.get_or_create(
            institute=item
        )

    name = [
        {"name": "Prof. Anjar", "no": 12345678, "institute": 1},
        {"name": "Prof. Tiwul", "no": 56498742, "institute": 2},
        {"name": "Prof. Sukiman", "no": 32122244, "institute": 3},
        {"name": "Prof. Andi", "no": 65464556, "institute": 4},
        {"name": "Prof. Alam", "no": 46545668, "institute": 5},
        {"name": "Prof. Sujiwo", "no": 98454665, "institute": 6},
    ]
    for item in name:
        Orderer.objects.get_or_create(
            name=item["name"],
            no=item["no"],
            institute_id=item["institute"]
        )

    size = [
        "160x250 (buku teks)",
        "A5",
        "A4",
        "A3",
        "A6",
        "B5",
        "B4",
        "Legal (8.5 x 14 inch)",
        "Letter (8.5 x 11 inch)",
        "Tabloid (11 x 17 inch)",
        "F4 / Folio (210 x 330 mm)",
        "Quarto (215 x 275 mm)",
        "Executive (7.25 x 10.5 inch)"
    ]
    for item in size:
        Size.objects.get_or_create(
            size=item
        )


    scripts = [
        {"title": "Values of Life", "institute": 1, "size": 1},
        {"title": "The Power of Core Values", "institute": 1, "size": 2}
    ]
    for item in scripts:
        Scripts.objects.get_or_create(
            title=item["title"],
            institute_id=item["institute"],
            size_id=item["size"]
        )

    color = [
        "Polos",
        "2 Warna",
        "3 Warna",
        "4 Warna"
    ]
    for item in color:
        CoverColor.objects.get_or_create(
            color=item
        )

    scriptsorderer = [
        {"scripts": 1, "orderer": 1},
        {"scripts": 1, "orderer": 3}
    ]
    for item in scriptsorderer:
        ScriptsOrderer.objects.get_or_create(
            scripts_id=item["scripts"],
            orderer_id=item["orderer"]
        )

    code1 = [
        {"scripts": 1, "scriptsstatuscode": 1, "purpose": 1},
        {"scripts": 1, "scriptsstatuscode": 3, "purpose": 1}
    ]
    for item in code1:
        ScriptsStatus.objects.get_or_create(
            scripts_id=item["scripts"],
            scriptsstatuscode_id=item["scriptsstatuscode"],
            purpose_id=item["purpose"]
        )

    isbn2 = [
        {"scripts": 1, "isbn": "32123123", "code": 1},
        {"scripts": 1, "isbn": "3212312323", "code": 2}
    ]
    for item in isbn2:
        ISBN.objects.get_or_create(
            scripts_id=item["scripts"],
            isbn=item["isbn"],
            code=item["code"]
        )
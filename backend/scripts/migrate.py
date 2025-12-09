from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Purpose, Institute, Orderer, Scripts, Size, CoverColor

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

    purpose = [
        {"code": 1, "purpose": "Cetak"},
        {"code": 1, "purpose": "E-Book"},
        {"code": 1, "purpose": "Cetak & E-Book"},
        {"code": 2, "purpose": "belum"},
        {"code": 2, "purpose": "Proses"},
        {"code": 2, "purpose": "Proval"},
        {"code": 2, "purpose": "Selesai"},
        {"code": 3, "purpose": "Cetak"},
        {"code": 3, "purpose": "E-Book"},
        {"code": 4, "purpose": "Belum"},
        {"code": 4, "purpose": "Proses"},
        {"code": 4, "purpose": "Selesai"},
    ]
    for item in purpose:
        """
        1. ProductionEbookStatus
        2. CoverStatus
        3. ScriptIsbn
        4. ScriptStatus
        """
        Purpose.objects.get_or_create(
            code=item["code"],
            purpose=item["purpose"]
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

    orderer = [
        {"orderer": "Orderer 1", "no": 12345678},
        {"orderer": "Orderer 2", "no": 56498742},
        {"orderer": "Orderer 3", "no": 32122244},
        {"orderer": "Orderer 4", "no": 65464556},
        {"orderer": "Orderer 5", "no": 46545668},
        {"orderer": "Orderer 6", "no": 98454665},
    ]
    for item in orderer:
        Orderer.objects.get_or_create(
            orderer=item["orderer"],
            no=item["no"]
        )

    scripts = [
        "Values of Life",
        "The Power of Core Values",
        "Values That Shape Us",
        "Living with Purpose and Values",
        "Hidden Values",
        "Values in Motion",
        "Timeless Values",
        "The Architecture of Values"
    ]
    for item in scripts:
        Scripts.objects.get_or_create(
            title=item
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
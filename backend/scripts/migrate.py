from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import (
    Status, Institute, Orderer, Scripts,
    Size, ScriptsOrderer, ScriptsProcess,
    ScriptsStatusCode, ISBN, Flag, Description, Note, By
)

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
        {"name": "Belum", "label": 1},
        {"name": "Proses", "label": 1},
        {"name": "Pengajuan", "label": 1},
        {"name": "Sudah", "label": 1},
        {"name": "ISBN", "label": 2},
        {"name": "EISBN", "label": 2}

    ]
    for item in code:
        ScriptsStatusCode.objects.get_or_create(
            name=item["name"],
            label=item["label"],
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
            name=item
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
            name=item
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


    purpose = [
        {"scripts": 1, "code": 1,"label": 1},
        {"scripts": 1, "code": 2, "label": 1}
    ]
    for item in purpose:
        Status.objects.get_or_create(
            scripts_id=item["scripts"],
            code_id=item["code"],
            label=item["label"]
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

    isbn2 = [
        {"scripts": 1, "isbn": "32123123", "code": 5},
        {"scripts": 1, "isbn": "3212312323", "code": 6}
    ]
    for item in isbn2:
        ISBN.objects.get_or_create(
            scripts_id=item["scripts"],
            isbn=item["isbn"],
            code_id=item["code"]
        )

    description = [
        {"scripts": 1, "text": "hoalaaaaa ngantuk", "label": 1},
        {"scripts": 1, "text": "ngantuk poooooolllllllll", "label": 2}
    ]
    for item in description:
        Description.objects.get_or_create(
            scripts_id=item["scripts"],
            text=item["text"],
            label=item["label"]
        )

    description2 = [
        {"scripts": 1, "content": "hoalaaaaa ngantuk", "label": 1},
        {"scripts": 1, "content": "ngantuk poooooolllllllll", "label": 2}
    ]
    for item in description2:
        Note.objects.get_or_create(
            scripts_id=item["scripts"],
            content=item["content"],
            label=item["label"]
        )

    bool = [
        {"scripts": 1, "label": 1, "is_active": False},
        {"scripts": 1, "label": 3, "is_active": True}
    ]
    for item in bool:
        Flag.objects.get_or_create(
            scripts_id=item["scripts"],
            label=item["label"],
            is_active=item["is_active"]
        )
        
    bool = [
        {"scripts": 1, "label": 1},
        {"scripts": 1, "label": 2}
    ]
    for item in bool:
        ScriptsProcess.objects.get_or_create(
            scripts_id=item["scripts"],
            label=item["label"]
        )
        
    balll = [
        {"scriptsprocess": 1, "user": 1},
        {"scriptsprocess": 1, "user": 2},
        {"scriptsprocess": 1, "user": 3},
    ]
    for item in balll:
        By.objects.get_or_create(
            scriptsprocess_id=item["scriptsprocess"],
            user_id=item["user"]
        )
        
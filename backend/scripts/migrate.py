from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import (
    Status,
    Institute,
    Orderer,
    Scripts,
    Size,
    ScriptsOrderer,
    ScriptsProcess,
    ScriptsStatusCode,
    ISBN,
    Flag,
    Description,
    Note,
    By,
    Text,
    Content,
    Label
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

    valuuu = [
        "value1",
        "value2",
        "value3",
        "value4",
        "value5",
        "value6",
        "value7",
        "value8",
        "value9"
    ]
    for item in valuuu:
        Label.objects.get_or_create(
            name=item
        )

    code = [
        "Belum",
        "Proses",
        "Pengajuan",
        "Sudah"
    ]
    for item in code:
        ScriptsStatusCode.objects.get_or_create(
            name=item
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
            label_id=item["label"]
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
        {"scripts": 1, "isbn": "32123123", "type": 1},
        {"scripts": 1, "isbn": "3212312323", "type": 2}
    ]
    for item in isbn2:
        ISBN.objects.get_or_create(
            scripts_id=item["scripts"],
            isbn=item["isbn"],
            type=item["type"]
        )

    bool = [
        {"scripts": 1, "label": 1, "is_active": False},
        {"scripts": 1, "label": 3, "is_active": True}
    ]
    for item in bool:
        Flag.objects.get_or_create(
            scripts_id=item["scripts"],
            label_id=item["label"],
            is_active=item["is_active"]
        )
        
    bool = [
        {"scripts": 1, "label": 1},
        {"scripts": 1, "label": 2}
    ]
    for item in bool:
        ScriptsProcess.objects.get_or_create(
            scripts_id=item["scripts"],
            label_id=item["label"]
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

    description = [
        {"scripts": 1, "label": 1},
        {"scripts": 1, "label": 2}
    ]
    for item in description:
        Description.objects.get_or_create(
            scripts_id=item["scripts"],
            label_id=item["label"]
        )

    description2 = [
        {"scripts": 1, "label": 1},
        {"scripts": 1, "label": 2}
    ]
    for item in description2:
        Note.objects.get_or_create(
            scripts_id=item["scripts"],
            label_id=item["label"]
        )

    content = [
        {"note": 1, "content": "testinggggggg"},
        {"note": 1, "content": "aku anak remaja"},
        {"note": 1, "content": "aku anak ibuk"},
        {"note": 1, "content": "aku anak bapak"}
    ]
    for item in content:
        Content.objects.get_or_create(
            note_id=item["note"],
            content=item["content"],
        )

    content22 = [
        {"description": 1, "text": "testinggggggg"},
        {"description": 1, "text": "aku anak remaja"},
        {"description": 1, "text": "aku anak ibuk"},
        {"description": 1, "text": "aku anak bapak"}
    ]
    for item in content22:
        Text.objects.get_or_create(
            description_id=item["description"],
            text=item["text"],
        )
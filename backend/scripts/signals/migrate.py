from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from scripts.models.script import (
    Status,
    Institute,
    Orderer,
    Script,
    Size,
    ScriptsOrderer,
    Flag,
    Description,
    Note,
    ByMade,
    TypeIsbn,
    SectionFlag,
    SectionMade,
    SectionDescription,
    SectionNote,
    LabelStatus,
    SectionStatus,
    Isbn,
    Made,
    TextNote,
    TextDescription,
    Cover
)

@receiver(post_migrate)
def create_default_table(sender, **kwargs):
    if sender.name != "scripts":
        return
    
    # USER
    for user in [
        {"username": "qodri", "password": "pakisaji"},
        {"username": "sarah", "password": "pakisaji"},
        {"username": "menik", "password": "pakisaji"},
    ]:
        User = get_user_model()
        if not User.objects.filter(username=user["username"]).exists():
            User.objects.create_user(
                username=user["username"],
                password=user["password"]
            )

    # SECTIONMADE
    for item in [
        "Layouter",
        "Desainer",
        "Produksi"
    ]:
        SectionMade.objects.get_or_create(
            name=item
        )

    # SECTIONDESCRIPTION
    for item in [
        "Layouter",
        "Desainer",
        "ISBN",
        "Produksi"
    ]:
        SectionDescription.objects.get_or_create(
            name=item
        )

    for item in [
        "Cover",
        "Isbn",
        "Produksi"
    ]:
        SectionNote.objects.get_or_create(
            name=item
        )

    for item in [
        "Layouter",
        "Desainer",
        "ISBN",
        "Produksi",
    ]:
        LabelStatus.objects.get_or_create(
            name=item
        )
 
    for item in [
        "File",
        "Photo",
        "CV",
        "Sinopsis",
        "Editor",
        "Kata Pengantar",
        "Daftar Isi",
        "Daftar Pustaka"
        #???
    ]:
        SectionFlag.objects.get_or_create(
            name=item
        )

    for item in [
        "Belum",
        "Proses",
        "Pengajuan",
        "Sudah"
    ]:
        SectionStatus.objects.get_or_create(
            name=item
        )

    for item in [
        "ISBN",
        "E-ISBN",
    ]:
        TypeIsbn.objects.get_or_create(
            name=item
        )

    for item in [
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
    ]:
        Institute.objects.get_or_create(
            name=item
        )

    for item in [
        {"name": "Prof. Anjar", "no": 12345678, "institute": 1},
        {"name": "Prof. Tiwul", "no": 56498742, "institute": 2},
        {"name": "Prof. Sukiman", "no": 32122244, "institute": 3},
        {"name": "Prof. Andi", "no": 65464556, "institute": 4},
        {"name": "Prof. Alam", "no": 46545668, "institute": 5},
        {"name": "Prof. Sujiwo", "no": 98454665, "institute": 6},
    ]:
        Orderer.objects.get_or_create(
            name=item["name"],
            no=item["no"],
            institute_id=item["institute"]
        )

    for item in [
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
    ]:
        Size.objects.get_or_create(
            name=item
        )

    for item in [
        {"title": "Values of Life", "institute": 1, "size": 1},
        {"title": "The Power of Core Values", "institute": 1, "size": 2}
    ]:
        Script.objects.get_or_create(
            title=item["title"],
            institute_id=item["institute"],
            size_id=item["size"]
        )

    for item in [
        {"script": 1, "sectionstatus": 1,"labelstatus": 1},
        {"script": 1, "sectionstatus": 2, "labelstatus": 2},
        {"script": 1, "sectionstatus": 4, "labelstatus": 3}
    ]:
        Status.objects.get_or_create(
            script_id=item["script"],
            sectionstatus_id=item["sectionstatus"],
            labelstatus_id=item["labelstatus"]
        )

    for item in [
        {"script": 1, "orderer": 1},
        {"script": 1, "orderer": 3}
    ]:
        ScriptsOrderer.objects.get_or_create(
            script_id=item["script"],
            orderer_id=item["orderer"]
        )

    for item in [
        {"script": 1, "isbn": "32123123", "typeisbn": 1},
        {"script": 1, "isbn": "3212312323", "typeisbn": 2}
    ]:
        Isbn.objects.get_or_create(
            script_id=item["script"],
            isbn=item["isbn"],
            typeisbn_id=item["typeisbn"]
        )

    for item in [
        {"scripts": 1, "sectionflag": 1, "is_active": False},
        {"scripts": 1, "sectionflag": 3, "is_active": True}
    ]:
        Flag.objects.get_or_create(
            scripts_id=item["scripts"],
            sectionflag_id=item["sectionflag"],
            is_active=item["is_active"]
        )
        
    for item in [
        {"script": 1, "sectionmade": 1},
        {"script": 1, "sectionmade": 2}
    ]:
        Made.objects.get_or_create(
            script_id=item["script"],
            sectionmade_id=item["sectionmade"]
        )
        
    for item in [
        {"made": 1, "user": 1},
        {"made": 1, "user": 2},
        {"made": 1, "user": 3},
    ]:
        ByMade.objects.get_or_create(
            made_id=item["made"],
            user_id=item["user"]
        )

    for item in [
        {"script": 1, "descriptionpart": 1},
        {"script": 1, "descriptionpart": 2}
    ]:
        Description.objects.get_or_create(
            script_id=item["script"],
            sectiondescription_id=item["descriptionpart"]
        )

    for item in [
        {"script": 1, "sectionnote": 1},
        {"script": 1, "sectionnote": 2}
    ]:
        Note.objects.get_or_create(
            script_id=item["script"],
            sectionnote_id=item["sectionnote"]
        )

    for item in [
        {"note": 1, "text": "Cover ini proval"},
        {"note": 1, "text": "Cover revisi terus"},
        {"note": 1, "text": "cover e angeeel"},
        {"note": 1, "text": "Penulis e njauk revisi terus hmm"}
    ]:
        TextNote.objects.get_or_create(
            note_id=item["note"],
            text=item["text"],
        )

    for item in [
        {"description": 1, "text": "cover warna biru"},
        {"description": 1, "text": "minta alternatif cover"},
        {"description": 1, "text": "biru sama merah"},
        {"description": 1, "text": "warna fakultas"}
    ]:
        TextDescription.objects.get_or_create(
            description_id=item["description"],
            text=item["text"],
        )

    for item in [
        {"script": 1, "thumbnail": "media/thumbnail/image001.jpeg", "length": 10, "height": 250, "width": 160, "x_axis": 1, "y_axis": 1},
    ]:
        Cover.objects.get_or_create(
            script_id=item["script"],
            thumbnail=item["thumbnail"],
            length=item["length"],
            height=item["height"],
            width=item["width"],
            x_axis=item["x_axis"],
            y_axis=item["y_axis"],
        )
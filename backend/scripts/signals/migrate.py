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
        {
            "username": "qodri",
            "password": "pakisaji"
        },
        {
            "username": "sarah",
            "password": "pakisaji"
            },
        {
            "username": "menik",
            "password": "pakisaji"
        },
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
        {
            "name": "Prof. Anjar",
            "no": 12345678,
            "institute": 1
        },
        {
            "name": "Prof. Tiwul",
            "no": 56498742,
            "institute": 2
        },
        {
            "name": "Prof. Sukiman",
            "no": 32122244,
            "institute": 3
        },
        {
            "name": "Prof. Andi",
            "no": 65464556,
            "institute": 4
        },
        {
            "name": "Prof. Alam",
            "no": 46545668,
            "institute": 5
        },
        {
            "name": "Prof. Sujiwo",
            "no": 98454665,
            "institute": 6
        },
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
        {
            "title": "Values of Life",
            "institute": 1,
            "size": 1
        },
        {
            "title": "The Power of Core Values",
            "institute": 1,
            "size": 2
        },
        {
            "title": "Living with Purpose",
            "institute": 2,
            "size": 1
        },
        {
            "title": "Integrity in Daily Life",
            "institute": 1,
            "size": 2
        },
        {
            "title": "Principles That Shape Us",
            "institute": 2,
            "size": 2
        },
        {
            "title": "Character Before Success",
            "institute": 1,
            "size": 1
        },
        {
            "title": "The Meaning of Responsibility",
            "institute": 2,
            "size": 1
        },
        {
            "title": "Ethics in the Modern World",
            "institute": 1,
            "size": 2
        },
        {
            "title": "Building Moral Foundations",
            "institute": 2,
            "size": 2
        },
        {
            "title": "Wisdom for Everyday Choices",
            "institute": 1,
            "size": 1
        },
        {
            "title": "Human Values and Society",
            "institute": 2,
            "size": 1
        },
        {
            "title": "Self-Discipline and Growth",
            "institute": 1,
            "size": 2
        },
        {
            "title": "The Art of Honest Living",
            "institute": 2,
            "size": 2
        },
        {
            "title": "Guided by Inner Values",
            "institute": 1,
            "size": 1
        },
        {
            "title": "Respect, Empathy, and You",
            "institute": 2,
            "size": 1
        },
        {
            "title": "Leadership Through Values",
            "institute": 1,
            "size": 2
        },
        {
            "title": "Foundations of Personal Ethics",
            "institute": 2,
            "size": 2
        },
        {
            "title": "Purpose-Driven Life Choices",
            "institute": 1,
            "size": 1
        },
        {
            "title": "Values that Define Humanity",
            "institute": 2,
            "size": 1
        },
        {
            "title": "Moral Compass for the Future",
            "institute": 1,
            "size": 2
        }
    ]:
        Script.objects.get_or_create(
            title=item["title"],
            institute_id=item["institute"],
            size_id=item["size"]
        )

    for item in [
        { "script": 1,  "sectionstatus": 2, "labelstatus": 4 },
        { "script": 2,  "sectionstatus": 1, "labelstatus": 3 },
        { "script": 3,  "sectionstatus": 4, "labelstatus": 2 },
        { "script": 4,  "sectionstatus": 3, "labelstatus": 1 },
        { "script": 5,  "sectionstatus": 2, "labelstatus": 2 },
        { "script": 6,  "sectionstatus": 1, "labelstatus": 4 },
        { "script": 7,  "sectionstatus": 4, "labelstatus": 1 },
        { "script": 8,  "sectionstatus": 3, "labelstatus": 3 },
        { "script": 9,  "sectionstatus": 2, "labelstatus": 1 },
        { "script": 10, "sectionstatus": 1, "labelstatus": 2 },
    
        { "script": 11, "sectionstatus": 4, "labelstatus": 4 },
        { "script": 12, "sectionstatus": 3, "labelstatus": 2 },
        { "script": 13, "sectionstatus": 2, "labelstatus": 3 },
        { "script": 14, "sectionstatus": 1, "labelstatus": 1 },
        { "script": 15, "sectionstatus": 4, "labelstatus": 2 },
        { "script": 16, "sectionstatus": 3, "labelstatus": 4 },
        { "script": 17, "sectionstatus": 2, "labelstatus": 4 },
        { "script": 18, "sectionstatus": 1, "labelstatus": 3 },
        { "script": 19, "sectionstatus": 3, "labelstatus": 1 },
        { "script": 20, "sectionstatus": 4, "labelstatus": 3 }
    ]:
        Status.objects.get_or_create(
            script_id=item["script"],
            sectionstatus_id=item["sectionstatus"],
            labelstatus_id=item["labelstatus"]
        )

    for item in [
        { "script": 1,  "orderer": 2 },
        { "script": 2,  "orderer": 5 },
        { "script": 3,  "orderer": 1 },
        { "script": 4,  "orderer": 6 },
        { "script": 5,  "orderer": 3 },
        { "script": 6,  "orderer": 4 },
        { "script": 7,  "orderer": 2 },
        { "script": 8,  "orderer": 1 },
        { "script": 9,  "orderer": 6 },
        { "script": 10, "orderer": 3 },
    
        { "script": 11, "orderer": 5 },
        { "script": 12, "orderer": 4 },
        { "script": 13, "orderer": 2 },
        { "script": 14, "orderer": 6 },
        { "script": 15, "orderer": 1 },
        { "script": 16, "orderer": 3 },
        { "script": 17, "orderer": 4 },
        { "script": 18, "orderer": 2 },
        { "script": 19, "orderer": 5 },
        { "script": 20, "orderer": 1 }
    ]:
        ScriptsOrderer.objects.get_or_create(
            script_id=item["script"],
            orderer_id=item["orderer"]
        )

    for item in [
        { "script": 1,  "isbn": "9781023456",  "typeisbn": 1 },
        { "script": 1,  "isbn": "9781023456789", "typeisbn": 2 },
        { "script": 2,  "isbn": "9782034567",  "typeisbn": 1 },
        { "script": 2,  "isbn": "9782034567890", "typeisbn": 2 },
        { "script": 3,  "isbn": "9783045678",  "typeisbn": 1 },
        { "script": 3,  "isbn": "9783045678901", "typeisbn": 2 },
        { "script": 4,  "isbn": "9784056789",  "typeisbn": 1 },
        { "script": 4,  "isbn": "9784056789012", "typeisbn": 2 },
        { "script": 5,  "isbn": "9785067890",  "typeisbn": 1 },
        { "script": 5,  "isbn": "9785067890123", "typeisbn": 2 },
        { "script": 6,  "isbn": "9786078901",  "typeisbn": 1 },
        { "script": 6,  "isbn": "9786078901234", "typeisbn": 2 },
        { "script": 7,  "isbn": "9787089012",  "typeisbn": 1 },
        { "script": 7,  "isbn": "9787089012345", "typeisbn": 2 },
        { "script": 8,  "isbn": "9788090123",  "typeisbn": 1 },
        { "script": 8,  "isbn": "9788090123456", "typeisbn": 2 },
        { "script": 9,  "isbn": "9789012345",  "typeisbn": 1 },
        { "script": 9,  "isbn": "9789012345678", "typeisbn": 2 },
        { "script": 10, "isbn": "9780123456",  "typeisbn": 1 },
        { "script": 10, "isbn": "9780123456789", "typeisbn": 2 },
        { "script": 11, "isbn": "9781122334",  "typeisbn": 1 },
        { "script": 11, "isbn": "9781122334455", "typeisbn": 2 },
        { "script": 12, "isbn": "9782233445",  "typeisbn": 1 },
        { "script": 12, "isbn": "9782233445566", "typeisbn": 2 },
        { "script": 13, "isbn": "9783344556",  "typeisbn": 1 },
        { "script": 13, "isbn": "9783344556677", "typeisbn": 2 },
        { "script": 14, "isbn": "9784455667",  "typeisbn": 1 },
        { "script": 14, "isbn": "9784455667788", "typeisbn": 2 },
        { "script": 15, "isbn": "9785566778",  "typeisbn": 1 },
        { "script": 15, "isbn": "9785566778899", "typeisbn": 2 },
        { "script": 16, "isbn": "9786677889",  "typeisbn": 1 },
        { "script": 16, "isbn": "9786677889900", "typeisbn": 2 },
        { "script": 17, "isbn": "9787788990",  "typeisbn": 1 },
        { "script": 17, "isbn": "9787788990011", "typeisbn": 2 },
        { "script": 18, "isbn": "9788899001",  "typeisbn": 1 },
        { "script": 18, "isbn": "9788899001122", "typeisbn": 2 },
        { "script": 19, "isbn": "9789900112",  "typeisbn": 1 },
        { "script": 19, "isbn": "9789900112233", "typeisbn": 2 },
        { "script": 20, "isbn": "9780011223",  "typeisbn": 1 },
        { "script": 20, "isbn": "9780011223344", "typeisbn": 2 }
    ]:
        Isbn.objects.get_or_create(
            script_id=item["script"],
            isbn=item["isbn"],
            typeisbn_id=item["typeisbn"]
        )

    for item in [
        { "scripts": 1, "sectionflag": 1, "is_active": False },
        { "scripts": 1, "sectionflag": 8, "is_active": True },
        { "scripts": 1, "sectionflag": 2, "is_active": True },
        { "scripts": 1, "sectionflag": 3, "is_active": False },
        { "scripts": 1, "sectionflag": 6, "is_active": False },
        { "scripts": 1, "sectionflag": 7, "is_active": True },
        { "scripts": 1, "sectionflag": 5, "is_active": True },
        { "scripts": 1, "sectionflag": 4, "is_active": False },
        { "scripts": 2, "sectionflag": 1, "is_active": True },
        { "scripts": 2, "sectionflag": 8, "is_active": False },
        { "scripts": 2, "sectionflag": 2, "is_active": False },
        { "scripts": 2, "sectionflag": 3, "is_active": True },
        { "scripts": 2, "sectionflag": 6, "is_active": True },
        { "scripts": 2, "sectionflag": 7, "is_active": False },
        { "scripts": 2, "sectionflag": 5, "is_active": False },
        { "scripts": 2, "sectionflag": 4, "is_active": True },
        { "scripts": 3, "sectionflag": 1, "is_active": False },
        { "scripts": 3, "sectionflag": 8, "is_active": True },
        { "scripts": 3, "sectionflag": 2, "is_active": True },
        { "scripts": 3, "sectionflag": 3, "is_active": True },
        { "scripts": 3, "sectionflag": 6, "is_active": False },
        { "scripts": 3, "sectionflag": 7, "is_active": False },
        { "scripts": 3, "sectionflag": 5, "is_active": True },
        { "scripts": 3, "sectionflag": 4, "is_active": False },
        { "scripts": 4, "sectionflag": 1, "is_active": True },
        { "scripts": 4, "sectionflag": 8, "is_active": True },
        { "scripts": 4, "sectionflag": 2, "is_active": False },
        { "scripts": 4, "sectionflag": 3, "is_active": False },
        { "scripts": 4, "sectionflag": 6, "is_active": True },
        { "scripts": 4, "sectionflag": 7, "is_active": True },
        { "scripts": 4, "sectionflag": 5, "is_active": False },
        { "scripts": 4, "sectionflag": 4, "is_active": False },
        { "scripts": 5, "sectionflag": 1, "is_active": False },
        { "scripts": 5, "sectionflag": 8, "is_active": False },
        { "scripts": 5, "sectionflag": 2, "is_active": True },
        { "scripts": 5, "sectionflag": 3, "is_active": True },
        { "scripts": 5, "sectionflag": 6, "is_active": True },
        { "scripts": 5, "sectionflag": 7, "is_active": False },
        { "scripts": 5, "sectionflag": 5, "is_active": True },
        { "scripts": 5, "sectionflag": 4, "is_active": False },
        { "scripts": 6, "sectionflag": 1, "is_active": True },
        { "scripts": 6, "sectionflag": 8, "is_active": False },
        { "scripts": 6, "sectionflag": 2, "is_active": True },
        { "scripts": 6, "sectionflag": 3, "is_active": False },
        { "scripts": 6, "sectionflag": 6, "is_active": False },
        { "scripts": 6, "sectionflag": 7, "is_active": True },
        { "scripts": 6, "sectionflag": 5, "is_active": False },
        { "scripts": 6, "sectionflag": 4, "is_active": True },
        { "scripts": 7, "sectionflag": 1, "is_active": False },
        { "scripts": 7, "sectionflag": 8, "is_active": True },
        { "scripts": 7, "sectionflag": 2, "is_active": False },
        { "scripts": 7, "sectionflag": 3, "is_active": True },
        { "scripts": 7, "sectionflag": 6, "is_active": True },
        { "scripts": 7, "sectionflag": 7, "is_active": False },
        { "scripts": 7, "sectionflag": 5, "is_active": True },
        { "scripts": 7, "sectionflag": 4, "is_active": False },
        { "scripts": 8, "sectionflag": 1, "is_active": True },
        { "scripts": 8, "sectionflag": 8, "is_active": False },
        { "scripts": 8, "sectionflag": 2, "is_active": True },
        { "scripts": 8, "sectionflag": 3, "is_active": True },
        { "scripts": 8, "sectionflag": 6, "is_active": False },
        { "scripts": 8, "sectionflag": 7, "is_active": False },
        { "scripts": 8, "sectionflag": 5, "is_active": False },
        { "scripts": 8, "sectionflag": 4, "is_active": True },
        { "scripts": 9, "sectionflag": 1, "is_active": False },
        { "scripts": 9, "sectionflag": 8, "is_active": True },
        { "scripts": 9, "sectionflag": 2, "is_active": True },
        { "scripts": 9, "sectionflag": 3, "is_active": False },
        { "scripts": 9, "sectionflag": 6, "is_active": True },
        { "scripts": 9, "sectionflag": 7, "is_active": False },
        { "scripts": 9, "sectionflag": 5, "is_active": True },
        { "scripts": 9, "sectionflag": 4, "is_active": False },
        { "scripts": 10, "sectionflag": 1, "is_active": True },
        { "scripts": 10, "sectionflag": 8, "is_active": True },
        { "scripts": 10, "sectionflag": 2, "is_active": False },
        { "scripts": 10, "sectionflag": 3, "is_active": False },
        { "scripts": 10, "sectionflag": 6, "is_active": True },
        { "scripts": 10, "sectionflag": 7, "is_active": True },
        { "scripts": 10, "sectionflag": 5, "is_active": False },
        { "scripts": 10, "sectionflag": 4, "is_active": False },
        { "scripts": 11, "sectionflag": 1, "is_active": False },
        { "scripts": 11, "sectionflag": 8, "is_active": False },
        { "scripts": 11, "sectionflag": 2, "is_active": True },
        { "scripts": 11, "sectionflag": 3, "is_active": True },
        { "scripts": 11, "sectionflag": 6, "is_active": False },
        { "scripts": 11, "sectionflag": 7, "is_active": True },
        { "scripts": 11, "sectionflag": 5, "is_active": False },
        { "scripts": 11, "sectionflag": 4, "is_active": True },
        { "scripts": 12, "sectionflag": 1, "is_active": True },
        { "scripts": 12, "sectionflag": 8, "is_active": False },
        { "scripts": 12, "sectionflag": 2, "is_active": False },
        { "scripts": 12, "sectionflag": 3, "is_active": True },
        { "scripts": 12, "sectionflag": 6, "is_active": True },
        { "scripts": 12, "sectionflag": 7, "is_active": False },
        { "scripts": 12, "sectionflag": 5, "is_active": True },
        { "scripts": 12, "sectionflag": 4, "is_active": False },
        { "scripts": 13, "sectionflag": 1, "is_active": False },
        { "scripts": 13, "sectionflag": 8, "is_active": True },
        { "scripts": 13, "sectionflag": 2, "is_active": True },
        { "scripts": 13, "sectionflag": 3, "is_active": False },
        { "scripts": 13, "sectionflag": 6, "is_active": False },
        { "scripts": 13, "sectionflag": 7, "is_active": True },
        { "scripts": 13, "sectionflag": 5, "is_active": True },
        { "scripts": 13, "sectionflag": 4, "is_active": False },
        { "scripts": 14, "sectionflag": 1, "is_active": True },
        { "scripts": 14, "sectionflag": 8, "is_active": True },
        { "scripts": 14, "sectionflag": 2, "is_active": False },
        { "scripts": 14, "sectionflag": 3, "is_active": True },
        { "scripts": 14, "sectionflag": 6, "is_active": False },
        { "scripts": 14, "sectionflag": 7, "is_active": False },
        { "scripts": 14, "sectionflag": 5, "is_active": True },
        { "scripts": 14, "sectionflag": 4, "is_active": False },
        { "scripts": 15, "sectionflag": 1, "is_active": False },
        { "scripts": 15, "sectionflag": 8, "is_active": False },
        { "scripts": 15, "sectionflag": 2, "is_active": True },
        { "scripts": 15, "sectionflag": 3, "is_active": False },
        { "scripts": 15, "sectionflag": 6, "is_active": True },
        { "scripts": 15, "sectionflag": 7, "is_active": True },
        { "scripts": 15, "sectionflag": 5, "is_active": False },
        { "scripts": 15, "sectionflag": 4, "is_active": True },
        { "scripts": 16, "sectionflag": 1, "is_active": True },
        { "scripts": 16, "sectionflag": 8, "is_active": False },
        { "scripts": 16, "sectionflag": 2, "is_active": False },
        { "scripts": 16, "sectionflag": 3, "is_active": True },
        { "scripts": 16, "sectionflag": 6, "is_active": False },
        { "scripts": 16, "sectionflag": 7, "is_active": True },
        { "scripts": 16, "sectionflag": 5, "is_active": True },
        { "scripts": 16, "sectionflag": 4, "is_active": False },
        { "scripts": 17, "sectionflag": 1, "is_active": False },
        { "scripts": 17, "sectionflag": 8, "is_active": True },
        { "scripts": 17, "sectionflag": 2, "is_active": True },
        { "scripts": 17, "sectionflag": 3, "is_active": True },
        { "scripts": 17, "sectionflag": 6, "is_active": False },
        { "scripts": 17, "sectionflag": 7, "is_active": False },
        { "scripts": 17, "sectionflag": 5, "is_active": False },
        { "scripts": 17, "sectionflag": 4, "is_active": True },
        { "scripts": 18, "sectionflag": 1, "is_active": True },
        { "scripts": 18, "sectionflag": 8, "is_active": False },
        { "scripts": 18, "sectionflag": 2, "is_active": True },
        { "scripts": 18, "sectionflag": 3, "is_active": False },
        { "scripts": 18, "sectionflag": 6, "is_active": True },
        { "scripts": 18, "sectionflag": 7, "is_active": False },
        { "scripts": 18, "sectionflag": 5, "is_active": True },
        { "scripts": 18, "sectionflag": 4, "is_active": False },
        { "scripts": 19, "sectionflag": 1, "is_active": False },
        { "scripts": 19, "sectionflag": 8, "is_active": True },
        { "scripts": 19, "sectionflag": 2, "is_active": False },
        { "scripts": 19, "sectionflag": 3, "is_active": True },
        { "scripts": 19, "sectionflag": 6, "is_active": True },
        { "scripts": 19, "sectionflag": 7, "is_active": False },
        { "scripts": 19, "sectionflag": 5, "is_active": True },
        { "scripts": 19, "sectionflag": 4, "is_active": False },
        { "scripts": 20, "sectionflag": 1, "is_active": True },
        { "scripts": 20, "sectionflag": 8, "is_active": True },
        { "scripts": 20, "sectionflag": 2, "is_active": False },
        { "scripts": 20, "sectionflag": 3, "is_active": False },
        { "scripts": 20, "sectionflag": 6, "is_active": True },
        { "scripts": 20, "sectionflag": 7, "is_active": True },
        { "scripts": 20, "sectionflag": 5, "is_active": False },
        { "scripts": 20, "sectionflag": 4, "is_active": False }
    ]:
        Flag.objects.get_or_create(
            scripts_id=item["scripts"],
            sectionflag_id=item["sectionflag"],
            is_active=item["is_active"]
        )
        
    for item in [
        { "script": 1,  "sectionmade": 1 },
        { "script": 1,  "sectionmade": 2 },
        { "script": 1,  "sectionmade": 3 },
        { "script": 2,  "sectionmade": 1 },
        { "script": 2,  "sectionmade": 2 },
        { "script": 2,  "sectionmade": 3 },
        { "script": 3,  "sectionmade": 1 },
        { "script": 3,  "sectionmade": 2 },
        { "script": 3,  "sectionmade": 3 },
        { "script": 4,  "sectionmade": 1 },
        { "script": 4,  "sectionmade": 2 },
        { "script": 4,  "sectionmade": 3 },
        { "script": 5,  "sectionmade": 1 },
        { "script": 5,  "sectionmade": 2 },
        { "script": 5,  "sectionmade": 3 },
        { "script": 6,  "sectionmade": 1 },
        { "script": 6,  "sectionmade": 2 },
        { "script": 6,  "sectionmade": 3 },
        { "script": 7,  "sectionmade": 1 },
        { "script": 7,  "sectionmade": 2 },
        { "script": 7,  "sectionmade": 3 },
        { "script": 8,  "sectionmade": 1 },
        { "script": 8,  "sectionmade": 2 },
        { "script": 8,  "sectionmade": 3 },
        { "script": 9,  "sectionmade": 1 },
        { "script": 9,  "sectionmade": 2 },
        { "script": 9,  "sectionmade": 3 },
        { "script": 10, "sectionmade": 1 },
        { "script": 10, "sectionmade": 2 },
        { "script": 10, "sectionmade": 3 },
        { "script": 11, "sectionmade": 1 },
        { "script": 11, "sectionmade": 2 },
        { "script": 11, "sectionmade": 3 },
        { "script": 12, "sectionmade": 1 },
        { "script": 12, "sectionmade": 2 },
        { "script": 12, "sectionmade": 3 },
        { "script": 13, "sectionmade": 1 },
        { "script": 13, "sectionmade": 2 },
        { "script": 13, "sectionmade": 3 },
        { "script": 14, "sectionmade": 1 },
        { "script": 14, "sectionmade": 2 },
        { "script": 14, "sectionmade": 3 },
        { "script": 15, "sectionmade": 1 },
        { "script": 15, "sectionmade": 2 },
        { "script": 15, "sectionmade": 3 },
        { "script": 16, "sectionmade": 1 },
        { "script": 16, "sectionmade": 2 },
        { "script": 16, "sectionmade": 3 },
        { "script": 17, "sectionmade": 1 },
        { "script": 17, "sectionmade": 2 },
        { "script": 17, "sectionmade": 3 },
        { "script": 18, "sectionmade": 1 },
        { "script": 18, "sectionmade": 2 },
        { "script": 18, "sectionmade": 3 },
        { "script": 19, "sectionmade": 1 },
        { "script": 19, "sectionmade": 2 },
        { "script": 19, "sectionmade": 3 },
        { "script": 20, "sectionmade": 1 },
        { "script": 20, "sectionmade": 2 },
        { "script": 20, "sectionmade": 3 }
    ]:
        Made.objects.get_or_create(
            script_id=item["script"],
            sectionmade_id=item["sectionmade"]
        )
        
    for item in [
        { "made": 1,  "user": 2 },
        { "made": 2,  "user": 1 },
        { "made": 3,  "user": 3 },
        { "made": 4,  "user": 2 },
        { "made": 5,  "user": 1 },
        { "made": 6,  "user": 3 },
        { "made": 7,  "user": 2 },
        { "made": 8,  "user": 1 },
        { "made": 9,  "user": 3 },
        { "made": 10, "user": 2 },
        { "made": 11, "user": 1 },
        { "made": 12, "user": 3 },
        { "made": 13, "user": 2 },
        { "made": 14, "user": 1 },
        { "made": 15, "user": 3 },
        { "made": 16, "user": 2 },
        { "made": 17, "user": 1 },
        { "made": 18, "user": 3 },
        { "made": 19, "user": 2 },
        { "made": 20, "user": 1 },
        { "made": 21, "user": 3 },
        { "made": 22, "user": 2 },
        { "made": 23, "user": 1 },
        { "made": 24, "user": 3 },
        { "made": 25, "user": 2 },
        { "made": 26, "user": 1 },
        { "made": 27, "user": 3 },
        { "made": 28, "user": 2 },
        { "made": 29, "user": 1 },
        { "made": 30, "user": 3 },
        { "made": 31, "user": 2 },
        { "made": 32, "user": 1 },
        { "made": 33, "user": 3 },
        { "made": 34, "user": 2 },
        { "made": 35, "user": 1 },
        { "made": 36, "user": 3 },
        { "made": 37, "user": 2 },
        { "made": 38, "user": 1 },
        { "made": 39, "user": 3 },
        { "made": 40, "user": 2 },
        { "made": 41, "user": 1 },
        { "made": 42, "user": 3 },
        { "made": 43, "user": 2 },
        { "made": 44, "user": 1 },
        { "made": 45, "user": 3 },
        { "made": 46, "user": 2 },
        { "made": 47, "user": 1 },
        { "made": 48, "user": 3 },
        { "made": 49, "user": 2 },
        { "made": 50, "user": 1 },
        { "made": 51, "user": 3 },
        { "made": 52, "user": 2 },
        { "made": 53, "user": 1 },
        { "made": 54, "user": 3 },
        { "made": 55, "user": 2 },
        { "made": 56, "user": 1 },
        { "made": 57, "user": 3 }
    ]:
        ByMade.objects.get_or_create(
            made_id=item["made"],
            user_id=item["user"]
        )

    for item in [
        {
            "script": 1,
            "descriptionpart": 1
        },
        {
            "script": 1,
            "descriptionpart": 2
        }
    ]:
        Description.objects.get_or_create(
            script_id=item["script"],
            sectiondescription_id=item["descriptionpart"]
        )

    for item in [
        {
            "script": 1,
            "sectionnote": 1
        },
        {
            "script": 1,
            "sectionnote": 2
        }
    ]:
        Note.objects.get_or_create(
            script_id=item["script"],
            sectionnote_id=item["sectionnote"]
        )

    for item in [
        {
            "note": 1,
            "text": "Cover ini proval"
        },
        {
            "note": 1,
            "text": "Cover revisi terus"
        },
        {
            "note": 1,
            "text": "cover e angeeel"
        },
        {
            "note": 1,
            "text": "Penulis e njauk revisi terus hmm"
        }
    ]:
        TextNote.objects.get_or_create(
            note_id=item["note"],
            text=item["text"],
        )

    for item in [
        {
            "description": 1,
            "text": "cover warna biru"
        },
        {
            "description": 1,
            "text": "minta alternatif cover"
        },
        {
            "description": 1,
            "text": "biru sama merah"
        },
        {
            "description": 1,
            "text": "warna fakultas"
        }
    ]:
        TextDescription.objects.get_or_create(
            description_id=item["description"],
            text=item["text"],
        )

    for item in [
        {
            "script": 1,
            "thumbnail": "media/thumbnail/image001.jpeg",
            "length": 12,
            "height": 240,
            "width": 160,
            "x_axis": 2,
            "y_axis": 1,
            "zoom": 1
        },
        {
            "script": 2,
            "thumbnail": "media/thumbnail/image002.jpeg",
            "length": 8,
            "height": 300,
            "width": 180,
            "x_axis": 1,
            "y_axis": 3,
            "zoom": 2
        },
        {
            "script": 3,
            "thumbnail": "media/thumbnail/image003.jpeg",
            "length": 15,
            "height": 220,
            "width": 200,
            "x_axis": 3,
            "y_axis": 2,
            "zoom": 1
        },
        {
            "script": 4,
            "thumbnail": "media/thumbnail/image004.jpeg",
            "length": 10,
            "height": 260,
            "width": 170,
            "x_axis": 1,
            "y_axis": 1,
            "zoom": 2
        },
        {
            "script": 5,
            "thumbnail": "media/thumbnail/image005.jpeg",
            "length": 18,
            "height": 280,
            "width": 190,
            "x_axis": 2,
            "y_axis": 2,
            "zoom": 3
        },
        {
            "script": 6,
            "thumbnail": "media/thumbnail/image006.jpeg",
            "length": 9,
            "height": 230,
            "width": 150,
            "x_axis": 1,
            "y_axis": 3,
            "zoom": 1
        },
        {
            "script": 7,
            "thumbnail": "media/thumbnail/image007.jpeg",
            "length": 14,
            "height": 320,
            "width": 210,
            "x_axis": 3,
            "y_axis": 1,
            "zoom": 2
        },
        {
            "script": 8,
            "thumbnail": "media/thumbnail/image008.jpeg",
            "length": 11,
            "height": 250,
            "width": 160,
            "x_axis": 2,
            "y_axis": 2,
            "zoom": 1
        },
        {
            "script": 9,
            "thumbnail": "media/thumbnail/image009.jpeg",
            "length": 20,
            "height": 300,
            "width": 220,
            "x_axis": 1,
            "y_axis": 1,
            "zoom": 3
        },
        {
            "script": 10,
            "thumbnail": "media/thumbnail/image010.jpeg",
            "length": 7,
            "height": 210,
            "width": 140,
            "x_axis": 2,
            "y_axis": 3,
            "zoom": 1
        },
    
        {
            "script": 11,
            "thumbnail": "media/thumbnail/image011.jpeg",
            "length": 13,
            "height": 270,
            "width": 180,
            "x_axis": 3,
            "y_axis": 2,
            "zoom": 2
        },
        {
            "script": 12,
            "thumbnail": "media/thumbnail/image012.jpeg",
            "length": 16,
            "height": 290,
            "width": 200,
            "x_axis": 1,
            "y_axis": 1,
            "zoom": 2
        },
        {
            "script": 13,
            "thumbnail": "media/thumbnail/image013.jpeg",
            "length": 9,
            "height": 240,
            "width": 150,
            "x_axis": 2,
            "y_axis": 2,
            "zoom": 1
        },
        {
            "script": 14,
            "thumbnail": "media/thumbnail/image014.jpeg",
            "length": 22,
            "height": 330,
            "width": 240,
            "x_axis": 3,
            "y_axis": 1,
            "zoom": 3
        },
        {
            "script": 15,
            "thumbnail": "media/thumbnail/image015.jpeg",
            "length": 10,
            "height": 260,
            "width": 170,
            "x_axis": 1,
            "y_axis": 2,
            "zoom": 1
        },
        {
            "script": 16,
            "thumbnail": "media/thumbnail/image016.jpeg",
            "length": 17,
            "height": 310,
            "width": 210,
            "x_axis": 2,
            "y_axis": 3,
            "zoom": 2
        },
        {
            "script": 17,
            "thumbnail": "media/thumbnail/image017.jpeg",
            "length": 8,
            "height": 220,
            "width": 150,
            "x_axis": 1,
            "y_axis": 1,
            "zoom": 1
        },
        {
            "script": 18,
            "thumbnail": "media/thumbnail/image018.jpeg",
            "length": 19,
            "height": 300,
            "width": 230,
            "x_axis": 3,
            "y_axis": 2,
            "zoom": 3
        },
        {
            "script": 19,
            "thumbnail": "media/thumbnail/image019.jpeg",
            "length": 12,
            "height": 250,
            "width": 180,
            "x_axis": 2,
            "y_axis": 1,
            "zoom": 2
        },
        {
            "script": 20,
            "thumbnail": "media/thumbnail/image020.jpeg",
            "length": 15,
            "height": 280,
            "width": 200,
            "x_axis": 1,
            "y_axis": 3,
            "zoom": 2
        }
    ]:
        Cover.objects.get_or_create(
            script_id=item["script"],
            thumbnail=item["thumbnail"],
            length=item["length"],
            height=item["height"],
            width=item["width"],
            x_axis=item["x_axis"],
            y_axis=item["y_axis"],
            zoom=item["zoom"],
        )

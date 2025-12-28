from .common import (
    SizeWriteSerializer,
    InstituteWriteSerializer
)
from .cover import CoverWriteSerializer
from .description import (
    TextDescriptionWriteSerializer,
    SectionDescriptionWriteSerializer,
    DescriptionWriteSerializer
)
from .flag import (
    SectionFlagWriteSerializer,
    FlagWriteSerializer
)
from .isbn import (
    TypeIsbnWriteSerializer,
    IsbnWriteSerializer,

)
from .note import (
    TextNoteWriteSerializer,
    SectionNoteWriteSerializer,
    NoteWriteSerializer
)
from .orderer import (
    OrdererWriteSerializer,
    ScriptOrdererWriteSerializer
)
from .scripts import ScriptsWriteSerializer
from .made import (
    SectionMadeWriteSerializer,
    ByMadeWriteSerializer,
    MadeWriteSerializer
)
from .status import (
    LabelStatusWriteSerializer,
    SectionStatusWriteSerializer,
    StatusWriteSerializer
)
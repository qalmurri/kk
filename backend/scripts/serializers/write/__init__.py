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
    PartWriteSerializer,
    FlagWriteSerializer
)
from .isbn import (
    TypeWriteSerializer,
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
from .scriptsprocess import (
    SectionWriteSerializer,
    ByWriteSerializer,
    ScriptProcessWriteSerializer
)
from .status import (
    LabelStatusWriteSerializer,
    SectionStatusWriteSerializer,
    StatusWriteSerializer
)
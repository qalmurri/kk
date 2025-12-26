from .common import (
    SizeQueryRepository,
    InstituteQueryRepository
)
from .cover import (
    CoverBookQueryRepository
)
from .description import (
    DescriptionQueryRepository, 
    DescriptionPartQueryRepository,
    TextQueryRepository
)
from .flag import (
    FlagQueryRepository,
    PartQueryRepository
)
from .isbn import (
    TypeQueryRepository,
    ISBNQueryRepository
)
from .note import (
    NotePartQueryRepository,
    ContentQueryRepository,
    NoteQueryRepository
)
from .orderer import (
    OrdererQueryRepository,
    ScriptsOrdererQueryRepository
)
from .scripts import (
    ScriptsQueryRepository
)
from .scriptsprocess import (
    SectionQueryRepository,
    ByQueryRepository,
    ScriptsProcessQueryRepository
)
from .status import (
    LabelQueryRepository,
    ScriptsStatusCodeQueryRepository,
    StatusQueryRepository
)
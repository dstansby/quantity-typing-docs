from sphinx.util.typing import stringify
from typing import Annotated

print(str(Annotated[str, "foo"]))
print(stringify(Annotated[str, "foo"]))

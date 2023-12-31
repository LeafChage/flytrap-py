from collections.abc import Sequence
from .parser import IParser
from .parser_exception import ParserException

class EofParser[E](IParser[None, Sequence[E]]):
    def __init__(self) -> None:
        pass

    def parse(self, stream: Sequence[E]) -> tuple[None, Sequence[E]]:
        if len(stream) == 0:
            return (None, stream)
        else:
            raise ParserException(expect="EOF", actual="{}".format(stream[0]))

def eof():
    return EofParser()

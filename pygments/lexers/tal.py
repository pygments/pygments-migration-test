"""
    pygments.lexers.tal
    ~~~~~~~~~~~~~~~~~~~

    Lexers for Uxntal

    .. versionadded:: 2.12

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
import keyword

from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Keyword, Name, String, Number, Punctuation, Whitespace, Literal

__all__ = ['TalLexer']

class TalLexer(RegexLexer):

    name = 'Tal'
    aliases = ['tal', 'uxntal']
    filenames = ['*.tal']
    mimetypes = ['text/x-uxntal']

    instructions = [
        'BRK', 'LIT', 'INC', 'POP', 'DUP', 'NIP', 'SWP', 'OVR', 'ROT',
        'EQU', 'NEQ', 'GTH', 'LTH', 'JMP', 'JCN', 'JSR', 'STH',
        'LDZ', 'STZ', 'LDR', 'STR', 'LDA', 'STA', 'DEI', 'DEO',
        'ADD', 'SUB', 'MUL', 'DIV', 'AND', 'ORA', 'EOR', 'SFT'
    ]

    tokens = {
        # the comment delimiters must not be adjacent to non-space characters.
        # this means ( foo ) is a valid comment but (foo) is not. this also
        # applies to nested comments.
        'comment': [
            (r'(?<!\S)\((?!\S)', Comment.Multiline, '#push'), # nested comments
            (r'(?<!\S)\)(?!\S)', Comment.Multiline, '#pop'), # nested comments
            (r'(\S[()]|[()]\S|[^()])+', Comment.Multiline), # comments
        ],
        'root': [
            (r'\s+', Whitespace), # spaces
            (r'(?<!\S)\((?!\S)', Comment.Multiline, 'comment'), # comments
            (words(instructions, prefix=r'(?<!\S)', suffix=r'2?k?r?(?!\S)'), Keyword.Reserved), # instructions
            (r'[][{}](?!\S)', Punctuation), # delimiters
            (r'#([0-9a-f]{2}){1,2}(?!\S)', Number.Hex), # integer
            (r'"\S+', String), # raw string
            (r"'\S(?!\S)", String.Char), # raw char
            (r'([0-9a-f]{2}){1,2}(?!\S)', Literal), # raw integer
            (r'[|$][0-9a-f]{1,4}(?!\S)', Keyword.Declaration), # abs/rel pad
            (r'%\S+', Name.Decorator), # macro
            (r'@\S+', Name.Function), # label
            (r'&\S+', Name.Label), # sublabel
            (r'/\S+', Name.Tag), # spacer
            (r'\.\S+', Name.Variable.Magic), # zero page addr
            (r',\S+', Name.Variable.Instance), # rel addr
            (r';\S+', Name.Variable.Global), # abs addr
            (r':\S+', Literal), # raw addr
            (r'~\S+', Keyword.Namespace), # include
            (r'\S+', Name),
        ]
    }

    def analyse_text(text):
        return '|0100' in text[:500]

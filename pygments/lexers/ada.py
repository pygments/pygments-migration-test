"""
    pygments.lexers.ada
    ~~~~~~~~~~~~~~~~~~~

    Lexers for Ada family languages.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, words, \
    using, this, default
from pygments.util import get_bool_opt, get_list_opt
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Error
from pygments.scanner import Scanner
from pygments.lexers._ada_builtins import KEYWORD_LIST, BUILTIN_LIST

# compatibility import
from pygments.lexers.modula2 import Modula2Lexer

__all__ = ['AdaLexer']


class AdaLexer(RegexLexer):
    """
    For Ada source code.

    .. versionadded:: 1.3
    """

    name = 'Ada'
    aliases = ['ada', 'ada95', 'ada2005']
    filenames = ['*.adb', '*.ads', '*.ada']
    mimetypes = ['text/x-ada']

    flags = re.MULTILINE | re.IGNORECASE

    tokens = {
        'root': [
            (r'[^\S\n]+', Text),
            (r'--.*?\n', Comment.Single),
            (r'[^\S\n]+', Text),
            (r'function|procedure|entry', Keyword.Declaration, 'subprogram'),
            (r'(subtype|type)(\s+)(\w+)',
             bygroups(Keyword.Declaration, Text, Keyword.Type), 'type_def'),
            (r'task|protected', Keyword.Declaration),
            (r'(subtype)(\s+)', bygroups(Keyword.Declaration, Text)),
            (r'(end)(\s+)', bygroups(Keyword.Reserved, Text), 'end'),
            (r'(pragma)(\s+)(\w+)', bygroups(Keyword.Reserved, Text,
                                             Comment.Preproc)),
            (r'(true|false|null)\b', Keyword.Constant),
            # builtin types
            (words(BUILTIN_LIST, suffix=r'\b'), Keyword.Type),
            (r'(and(\s+then)?|in|mod|not|or(\s+else)|rem)\b', Operator.Word),
            (r'generic|private', Keyword.Declaration),
            (r'package', Keyword.Declaration, 'package'),
            (r'array\b', Keyword.Reserved, 'array_def'),
            (r'(with|use)(\s+)', bygroups(Keyword.Namespace, Text), 'import'),
            (r'(\w+)(\s*)(:)(\s*)(constant)',
             bygroups(Name.Constant, Text, Punctuation, Text,
                      Keyword.Reserved)),
            (r'<<\w+>>', Name.Label),
            (r'(\w+)(\s*)(:)(\s*)(declare|begin|loop|for|while)',
             bygroups(Name.Label, Text, Punctuation, Text, Keyword.Reserved)),
            # keywords
            (words(KEYWORD_LIST, prefix=r'\b', suffix=r'\b'),
             Keyword.Reserved),
            (r'"[^"]*"', String),
            include('attribute'),
            include('numbers'),
            (r"'[^']'", String.Character),
            (r'(\w+)(\s*|[(,])', bygroups(Name, using(this))),
            (r"(<>|=>|:=|@|[\[\]]|[()|:;,.'])", Punctuation),
            (r'[*<>+=/&-]', Operator),
            (r'\n+', Text),
        ],
        'numbers': [
            (r'[0-9_]+#[0-9a-f_\.]+#', Number.Hex),
            (r'[0-9_]+\.[0-9_]*', Number.Float),
            (r'[0-9_]+', Number.Integer),
        ],
        'attribute': [
            (r"(')(\w+)", bygroups(Punctuation, Name.Attribute)),
        ],
        'subprogram': [
            (r'\(', Punctuation, ('#pop', 'formal_part')),
            (r';', Punctuation, '#pop'),
            (r'is\b', Keyword.Reserved, '#pop'),
            (r'"[^"]+"|\w+', Name.Function),
            include('root'),
        ],
        'end': [
            ('(if|case|record|loop|select)', Keyword.Reserved),
            (r'"[^"]+"|[\w.]+', Name.Function),
            (r'\s+', Text),
            (';', Punctuation, '#pop'),
        ],
        'type_def': [
            (r';', Punctuation, '#pop'),
            (r'\(', Punctuation, 'formal_part'),
            (r'\[', Punctuation, 'formal_part'),
            (r'with|and|use', Keyword.Reserved),
            (r'array\b', Keyword.Reserved, ('#pop', 'array_def')),
            (r'record\b', Keyword.Reserved, ('record_def')),
            (r'(null record)(;)', bygroups(Keyword.Reserved, Punctuation), '#pop'),
            include('root'),
        ],
        'array_def': [
            (r';', Punctuation, '#pop'),
            (r'(\w+)(\s+)(range)', bygroups(Keyword.Type, Text, Keyword.Reserved)),
            include('root'),
        ],
        'record_def': [
            (r'end record', Keyword.Reserved, '#pop'),
            include('root'),
        ],
        'import': [
            (r'[\w.]+', Name, '#pop'),
            default('#pop'),
        ],
        'formal_part': [
            (r'\)', Punctuation, '#pop'),
            (r'\]', Punctuation, '#pop'),
            (r'\w+', Name.Variable),
            (r',|:[^=]', Punctuation),
            (r'(in|not|null|out|access)\b', Keyword.Reserved),
            include('root'),
        ],
        'package': [
            ('body', Keyword.Declaration),
            (r'is\s+new|renames', Keyword.Reserved),
            ('is', Keyword.Reserved, '#pop'),
            (';', Punctuation, '#pop'),
            (r'\(', Punctuation, 'package_instantiation'),
            (r'([\w.]+)', Name.Class),
            include('root'),
        ],
        'package_instantiation': [
            (r'("[^"]+"|\w+)(\s+)(=>)', bygroups(Name.Variable, Text, Punctuation)),
            (r'[\w.\'"]', Text),
            (r'\)', Punctuation, '#pop'),
            include('root'),
        ],
    }

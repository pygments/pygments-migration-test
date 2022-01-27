"""
    pygments.lexers.floscript
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for FloScript

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Whitespace

__all__ = ['FloScriptLexer']


class FloScriptLexer(RegexLexer):
    """
    For `FloScript <https://github.com/ioflo/ioflo>`_ configuration language source code.

    .. versionadded:: 2.4
    """

    name = 'FloScript'
    aliases = ['floscript', 'flo']
    filenames = ['*.flo']

    def innerstring_rules(ttype):
        return [
            # the old style '%s' % (...) string formatting
            (r'%(\(\w+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?'
             '[hlL]?[E-GXc-giorsux%]', String.Interpol),
            # backslashes, quotes and formatting signs must be parsed one at a time
            (r'[^\\\'"%\n]+', ttype),
            (r'[\'"\\]', ttype),
            # unhandled string formatting sign
            (r'%', ttype),
            # newlines are an error (use "nl" state)
        ]

    tokens = {
        'root': [
            (r'\s+', Whitespace),

            (r'[]{}:(),;[]', Punctuation),
            (r'(\\)(\n)', bygroups(Text, Whitespace)),
            (r'\\', Text),
            (r'(to|by|with|from|per|for|cum|qua|via|as|at|in|of|on|re|is|if|be|into|'
             r'and|not)\b', Operator.Word),
            (r'!=|==|<<|>>|[-~+/*%=<>&^|.]', Operator),
            (r'(load|init|server|logger|log|loggee|first|over|under|next|done|timeout|'
             r'repeat|native|benter|enter|recur|exit|precur|renter|rexit|print|put|inc|'
             r'copy|set|aux|rear|raze|go|let|do|bid|ready|start|stop|run|abort|use|flo|'
             r'give|take)\b', Name.Builtin),
            (r'(frame|framer|house)\b', Keyword),
            ('"', String, 'string'),

            include('name'),
            include('numbers'),
            (r'#.+$', Comment.Single),
        ],
        'string': [
            ('[^"]+', String),
            ('"', String, '#pop'),
        ],
        'numbers': [
            (r'(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?j?', Number.Float),
            (r'\d+[eE][+-]?[0-9]+j?', Number.Float),
            (r'0[0-7]+j?', Number.Oct),
            (r'0[bB][01]+', Number.Bin),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),
            (r'\d+L', Number.Integer.Long),
            (r'\d+j?', Number.Integer)
        ],

        'name': [
            (r'@[\w.]+', Name.Decorator),
            (r'[a-zA-Z_]\w*', Name),
        ],
    }

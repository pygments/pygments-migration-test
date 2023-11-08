"""
    pygments.lexers.tact
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Tact.

    :copyright: Copyright 2006-2023 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Comment, Operator, Keyword, Name, String, \
    Number, Whitespace, Punctuation

__all__ = ['TactLexer']


class TactLexer(RegexLexer):
    """
    For Tact source code.

    .. versionadded:: 2.17.0
    """

    name = 'Tact'
    aliases = ['tact']
    filenames = ['*.tact']
    url = "https://tact-lang.org"

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'[.;(),\[\]{}]', Punctuation),
            (r'\?|!!', Operator),
            include('comments'),
            include('import-in'),
            include('struct-in'),
            include('contract-or-trait-in'),
            include('annotation-in'),
            include('fun-declaration-in'),
            include('const-declaration-in'),
            include('statements'),
        ],
        'import-in': [
            (r'((?<=\.\.\.)|(?<![.$]))\b(import)\b(\s*)', bygroups(Punctuation, Keyword, Whitespace), 'import'),
        ],
        'import': [
            (r'\s*;', Punctuation, '#pop'),
            include('comments'),
            include('string-in'),
            (r'\s+', Whitespace),
        ],
        'struct-in': [
            (r'((?<=\.\.\.)|(?<![.$]))\b(struct|message)\b', bygroups(Punctuation, Keyword), 'struct'),
        ],
        'struct': [
            (r'(?<=\})', Punctuation, '#pop'),
            include('comments'),
            include('struct-header'),
            include('struct-body-in'),
            (r'\s+', Whitespace),
        ],
        'struct-header': [
            include('comments'),
            (r'\b[\w]+\b', Name.Class),
            (r'\(((?:\b0(?:x|X)[0-9a-fA-F][0-9a-fA-F_]*\b)|(?:\b[0-9]+\b))\)', Number),
        ],
        'struct-body-in': [
            (r'\{', Punctuation, 'struct-body'),
        ],
        'struct-body': [
            (r'\}', Punctuation, '#pop'),
            include('comments'),
            include('field-declaration-in'),
        ],
        'contract-or-trait-in': [
            (r'((?<=\.\.\.)|(?<![.$]))\b(contract|trait)\b', Keyword, 'contract-or-trait'),
        ],
        'contract-or-trait': [
            (r'(?<=\})', Punctuation, '#pop'),
            include('comments'),
            (r'with', Keyword),
            (r'\b[\w]+\b', Name.Class),
            include('contract-or-trait-body-in'),
            (r'\s+', Whitespace),
            (r',', Punctuation),
        ],
        'contract-or-trait-body-in': [
            (r'\{', Punctuation, 'contract-or-trait-body'),
        ],
        'contract-or-trait-body': [
            (r'\}', Punctuation, '#pop'),
            include('comments'),
            include('init-declaration-in'),
            include('receive-declaration-in'),
            include('bounce-declaration-in'),
            include('fun-declaration-in'),
            include('const-declaration-in'),
            include('field-declaration-in'),
            (r'\s+', Whitespace),
        ],
        'field-declaration-in': [
            (r'(\b[\w]+\b)', Name.Property, 'field-declaration'),
        ],
        'field-declaration': [
            (r';', Punctuation, '#pop'),
            include('comments'),
            include('type-annotation-in'),
            include('variable-init-in'),
        ],
        'const-declaration-in': [
            (r'(?=\b(?:(?:get|native|extends|mutates|virtual|override|inline|abstract)\s*)*const\b)', Keyword, 'const-declaration'),
        ],
        'const-declaration': [
            (r'(;)', Punctuation, '#pop'),
            (r'const', Keyword),
            (r'\b(get|native|extends|mutates|virtual|override|inline|abstract)\b', Keyword),
            (r'\b[\w]+\b', Name.Constant),
            include('comments'),
            include('type-annotation-in'),
            include('variable-init-in'),
            (r'\s+', Whitespace),
        ],
        'init-declaration-in': [
            (r'(init)', Keyword, 'init-declaration')
        ],
        'init-declaration': [
            (r'(?<=\})', Punctuation, '#pop'),
            include('comments'),
            include('fun-arguments-in'),
            include('block-declaration-in'),
            (r'\s+', Whitespace),
        ],
        'receive-declaration-in': [
            (r'(receive|exernal)', Keyword, 'receive-declaration')
        ],
        'receive-declaration': [
            (r'(?<=\})', Punctuation, '#pop'),
            include('comments'),
            include('fun-arguments-in'),
            include('block-declaration-in'),
        ],
        'bounce-declaration-in': [
            (r'(bounced)', Keyword, 'bounce-declaration')
        ],
        'bounce-declaration': [
            (r'(?<=\})', Punctuation, '#pop'),
            include('comments'),
            include('fun-arguments-in'),
            include('block-declaration-in'),
        ],
        'fun-declaration-in': [
            (r'(?=\b(?:(?:get|native|extends|mutates|virtual|override|inline|abstract)\s*)*fun\b)', Keyword, 'fun-declaration')
        ],
        'fun-declaration': [
            (r'(?<=\}|\;)', Punctuation, '#pop'),
            (r'fun', Keyword),
            (r'\b(get|native|extends|mutates|virtual|override|inline|abstract)\b', Keyword),
            (r'(\b[\w]+\b)', Name.Function),
            include('fun-declaration-body'),
            (r'[,;]', Punctuation),
        ],
        'fun-declaration-body': [
            include('comments'),
            include('fun-arguments-in'),
            include('type-annotation-in'),
            include('block-declaration-in'),
            (r'\s+', Whitespace),
        ],
        'fun-arguments-in': [
            (r'\(', Punctuation, 'fun-arguments'),
        ],
        'fun-arguments': [
            (r'\)', Punctuation, '#pop'),
            include('comments'),
            include('string-in'),
            include('type-annotation-in'),
            (r'(self)|(\b[\w]+\b)', Name.Variable),
            (r',', Punctuation),
            (r'\s+', Whitespace),
        ],
        'block-declaration-in': [
            (r'\{', Punctuation, 'block-declaration')
        ],
        'block-declaration': [
            (r'\}', Punctuation, '#pop'),
            include('statements'),
        ],
        'statements': [
            include('comments'),
            include('block-declaration-in'),
            include('expressions'),
        ],
        'annotation-in': [
            (r'(@)([\w_]+)(\()', bygroups(Keyword.Pseudo, Keyword, Punctuation), 'annotation')
        ],
        'annotation': [
            (r'\)', Punctuation, '#pop'),
            include('annotation-argument'),
            (r'\s+', Whitespace),
        ],
        'annotation-argument': [
            (r'[\w_]+', Name.Function.Magic),
        ],
        'expressions': [
            include('comments'),
            include('type-annotation-in'),
            include('keywords'),
            include('numeric'),
            include('string-in'),
            include('variable'),
            include('function-call'),
            include('struct-init-in'),
        ],
        'struct-init-in': [
            (r'(\b[\w]+\b)\s*(\{)', bygroups(Name.Class, Punctuation), 'struct-init')
        ],
        'struct-init': [
            (r'(})', Punctuation, '#pop'),
            include('comments'),
            include('struct-property-in'),
            (r'\s+', Whitespace),
            (r',', Punctuation),
        ],
        'struct-property-in': [
            (r'(\b[\w]+\b)\s*(:)', bygroups(Name.Property, Punctuation), 'struct-property')
        ],
        'struct-property': [
            (r'(?=\}|\,)', Punctuation, '#pop'),
            include('comments'),
            include('expressions'),
            (r'\s+', Whitespace),
        ],
        'variable-init-in': [
            (r'(=)', Operator, 'variable-init')
        ],
        'variable-init': [
            (r'(?=\}|\{|\,|\;)',Punctuation, '#pop'),
            include('comments'),
            include('expressions'),
            (r'\s+', Whitespace),
        ],
        'type-annotation-in': [
            (r'(:)\s+', Punctuation, 'type-annotation')
        ],
        'type-annotation': [
            (r'(?=\{|\;|\=|\,|\))', Punctuation, '#pop'),
            include('comments'),
            include('type-as-in'),
            include('type-generic-in'), 
            (r'\?', Operator),
            (r'\b[\w]+\b', Keyword.Type),
            (r'\s+', Whitespace),
        ],
        'type-generic-in': [
            (r'<', Punctuation, 'type-generic'),
        ],
        'type-generic': [
            (r'>', Punctuation, '#pop'),
            include('comments'),
            include('type-as-in'),
            (r'\b[\w]+\b', Keyword.Type),
            (r'\s+', Whitespace),
            (r',', Punctuation),
        ],
        'type-as-in': [
            (r'\b(as)\s+', Keyword, 'type-as'),
        ],
        'type-as': [
            (r'(?=\{|\;|\=|\,|\)|\>)', Punctuation, '#pop'),
            include('comments'),
            (r'\b[\w]+\b', Keyword.Type),
            (r'\s+', Whitespace),
        ],
        'keywords': [
            (r'\b(if|else|while|do|until|repeat|return|extends|mutates|virtual|override|inline|native|let|const|fun|self|is|initOf|map|bounced|get|as)\b', Keyword),
            (r'(<=>|>=|<=|!=|==|\^>>|~>>|>>|<<|\/%|\^%|~%|\^\/|~\/|\+=|-=|\*=|\/=|~\/=|\^\/=|%=|\^%=|<<=|>>=|~>>=|\^>>=|&=|\|=|\^=|\^|=|~|\/|%|-|\*|\+|>|<|&|\||:|\?)(?=\s)', Operator),
            (r'\b(true|false)\b', Keyword.Constant),
        ],
        'string-in': [
            (r'"', String, 'string'),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\.', String.Escape),
            (r'[^\\"]+', String.Double),
        ],
        'numeric': [
            (r'(?:\b0(?:x|X)[0-9a-fA-F][0-9a-fA-F_]*\b)|(?:\b[0-9]+\b)', Number)
        ],
        'comments': [
            (r'//(.*)', Comment.Single),
            (r'/\*', Comment.Multiline, 'comments-multiline'),
        ],
        'comments-multiline': [
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[^*]+', Comment.Multiline),
            (r'[*]', Comment.Multiline),
        ],
        'variable': [
            (r'\b[\w]+\b(?!\s*\()(?!\s*\{)', Name.Variable)
        ],
        'function-call': [
            (r'\b[\w]+\b(?=\s*\()(?!\s*\{)', Name.Function)
        ],
    }
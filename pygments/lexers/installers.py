"""
    pygments.lexers.installers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for installer/packager DSLs and formats.

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, using, this, default
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Punctuation, Generic, Number, Whitespace

__all__ = ['NSISLexer', 'RPMSpecLexer', 'SourcesListLexer',
           'DebianControlLexer']


class NSISLexer(RegexLexer):
    """
    For `NSIS <http://nsis.sourceforge.net/>`_ scripts.

    .. versionadded:: 1.6
    """
    name = 'NSIS'
    aliases = ['nsis', 'nsi', 'nsh']
    filenames = ['*.nsi', '*.nsh']
    mimetypes = ['text/x-nsis']

    flags = re.IGNORECASE

    tokens = {
        'root': [
            (r'[;#].*\n', Comment),
            (r"'.*?'", String.Single),
            (r'"', String.Double, 'str_double'),
            (r'`', String.Backtick, 'str_backtick'),
            include('macro'),
            include('interpol'),
            include('basic'),
            (r'\$\{[a-z_|][\w|]*\}', Keyword.Pseudo),
            (r'/[a-z_]\w*', Name.Attribute),
            ('.', Text),
        ],
        'basic': [
            (r'(\n)(Function)(\s+)([._a-z][.\w]*)\b',
             bygroups(Text, Keyword, Text, Name.Function)),
            (r'\b([_a-z]\w*)(::)([a-z][a-z0-9]*)\b',
             bygroups(Keyword.Namespace, Punctuation, Name.Function)),
            (r'\b([_a-z]\w*)(:)', bygroups(Name.Label, Punctuation)),
            (r'(\b[ULS]|\B)([!<>=]?=|\<\>?|\>)\B', Operator),
            (r'[|+-]', Operator),
            (r'\\', Punctuation),
            (r'\b(Abort|Add(?:BrandingImage|Size)|'
             r'Allow(?:RootDirInstall|SkipFiles)|AutoCloseWindow|'
             r'BG(?:Font|Gradient)|BrandingText|BringToFront|Call(?:InstDLL)?|'
             r'(?:Sub)?Caption|ChangeUI|CheckBitmap|ClearErrors|CompletedText|'
             r'ComponentText|CopyFiles|CRCCheck|'
             r'Create(?:Directory|Font|Shortcut)|Delete(?:INI(?:Sec|Str)|'
             r'Reg(?:Key|Value))?|DetailPrint|DetailsButtonText|'
             r'Dir(?:Show|Text|Var|Verify)|(?:Disabled|Enabled)Bitmap|'
             r'EnableWindow|EnumReg(?:Key|Value)|Exch|Exec(?:Shell|Wait)?|'
             r'ExpandEnvStrings|File(?:BufSize|Close|ErrorText|Open|'
             r'Read(?:Byte)?|Seek|Write(?:Byte)?)?|'
             r'Find(?:Close|First|Next|Window)|FlushINI|Function(?:End)?|'
             r'Get(?:CurInstType|CurrentAddress|DlgItem|DLLVersion(?:Local)?|'
             r'ErrorLevel|FileTime(?:Local)?|FullPathName|FunctionAddress|'
             r'InstDirError|LabelAddress|TempFileName)|'
             r'Goto|HideWindow|Icon|'
             r'If(?:Abort|Errors|FileExists|RebootFlag|Silent)|'
             r'InitPluginsDir|Install(?:ButtonText|Colors|Dir(?:RegKey)?)|'
             r'Inst(?:ProgressFlags|Type(?:[GS]etText)?)|Int(?:CmpU?|Fmt|Op)|'
             r'IsWindow|LangString(?:UP)?|'
             r'License(?:BkColor|Data|ForceSelection|LangString|Text)|'
             r'LoadLanguageFile|LockWindow|Log(?:Set|Text)|MessageBox|'
             r'MiscButtonText|Name|Nop|OutFile|(?:Uninst)?Page(?:Ex(?:End)?)?|'
             r'PluginDir|Pop|Push|Quit|Read(?:(?:Env|INI|Reg)Str|RegDWORD)|'
             r'Reboot|(?:Un)?RegDLL|Rename|RequestExecutionLevel|ReserveFile|'
             r'Return|RMDir|SearchPath|Section(?:Divider|End|'
             r'(?:(?:Get|Set)(?:Flags|InstTypes|Size|Text))|Group(?:End)?|In)?|'
             r'SendMessage|Set(?:AutoClose|BrandingImage|Compress(?:ionLevel|'
             r'or(?:DictSize)?)?|CtlColors|CurInstType|DatablockOptimize|'
             r'DateSave|Details(?:Print|View)|Error(?:s|Level)|FileAttributes|'
             r'Font|OutPath|Overwrite|PluginUnload|RebootFlag|ShellVarContext|'
             r'Silent|StaticBkColor)|'
             r'Show(?:(?:I|Uni)nstDetails|Window)|Silent(?:Un)?Install|Sleep|'
             r'SpaceTexts|Str(?:CmpS?|Cpy|Len)|SubSection(?:End)?|'
             r'Uninstall(?:ButtonText|(?:Sub)?Caption|EXEName|Icon|Text)|'
             r'UninstPage|Var|VI(?:AddVersionKey|ProductVersion)|WindowIcon|'
             r'Write(?:INIStr|Reg(:?Bin|DWORD|(?:Expand)?Str)|Uninstaller)|'
             r'XPStyle)\b', Keyword),
            (r'\b(CUR|END|(?:FILE_ATTRIBUTE_)?'
             r'(?:ARCHIVE|HIDDEN|NORMAL|OFFLINE|READONLY|SYSTEM|TEMPORARY)|'
             r'HK(CC|CR|CU|DD|LM|PD|U)|'
             r'HKEY_(?:CLASSES_ROOT|CURRENT_(?:CONFIG|USER)|DYN_DATA|'
             r'LOCAL_MACHINE|PERFORMANCE_DATA|USERS)|'
             r'ID(?:ABORT|CANCEL|IGNORE|NO|OK|RETRY|YES)|'
             r'MB_(?:ABORTRETRYIGNORE|DEFBUTTON[1-4]|'
             r'ICON(?:EXCLAMATION|INFORMATION|QUESTION|STOP)|'
             r'OK(?:CANCEL)?|RETRYCANCEL|RIGHT|SETFOREGROUND|TOPMOST|USERICON|'
             r'YESNO(?:CANCEL)?)|SET|SHCTX|'
             r'SW_(?:HIDE|SHOW(?:MAXIMIZED|MINIMIZED|NORMAL))|'
             r'admin|all|auto|both|bottom|bzip2|checkbox|colored|current|false|'
             r'force|hide|highest|if(?:diff|newer)|lastused|leave|left|'
             r'listonly|lzma|nevershow|none|normal|off|on|pop|push|'
             r'radiobuttons|right|show|silent|silentlog|smooth|textonly|top|'
             r'true|try|user|zlib)\b', Name.Constant),
        ],
        'macro': [
            (r'\!(addincludedir(?:dir)?|addplugindir|appendfile|cd|define|'
             r'delfilefile|echo(?:message)?|else|endif|error|execute|'
             r'if(?:macro)?n?(?:def)?|include|insertmacro|macro(?:end)?|packhdr|'
             r'search(?:parse|replace)|system|tempfilesymbol|undef|verbose|'
             r'warning)\b', Comment.Preproc),
        ],
        'interpol': [
            (r'\$(R?[0-9])', Name.Builtin.Pseudo),    # registers
            (r'\$(ADMINTOOLS|APPDATA|CDBURN_AREA|COOKIES|COMMONFILES(?:32|64)|'
             r'DESKTOP|DOCUMENTS|EXE(?:DIR|FILE|PATH)|FAVORITES|FONTS|HISTORY|'
             r'HWNDPARENT|INTERNET_CACHE|LOCALAPPDATA|MUSIC|NETHOOD|PICTURES|'
             r'PLUGINSDIR|PRINTHOOD|PROFILE|PROGRAMFILES(?:32|64)|QUICKLAUNCH|'
             r'RECENT|RESOURCES(?:_LOCALIZED)?|SENDTO|SM(?:PROGRAMS|STARTUP)|'
             r'STARTMENU|SYSDIR|TEMP(?:LATES)?|VIDEOS|WINDIR|\{NSISDIR\})',
             Name.Builtin),
            (r'\$(CMDLINE|INSTDIR|OUTDIR|LANGUAGE)', Name.Variable.Global),
            (r'\$[a-z_]\w*', Name.Variable),
        ],
        'str_double': [
            (r'"', String, '#pop'),
            (r'\$(\\[nrt"]|\$)', String.Escape),
            include('interpol'),
            (r'.', String.Double),
        ],
        'str_backtick': [
            (r'`', String, '#pop'),
            (r'\$(\\[nrt"]|\$)', String.Escape),
            include('interpol'),
            (r'.', String.Double),
        ],
    }


class RPMSpecLexer(RegexLexer):
    """
    For RPM ``.spec`` files.

    .. versionadded:: 1.6
    """

    name = 'RPMSpec'
    aliases = ['spec']
    filenames = ['*.spec']
    mimetypes = ['text/x-rpm-spec']

    _directives = ('(?:package|prep|build|install|clean|check|pre[a-z]*|'
                   'post[a-z]*|trigger[a-z]*|files)')

    tokens = {
        'root': [
            (r'#.*\n', Comment),
            include('basic'),
        ],
        'description': [
            (r'^(%' + _directives + ')(.*)$',
             bygroups(Name.Decorator, Text), '#pop'),
            (r'\n', Text),
            (r'.', Text),
        ],
        'changelog': [
            (r'\*.*\n', Generic.Subheading),
            (r'^(%' + _directives + ')(.*)$',
             bygroups(Name.Decorator, Text), '#pop'),
            (r'\n', Text),
            (r'.', Text),
        ],
        'string': [
            (r'"', String.Double, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            include('interpol'),
            (r'.', String.Double),
        ],
        'basic': [
            include('macro'),
            (r'(?i)^(Name|Version|Release|Epoch|Summary|Group|License|Packager|'
             r'Vendor|Icon|URL|Distribution|Prefix|Patch[0-9]*|Source[0-9]*|'
             r'Requires\(?[a-z]*\)?|[a-z]+Req|Obsoletes|Suggests|Provides|Conflicts|'
             r'Build[a-z]+|[a-z]+Arch|Auto[a-z]+)(:)(.*)$',
             bygroups(Generic.Heading, Punctuation, using(this))),
            (r'^%description', Name.Decorator, 'description'),
            (r'^%changelog', Name.Decorator, 'changelog'),
            (r'^(%' + _directives + ')(.*)$', bygroups(Name.Decorator, Text)),
            (r'%(attr|defattr|dir|doc(?:dir)?|setup|config(?:ure)?|'
             r'make(?:install)|ghost|patch[0-9]+|find_lang|exclude|verify)',
             Keyword),
            include('interpol'),
            (r"'.*?'", String.Single),
            (r'"', String.Double, 'string'),
            (r'.', Text),
        ],
        'macro': [
            (r'%define.*\n', Comment.Preproc),
            (r'%\{\!\?.*%define.*\}', Comment.Preproc),
            (r'(%(?:if(?:n?arch)?|else(?:if)?|endif))(.*)$',
             bygroups(Comment.Preproc, Text)),
        ],
        'interpol': [
            (r'%\{?__[a-z_]+\}?', Name.Function),
            (r'%\{?_([a-z_]+dir|[a-z_]+path|prefix)\}?', Keyword.Pseudo),
            (r'%\{\?\w+\}', Name.Variable),
            (r'\$\{?RPM_[A-Z0-9_]+\}?', Name.Variable.Global),
            (r'%\{[a-zA-Z]\w+\}', Keyword.Constant),
        ]
    }


class SourcesListLexer(RegexLexer):
    """
    Lexer that highlights debian sources.list files.

    .. versionadded:: 0.7
    """

    name = 'Debian Sourcelist'
    aliases = ['debsources', 'sourceslist', 'sources.list']
    filenames = ['sources.list']
    mimetype = ['application/x-debian-sourceslist']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'#.*?$', Comment),
            (r'^(deb(?:-src)?)(\s+)',
             bygroups(Keyword, Text), 'distribution')
        ],
        'distribution': [
            (r'#.*?$', Comment, '#pop'),
            (r'\$\(ARCH\)', Name.Variable),
            (r'[^\s$[]+', String),
            (r'\[', String.Other, 'escaped-distribution'),
            (r'\$', String),
            (r'\s+', Text, 'components')
        ],
        'escaped-distribution': [
            (r'\]', String.Other, '#pop'),
            (r'\$\(ARCH\)', Name.Variable),
            (r'[^\]$]+', String.Other),
            (r'\$', String.Other)
        ],
        'components': [
            (r'#.*?$', Comment, '#pop:2'),
            (r'$', Text, '#pop:2'),
            (r'\s+', Text),
            (r'\S+', Keyword.Pseudo),
        ]
    }

    def analyse_text(text):
        for line in text.splitlines():
            line = line.strip()
            if line.startswith('deb ') or line.startswith('deb-src '):
                return True


class DebianControlLexer(RegexLexer):
    """
    Lexer for Debian ``control`` files and ``apt-cache show <pkg>`` outputs.

    Specification of `control`` files is available at
    https://www.debian.org/doc/debian-policy/ch-controlfields.html

    .. versionadded:: 0.9
    """
    name = 'Debian Control file'
    aliases = ['debcontrol', 'control']
    filenames = ['control']

    tokens = {
        'root': [
            (r'^(Description)', Keyword, 'description'),
            (r'^(Maintainer)(:\s*)', bygroups(Keyword, Text), 'maintainer'),
            (r'^((Build-|Pre-)?Depends(-Indep|-Arch)?)', Keyword, 'depends'),
            (r'^(Recommends|Suggests|Enhances)', Keyword, 'depends'),
            (r'^((?:Python-)?Version)(:\s*)(\S+)$',
             bygroups(Keyword, Text, Number)),
            (r'^((?:Installed-)?Size)(:\s*)(\S+)$',
             bygroups(Keyword, Text, Number)),
            (r'^(MD5Sum|SHA1|SHA256)(:\s*)(\S+)$',
             bygroups(Keyword, Text, Number)),
            (r'^([a-zA-Z\-0-9\.]*?)(:\s*)(.*?)$',
             bygroups(Keyword, Whitespace, String)),
        ],
        'maintainer': [
            (r'<[^>]+>', Generic.Strong),
            (r'<[^>]+>$', Generic.Strong, '#pop'),
            (r',\n?', Text),
            (r'.', Text),
        ],
        'description': [
            (r'(.*)(Homepage)(: )(\S+)',
             bygroups(Text, String, Name, Name.Class)),
            (r':.*\n', Generic.Strong),
            (r' .*\n', Text),
            default('#pop'),
        ],
        'depends': [
            (r':\s*', Text),
            (r'(\$)(\{)(\w+\s*:\s*\w+)', bygroups(Operator, Text, Name.Entity)),
            (r'\(', Text, 'depend_vers'),
            (r',', Text),
            (r'\|', Operator),
            (r'[\s]+', Text),
            (r'[})]\s*$', Text, '#pop'),
            (r'\}', Text),
            (r'[^,]$', Name.Function, '#pop'),
            (r'([+.a-zA-Z0-9-])(\s*)', bygroups(Name.Function, Text)),
            (r'\[.*?\]', Name.Entity),
        ],
        'depend_vers': [
            (r'\),', Text, '#pop'),
            (r'\)[^,]', Text, '#pop:2'),
            (r'([><=]+)(\s*)([^)]+)', bygroups(Operator, Text, Number))
        ]
    }

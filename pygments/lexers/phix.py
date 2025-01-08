"""
    pygments.lexers.phix
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Phix.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
import typing

from pygments.lexer import RegexLexer, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Whitespace

__all__ = ['PhixLexer']


class PhixLexer(RegexLexer):
    """
    Pygments Lexer for Phix files (.exw).
    See http://phix.x10.mx
    """

    name = 'Phix'
    url = 'http://phix.x10.mx'
    aliases = ['phix']
    filenames = ['*.exw']
    mimetypes = ['text/x-phix']
    version_added = '2.14'

    flags = re.MULTILINE    # nb: **NOT** re.DOTALL! (totally spanners comment handling)

    preproc = (
        'ifdef', 'elsifdef', 'elsedef'
    )
    # Note these lists are auto-generated by pwa/p2js.exw, when pwa\src\p2js_keywords.e (etc)
    #     change, though of course subsequent copy/commit/pull requests are all manual steps.
    types = (
        'string', 'nullable_string', 'atom_string', 'atom', 'bool', 'boolean',
        'cdCanvan', 'cdCanvas', 'complex', 'CURLcode', 'dictionary', 'int',
        'integer', 'Ihandle', 'Ihandles', 'Ihandln', 'mpfr', 'mpq', 'mpz',
        'mpz_or_string', 'number', 'rid_string', 'seq', 'sequence', 'timedate',
        'object'
    )
    keywords = (
        'abstract', 'class', 'continue', 'export', 'extends', 'nullable',
        'private', 'public', 'static', 'struct', 'trace',
        'and', 'break', 'by', 'case', 'catch', 'const', 'constant', 'debug',
        'default', 'do', 'else', 'elsif', 'end', 'enum', 'exit', 'fallthru',
        'fallthrough', 'for', 'forward', 'function', 'global', 'if', 'in',
        'include', 'js', 'javascript', 'javascript_semantics', 'let', 'not',
        'or', 'procedure', 'profile', 'profile_time', 'return', 'safe_mode',
        'switch', 'then', 'to', 'try', 'type', 'type_check', 'until', 'warning',
        'while', 'with', 'without', 'xor'
    )
    routines = (
        'abort', 'abs', 'adjust_timedate', 'and_bits', 'and_bitsu', 'apply',
        'append', 'arccos', 'arcsin', 'arctan', 'assert', 'atan2',
        'atom_to_float32', 'atom_to_float64', 'bankers_rounding', 'beep',
        'begins', 'binary_search', 'bits_to_int', 'bk_color', 'bytes_to_int',
        'call_func', 'call_proc', 'cdCanvasActivate', 'cdCanvasArc',
        'cdCanvasBegin', 'cdCanvasBox', 'cdCanvasChord', 'cdCanvasCircle',
        'cdCanvasClear', 'cdCanvasEnd', 'cdCanvasFlush', 'cdCanvasFont',
        'cdCanvasGetImageRGB', 'cdCanvasGetSize', 'cdCanvasGetTextAlignment',
        'cdCanvasGetTextSize', 'cdCanvasLine', 'cdCanvasMark',
        'cdCanvasMarkSize', 'cdCanvasMultiLineVectorText', 'cdCanvasPixel',
        'cdCanvasRect', 'cdCanvasRoundedBox', 'cdCanvasRoundedRect',
        'cdCanvasSector', 'cdCanvasSetAttribute', 'cdCanvasSetBackground',
        'cdCanvasSetFillMode', 'cdCanvasSetForeground',
        'cdCanvasSetInteriorStyle', 'cdCanvasSetLineStyle',
        'cdCanvasSetLineWidth', 'cdCanvasSetTextAlignment', 'cdCanvasText',
        'cdCanvasSetTextOrientation', 'cdCanvasGetTextOrientation',
        'cdCanvasVectorText', 'cdCanvasVectorTextDirection',
        'cdCanvasVectorTextSize', 'cdCanvasVertex', 'cdCreateCanvas',
        'cdDecodeAlpha', 'cdDecodeColor', 'cdDecodeColorAlpha', 'cdEncodeAlpha',
        'cdEncodeColor', 'cdEncodeColorAlpha', 'cdKillCanvas', 'cdVersion',
        'cdVersionDate', 'ceil', 'change_timezone', 'choose', 'clear_screen',
        'columnize', 'command_line', 'compare', 'complex_abs', 'complex_add',
        'complex_arg', 'complex_conjugate', 'complex_cos', 'complex_cosh',
        'complex_div', 'complex_exp', 'complex_imag', 'complex_inv',
        'complex_log', 'complex_mul', 'complex_neg', 'complex_new',
        'complex_norm', 'complex_power', 'complex_rho', 'complex_real',
        'complex_round', 'complex_sin', 'complex_sinh', 'complex_sprint',
        'complex_sqrt', 'complex_sub', 'complex_theta', 'concat', 'cos',
        'crash', 'custom_sort', 'date', 'day_of_week', 'day_of_year',
        'days_in_month', 'decode_base64', 'decode_flags', 'deep_copy', 'deld',
        'deserialize', 'destroy_dict', 'destroy_queue', 'destroy_stack',
        'dict_name', 'dict_size', 'elapsed', 'elapsed_short', 'encode_base64',
        'equal', 'even', 'exp', 'extract', 'factorial', 'factors',
        'file_size_k', 'find', 'find_all', 'find_any', 'find_replace', 'filter',
        'flatten', 'float32_to_atom', 'float64_to_atom', 'floor',
        'format_timedate', 'free_console', 'from_polar', 'gcd', 'get_file_base',
        'get_file_extension', 'get_file_name', 'get_file_name_and_path',
        'get_file_path', 'get_file_path_and_name', 'get_maxprime', 'get_prime',
        'get_primes', 'get_primes_le', 'get_proper_dir', 'get_proper_path',
        'get_rand', 'get_routine_info', 'get_test_abort', 'get_test_logfile',
        'get_test_pause', 'get_test_verbosity', 'get_tzid', 'getd', 'getdd',
        'getd_all_keys', 'getd_by_index', 'getd_index', 'getd_partial_key',
        'glAttachShader', 'glBindBuffer', 'glBindTexture', 'glBufferData',
        'glCanvasSpecialText', 'glClear', 'glClearColor', 'glColor',
        'glCompileShader', 'glCreateBuffer', 'glCreateProgram',
        'glCreateShader', 'glCreateTexture', 'glDeleteProgram',
        'glDeleteShader', 'glDrawArrays', 'glEnable',
        'glEnableVertexAttribArray', 'glFloat32Array', 'glInt32Array',
        'glFlush', 'glGetAttribLocation', 'glGetError', 'glGetProgramInfoLog',
        'glGetProgramParameter', 'glGetShaderInfoLog', 'glGetShaderParameter',
        'glGetUniformLocation', 'glLinkProgram', 'glLoadIdentity',
        'glMatrixMode', 'glOrtho', 'glRotatef', 'glShadeModel',
        'glShaderSource', 'glSimpleA7texcoords', 'glTexImage2Dc',
        'glTexParameteri', 'glTranslate', 'glUniform1f', 'glUniform1i',
        'glUniformMatrix4fv', 'glUseProgram', 'glVertex',
        'glVertexAttribPointer', 'glViewport', 'head', 'hsv_to_rgb', 'iff',
        'iif', 'include_file', 'incl0de_file', 'insert', 'instance',
        'int_to_bits', 'int_to_bytes', 'is_dict', 'is_integer', 's_leap_year',
        'is_prime', 'is_prime2', 'islower', 'isupper', 'Icallback',
        'iup_isdouble', 'iup_isprint', 'iup_XkeyBase', 'IupAppend', 'IupAlarm',
        'IupBackgroundBox', 'IupButton', 'IupCalendar', 'IupCanvas',
        'IupClipboard', 'IupClose', 'IupCloseOnEscape', 'IupControlsOpen',
        'IupDatePick', 'IupDestroy', 'IupDialog', 'IupDrawArc', 'IupDrawBegin',
        'IupDrawEnd', 'IupDrawGetSize', 'IupDrawGetTextSize', 'IupDrawLine',
        'IupDrawRectangle', 'IupDrawText', 'IupExpander', 'IupFill',
        'IupFlatLabel', 'IupFlatList', 'IupFlatTree', 'IupFlush', 'IupFrame',
        'IupGetAttribute', 'IupGetAttributeId', 'IupGetAttributePtr',
        'IupGetBrother', 'IupGetChild', 'IupGetChildCount', 'IupGetClassName',
        'IupGetDialog', 'IupGetDialogChild', 'IupGetDouble', 'IupGetFocus',
        'IupGetGlobal', 'IupGetGlobalInt', 'IupGetGlobalIntInt', 'IupGetInt',
        'IupGetInt2', 'IupGetIntId', 'IupGetIntInt', 'IupGetParent',
        'IupGLCanvas', 'IupGLCanvasOpen', 'IupGLMakeCurrent', 'IupGraph',
        'IupHbox', 'IupHide', 'IupImage', 'IupImageRGBA', 'IupItem',
        'iupKeyCodeToName', 'IupLabel', 'IupLink', 'IupList', 'IupMap',
        'IupMenu', 'IupMenuItem', 'IupMessage', 'IupMessageDlg', 'IupMultiBox',
        'IupMultiLine', 'IupNextField', 'IupNormaliser', 'IupOpen',
        'IupPlayInput', 'IupPopup', 'IupPreviousField', 'IupProgressBar',
        'IupRadio', 'IupRecordInput', 'IupRedraw', 'IupRefresh',
        'IupRefreshChildren', 'IupSeparator', 'IupSetAttribute',
        'IupSetAttributes', 'IupSetAttributeHandle', 'IupSetAttributeId',
        'IupSetAttributePtr', 'IupSetCallback', 'IupSetCallbacks',
        'IupSetDouble', 'IupSetFocus', 'IupSetGlobal', 'IupSetGlobalInt',
        'IupSetGlobalFunction', 'IupSetHandle', 'IupSetInt',
        'IupSetStrAttribute', 'IupSetStrGlobal', 'IupShow', 'IupShowXY',
        'IupSplit', 'IupStoreAttribute', 'IupSubmenu', 'IupTable',
        'IupTableClearSelected', 'IupTableClick_cb', 'IupTableGetSelected',
        'IupTableResize_cb', 'IupTableSetData', 'IupTabs', 'IupText',
        'IupTimer', 'IupToggle', 'IupTreeAddNodes', 'IupTreeView', 'IupUpdate',
        'IupValuator', 'IupVbox', 'join', 'join_by', 'join_path', 'k_perm',
        'largest', 'lcm', 'length', 'log', 'log10', 'log2', 'lower',
        'm4_crossProduct', 'm4_inverse', 'm4_lookAt', 'm4_multiply',
        'm4_normalize', 'm4_perspective', 'm4_subtractVectors', 'm4_xRotate',
        'm4_yRotate', 'machine_bits', 'machine_word', 'match', 'match_all',
        'match_replace', 'max', 'maxsq', 'min', 'minsq', 'mod', 'mpfr_add',
        'mpfr_ceil', 'mpfr_cmp', 'mpfr_cmp_si', 'mpfr_const_pi', 'mpfr_div',
        'mpfr_div_si', 'mpfr_div_z', 'mpfr_floor', 'mpfr_free', 'mpfr_get_d',
        'mpfr_get_default_precision', 'mpfr_get_default_rounding_mode',
        'mpfr_get_fixed', 'mpfr_get_precision', 'mpfr_get_si', 'mpfr_init',
        'mpfr_inits', 'mpfr_init_set', 'mpfr_init_set_q', 'mpfr_init_set_z',
        'mpfr_mul', 'mpfr_mul_si', 'mpfr_pow_si', 'mpfr_set', 'mpfr_set_d',
        'mpfr_set_default_precision', 'mpfr_set_default_rounding_mode',
        'mpfr_set_precision', 'mpfr_set_q', 'mpfr_set_si', 'mpfr_set_str',
        'mpfr_set_z', 'mpfr_si_div', 'mpfr_si_sub', 'mpfr_sqrt', 'mpfr_sub',
        'mpfr_sub_si', 'mpq_abs', 'mpq_add', 'mpq_add_si', 'mpq_canonicalize',
        'mpq_cmp', 'mpq_cmp_si', 'mpq_div', 'mpq_div_2exp', 'mpq_free',
        'mpq_get_den', 'mpq_get_num', 'mpq_get_str', 'mpq_init', 'mpq_init_set',
        'mpq_init_set_si', 'mpq_init_set_str', 'mpq_init_set_z', 'mpq_inits',
        'mpq_inv', 'mpq_mul', 'mpq_neg', 'mpq_set', 'mpq_set_si', 'mpq_set_str',
        'mpq_set_z', 'mpq_sub', 'mpz_abs', 'mpz_add', 'mpz_addmul',
        'mpz_addmul_ui', 'mpz_addmul_si', 'mpz_add_si', 'mpz_add_ui', 'mpz_and',
        'mpz_bin_uiui', 'mpz_cdiv_q', 'mpz_cmp', 'mpz_cmp_si', 'mpz_divexact',
        'mpz_divexact_ui', 'mpz_divisible_p', 'mpz_divisible_ui_p', 'mpz_even',
        'mpz_fac_ui', 'mpz_factorstring', 'mpz_fdiv_q', 'mpz_fdiv_q_2exp',
        'mpz_fdiv_q_ui', 'mpz_fdiv_qr', 'mpz_fdiv_r', 'mpz_fdiv_ui',
        'mpz_fib_ui', 'mpz_fib2_ui', 'mpz_fits_atom', 'mpz_fits_integer',
        'mpz_free', 'mpz_gcd', 'mpz_gcd_ui', 'mpz_get_atom', 'mpz_get_integer',
        'mpz_get_short_str', 'mpz_get_str', 'mpz_init', 'mpz_init_set',
        'mpz_inits', 'mpz_invert', 'mpz_lcm', 'mpz_lcm_ui', 'mpz_max',
        'mpz_min', 'mpz_mod', 'mpz_mod_ui', 'mpz_mul', 'mpz_mul_2exp',
        'mpz_mul_d', 'mpz_mul_si', 'mpz_neg', 'mpz_nthroot', 'mpz_odd',
        'mpz_pollard_rho', 'mpz_pow_ui', 'mpz_powm', 'mpz_powm_ui', 'mpz_prime',
        'mpz_prime_factors', 'mpz_prime_mr', 'mpz_rand', 'mpz_rand_ui',
        'mpz_re_compose', 'mpz_remove', 'mpz_scan0', 'mpz_scan1', 'mpz_set',
        'mpz_set_d', 'mpz_set_si', 'mpz_set_str', 'mpz_set_v', 'mpz_sign',
        'mpz_sizeinbase', 'mpz_sqrt', 'mpz_sub', 'mpz_sub_si', 'mpz_sub_ui',
        'mpz_si_sub', 'mpz_tdiv_q_2exp', 'mpz_tdiv_r_2exp', 'mpz_tstbit',
        'mpz_ui_pow_ui', 'mpz_xor', 'named_dict', 'new_dict', 'new_queue',
        'new_stack', 'not_bits', 'not_bitsu', 'odd', 'or_all', 'or_allu',
        'or_bits', 'or_bitsu', 'ord', 'ordinal', 'ordinant',
        'override_timezone', 'pad', 'pad_head', 'pad_tail', 'parse_date_string',
        'papply', 'peep', 'peepn', 'peep_dict', 'permute', 'permutes',
        'platform', 'pop', 'popn', 'pop_dict', 'power', 'pp', 'ppEx', 'ppExf',
        'ppf', 'ppOpt', 'pq_add', 'pq_destroy', 'pq_empty', 'pq_new', 'pq_peek',
        'pq_pop', 'pq_pop_data', 'pq_size', 'prepend', 'prime_factors',
        'printf', 'product', 'proper', 'push', 'pushn', 'putd', 'puts',
        'queue_empty', 'queue_size', 'rand', 'rand_range', 'reinstate',
        'remainder', 'remove', 'remove_all', 'repeat', 'repeatch', 'replace',
        'requires', 'reverse', 'rfind', 'rgb', 'rmatch', 'rmdr', 'rnd', 'round',
        'routine_id', 'scanf', 'serialize', 'series', 'set_rand',
        'set_test_abort', 'set_test_logfile', 'set_test_module',
        'set_test_pause', 'set_test_verbosity', 'set_timedate_formats',
        'set_timezone', 'setd', 'setd_default', 'shorten', 'sha256',
        'shift_bits', 'shuffle', 'sign', 'sin', 'smallest', 'sort',
        'sort_columns', 'speak', 'splice', 'split', 'split_any', 'split_by',
        'sprint', 'sprintf', 'sq_abs', 'sq_add', 'sq_and', 'sq_and_bits',
        'sq_arccos', 'sq_arcsin', 'sq_arctan', 'sq_atom', 'sq_ceil', 'sq_cmp',
        'sq_cos', 'sq_div', 'sq_even', 'sq_eq', 'sq_floor', 'sq_floor_div',
        'sq_ge', 'sq_gt', 'sq_int', 'sq_le', 'sq_log', 'sq_log10', 'sq_log2',
        'sq_lt', 'sq_max', 'sq_min', 'sq_mod', 'sq_mul', 'sq_ne', 'sq_not',
        'sq_not_bits', 'sq_odd', 'sq_or', 'sq_or_bits', 'sq_power', 'sq_rand',
        'sq_remainder', 'sq_rmdr', 'sq_rnd', 'sq_round', 'sq_seq', 'sq_sign',
        'sq_sin', 'sq_sqrt', 'sq_str', 'sq_sub', 'sq_tan', 'sq_trunc',
        'sq_uminus', 'sq_xor', 'sq_xor_bits', 'sqrt', 'square_free',
        'stack_empty', 'stack_size', 'substitute', 'substitute_all', 'sum',
        'tail', 'tan', 'test_equal', 'test_fail', 'test_false',
        'test_not_equal', 'test_pass', 'test_summary', 'test_true',
        'text_color', 'throw', 'time', 'timedate_diff', 'timedelta',
        'to_integer', 'to_number', 'to_rgb', 'to_string', 'traverse_dict',
        'traverse_dict_partial_key', 'trim', 'trim_head', 'trim_tail', 'trunc',
        'tagset', 'tagstart', 'typeof', 'unique', 'unix_dict', 'upper',
        'utf8_to_utf32', 'utf32_to_utf8', 'version', 'vlookup', 'vslice',
        'wglGetProcAddress', 'wildcard_file', 'wildcard_match', 'with_rho',
        'with_theta', 'xml_new_doc', 'xml_new_element', 'xml_set_attribute',
        'xml_sprint', 'xor_bits', 'xor_bitsu',
        'accept', 'allocate', 'allocate_string', 'allow_break', 'ARM',
        'atom_to_float80', 'c_func', 'c_proc', 'call_back', 'chdir',
        'check_break', 'clearDib', 'close', 'closesocket', 'console',
        'copy_file', 'create', 'create_directory', 'create_thread',
        'curl_easy_cleanup', 'curl_easy_get_file', 'curl_easy_init',
        'curl_easy_perform', 'curl_easy_perform_ex', 'curl_easy_setopt',
        'curl_easy_strerror', 'curl_global_cleanup', 'curl_global_init',
        'curl_slist_append', 'curl_slist_free_all', 'current_dir', 'cursor',
        'define_c_func', 'define_c_proc', 'delete', 'delete_cs', 'delete_file',
        'dir', 'DLL', 'drawDib', 'drawShadedPolygonToDib', 'ELF32', 'ELF64',
        'enter_cs', 'eval', 'exit_thread', 'free', 'file_exists', 'final',
        'float80_to_atom', 'format', 'get_bytes', 'get_file_date',
        'get_file_size', 'get_file_type', 'get_interpreter', 'get_key',
        'get_socket_error', 'get_text', 'get_thread_exitcode', 'get_thread_id',
        'getc', 'getenv', 'gets', 'getsockaddr', 'glBegin', 'glCallList',
        'glFrustum', 'glGenLists', 'glGetString', 'glLight', 'glMaterial',
        'glNewList', 'glNormal', 'glPopMatrix', 'glPushMatrix', 'glRotate',
        'glEnd', 'glEndList', 'glTexImage2D', 'goto', 'GUI', 'icons', 'ilASM',
        'include_files', 'include_paths', 'init_cs', 'ip_to_string',
        'IupConfig', 'IupConfigDialogClosed', 'IupConfigDialogShow',
        'IupConfigGetVariableInt', 'IupConfigLoad', 'IupConfigSave',
        'IupConfigSetVariableInt', 'IupExitLoop', 'IupFileDlg', 'IupFileList',
        'IupGLSwapBuffers', 'IupHelp', 'IupLoopStep', 'IupMainLoop',
        'IupNormalizer', 'IupPlot', 'IupPlotAdd', 'IupPlotBegin', 'IupPlotEnd',
        'IupPlotInsert', 'IupSaveImage', 'IupTreeGetUserId', 'IupUser',
        'IupVersion', 'IupVersionDate', 'IupVersionNumber', 'IupVersionShow',
        'killDib', 'leave_cs', 'listen', 'manifest', 'mem_copy', 'mem_set',
        'mpfr_gamma', 'mpfr_printf', 'mpfr_sprintf', 'mpz_export', 'mpz_import',
        'namespace', 'new', 'newDib', 'open', 'open_dll', 'PE32', 'PE64',
        'peek', 'peek_string', 'peek1s', 'peek1u', 'peek2s', 'peek2u', 'peek4s',
        'peek4u', 'peek8s', 'peek8u', 'peekNS', 'peekns', 'peeknu', 'poke',
        'poke2', 'poke4', 'poke8', 'pokeN', 'poke_string', 'poke_wstring',
        'position', 'progress', 'prompt_number', 'prompt_string', 'read_file',
        'read_lines', 'recv', 'resume_thread', 'seek', 'select', 'send',
        'setHandler', 'shutdown', 'sleep', 'SO', 'sockaddr_in', 'socket',
        'split_path', 'suspend_thread', 'system', 'system_exec', 'system_open',
        'system_wait', 'task_clock_start', 'task_clock_stop', 'task_create',
        'task_delay', 'task_list', 'task_schedule', 'task_self', 'task_status',
        'task_suspend', 'task_yield', 'thread_safe_string', 'try_cs',
        'utf8_to_utf16', 'utf16_to_utf8', 'utf16_to_utf32', 'utf32_to_utf16',
        'video_config', 'WSACleanup', 'wait_thread', 'walk_dir', 'where',
        'write_lines', 'wait_key'
    )
    constants = (
        'ANY_QUEUE', 'ASCENDING', 'BLACK', 'BLOCK_CURSOR', 'BLUE',
        'BRIGHT_CYAN', 'BRIGHT_BLUE', 'BRIGHT_GREEN', 'BRIGHT_MAGENTA',
        'BRIGHT_RED', 'BRIGHT_WHITE', 'BROWN', 'C_DWORD', 'C_INT', 'C_POINTER',
        'C_USHORT', 'C_WORD', 'CD_AMBER', 'CD_BLACK', 'CD_BLUE', 'CD_BOLD',
        'CD_BOLD_ITALIC', 'CD_BOX', 'CD_CENTER', 'CD_CIRCLE', 'CD_CLOSED_LINES',
        'CD_CONTINUOUS', 'CD_CUSTOM', 'CD_CYAN', 'CD_DARK_BLUE', 'CD_DARK_CYAN',
        'CD_DARK_GRAY', 'CD_DARK_GREY', 'CD_DARK_GREEN', 'CD_DARK_MAGENTA',
        'CD_DARK_RED', 'CD_DARK_YELLOW', 'CD_DASH_DOT', 'CD_DASH_DOT_DOT',
        'CD_DASHED', 'CD_DBUFFER', 'CD_DEG2RAD', 'CD_DIAMOND', 'CD_DOTTED',
        'CD_EAST', 'CD_EVENODD', 'CD_FILL', 'CD_GL', 'CD_GRAY', 'CD_GREY',
        'CD_GREEN', 'CD_HATCH', 'CD_HOLLOW', 'CD_HOLLOW_BOX',
        'CD_HOLLOW_CIRCLE', 'CD_HOLLOW_DIAMOND', 'CD_INDIGO', 'CD_ITALIC',
        'CD_IUP', 'CD_IUPDBUFFER', 'CD_LIGHT_BLUE', 'CD_LIGHT_GRAY',
        'CD_LIGHT_GREY', 'CD_LIGHT_GREEN', 'CD_LIGHT_PARCHMENT', 'CD_MAGENTA',
        'CD_NAVY', 'CD_NORTH', 'CD_NORTH_EAST', 'CD_NORTH_WEST', 'CD_OLIVE',
        'CD_OPEN_LINES', 'CD_ORANGE', 'CD_PARCHMENT', 'CD_PATTERN',
        'CD_PRINTER', 'CD_PURPLE', 'CD_PLAIN', 'CD_PLUS', 'CD_QUERY',
        'CD_RAD2DEG', 'CD_RED', 'CD_SILVER', 'CD_SOLID', 'CD_SOUTH_EAST',
        'CD_SOUTH_WEST', 'CD_STAR', 'CD_STIPPLE', 'CD_STRIKEOUT',
        'CD_UNDERLINE', 'CD_WEST', 'CD_WHITE', 'CD_WINDING', 'CD_VIOLET',
        'CD_X', 'CD_YELLOW', 'CURLE_OK', 'CURLOPT_MAIL_FROM',
        'CURLOPT_MAIL_RCPT', 'CURLOPT_PASSWORD', 'CURLOPT_READDATA',
        'CURLOPT_READFUNCTION', 'CURLOPT_SSL_VERIFYPEER',
        'CURLOPT_SSL_VERIFYHOST', 'CURLOPT_UPLOAD', 'CURLOPT_URL',
        'CURLOPT_USE_SSL', 'CURLOPT_USERNAME', 'CURLOPT_VERBOSE',
        'CURLOPT_WRITEFUNCTION', 'CURLUSESSL_ALL', 'CYAN', 'D_NAME',
        'D_ATTRIBUTES', 'D_SIZE', 'D_YEAR', 'D_MONTH', 'D_DAY', 'D_HOUR',
        'D_MINUTE', 'D_SECOND', 'D_CREATION', 'D_LASTACCESS', 'D_MODIFICATION',
        'DT_YEAR', 'DT_MONTH', 'DT_DAY', 'DT_HOUR', 'DT_MINUTE', 'DT_SECOND',
        'DT_DOW', 'DT_MSEC', 'DT_DOY', 'DT_GMT', 'EULER', 'E_CODE', 'E_ADDR',
        'E_LINE', 'E_RTN', 'E_NAME', 'E_FILE', 'E_PATH', 'E_USER', 'false',
        'False', 'FALSE', 'FIFO_QUEUE', 'FILETYPE_DIRECTORY', 'FILETYPE_FILE',
        'GET_EOF', 'GET_FAIL', 'GET_IGNORE', 'GET_SUCCESS',
        'GL_AMBIENT_AND_DIFFUSE', 'GL_ARRAY_BUFFER', 'GL_CLAMP',
        'GL_CLAMP_TO_BORDER', 'GL_CLAMP_TO_EDGE', 'GL_COLOR_BUFFER_BIT',
        'GL_COMPILE', 'GL_COMPILE_STATUS', 'GL_CULL_FACE',
        'GL_DEPTH_BUFFER_BIT', 'GL_DEPTH_TEST', 'GL_EXTENSIONS', 'GL_FLAT',
        'GL_FLOAT', 'GL_FRAGMENT_SHADER', 'GL_FRONT', 'GL_LIGHT0',
        'GL_LIGHTING', 'GL_LINEAR', 'GL_LINK_STATUS', 'GL_MODELVIEW',
        'GL_NEAREST', 'GL_NO_ERROR', 'GL_NORMALIZE', 'GL_POSITION',
        'GL_PROJECTION', 'GL_QUAD_STRIP', 'GL_QUADS', 'GL_RENDERER',
        'GL_REPEAT', 'GL_RGB', 'GL_RGBA', 'GL_SMOOTH', 'GL_STATIC_DRAW',
        'GL_TEXTURE_2D', 'GL_TEXTURE_MAG_FILTER', 'GL_TEXTURE_MIN_FILTER',
        'GL_TEXTURE_WRAP_S', 'GL_TEXTURE_WRAP_T', 'GL_TRIANGLES',
        'GL_UNSIGNED_BYTE', 'GL_VENDOR', 'GL_VERSION', 'GL_VERTEX_SHADER',
        'GRAY', 'GREEN', 'GT_LF_STRIPPED', 'GT_WHOLE_FILE', 'INVLN10',
        'IUP_CLOSE', 'IUP_CONTINUE', 'IUP_DEFAULT', 'IUP_BLACK', 'IUP_BLUE',
        'IUP_BUTTON1', 'IUP_BUTTON3', 'IUP_CENTER', 'IUP_CYAN', 'IUP_DARK_BLUE',
        'IUP_DARK_CYAN', 'IUP_DARK_GRAY', 'IUP_DARK_GREY', 'IUP_DARK_GREEN',
        'IUP_DARK_MAGENTA', 'IUP_DARK_RED', 'IUP_GRAY', 'IUP_GREY', 'IUP_GREEN',
        'IUP_IGNORE', 'IUP_INDIGO', 'IUP_MAGENTA', 'IUP_MASK_INT',
        'IUP_MASK_UINT', 'IUP_MOUSEPOS', 'IUP_NAVY', 'IUP_OLIVE', 'IUP_RECTEXT',
        'IUP_RED', 'IUP_LIGHT_BLUE', 'IUP_LIGHT_GRAY', 'IUP_LIGHT_GREY',
        'IUP_LIGHT_GREEN', 'IUP_ORANGE', 'IUP_PARCHMENT', 'IUP_PURPLE',
        'IUP_SILVER', 'IUP_TEAL', 'IUP_VIOLET', 'IUP_WHITE', 'IUP_YELLOW',
        'K_BS', 'K_cA', 'K_cC', 'K_cD', 'K_cF5', 'K_cK', 'K_cM', 'K_cN', 'K_cO',
        'K_cP', 'K_cR', 'K_cS', 'K_cT', 'K_cW', 'K_CR', 'K_DEL', 'K_DOWN',
        'K_END', 'K_ESC', 'K_F1', 'K_F2', 'K_F3', 'K_F4', 'K_F5', 'K_F6',
        'K_F7', 'K_F8', 'K_F9', 'K_F10', 'K_F11', 'K_F12', 'K_HOME', 'K_INS',
        'K_LEFT', 'K_MIDDLE', 'K_PGDN', 'K_PGUP', 'K_RIGHT', 'K_SP', 'K_TAB',
        'K_UP', 'K_h', 'K_i', 'K_j', 'K_p', 'K_r', 'K_s', 'JS', 'LIFO_QUEUE',
        'LINUX', 'MAX_HEAP', 'MAGENTA', 'MIN_HEAP', 'Nan', 'NO_CURSOR', 'null',
        'NULL', 'PI', 'pp_Ascii', 'pp_Brkt', 'pp_Date', 'pp_File', 'pp_FltFmt',
        'pp_Indent', 'pp_IntCh', 'pp_IntFmt', 'pp_Maxlen', 'pp_Nest',
        'pp_Pause', 'pp_Q22', 'pp_StrFmt', 'RED', 'SEEK_OK', 'SLASH',
        'TEST_ABORT', 'TEST_CRASH', 'TEST_PAUSE', 'TEST_PAUSE_FAIL',
        'TEST_QUIET', 'TEST_SHOW_ALL', 'TEST_SHOW_FAILED', 'TEST_SUMMARY',
        'true', 'True', 'TRUE', 'VC_SCRNLINES', 'WHITE', 'WINDOWS', 'YELLOW'
    )

    tokens: typing.ClassVar = {
        'root': [
            (r"\s+", Whitespace),
            (r'/\*|--/\*|#\[', Comment.Multiline, 'comment'),
            (r'(?://|--|#!).*$', Comment.Single),
#Alt:
#           (r'//.*$|--.*$|#!.*$', Comment.Single),
            (r'"([^"\\]|\\.)*"', String.Other),
            (r'\'[^\']*\'', String.Other),
            (r'`[^`]*`', String.Other),

            (words(types, prefix=r'\b', suffix=r'\b'), Name.Function),
            (words(routines, prefix=r'\b', suffix=r'\b'), Name.Function),
            (words(preproc, prefix=r'\b', suffix=r'\b'), Keyword.Declaration),
            (words(keywords, prefix=r'\b', suffix=r'\b'), Keyword.Declaration),
            (words(constants, prefix=r'\b', suffix=r'\b'), Name.Constant),
            # Aside: Phix only supports/uses the ascii/non-unicode tilde
            (r'!=|==|<<|>>|:=|[-~+/*%=<>&^|\.(){},?:\[\]$\\;#]', Operator),
            (r'[\w-]+', Text)
        ],
        'comment': [
            (r'[^*/#]+', Comment.Multiline),
            (r'/\*|#\[', Comment.Multiline, '#push'),
            (r'\*/|#\]', Comment.Multiline, '#pop'),
            (r'[*/#]', Comment.Multiline)
        ]
    }

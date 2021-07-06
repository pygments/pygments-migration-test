%% Autogenerate a list of LilyPond keywords

%% Usage: lilypond external/lilypond-builtins-generator.ly > pygments/lexers/_lilypond_builtins.py

\version "2.23.3"

#(use-modules (ice-9 receive)
              (ice-9 regex))

#(define port (open-output-file "../pygments/lexers/_lilypond_builtins.py"))

#(define output-preamble
   "# -*- coding: utf-8 -*-
\"\"\"
    pygments.lexers._lilypond_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    LilyPond builtins.

    :copyright: Copyright 2021-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
\"\"\"

# Contents generated by the script lilypond-builtins-generator.ly
# found in the external/ directory of the source tree.

")

#(format port "~a" output-preamble)

#(define (dump-py-list name vals)
   (let* ((string-vals
            (map symbol->string vals))
          (fixed-vals
            (filter-map
              (lambda (str)
                ; To avoid conflicts with Scheme builtins,
                ; a leading backslash is prepended to \<,
                ; \= and a few others. The lexer finds it
                ; itself, so remove it here.
                (cond
                  ((equal? str "\\\\")
                   #f)
                  ((string-startswith str "\\")
                   (string-drop str 1))
                  (else
                   str)))
              string-vals))
          (sorted-vals ; reproducibility
            ; Avoid duplicates (e.g., identical pitches
            ; in different languages)
            (uniq-list
              (sort fixed-vals string<?)))
          (formatted-vals
            (map
              (lambda (val)
                (format #f "  \"~a\"," val name))
              sorted-vals))
          (joint-vals
            (string-join formatted-vals "\n")))
     (format port
             "~a = [
~a
]

"
             name
             joint-vals)))


%% KEYWORDS

#(define keywords
   '(
      ; Lexical modes.
      notemode
      lyricmode
      lyricsto
      addlyrics
      chordmode
      chords
      figuremode
      figures
      drummode
      drums
      ; Output definitions.
      header
      layout
      midi
      paper
      ; Context definitions.
      ;; \context is also used in music.  We take it as
      ;; a keyword in both cases.
      context
      with
      name
      type
      accepts
      denies
      alias
      defaultchild
      consists
      remove
      description
      ;; Not strictly a keyword, but can be viewed so.
      inherit-acceptability
      ; Blocks.
      book
      bookpart
      score
      ; Other.
      new
      etc
      include
      language
      version))

#(dump-py-list 'keywords keywords)

%% CLEFS

#(define all-clefs
   (map string->symbol (map car supported-clefs)))

#(dump-py-list 'clefs all-clefs)

%% SCALES

#(define all-scales
   '(major
     minor
     ionian
     locrian
     aeolian
     mixolydian
     lydian
     phrygian
     dorian))

#(dump-py-list 'scales all-scales)

%% REPEAT TYPES

#(define all-repeat-types
   '(volta percent unfold))

#(dump-py-list 'repeat_types all-repeat-types)

%% PITCHES

#(define all-pitch-names
   (append
     ; We highlight rests just like pitches.
     '(r R)
     (apply append
            (map
              (lambda (lang)
                (map car (cdr lang)))
              language-pitch-names))
     ; Drum note names.
     (map car drumPitchNames)))

#(dump-py-list 'pitches all-pitch-names)

%% MUSIC FUNCTIONS AND SHORTCUTS

% View these as music functions.
#(define extra-music-functions
   '(set
     unset
     override
     revert
     tweak
     once
     undo
     temporary
     repeat
     alternative
     tempo
     change))

#(let* ((module (current-module))
        (module-alist (ly:module->alist module))
        (all-music-functions
          (filter
            (lambda (entry)
              (ly:music-function? (cdr entry)))
            module-alist))
        (all-predefined-music-objects
          (filter
            (lambda (entry)
              (ly:music? (cdr entry)))
            module-alist)))
   (receive (articulations non-articulations)
     (partition
       (lambda (entry)
         (ly:event? (cdr entry)))
       all-predefined-music-objects)
     (receive (dynamics non-dynamic-articulations)
       (partition
         (lambda (entry)
           (any
             (lambda (type)
               (music-is-of-type? (cdr entry)
                                  type))
             '(dynamic-event crescendo-event decrescendo-event)))
         articulations)
       (dump-py-list 'music_functions
                     (append extra-music-functions
                             (map car all-music-functions)))
       (dump-py-list 'dynamics (map car dynamics))
       (dump-py-list 'articulations (map car non-dynamic-articulations))
       (dump-py-list 'music_commands (map car non-articulations)))))

%% MARKUP COMMANDS

#(let* ((markup-name-regexp
          (make-regexp "(.*)-markup(-list)?"))
        (modules
          (cons (current-module)
                (map resolve-module '((lily) (lily accreg)))))
        (alist
          (apply append
                 (map ly:module->alist modules)))
        (markup-commands
          (filter
            (lambda (entry)
              (or (markup-function? (cdr entry))
                  (markup-list-function? (cdr entry))))
            alist))
        (markup-command-names
          (map
            (lambda (entry)
              (let* ((string-name (symbol->string (car entry)))
                     (match (regexp-exec markup-name-regexp string-name)))
                (string->symbol (match:substring match 1))))
            markup-commands))
        (markup-words
          (append '(markup markuplist)
                  markup-command-names)))
   (dump-py-list 'markup_commands markup-words))

%% GROBS

#(let ((grob-names (map car all-grob-descriptions)))
   (dump-py-list 'grobs grob-names))

%% CONTEXTS

#(let* ((layout-module
          (ly:output-def-scope $defaultlayout))
        (layout-alist
          (ly:module->alist layout-module))
        (all-context-defs
          (filter
            (lambda (entry)
              (ly:context-def? (cdr entry)))
            layout-alist))
        (context-def-names
          (map car all-context-defs)))
   (dump-py-list 'contexts context-def-names))

%% TRANSLATORS

#(let* ((all-translators
          (ly:get-all-translators))
        (translator-names
          (map ly:translator-name all-translators)))
   (dump-py-list 'translators translator-names))

%% SCHEME FUNCTIONS

#(let* ((module (resolve-module '(lily)))
        (module-alist (ly:module->alist module))
        (all-functions
           (filter
             (lambda (entry)
               (or (procedure? (cdr entry))
                   (macro? (cdr entry))))
             module-alist))
        (all-function-names
          (map car all-functions)))
   (dump-py-list 'scheme_functions all-function-names))

%% PROPERTIES

#(dump-py-list 'context_properties all-translation-properties)
#(dump-py-list 'grob_properties all-backend-properties)

%% PAPER VARIABLES

% Reference: https://lilypond.org/doc/v2.22/Documentation/notation/page-layout
#(define all-paper-variables
   '(paper-height
     top-margin
     bottom-margin
     ragged-bottom
     ragged-last-bottom
     markup-system-spacing
     score-markup-spacing
     score-system-spacing
     system-system-spacing
     markup-markup-spacing
     last-bottom-spacing
     top-system-spacing
     top-markup-spacing
     paper-width
     line-width
     left-margin
     right-margin
     check-consistency
     ragged-right
     ragged-last
     two-sided
     inner-margin
     outer-margin
     binding-offset
     horizontal-shift
     indent
     short-indent
     max-systems-per-page
     min-systems-per-page
     systems-per-page
     system-count
     page-breaking
     page-breaking-system-system-spacing
     page-count
     blank-page-penalty
     blank-last-page-penalty
     auto-first-page-number
     first-page-number
     print-first-page-number
     page-number-type
     page-spacing-weight
     print-all-headers
     system-separator-markup
     footnote-separator-markup
     ; Let's view these four as \paper variables.
     basic-distance
     minimum-distance
     padding
     stretchability))

#(dump-py-list 'paper_variables all-paper-variables)

%% HEADER VARIABLES

% Reference: https://lilypond.org/doc/v2.22/Documentation/notation/creating-titles-headers-and-footers.html#default-layout-of-bookpart-and-score-titles
#(define all-header-variables
   '(dedication
     title
     subtitle
     subsubtitle
     instrument
     poet
     composer
     meter
     arranger
     tagline
     copyright
     piece
     opus
     ; The following are used in LSR snippets and regression tests.
     lsrtags
     doctitle
     texidoc))

#(dump-py-list 'header_variables all-header-variables)


#(close-port port)

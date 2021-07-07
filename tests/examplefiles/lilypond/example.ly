\version "2.23.3"

% This is a test file for Pygments' LilyPond support. To compile
% it with Guile 1 (as in official releases as of this writing),
% remove the "commented form" below.

%{
  All supported constructs are covered in
  this file.  For example, multi-line comments.

  These are non-nested. The following will
  end the whole comment:
  %{ %}

\include "lilypond-book-preamble.ly"

\header {
  title = "This is an assignment to a string."
  composer = \markup \smallCaps "And this is a markup"
}
% The following is just a comment.
%}

\paper {
  indent = 30\staff-space
  page-count = 1
}

myFunc =
# #;(This is a commented form. After it, we are still in Scheme mode.)
(define-music-function (music n) (ly:music? index?)
   (let* ((repeated (make-list n music))
          (copied (map ly:music-deep-copy repeated)))
     ; This is a Scheme comment.
     (make-sequential-music copied)))

mySecondFunc =
#(define-music-function (music) (ly:music?)
   #{
     % LilyPond syntax here.
     \compressMMRests
       \shiftDurations -2 1
        # ; Scheme syntax again.
         (ly:music-deep-copy music)
   #})

#(define-markup-command (small-italic layout props arg) (markup?)
   (interpret-markup layout props
     (make-small-markup (make-italic-markup arg))))

myPitch = ##{ c #}

% Here we should be back to LilyPond mode. This
% is a LilyPond comment.

myVariable = c4
piuPiano = \markup \italic "più piano"

#(symbol->string 'some-symbol)

<<
  \new Staff \with {
    \consists Duration_line_engraver
  }
  \relative c' {
    \clef alto
    \time 6/8
    \key d \major
    \cadenzaOn
    deses'!4.~(\tweak thickness 4\( deses^\p-\signumcongruentiae_1\4
    deses\longa) \myFunc { r } 4 des8 8[ <des ges>8]\)
    \bar "||"
    \cadenzaOff
    \once \hide NoteHead
    \once \override NoteHead.no-ledgers = ##t
    \once \omit Dots
    \once \override Staff.DurationLine.thickness = #5
    c''?2.:16\-^"Some music" |
    \mySecondFunc
      R1*1/2^\markup \center-column {
               Some
               Text
               In
               A
               \bold \italic Column!
               \small-italic super
             }
    \repeat unfold 4 { c8\< c^\> c\p\! }
    c^\piuPiano^\markup dolce
  }
  \addlyrics {
    \set Score.melismaBusyProperties = #'()
    My Lily -- Song
  }
  \chordmode {
    c cis:3+ des:maj7/+e
  }
  \new TabVoice {
    f'4\^ g'4\^ f'2
  }
  \drums {
    hihat4 hh bassdrum bd
  }
>>

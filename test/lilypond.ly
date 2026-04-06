
\version "2.24.0"

\header {
  title = "C 大调练习曲"
}

\score {
  <<
    \new Staff \relative c' {
      \time 4/4
      \key c \major

      c4 d e f g a b c |
      c2 b4 a g2 |
      f4 e d c2 r |
    }
    \new ChordNames {
      c1 f g c
    }
  >>
  \layout { }
  \midi { }
}



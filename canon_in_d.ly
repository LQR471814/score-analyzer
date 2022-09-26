\version "2.20.0"
#(set-global-staff-size 28)

\paper {
  #(set-paper-size "letter")
  indent = 0\mm
  top-margin = 15
  bottom-margin = 15
  left-margin = 15
  right-margin = 15
  print-page-number = false
}

subMp = \markup { \dynamic mp \italic subito }

\book {
  \header {
    title = \markup { Canon in D }
    composer = "J. Pachelbel"
    tagline = "© 2022 — 8VA Music"
  }

  \score {
    \new GrandStaff <<
      \new Staff = "upper"
      \relative c' {
        \key d \major \clef treble \time 4/4
        \set fingeringOrientations = #'(up)

        \tempo "Andante"

        r8\p <fis-1>( <a-2> <d-5>) r <e,-1>( <a-3> <cis-5>) | r d,( fis b) r cis,( fis a) |
        r b,( d g) r a,( d fis) | r b,( d g) r cis,( e a) |

        <fis'-3>2-- e-- | d-- <cis-3>-- | b-- a-- | b-- cis-- |

        <d-3 fis-5>--\mp <cis-2 e-4> | <b-1 d-3>-- <a-2 cis-4>-- | <g-1 b-3>-- <fis-1 a-2>-- | <g-1 b-3>-- <e-1 cis'-4>-- |

        <<
          {
            <d'-5>8( cis d4) <e,-1> <cis'-4>4 | <d-1>4 <fis-2> <a-4> a8 <b-5> |
            <g-5>( fis e g) <fis-4>( <e-3> <d-1> <cis-4> | <b-3> a <g-1> <fis-4>) <e-3>( <g-5> fis e)
          }
          \\
          {
            \set fingeringOrientations = #'(down) <fis-1>2 s4 s4 | s4 s4 <cis'-1>8 <fis-2> s s |
            <b,-1>4 s <a-1> s | <g-1> s4 <d-2>4.( <cis-1>8)
          }
        >> |

        <d-2>8(\< <e-1> <fis-3> <g-4>) <a-5>(\! <cis,-1>) <a'-4>( <g-3> | <d-1 fis-2>) <b'-5>( a g) <a-5>( g fis e |
        <d-1>4) << { <b'-3>8( cis) <d-5>( cis b a) | b(\< a b d) <d-5>4( cis)\! } \\ { s4 fis, s4 | g2 e } >> |

        <a'-5>8\mf <fis-3>16 <g-4> <a-5>8 fis16 g a <a,-1> b <cis-3> <d-1> e fis g |
        <fis-3>8 <d-1>16 e fis8 <fis,-2>16 <g-3> <a-4> b a g a fis g a |
        <g-3>8 <b-5>16 a g8 fis16 <e-1> <fis-3> e d e fis <g-1> a b |
        g8 b16 a b8 <cis-4>16 <d-5> <cis-3>\< <a-1> b cis <d-1> e fis g\! |

        <a-5>8\f <fis-3>16 <g-4> <a-5>8 fis16 g a <a,-1>\< b cis <d-1> e fis g |
        <fis-3>8\! <d-1>16 e fis8 <fis,-2>16 <g-1> <a-2> b a g a <d-5> <cis-4> <d-5> |
        <b-3>8 d16 cis b8 a16 g <a-4> <g-3> <fis-2> <g-1> <a-2> b cis d |
        <g,-1 b-3>8 d'16( cis <d-5>8) <b-2 d-4>8 << { <d-4>4.( <cis-3>8) } \\ { a2 } >> |

        <fis'-3 a-5>4.\ff <fis a>8 <fis-2 a-4>( <g b> <fis a> <e-1 g-3> |
        <d-1 fis-2>4.) <d fis>8 <d-1 fis-3>(\> <e g> <d fis> <cis-2 e-4> |
        <b-1 d-3> <cis-2> <b-1> <cis-4>) <fis, d'>2 |
        <g-1 d'-4>8( <c-3> <b-2> c) <g-1 cis-4>4.( <d'-5>8)\! |

        <<
          {
            <d-1>4.\mp <fis-2>8 <fis-3>( g fis <e-2> | <d-1>4.) <d-2>8 <d-3>( e d <cis-2>) |
            r4 <g'-5> r <fis-4> |
            r <g-4> <a-5>2 |

            r4 <d,-5>2( <cis-4>4) | r4 <b-5>2( <a-4>4) | r4 <g-5>2( <fis-4>4) | <g-5>2 <e-4>
          }
          \\
          {
            r4 \set fingeringOrientations = #'(up) <d''-5> \set fingeringOrientations = #'(down) <cis,-1> r4 |
            r \set fingeringOrientations = #'(up) <b'-5> \set fingeringOrientations = #'(down) <a,-1> r |
            <b-1>2\> <a-1>2 |
            <b-1> <d-2>4( <cis-1>)\! |

            \set fingeringOrientations = #'(right) <d,-1 fis-2>2\p <e-1> | <d-1>2 <cis-1> | <b-1> <a-1> |
            <b-1> \set fingeringOrientations = #'(down) <d-3>4( <cis-2>)
          }
        >>

        \set fingeringOrientations = #'(right) <a-1 d-3 fis-5>1\pp\fermata \bar "|."
      }

      \new Staff = "lower"
      \relative c {
        \key d \major \clef bass \time 4/4
        \set fingeringOrientations = #'(down)
        \phrasingSlurUp

        d2 a2 | b fis | g d | g a |

        <d-5>8 <a'-2> <d-1> a a, e' <a-1> <cis-2> | b, fis' b fis fis, cis' fis a |
        g, d' g d d, a' d fis | g, d' g d a e' a cis |

        d, a' d a a, e' a cis | b, fis' b fis fis, cis' fis a |
        g, d' g d d, a' d fis | g, d' g d a^\< e' a cis\! |

        d,8 a' d4 a,8 e' a4 | b,8 fis' b4 fis,8 cis' fis4 |
        g,8 d' g4 d,8 a' d4 | g,8 d' g4 a, a' |

        d,8 a' d4 a,8 e' a4 | b,8 fis' b4 fis,8 cis' fis4 |
        g,8 d' g4 d,8 a' d4 | g,8 d' g4 a,8 e' a e |

        d8 a' d4 a,8 e' a4 | b,8 fis' b4 fis,8 cis' fis4 |
        g,8 d' g4 d,8 a' d4 | g,8 d' g4 a,8 e' a4 |

        d,8 a' d4 a,8 e' a4 | b,8 fis' b4 fis,8 cis' fis4 |
        g,8 d' g4 d,8 a' d4 | g,8 d' g4 a,8 e' a4 |

        d,8 a' d4 a,8 e' a4 | b,8 fis' b4 fis,8 cis' fis4 |
        g,8 d' g4 d,8 a' d a | g8 d' g d a8 e' a4 |

        d,8 a' d4 a,8 e' a4 | b,8 fis' b4 fis,8 cis' fis4 |
        g,8 d' g4 d,8 a' d4 | g,8 d' g4 a,8 e' a4 |

        <d,-3 a'-1>2 <a-5 a'-1> | <b-3 fis'-1> <fis-5 fis'-1> |
        <g d'> <d d'> |
        <<
          { \set fingeringOrientations = #'(right) <d'-2>4 <g-1> }
          \\
          {\set fingeringOrientations = #'(down)<g,-5>2}
        >> \stemDown <a-2>2 |

        <d,-5>1\fermata  \bar "|."
      }
    >>
    \layout {
      \context {
        \Score
        proportionalNotationDuration = #(ly:make-moment 1/8)
      }
    }
  }
}
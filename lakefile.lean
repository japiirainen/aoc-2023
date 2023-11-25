import Lake

open Lake DSL

def moreServerArgs := #[
  "-Dpp.unicode.fun=true",
  "-Dpp.proofs.withType=false",
  "-DautoImplicit=false",
  "-DrelaxedAutoImplicit=false"
]

def moreLeanArgs := moreServerArgs

def weakLeanArgs : Array String :=
  if get_config? CI |>.isSome then
    #["-DwarningAsError=true"]
  else
    #[]

package aoc where
  moreServerArgs := moreServerArgs
  moreLeanArgs := moreLeanArgs
  weakLeanArgs := weakLeanArgs

/- Internal libraries -/
lean_lib Solutions
lean_lib Lib

/- External libraries -/
require std from git "https://github.com/leanprover/std4" @ "main"
require mathlib from git "https://github.com/leanprover-community/mathlib4" @ "master"

/- run with `lake exe aoc` -/
@[default_target]
lean_exe aoc where
  root := `Main

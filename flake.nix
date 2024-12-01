{
  description = "Advent of Code 2023";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    flake-utils.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs =
    {
      nixpkgs,
      flake-utils,
      ...
    }:

    flake-utils.lib.eachDefaultSystem (
      system:
      let
        overlays = [
          (_: super: {
            python = super.python311;
          })
        ];
        pkgs = import nixpkgs { inherit overlays system; };
      in
      {
        devShells.default = pkgs.mkShell {
          packages =
            (with pkgs; [
              python
              pypy310
              pyright
              ruff
              pylint
            ])
            ++ (with pkgs.pythonPackages; [
              more-itertools
              numpy
              sympy
              networkx
              matplotlib
              requests
              z3
            ]);

          shellHook = with pkgs; ''
            ${python}/bin/python --version
          '';
        };
      }
    );
}

{
  description = "Python application managed with poetry2nix";

  inputs = {
    flake-utils = {
      type = "github";
      owner = "numtide";
      repo = "flake-utils";
      ref = "master";
    };

    nixpkgs = {
      type = "github";
      owner = "NixOS";
      repo = "nixpkgs";
      ref = "nixpkgs-unstable";
    };

    pre-commit-hooks = {
      type = "github";
      owner = "cachix";
      repo = "pre-commit-hooks.nix";
      ref = "master";
      inputs = {
        flake-utils.follows = "flake-utils";
        nixpkgs.follows = "nixpkgs";
      };
    };
  };

  outputs = { self, flake-utils, nixpkgs, pre-commit-hooks }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python3.withPackages (ps: with ps; [
          black
          isort
          mypy
        ]);
      in
      {
        checks = {
          pre-commit = pre-commit-hooks.lib.${system}.run {
            src = self;

            hooks = {
              black = {
                enable = true;
              };

              clang-format = {
                enable = true;
                types_or = [ "c" "c++" ];
              };

              isort = {
                enable = true;
              };

              nixpkgs-fmt = {
                enable = true;
              };
            };
          };
        };

        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python
            pyright
          ];

          inherit (self.checks.${system}.pre-commit) shellHook;
        };
      });
}

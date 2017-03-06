with import <nixpkgs> {};

let

  # to update, run:
  # nix-prefetch-git git://github.com/NixOS/nixpkgs-channels refs/heads/nixpkgs-unstable
  src = pkgs.fetchFromGitHub {
    owner = "NixOS";
    repo = "nixpkgs-channels";
    rev = "89a036506396dd869474a32e984f5cab5c07992a"; # 2017/02/17
    sha256 = "04fxjh5ca41rlnvc4ggbgh41j4mkqj685inxj2xbm9i8giabncw1";
  };

  pinned-pkgs = import src {};

in
pinned-pkgs

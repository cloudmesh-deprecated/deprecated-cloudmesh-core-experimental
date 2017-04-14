{ pkgs ? import ./nixpkgs.nix
, name ? "cloudmesh.core"
, install ? "install"
}:

with pkgs;

let

  pip = callPackage ./nixpip.nix {
    runtime = ./requirements.open;
    testing = ./test_requirements.open;
  };

  attr = {
    install = "runtime";
    dev     = "all";
  }."${install}";

  buildInputs = [ awscli ];

in

pythonPackages.buildPythonPackage {
  name = "${name}";
  buildInputs = [ pip.python."${attr}" ] ++ buildInputs;
  propagatedBuildInputs = pip.requirements."${attr}";
}

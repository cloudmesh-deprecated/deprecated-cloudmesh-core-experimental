
.PHONY: dev test upgrade


dev: shell.nix requirements.nix nixpkgs.nix
	nix-shell --argstr install dev

# assumed that `make dev` is called first
test:
	py.test

upgrade: requirements.nix


################################################################

requirements.nix: requirements.open test_requirements.open nixpkgs.nix
	nix-pip

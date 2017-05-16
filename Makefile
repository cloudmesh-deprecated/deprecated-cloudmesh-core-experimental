
.PHONY: dev test upgrade


dev: shell.nix nixpkgs.nix
	nix-shell --argstr install dev

# assumed that `make dev` is called first
test:
	py.test

upgrade: requirements.nix


################################################################

requirements.nix: requirements.open requirements.dev nixpkgs.nix
	nix-pip

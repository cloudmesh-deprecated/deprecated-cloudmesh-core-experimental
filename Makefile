
.PHONY: dev test


dev: shell.nix requirements.nix nixpkgs.nix
	nix-shell

# assumed that `make dev` is called first
test:
	py.test


################################################################

requirements.nix: requirements.open nixpkgs.nix
	nix-pip

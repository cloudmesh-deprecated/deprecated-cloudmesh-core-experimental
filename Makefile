
.PHONY: dev test


dev: shell.nix requirements.nix nixpkgs.nix
	nix-shell

# assumed that `make dev` is called first
test:
	py.test


################################################################

requirements.nix: pip2nix requirements.open nixpkgs.nix
	./pip2nix


.PHONY: dev
dev: shell.nix requirements.nix nixpkgs.nix
	nix-shell

.PHONY: test
test:
	py.test

requirements.nix: pip2nix requirements.open nixpkgs.nix
	./pip2nix

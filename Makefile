
.PHONY: dev
dev: shell.nix requirements.nix nixpkgs.nix
	nix-shell

requirements.nix: pip2nix requirements.open nixpkgs.nix
	./pip2nix

{pkgs ? import <nixpkgs> {}}: let
  minhtmlRepo = pkgs.fetchFromGitHub {
    owner = "wilsonzlin";
    repo = "minify-html";
    rev = "2301223773dadce30a33b4c407d8b2524adeb5e2"; # You can change this to a specific commit or tag
    sha256 = "sha256-346S5Yl8140B7Bnn1hdtYRHqssgGEWCEvbiBkPXrDeg="; # Placeholder for the actual hash, will be replaced
  };
in
  pkgs.mkShell {
    buildInputs = [
      pkgs.rustc
      pkgs.cargo
    ];

    packages = with pkgs; [
      zola
      pigz
      lightningcss
    ];

    shellHook = ''
      export PATH=$PATH:$HOME/.cargo/bin
      echo "🔧 Entered dev shell for 'minhtml'"
      # Download the repo and install the crate if not already installed
      if ! command -v minhtml >/dev/null; then
        echo "🚀 Installing minhtml with cargo..."

        # # Create a temporary folder to unpack the repo
        tmpDir=$(mktemp -d)

        # Go into the crate directory
        cd ${minhtmlRepo}/minhtml

        # Run cargo install
        cargo install --path . --force --target-dir $tmpDir

        cd -  # Go back to the original directory
      else
        echo "✅ minhtml already installed in ~/.cargo/bin"
      fi
    '';
  }

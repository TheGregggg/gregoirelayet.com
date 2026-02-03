{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  packages = with pkgs; [
    zola
    pigz
    lightningcss
  ];
}

{ pkgs }: {
  deps = [
    pkgs.python39Packages.pip
    pkgs.qtile
    pkgs.systemd
    pkgs.jq.bin
    pkgs.bashInteractive
    pkgs.nodePackages.bash-language-server
    pkgs.man
  ];
}
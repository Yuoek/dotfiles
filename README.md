# dotfiles
This is my conf

<!-- mtoc-start -->

* [Install](#install)
* [Blog](#blog)
* [Todo](#todo)

<!-- mtoc-end -->

## Termux 备份
```bash
tar -zcvf /sdcard/v0.10_termux_archlinux.tar.gz -C /data/data/com.termux/files ./home ./usr
tar -zxvf /sdcard/v0.10_termux_archlinux_20260404.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions

proot-distro backup archlinux --output archlinux_20260404.tar.gz
proot-distro restore archlinux_20260404.tar.gz
```

## Install
**ssh**
```bash
 ssh-keygen -t rsa -C "2055048783@qq.com"
 git config --global user.name "yuoek"
 git config --global user.email "2055048783@qq.com"
```

**Dotfiles**
```bash
git clone git@github.com:Yuoek/dotfiles ~/.yuoek
```

## Blog
```bash
git clone git@github.com:Yuoek/dotfiles ~/hugo
```

## Todo

- [x] termux-desktop(openbox)
- [x] terminal(zsh oh-my-zsh)
- [x] proot-distro(archlinux)
- [x] nvim(plugins)      
- [x] hugo

- [-] Todo(2026-04-06) 🚩
- [ ] texlive
- [ ] package
- [-] 😃


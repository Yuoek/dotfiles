# V1.00

> [!info] 
> 添加了 texlive, 配置 ssh  
> 安装 git curl neovim mpv yazi termux-api fluidsynth lilypond lazygit glow gdb chafa debugpy


- [x] termux-desktop nvim
- [x] texlive-bin 🎏
- [ ] nvim-plugins 
- [ ] Todo 2026-04-07

## Termux restore
**备份**
```bash
tar -zcvf /sdcard/v1.00_termux.tar.gz -C /data/data/com.termux/files ./home ./usr
```

**恢复备份**
```bash
tar -zxvf /sdcard/v1.00_termux.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
```

## git
**克隆**
```bash
git clone git@github.com:Yuoek/dotfiles ~/.yuoek
```

**切换分支**
```bash
git checkout feacture_v1.00
```

**创建并切换分支**
```bash
git checkout -b feacture_v1.00
```

**查看分支**
```bash
git branch -vv
```

**推送分支**
```bash
git push origin feacture_v1.00
```

## 包安装
```bash
pkg update && pkg install git curl neovim mpv yazi termux-api fluidsynth lilypond lazygit glow gdb chafa debugpy
```
## zshrc
**设置 texlive 环境变量**
```bash
source /data/data/com.termux/files/usr/etc/profile.d/texlive.sh
```

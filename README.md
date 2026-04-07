# V1.00

> [!info] 
> 添加了 texlive, 配置 ssh  
> 安装 git curl neovim mpv yazi termux-api fluidsynth lilypond lazygit glow gdb chafa debugpy

## git
**克隆 feactur 分支**
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

## zshrc
**设置 texlive 环境变量**
```bash
source /data/data/com.termux/files/usr/etc/profile.d/texlive.sh
```

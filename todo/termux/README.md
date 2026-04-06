# Todo Termux

<!-- mtoc-start -->

* [1. termux-desktop](#1-termux-desktop)
* [2. 终端美化](#2-终端美化)
  * [zsh](#zsh)
  * [oh-my-zsh](#oh-my-zsh)
  * [starship](#starship)
* [3. proot-distro archlinux](#3-proot-distro-archlinux)
* [4. nvim](#4-nvim)
  * [optionYu](#optionyu)
  * [plugins](#plugins)
* [Link](#link)

<!-- mtoc-end -->

## 1. termux-desktop

## 2. 终端美化

### zsh
```bash
chsh -s /bin/zsh
```

### oh-my-zsh
```bash
 sh -c "$(curl -fsSL https://gitee.com/pocmon/ohmyzsh/raw/master/tools/install.sh)"
 git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
 git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
 plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```

### starship
```bash
pkg install starship
```

## 3. proot-distro archlinux
```bash
pkg install proot-distro
```

## 4. nvim

### optionYu

1. 录音
```bash
pkg install mpv
```

2. 拍照

3. 插入图片

### [plugins](./nvim/extra.lua)
1. [render-markdown]()
    - [libtexprintf]()
        + [install](./termux-app/libtexprintf.md)

    
2. [cmp-english]()
      - [cmp-nvim-lsp]()
      - [cmp-buffer]()
      - [cmp-path]()
      - [cmp-cmdline]()
      - [cmp-dictionary]()
      - [cmp-emoji]()

      - [english-word](https://github.com/dwyl/english-words)



3. [eskk]()

    - [eskk-world](https://raw.githubusercontent.com/skk-dev/dict/master/SKK-JISYO.L)


4. [yazi](https://github.com/mikavilpas/yazi.nvim)
    + pkg install yazi

5. [flash](https://github.com/folke/flash.nvim.git)

6. [markdown-toc](https://github.com/hedyhli/markdown-toc.nvim)

7. [screenkey](https://github.com/NStefan002/screenkey.nvim)

8. [veen](https://github.com/jbyuki/venn.nvim.git)

9. [url-open](https://github.com/sontungexpt/url-open)

10. [lilypond](https://github.com/martineausimon/nvim-lilypond-suite)
    - pkg install mpv fluidsynth lilypond
    - [FluidR3_GM.sf2](https://github.com/pianobooster/fluid-soundfont/releases/download/v3.1/FluidR3_GM.sf2)


11. [vimtex](https://github.com/lervag/vimtex.git)
    - pkg install texlive-installer

12. [lazygit](https://github.com/kdheepak/lazygit.nvim)
    - pkg install lazygit

13. [browser](https://github.com/claydugo/browsher.nvim)

14. [diffview]()

15. [dap-ui](https://github.com/rcarriga/nvim-dap-ui)
    - pip install debugpy
    - pkg install dbg

16. [dadbod-ui](https://github.com/kristijanhusak/vim-dadbod-ui)

17. [trans](https://github.com/JuanZoran/Trans.nvim)
    - pkg install sqlite
    [ecdict](https://github.com/skywind3000/ECDICT-ultimate/releases/download/1.0.0/ecdict-ultimate-sqlite.zip)

18. [llm](https://github.com/Kurama622/llm.nvim)

19. [todo-comments](https://github.com/folke/todo-comments.nvim)

## Link

[english-word](https://github.com/dwyl/english-words)
[eskk-world](https://raw.githubusercontent.com/skk-dev/dict/master/SKK-JISYO.L)
[FluidR3_GM.sf2](https://github.com/pianobooster/fluid-soundfont/releases/download/v3.1/FluidR3_GM.sf2)
[ecdict](https://github.com/skywind3000/ECDICT-ultimate/releases/download/1.0.0/ecdict-ultimate-sqlite.zip)

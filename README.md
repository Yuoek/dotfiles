# V2.00

> [!INFO] 
> 扩展 Nvchad  插件
> 安装 sqlite3

- [x] termux-desktop nvim
- [x] texlive-bin
- [x] nvim-plugins 🎏
- [ ] Todo 2026-04-07

## Termux restore
**备份**
```bash
tar -zcvf /sdcard/v2.00_termux.tar.gz -C /data/data/com.termux/files ./home ./usr
```

**恢复备份**
```bash
tar -zxvf /sdcard/v2.00_termux.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
```

## Nvim plugins
**nvim plugins**

1. [render-markdown]()
2. [cmp-english]()
3. [eskk]()
4. [yazi](https://github.com/mikavilpas/yazi.nvim)
5. [flash](https://github.com/folke/flash.nvim.git)
7. [screenkey](https://github.com/NStefan002/screenkey.nvim)
8. [veen](https://github.com/jbyuki/venn.nvim.git)
9. [url-open](https://github.com/sontungexpt/url-open)
10. [lilypond](https://github.com/martineausimon/nvim-lilypond-suite)
11. [vimtex](https://github.com/lervag/vimtex.git)
12. [lazygit](https://github.com/kdheepak/lazygit.nvim)
13. [browser](https://github.com/claydugo/browsher.nvim)
14. [diffview]()
15. [dap-ui](https://github.com/rcarriga/nvim-dap-ui)
16. [dadbod-ui](https://github.com/kristijanhusak/vim-dadbod-ui)
17. [trans](https://github.com/JuanZoran/Trans.nvim)
18. [llm](https://github.com/Kurama622/llm.nvim)
19. [todo-comments](https://github.com/folke/todo-comments.nvim)

**sqlite3安装**
```bash
pkg update && pkg install sqlite3
```

**Trans 英语词库下载**
```bash
wget https://github.com/skywind3000/ECDICT-ultimate/releases/download/1.0.0/ecdict-ultimate-sqlite.zip
```

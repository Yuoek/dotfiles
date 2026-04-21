# V4.01

> [!INFO] 
> Yuoek 文件

- [x] termux-desktop nvim
- [x] texlive-bin
- [x] nvim-plugins
- [x] application 
- [x] pkg-extra
- [x] Yuoek 🎏 
- [ ] Todo 2026-04-14

<!-- mtoc-start -->

* [Termux restore](#termux-restore)
* [克隆](#克隆)
* [目录](#目录)
  * [web](#web)
  * [code](#code)
  * [project](#project)
  * [hugo](#hugo)
  * [class](#class)
  * [tools](#tools)
  * [film](#film)
  * [life](#life)
  * [science](#science)

<!-- mtoc-end -->
## Termux restore
**备份**
```bash
tar -zcvf /sdcard/Termux_backup/v4.01_termux.tar.gz -C /data/data/com.termux/files ./home ./usr
```

**恢复备份**
```bash
tar -zxvf /sdcard/Termux_backup/v4.01_termux.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
```

## 克隆
```bash
git clone git@github.com:Yuoek/Yuoek.git
```

## 目录
```markdown
Yuuoek
  |--- web
  |--- code
  |--- project
  |--- hugo
  |--- class
  |--- tools
  |--- film
  |--- life
  |--- science
```

### web
**qwerty**
```bash
git submodule add git@github.com:Yuoek/qwerty.git
```

### code
```bash
git submodule add git@github.com:Yuoek/python.git
```

### project

### hugo

### class

### tools

### film

### life

### science


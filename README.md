# V3.02

> [!INFO] 

- [x] termux-desktop nvim
- [x] texlive-bin
- [x] nvim-plugins
- [x] application 
- [x] pkg-extra 🎏
- [x] tome ubuntu mate
- [ ] Todo 2026-04-12

<!-- mtoc-start -->

* [Termux restore](#termux-restore)
* [tome](#tome)

<!-- mtoc-end -->
## Termux restore
**备份**
```bash
tar -zcvf /sdcard/v3.02_termux.tar.gz -C /data/data/com.termux/files ./home ./usr
```

**恢复备份**
```bash
tar -zxvf /sdcard/v3.02_termux.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
```

## tome
```bash
apt install -y curl
bash -c "$(curl -LfsS 'https://gitee.com/mo2/linux/raw/master/debian.sh')"
```


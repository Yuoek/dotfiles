# lilypond

## 安装依赖

pkg install mpv fluidsynth lilypond

## 克隆源码

git clone https://github.com/martineausimon/nvim-lilypond-suite

## FluidR3_GM 音效
**下载** [FluidR3_GM.sf2](https://github.com/pianobooster/fluid-soundfont/releases/download/v3.1/FluidR3_GM.sf2)

```bash
wget https://github.com/pianobooster/fluid-soundfont/releases/download/v3.1/FluidR3_GM.sf2
```

**创建软链接**
- 创建 `soundfonts`目录并移入
```bash
mkdir $PREFIX/share/soundfonts && cp FluidR3_GM.sf2 $PREFIX/share/soundfonts/
```

- 链接
```bash
ln -s $PREFIX/share/soundfonts/FluidR3_GM.sf2 $PREFIX/share/soundfonts/default.sf2 
```
                                                                      

## nvim 配置

### lua
```lua
 { 
  'martineausimon/nvim-lilypond-suite',
  opts = {
    -- edit config here (see "Customize default settings" in wiki)
  }
}
```

### 命令行
| 命令行 | 功能 |
| -------------- | --------------- |
| :Lilycmp | 编译生成 midi、pdf 文件 |
| :LilyPlayer | 生成 mp3 并播放 |



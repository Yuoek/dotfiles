# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH


alias yuoek='cd ~/Yuoek && nvim yuoek.md'
alias help='cd ~/Yuoek/db/rime/external/data/rime/lua && nvim help.lua'
alias rime='cd ~/Yuoek/db/rime/external/data/rime && nvim'
alias symbols='cd ~/Yuoek/db/rime/external/data/rime/yuoek/symbols && nvim zero.md'
alias symbolscat='cd ~/Yuoek/db/rime/external/data/rime/yuoek && cat symbols/*.md > ../symbols.yaml'
alias symbolstoc='cd ~/Yuoek/db/rime/external/data/rime/yuoek/symbols && toclink . zero.md'
alias dict='cd ~/Yuoek/db/rime/external/data/rime/lua && nvim "phraseExt personal.txt"'
alias personal='cd ~/Yuoek/db/rime/external/data/rime/lua/ && nvim "phraseComment personal.txt"'
alias rimezip='cd ~/Yuoek/db/rime && echo "rime.zip Deleted" && echo "now is zipping" && rm -rf rime.zip && zip -r rime.zip * && echo "zip Finished" && echo "move to ~/Yu/db/zip/" && mv rime.zip ~/Yu/db/zip'

alias push='
git submodule foreach "
  git checkout main 2>/dev/null || git checkout master 2>/dev/null || echo \"submodule \$name no main/master branch, skip\"
  git add .
  git commit -m \" push \$name: finish \" 2>/dev/null || echo \"submodule \$name skip\"
  git push 2>/dev/null || echo \"submodule \$name push error\"
"
git add .
git commit -m "push all submodules" 2>/dev/null || echo " nothing to push"
git push origin main
'

## texlive-bin
source /data/data/com.termux/files/usr/etc/profile.d/texlive.sh

## llm
export LLM_KEY=sk-eed203e77451477da6b0a55ac44e2246
export SILICONFLOW_TOKEN=sk-psbulfyeksopdecegacsawiimusfpjdxoqkxudhivqnjbaim

# proot-distro login
alias arch='proot-distro login archlinux --user yuoek --bind /sdcard:/sdcard'

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# ZSH_THEME="aditya"
eval "$(starship init zsh)"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME="aditya"
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-autosuggestions zsh-syntax-highlighting z)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='nvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"

# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#------------------------------------------
alias l='ls -lh'
alias ll='ls -lah'
alias la='ls -a'
alias ld='ls -lhd'
alias p='pwd'

#alias rm='rm -rf'
alias u='cd /data/data/com.termux/files/usr'
alias h='cd /data/data/com.termux/files/home'
alias :q='exit'
alias grep='grep --color=auto'
alias open='termux-open'
alias lc='lolcat'
alias xx='chmod +x'
alias rel='termux-reload-settings'

#------------------------------------------

# SSH Server Connections

# linux (Arch)
#alias arch='ssh UNAME@IP -i ~/.ssh/id_rsa.DEVICE'

# linux sftp (Arch)
#alias archfs='sftp -i ~/.ssh/id_rsa.DEVICE UNAME@IP'

neofetch

# symble/*.md -> zero.md
toclink() {
  local dir="${1:-$HOME/Yuoek/db/rime/external/data/rime/symbles}"
  local out="${2:-$HOME/Yuoek/db/rime/external/data/rime/symbles/zero.md}"
  for f in "$dir"/*.md; do
    if [ -f "$f" ]; then
      name=$(basename "$f" .md)
      echo "## [$name]($name.md)"
    fi
  done > "$out"
}




symblelink() {
  cd "$HOME" || { echo "❌ 无法进入 HOME 目录"; return 1; }

  local dir="${1:-$HOME/Yuoek/db/rime/yuoek/symbols}"
  local out_yaml="${2:-$HOME/Yuoek/db/rime/symbols.yaml}"
  # 修正为带空格文件名路径
  local out_personal="${3:-"$HOME/Yuoek/db/rime/lua/phraseComment personal.txt"}"

  echo "====================================="
  echo "📂 源目录: $dir"
  echo "📄 YAML输出: $out_yaml"
  echo "📄 Personal输出: $out_personal"
  echo "====================================="

  if [[ ! -d "$dir" ]]; then
    echo "❌ 错误：源目录不存在 -> $dir"
    return 1
  fi

  echo "[1/5] 创建输出目录"
  mkdir -p "$(dirname "$out_yaml")"
  mkdir -p "$(dirname "$out_personal")"

  echo "[2/5] 初始化空白文件"
  echo -n > "$out_yaml"
  echo -n > "$out_personal"

  # 按文件名排序读取，排除 zero.md
  echo "[3/5] 按序读取MD文档，跳过zero.md"
  local md_list
  IFS=$'\n' md_list=($(ls -1 "$dir"/*.md 2>/dev/null | sort | grep -v zero.md))
  unset IFS

  local total_file=${#md_list[@]}
  if [[ $total_file -eq 0 ]]; then
    echo "ℹ️ 排除zero.md后无待处理文件"
    return 0
  fi
  echo "[3/5] 总计 $total_file 个文件待处理"
  echo

  local count=0
  for file in "${md_list[@]}"; do
    ((count++))
    echo "[进度 $count/$total_file] 处理：$(basename "$file")"

    # yaml 过滤二级标题，原样留存内容
    awk '!/^## /' "$file" >> "$out_yaml"
    echo "" >> "$out_yaml"

    awk '
    BEGIN{OFS="\t"}
    /^## /{
      title=substr($0,4)
      getline
      gsub(/^[ \t]+|[ \t]+$/,"")
      gsub(/,$/,"")
      # 正常原样输出 &nbsp;
      gsub(/ /,"\\&nbsp",title)
      gsub(/ /,"\\&nbsp",$0)
      if($0 != ""){
        print $0, title
      }
    }
    ' "$file" >> "$out_personal"
  done

  echo
  echo "====================================="
  echo "✅ 处理完成：空格转为&nbsp原样输出"
  echo "symbles.yaml 行数：$(wc -l < "$out_yaml")"
  echo "personal.txt 行数：$(wc -l < "$out_personal")"
  echo "====================================="
}

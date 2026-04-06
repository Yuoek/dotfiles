mv ~/.config/nvim/init.lua ~/.config/nvim/init.lua.old
ln -s nvim/init.lua ~/.config/nvim
ln -s nvim/extra.lua ~/.config/nvim/lua/plugins
ln -s -r nvim/custom ~/.config/nvim/lua

ln -s -r fonts ~/.local/share

mv ~/.zshrc ~/.zshrc.old
ln -s .zshrc ~/

mv ~/.tmux.conf ~/.tmux.conf.old
ln -s .zshrc ~/


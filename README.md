# unix
All you need for a advanced unix bash


# 1. Install vim
    apt-get install -y vim
# 2. Install [zsh (Oh My Zsh)](https://github.com/robbyrussell/oh-my-zsh)
    apt-get install -y zsh
## If you want change to my favorite theme go to ZSH_THEME="robbyrussel" and change to ZSH_THEME="agnoster"

    nano ~/.zshrc # 
        
 - https://camo.githubusercontent.com/6d971fb4a462a11da0efee2206d98afeb5fffd47/687474703a2f2f692e696d6775722e636f6d2f61506d4c692e706e67

# 3. If use custom theme, you have Install fonts-powerline and restart your pc

    apt-get install fonts-powerline
    
# 4. Install zsh

    apt-get install zsh
# 5. Install tmux

     apt-get install tmux
## Put code of tmux.conf in this gist on your ~/.tmux.conf.

    vim ~/.tmux.conf
## Reloading tmux config

    tmux source-file ~/.tmux.conf
    
## Install plugins for tmux

    https://github.com/tmux-plugins
    
# Install VIM
apt-get install vim

# Links
    http://www.vim-bootstrap.com/
    https://vim-adventures.com/

# Advanced
    Powerline Shell- https://github.com/banga/powerline-shell
    Vim Bootstrap 
    Nerd Icons - https://github.com/ryanoasis/vim-devicons
    Powerline theme and font extra - https://github.com/ryanoasis/powerline-extra-symbols

# Turn background vim transparent
vim ~/.vimrc.local:

highlight Normal ctermbg=none
highlight NonText ctermbg=none

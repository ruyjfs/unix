# unix
All you need for a advanced unix bash

# 1. Install Git - Needed for plugins
    apt-get install -y git
# 2. Install VIM
    apt-get install -y vim
## 2.1 Vim Bootstrap for pre configuration plugins essential 
   [www.vim-bootstrap.com](https://github.com/avelino/vim-bootstrap)

# 3. Install [zsh (Oh My Zsh)](https://github.com/robbyrussell/oh-my-zsh)
    apt-get install -y zsh
## 3.1 Turn zsh default for shell
    chsh -s $(which zsh)
## 3.2 If you want change to my favorite theme go to ZSH_THEME="robbyrussel" and change to ZSH_THEME="agnoster"
    vim ~/.zshrc # 
![Image](https://camo.githubusercontent.com/6d971fb4a462a11da0efee2206d98afeb5fffd47/687474703a2f2f692e696d6775722e636f6d2f61506d4c692e706e67)
## 3.2 If use custom theme, you have Install fonts-powerline and restart your pc
    apt-get install -y fonts-powerline 
```    
apt-get install -y python python-pip

git clone https://github.com/b-ryan/powerline-shell
cd powerline-shell
python setup.py install
```
## 3.3 Install Auto Suggestion
[ZSH Auto Suggestion](https://github.com/zsh-users/zsh-autosuggestions)


# 4. Advanced
   - [Powerline Shell](https://github.com/banga/powerline-shell)
   - [Nerd Font](https://github.com/ryanoasis/nerd-fonts#patched-fonts)
   - [Nerd Icons](https://github.com/ryanoasis/vim-devicons)
   - [Powerline theme and font extra](https://github.com/ryanoasis/powerline-extra-symbols)

# 4. Install tmux - Tmux is like terminator but without using graphical interface, it divides the screens directly into the terminal
     apt-get install -y tmux
## My hotkeys configuration - Put code of tmux.conf in this gist on your ~/.tmux.conf.

    vim ~/.tmux.conf
## Reloading tmux config

    tmux source-file ~/.tmux.conf
    
## Install plugins for tmux

    https://github.com/tmux-plugins
    

# Links:
- [https://vim-adventures.com/](https://vim-adventures.com/) - For vim begginers


# Install Tilda - Is a terminal with scroll of top
    sudo apt-get install tilda



# Turn background vim transparent
vim ~/.vimrc.local:

highlight Normal ctermbg=none
highlight NonText ctermbg=none

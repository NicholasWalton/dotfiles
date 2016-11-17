# Setup fzf
# ---------
if [[ ! "$PATH" == */home/nicholaswalton/src/fzf/bin* ]]; then
  export PATH="$PATH:/home/nicholaswalton/src/fzf/bin"
fi

# Man path
# --------
if [[ ! "$MANPATH" == */home/nicholaswalton/src/fzf/man* && -d "/home/nicholaswalton/src/fzf/man" ]]; then
  export MANPATH="$MANPATH:/home/nicholaswalton/src/fzf/man"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "$HOME/src/fzf/shell/completion.zsh" 2> /dev/null

# Key bindings
# ------------
source "$HOME/src/fzf/shell/key-bindings.zsh"


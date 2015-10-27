export ANDROID_HOME=~/android-sdk-linux
# Set the key mapping style to 'emacs' or 'vi'.
zstyle ':omz:editor' keymap 'emacs'

# Auto convert .... to ../..
zstyle ':omz:editor' dot-expansion 'no'

# Set case-sensitivity for completion, history lookup, etc.
zstyle ':omz:*:*' case-sensitive 'no'

# Color output (auto set to 'no' on dumb terminals).
zstyle ':omz:*:*' color 'yes'

# Auto set the tab and window titles.
zstyle ':omz:terminal:auto' title 'yes'

# Set the plugins to load (see $OMZ/plugins/).
zstyle ':omz:load' plugin 'archive' 'git'

# Set the prompt theme to load.
# Setting it to 'random' loads a random theme.
# Auto set to 'off' on dumb terminals.
zstyle ':omz:prompt' theme 'sorin'

# This will make you shout: OH MY ZSHELL!
source "$HOME/.oh-my-zsh/init.zsh"

# The following lines were added by compinstall

zstyle ':completion:*' completer _oldlist _expand _complete _ignored _match _correct _approximate _prefix
zstyle ':completion:*' matcher-list '+' '+m:{[:lower:]}={[:upper:]}' '+m:{[:lower:][:upper:]}={[:upper:][:lower:]}' '+r:|[._-]=** r:|=** l:|=*'
zstyle :compinstall filename '/home/nicholaswalton/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall


alias make="nice -n15 make"
export PATH=~/CodeSourcery/Sourcery_CodeBench_for_ARM_GNU_Linux:~/CodeSourcery/Sourcery_CodeBench_Lite_for_ARM_GNU_Linux/bin:~/CodeSourcery/Sourcery_CodeBench_Lite_for_ARM_EABI/bin:$PATH
export PATH=~/android-sdk-linux/tools:$PATH
export PATH=~/android-sdk-linux/platform-tools/adb:~/android-sdk-linux/platform-tools:~/android-ndk-r8b:$PATH
export PATH=~/bin:$PATH
export PATH=~/android-ndk-r8b/toolchains/arm-linux-androideabi-4.4.3/prebuilt/linux-x86/bin:/home/nicholaswalton/android-ndk-r8b/toolchains/arm-linux-androideabi-4.4.3/prebuilt/linux-x86/bin:$PATH

alias bd=popd
export BUILDROOT_DL_DIR=/home/nicholaswalton/buildroot_dl
export BR2_DL_DIR=$BUILDROOT_DL_DIR

PATH="/home/nicholaswalton/perl5/bin${PATH+:}${PATH}"; export PATH;
PERL5LIB="/home/nicholaswalton/perl5/lib/perl5${PERL5LIB+:}${PERL5LIB}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/nicholaswalton/perl5${PERL_LOCAL_LIB_ROOT+:}${PERL_LOCAL_LIB_ROOT}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/nicholaswalton/perl5\""; export PERL_MB_OPT;
#PERL_MM_OPT="INSTALL_BASE=/home/nicholaswalton/perl5"; export PERL_MM_OPT;

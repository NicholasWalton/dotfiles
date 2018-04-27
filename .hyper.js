module.exports = {
  config: {
    // default font size in pixels for all tabs
    fontSize: 16,

    // font family with optional fallbacks
    fontFamily: '"Ubuntu Mono", Menlo, "DejaVu Sans Mono", "Lucida Console", monospace',

    // terminal cursor background color and opacity (hex, rgb, hsl, hsv, hwb or cmyk)
    cursorColor: 'rgba(248,48,229,0.50)',

    // `BEAM` for |, `UNDERLINE` for _, `BLOCK` for █
    cursorShape: 'BLOCK',

    // color of the text
    foregroundColor: '#e5e660',

    // terminal background color
    backgroundColor: '#000130',

    // border color (window, tabs)
    borderColor: '#fff',

    // custom css to embed in the main window
    css: '.header_windowHeader { background-color: #c0bebf; color: #0b0000; height: 16px} \
    .header_appTitle { font-size: 11pt; font-family:"Ubuntu"',
    

    // custom css to embed in the terminal window
    termCSS: 'x-row {line-height: 1}',

    // custom padding (css format, i.e.: `top right bottom left`)
    padding: '',

    // the full list. if you're going to provide the full color palette,
    // including the 6 x 6 color cubes and the grayscale map, just provide
    // an array here instead of a color map object
    colors: {
      black: 		'#000000',
      red: 			'#cd0000',
      green: 		'#00cd00',
      yellow: 		'#cdcd00',
      blue: 		'#1e90ff',
      magenta: 		'#cd00cd',
      cyan: 		'#00cdcd',
      white: 		'#e5e5e5',
      lightBlack: 	'#4c4c4c',
      lightRed: 	'#ff0000',
      lightGreen: 	'#00ff00',
      lightYellow: 	'#ffff00',
      lightBlue: 	'#4682b4',
      lightMagenta:	'#ff00ff',
      lightCyan: 	'#00ffff',
      lightWhite: 	'#ffffff'
    },

    // the shell to run when spawning a new session (i.e. /usr/local/bin/fish)
    // if left empty, your system's login shell will be used by default
    shell: '',

    // for setting shell arguments (i.e. for using interactive shellArgs: ['-i'])
    // by default ['--login'] will be used
    shellArgs: ['--login'],

    // for environment variables
    env: {},

    // set to false for no bell
    bell: 'SOUND',

    // if true, selected text will automatically be copied to the clipboard
    copyOnSelect: true,

    // URL to custom bell
    // bellSoundURL: 'http://example.com/bell.mp3',

    // for advanced config flags please refer to https://hyperterm.org/#cfg
    
/*    paneNavigation: {
      debug: false,
      hotkeys: {
        navigation: {
          up: 'ctrl+alt+pageup',
          down: 'ctrl+alt+pagedown',
          left: 'ctrl+alt+home',
          right: 'ctrl+alt+end'
        },
        jump_prefix: 'ctrl+alt', // completed with 1-9 digits
        permutation_modifier: 'shift', // Added to jump and navigation hotkeys for pane permutation
      },
      showIndicators: false, // Show pane number
      indicatorPrefix: '^⌥', // Will be completed with pane number
      indicatorStyle: { // Added to indicator <div>
        position: 'absolute',
        top: 0,
        left: 0,
        fontSize: '10px'
      },
      focusOnMouseHover: true
    },*/
  },

  // a list of plugins to fetch and install from npm
  // format: [@org/]project[#version]
  // examples:
  //   `hyperpower`
  //   `@company/project`
  //   `project#1.0.1`
  plugins: [//"hyper-pane",
  "hyper-font-smoothing", 
    //"hyper-simple-highlight-active-session", "hyperterm-crosshair", "hyperzsh"
  ],
  // in development, you can create a directory under
  // `~/.hyperterm_plugins/local/` and include it here
  // to load it and avoid it being `npm install`ed
  localPlugins: [],
  
  keymaps: {
    "tab:next": "ctrl+pagedown",
    "tab:prev": "ctrl+pageup",
    "pane:next": "ctrl+shift+tab",
    "pane:prev": "ctrl+tab",
    "pane:splitVertical": "ctrl+shift+o",
  }
  
};

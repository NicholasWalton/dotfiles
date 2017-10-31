# Your init script
#
# Atom will evaluate this file each time a new window is opened. It is run
# after packages are loaded/activated and after the previous editor state
# has been restored.
#
# An example hack to log to the console when each text editor is saved.
#
# atom.workspace.observeTextEditors (editor) ->
#   editor.onDidSave ->
#     console.log "Saved! #{editor.getPath()}"

atom.commands.add 'atom-text-editor', 'bracket:close-hint', ->
  editor = atom.workspace.getActiveTextEditor()
  blocks = editor.getText().split("\{").length
  console.log "There are #{blocks} blocks"

atom.commands.add 'atom-workspace', 'custom:debug', ->
  editor = atom.workspace.getActiveTextEditor()
  view = atom.views.getView(editor)
  atom.commands.dispatch(view,"dbg:stop") and atom.commands.dispatch(view,"build:trigger") and atom.commands.dispatch(view,"dbg:debug")

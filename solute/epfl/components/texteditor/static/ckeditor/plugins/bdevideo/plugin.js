/**
 * BDEVideoPlugin
 * Plugin to be used for creating texts for bde6 using seocms.
 */

CKEDITOR.plugins.add('bdevideo', {
    icons: 'bdevideo',
    init: function(editor) {
        editor.addCommand('bdevideo', new CKEDITOR.dialogCommand('bdeVideoDialog'));
        editor.ui.addButton('BdeVideo', {
            label: 'Add a youtube or vimeo video',
            command: 'bdevideo',
            icon: CKEDITOR.plugins.getPath('bdevideo') + '/icons/bdevideo.svg'
        });

        CKEDITOR.dialog.add('bdeVideoDialog', this.path + 'dialogs/bdeVideoDialog.js');
    }
});
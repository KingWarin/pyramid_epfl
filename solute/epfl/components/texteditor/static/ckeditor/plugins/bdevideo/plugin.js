/**
 * BDEVideoPlugin
 * Plugin to be used for creating texts for bde6 using seocms.
 */

CKEDITOR.plugins.add('bdevideo', {
    icons: 'bdevideo',
    init: function(editor) {
        editor.addCommand('bdevideo', new CKEDITOR.dialogCommand('bdeVideoDialog'));
        editor.addCommand('delbdevideo', {
            exec: function(ed) {
                var sel = ed.getSelection().getStartElement();
                var video = sel ? sel.getAscendant(function(el) { return (el.hasClass && el.hasClass('bde-video-placeholder')); }, true) : false;
                if (video) {
                    video.remove();
                }
            }
        });
        editor.ui.addButton('BdeVideo', {
            label: 'Add a youtube or vimeo video',
            command: 'bdevideo',
            icon: CKEDITOR.plugins.getPath('bdevideo') + '/icons/bdevideo.svg'
        });

        CKEDITOR.dialog.add('bdeVideoDialog', this.path + 'dialogs/bdeVideoDialog.js');

        if (editor.contextMenu) {
            editor.addMenuGroup('bdeVideoGroup');
            editor.addMenuItem('bdeVideoItem', {
                label: 'Video entfernen',
                command: 'delbdevideo',
                group: 'bdeVideoGroup'
            });
            editor.contextMenu.addListener(function(element) {
                if (element.getAscendant(function(el) { return (el.hasClass && el.hasClass('bde-video-placeholder')); }, true)) {
                    return { bdeVideoItem: CKEDITOR.TRISTATE_OFF };
                }
            });
        }
    }
});
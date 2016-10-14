/**
 * BDEVideoDialog
 * Dialog for the BDEVideoPlugin to be used on ckEditor in SEOCMS
 */
function createThumb(target, video) {
    var path;
    var create = function(url) {
        var icon = new CKEDITOR.dom.element('div');
        icon.setAttribute('class', 'bde-video bde-video-play-icon');

        var thumbLink = new CKEDITOR.dom.element('div');
        thumbLink.setAttribute('class', 'bde-video bde-video-thumb');
        thumbLink.setAttribute('style', 'background: no-repeat center/80% url(' + url + ');');

        target.append(thumbLink);
        target.append(icon);
    };

    if (video.platform === 'youtube') {
        path = 'https://img.youtube.com/vi/' + video.id + '/hqdefault.jpg';
        create(path);
    } else if (video.platform === 'vimeo') {
        $.ajax({
            type: 'GET',
            url: 'https://vimeo.com/api/v2/video/' + video.id + '.json',
            jsonp: 'callback',
            dataType: 'jsonp',
            success: function(data) {
                path = data[0].thumbnail_large;
                create(path);
            }
        });
    }
};

function getVideoData() {
    var getDialog = document.getElementsByClassName('cke_dialog_contents').item(0);
    var url = getDialog.getElementsByTagName('input').item(0).value;
    var urlClean = '';
    var id = '';
    var platform = '';
    var startTime = false;

    if (url.indexOf('youtu.be') >= 0) {
        platform = 'youtube';
        id = url.substring(url.lastIndexOf('/') + 1, url.length);
    }
    if (url.indexOf('youtube') >= 0) {
        platform = 'youtube';
        if (url.indexOf('</iframe>') >= 0) {
            var end = url.substring(url.indexOf('embed/') + 6, url.length);
            id = end.substring(end.indexOf('"'), 0);
        } else {
            if (url.indexOf('&') >= 0) {
                id = url.substring(url.indexOf('?v=') + 3, url.indexOf('&'));
            } else {
                id = url.substring(url.indexOf('?v=') + 3, url.length);
            }
        }
    }
    if (url.indexOf('vimeo') >= 0) {
        platform = 'vimeo';
        if (url.indexOf('</iframe>') >= 0) {
            var end = url.substring(url.lastIndexOf('vimeo.com/"') + 6, url.indexOf('>'));
            id = end.substring(end.lastIndexOf('/') + 1, end.indexOf('"', end.lastIndexOf('/') + 1));
        } else {
            id = url.substring(url.lastIndexOf('/') + 1, url.length);
        }
    }
    if (url.indexOf('#t=') !== -1) {
        startTime = url.substring(url.indexOf('#t=') + 3);
    } else if (url.indexOf('start=') !== -1) {
        startTime = url.substring(url.indexOf('start=') + 6);
    }
    if (id.indexOf('#') !== -1) {
        id = id.substring(0, id.indexOf('#'));
    }
    if (platform === 'youtube') {
        urlClean = 'https://www.youtube.com/embed/' + id + '?autoplay=1';
        if (startTime) {
            urlClean += '&start=' + startTime;
        }
    } else if (platform === 'vimeo') {
        urlClean = 'https://player.vimeo.com/video/' + id + '?autoplay=1';
        if (startTime) {
            urlClean += '#t=' + startTime;
        }
    }
    return {'platform': platform, 'id': id, 'url': urlClean};
};

CKEDITOR.dialog.add('bdeVideoDialog', function(editor) {
    return {
        title: 'Insert a YouTube or Vimeo URL',
        minWidth: 400,
        minHeight: 100,
        contents: [
            {
                id: 'tab-basic',
                label: 'Basic Settings',
                elements: [
                    {
                        type: 'text',
                        id: 'url_video',
                        label: 'Youtube or Vimeo URL',
                        validate: CKEDITOR.dialog.validate.notEmpty('Empty!')
                    }
                ]
            }
        ],
        onOk: function() {
            var videoData = getVideoData();

            var p = new CKEDITOR.dom.element('div');
            p.setAttribute('class', 'bde-video bde-video-placeholder');
            p.setAttribute('data-video', videoData.url);

            createThumb(p, videoData);
            editor.insertElement(p);
            this.destroy();
        }
    };
});

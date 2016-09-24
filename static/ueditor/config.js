/**
 * Created by owner on 9/15/16.
 */
// function hasClass(element, cls) {
//     return (' ' + element.className + ' ').indexOf(' ' + cls + ' ') > -1;
// }


function getTextArea(){
    var elem = document.getElementsByTagName("textarea");
    if (elem.length>0){
        for (var i=0; i<elem.length; i++){
            id = elem[i].getAttribute("id");
            window.UE.getEditor(id);
        }
    }
}

window.onload = getTextArea;

// var hasClass = function(elem, className) {
//     var reg = new RegExp('(^|\\s+)' + className + '($|\\s+)');
//     return reg.test(elem.className);
// };
//
// var elem = document.getElementsByTagName('textarea');
// alert(document.getElementsByTagName('textarea')[0])
// alert(elem.length)

// hasClass(document.querySelector("textarea"), 'vLargeTextField');
// alert(elem.length);
//     window.UE.getEditor('id_nr');
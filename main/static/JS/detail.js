// 좌표 가져오기//
var Y_axis = document.querySelectorAll('#Y');
var Dots = document.querySelectorAll('#dots');
// 좌표 숨김//
function Clear(){
    for( var i=0; i<Y_axis.length; i++){
        var item = Y_axis.item(i);
        item.style.display = 'none';
    }
}
Clear();
// 가져온 좌표 묶고, 위치 배정//
function Cooridate(){
    for(var i =0; i<Dots.length; i++){
        var item = Dots.item(i);
        var X=(i*150+'px');
        var Before_Y = Y_axis[i].value;
        var Y = (Before_Y*150+'px');
        item.style.setProperty('padding-left',X);
        item.style.setProperty('padding-top',Y);
        }
}
Cooridate();
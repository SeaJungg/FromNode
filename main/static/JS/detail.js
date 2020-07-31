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

        for( var i =0; i<Dots.length; i++){

            var item = Dots.item(i);
            var X=(i*150+'px');
            var Before_Y = Y_axis[i].value;
            var Y = (Before_Y*150+'px');
            // X축과 Y축 좌표 -> 각각 item과 Before_Y, X,Y는 150배 해준거

            item.style.setProperty('margin-left',X);
            item.style.setProperty('margin-top',Y);
            // Padding으로 div를 밀어버림
        }

    }


    Cooridate();

// 대각선 그어버리기 //

// 우선 밀어버리기 //
    function line(){
        var dictXY = {};
        var BeforedictXY={};
        var BeforeX=0;
        for( var i =0; i<Dots.length; i++){

            var item = lines.item(i);
            var Before_Y = Y_axis.item(i).value;
            dictXY['X'] = i;
            dictXY['Y'] = Before_Y;

            console.log(dictXY);

            if(dictXY['Y']==BeforedictXY['Y']){
                var degree = "rotate(0deg)";
            }
            else if(dictXY['X']==0){
                var degree = "rotate(0deg)";
            }
            else if(dictXY['X']==(Dots.length-1)){
                var degree = "rotate(0deg)";
            }
            else{
                var degree = "rotate(-45deg)";

            }

            var X_dif = dictXY['X']-BeforedictXY['X'];
            var Y_dif = dictXY['Y']-BeforedictXY['Y'];


            BeforedictXY['X']=dictXY['X'];
            BeforedictXY['Y']=dictXY['Y'];


            console.log(X_dif,Y_dif);

            var X=(i*150+20+'px');
            var Y = (Before_Y*150+'px');
           
            item.style.setProperty('transform',degree);
            item.style.setProperty('margin-left', X);
            item.style.setProperty('margin-top',Y);

        }
            
            }
    
line();
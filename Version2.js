Java.perform(function(){
var obj = Java.use('sg.vantagepoint.a.c');
obj.a.implementation = function(){
  console.log(obj);
  this.a.call(this);
  return false;
}

var ob1 = Java.use('sg.vantagepoint.a.a');
ob1.a.implementation = function(x,y){
  var ref = this.a(x,y);
  var i;
  var y='';
  for(i=0;i<ref.length;i++){
      y=y+String.fromCharCode(ref[i]);
    }
  console.log(y);
  return ref;
}
});

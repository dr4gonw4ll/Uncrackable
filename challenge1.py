import frida, sys
ss = """
Java.perform(function(){
var obj = Java.use('sg.vantagepoint.a.c');
obj.a.implementation = function(){
  console.log(obj);
  this.a.call(this);
  return false;
}
var obj1 = Java.use('sg.vantagepoint.uncrackable1.a');
obj1.a.implementation=function(x){
console.log('Value of var1 is: '+x);
return true;
}
});

"""
device = frida.get_usb_device(1)
pid = device.spawn(["owasp.mstg.uncrackable1"])
session = device.attach(pid)
script = session.create_script(ss)
script.load()
device.resume(pid)
sys.stdin.read()

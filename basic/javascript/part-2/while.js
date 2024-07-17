let j = 1; 
while (j <= 5) { 
console.log("while loop iteration:", j);
 j++; }


const prompt = require('prompt-sync')({sigint: true});
var ulangi = prompt("Are you ready? "); //Input 1
console.log("Start")
var counter = 0;
while(ulangi){
var jawab = prompt("Apakah anda mau mengulang? (yes/no) :")
counter++;
if(jawab == false || jawab == "no"){
ulangi = false;
}
console.log("Pengulangan ke-"+counter)
}

var mobil = ["Avanza","Yaris","Alya"];
//Mengambil elemen pertama pada array
mobil[0] = 'bebek';
//Mengisi element array dengan push
mobil.push("Veloz");
//Membuat array kosong
var arrayKosong = [];
// menghapus paling belakang
mobil.pop()
// menghapus paling depan
mobil.shift()
//Mencetak semua elemen array
for(let i=0; i < mobil.length; i++){
console.log('Cetak mobil ke-' + i + ": " + mobil[i]);
}

let fruits = ["Apple", "Banana", "Cherry"]; 
console.log(fruits[0]); 
console.log(fruits[2]); 
fruits.push("mango");   
console.log(fruits); 
fruits[1] = "Blueberry";
console.log(fruits); 
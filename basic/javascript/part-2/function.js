// fungsi biasa
function namaFungsi(){
    console.log("Hello World!");
    }
    //Cara memanggil Fungsi
    namaFungsi()
    //output : "Hello World!"

//function expression
var namaFungsi = function(){
    console.log("Hello World!");
    }

// arrow function
var namaFungsi = () => {
    console.log("Hello World!");
    }
    // atau seperti ini (jika isi fungsi hanya satu baris):
    var namaFungsi = () => console.log("Hello World!");

// fungsi dgn parameter
function kali(a, b){
    hasilKali = a * b;
    console.log("Hasil kali a*b = " + hasilKali);
    }
    kali(3, 2); // -> Hasil kali a*b = 6

// fungsi mengembalikan nilai
function bagi(a,b){
    hasilBagi = a / b;
    return hasilBagi;
    }
    // memanggil fungsi
    var nilai1 = 20;
    var nilai2 = 5;
    var hasilPembagian = bagi(nilai1, nilai2);
    console.log(hasilPembagian); //-> 4
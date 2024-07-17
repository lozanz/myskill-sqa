// operator aritmatika
let a = 20;
let b = 3;
console.log(a + b);  
console.log(a - b);  
console.log(a * b);  
console.log(a / b);  
console.log(a % b);  
console.log(a ** b);

// operator perbandingan
let x = 5;
let y = 6;
console.log(x === y); 
console.log(x == y);
console.log(x !== y);
console.log(x > y);  
console.log(x >= 5); 
console.log(x < y);  
console.log(x <= 5)

// operator penugasan
let m = 20;
m += 5; 
console.log(m); 
m -= 4;  
console.log(m);
m *= 2;  
console.log(m); 
m /= 6;  
console.log(m); 
m %= 5;  
console.log(m); 

// operator logika
let p = true;
let q = false;
console.log(p && q);
console.log(p || q);
console.log(!p);    

a=1
b=5
let andResult = (a > 0 && b > 7);
console.log(andResult); 

let orResult = (a > 0 || b < 0);
console.log("a > 0 || b < 0:", orResult);

let notResult = !(a > 0);
console.log("!(a > 0):", notResult); 

//operator unary
let nama = "Alice"; 
let umur = 30;
 let isactive = true; 
let phone = { brand: "Samsung", model: "Galaxy S20", year: 2020 };
console.log(typeof nama); // Output: string 
console.log(typeof umur); // Output: number 
console.log(typeof isactive); // Output: boolean
console.log(typeof car); //object

console.log(phone); 
delete phone.year; 
console.log(phone); 

//operator ternary
let age = 20;
let isAdult = (age >= 18) ? "Yes" : "No";
console.log("Is adult:", isAdult); // Output: Is adult: Yes
